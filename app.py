import streamlit as st
import uuid

st.set_page_config(page_title="ChatBot AI", page_icon="💬", layout="wide")

# ---------------- INIT ----------------
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

def new_chat():
    chat_id = str(uuid.uuid4())[:8]
    st.session_state.chats[chat_id] = []
    st.session_state.current_chat = chat_id

if not st.session_state.chats:
    new_chat()

# ---------------- DARK THEME STYLE ----------------
st.markdown("""
<style>

/* Background */
body {
    background-color: #0f172a;
}

/* Title */
.main-title {
    text-align:center;
    font-size:38px;
    font-weight:800;
    color:#00ffcc;
}

.sub-text {
    text-align:center;
    color:#94a3b8;
    margin-bottom:25px;
}

/* USER BUBBLE */
.chat-bubble-user {
    background: linear-gradient(135deg, #00ffcc, #00b3a4);
    color:black;
    padding:12px 15px;
    border-radius:15px;
    margin:8px 0;
    text-align:right;
    max-width:70%;
    margin-left:auto;
    font-weight:500;
}

/* BOT BUBBLE */
.chat-bubble-bot {
    background: #1e293b;
    color:white;
    padding:12px 15px;
    border-radius:15px;
    margin:8px 0;
    max-width:70%;
    font-weight:500;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color:#0b1220;
}

/* CHAT INPUT */
.stChatInput textarea {
    background-color:#1e293b !important;
    color:white !important;
    border-radius:12px !important;
    border:1px solid #00ffcc !important;
    padding:12px !important;
    font-size:15px !important;
}

/* PLACEHOLDER */
.stChatInput textarea::placeholder {
    color:#94a3b8 !important;
}

/* SEND BUTTON */
.stChatInput button {
    background-color:#00ffcc !important;
    color:black !important;
    border-radius:10px !important;
    font-weight:bold !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💬 ChatGPT Clone")

    if st.button("➕ New Chat"):
        new_chat()

    st.markdown("---")
    st.markdown("### 🗂 Chats")

    for cid in st.session_state.chats:
        if st.button(f"💬 Chat {cid}", key=cid):
            st.session_state.current_chat = cid

    st.markdown("---")
    st.markdown("⚙️ Settings")
    st.selectbox("Theme", ["Dark", "Light"])

# ---------------- MAIN TITLE ----------------
st.markdown("<div class='main-title'>ChatBot AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>Modern & Stylish Chatbot UI 🔥</div>", unsafe_allow_html=True)

# ---------------- CHAT ----------------
chat_id = st.session_state.current_chat
messages = st.session_state.chats[chat_id]

for msg in messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
user_input = st.chat_input("💬 Type your message here...")

if user_input:
    messages.append({"role": "user", "content": user_input})

    reply = "✨ I received: " + user_input

    messages.append({"role": "assistant", "content": reply})

    st.rerun()