import streamlit as st
from groq import Groq
import uuid

# ---------------- API SETUP ----------------
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Cosmic AI Hub",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION STATE ----------------
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

if "suggestion_prompt" not in st.session_state:
    st.session_state.suggestion_prompt = ""

if "temp_prompt" not in st.session_state:
    st.session_state.temp_prompt = ""

def create_new_chat():
    chat_id = str(uuid.uuid4())[:8]
    st.session_state.chats[chat_id] = {
        "title": "⚡ New Cosmic Orbit",
        "messages": []
    }
    st.session_state.current_chat = chat_id

if not st.session_state.chats or st.session_state.current_chat is None:
    create_new_chat()

# ---------------- PREMIUM PURE COSMIC CSS ----------------
st.markdown("""
<style>

.stApp, [data-testid="stHeader"], [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%) !important;
    color: #f8fafc !important;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background-color: transparent !important;
    border: none !important;
}

/* Sidebar Adjustment */
.cosmic-sidebar {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    width: 68px;
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(20px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 30px 0;
    z-index: 99999;
    border-right: 1px solid rgba(56, 189, 248, 0.15);
}

.top-icons, .bottom-icons {
    display: flex;
    flex-direction: column;
    gap: 28px;
    align-items: center;
}

.cosmic-icon {
    color: #94a3b8;
    font-size: 22px;
    text-decoration: none;
    padding: 12px;
}

/* Main Layout Shift */
.cosmic-layout {
    margin-left: 90px;
    padding: 30px;
    padding-bottom: 140px;
}

/* Front Page Title */
.front-page-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 35vh;
    text-align: center;
}

.cosmic-title {
    font-size: 56px;
    font-weight: 800;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 40%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.cosmic-subtitle {
    color: #94a3b8;
    font-size: 19px;
    margin-top: 12px;
}

/* Suggestion Cards */
.suggestions-grid {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 40px;
}

div.stButton > button {
    background: rgba(30, 41, 59, 0.3) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #f8fafc !important;
    border-radius: 16px !important;
    padding: 15px !important;
}

/* CHAT BUBBLE & TEXT COLOR FIXED */
.stChatMessage {
    background: rgba(30, 41, 59, 0.4) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 20px !important;
}

.stChatMessage div, .stChatMessage p, .stChatMessage span {
    color: #ffffff !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
}


div[data-testid="stChatInput"] {
    display: none !important;
}


.unified-capsule-bar {
    position: fixed;
    bottom: 35px;
    left: 52%; 
    transform: translateX(-50%);
    width: 68%;
    background-color: #1e1f20 !important;
    border-radius: 35px;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 15px 40px rgba(0,0,0,0.6);
    border: none !important;
    z-index: 999994;
}

.capsule-left-side {
    display: flex;
    align-items: center;
    gap: 15px;
    width: 75%;
    position: relative;
}

.plus-container {
    position: relative;
    display: inline-block;
    z-index: 1000001 !important;
}

.plus-btn-custom {
    color: #e3e3e3;
    font-size: 22px;
    cursor: pointer;
    user-select: none;
    padding: 5px;
}


.plus-dropdown-menu {
    display: none;
    position: absolute;
    bottom: 45px;
    left: 0;
    background-color: #232425;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.5);
    border-radius: 12px;
    z-index: 1000002 !important;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.05);
}


.plus-dropdown-menu label {
    color: #e3e3e3;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    font-size: 14px;
    cursor: pointer;
    transition: background 0.2s;
    margin: 0;
}

.plus-dropdown-menu label:hover {
    background-color: #303132;
    color: #38bdf8;
}

.show-menu {
    display: block !important;
}

.capsule-right-side {
    display: flex;
    align-items: center;
    gap: 20px;
}

.model-selector-custom {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #e3e3e3;
    font-size: 15px;
    font-weight: 500;
    white-space: nowrap;
}

.blue-glow-dot {
    width: 8px;
    height: 8px;
    background-color: #1a73e8;
    border-radius: 50%;
}

.mic-icon-custom {
    color: #e3e3e3;
    font-size: 19px;
    cursor: pointer;
}


.element-container:has(input[type="text"]) {
    position: fixed !important;
    bottom: 51px !important;
    left: 24% !important;   
    width: 42% !important;   
    z-index: 999999 !important; 
}

div[data-testid="stTextInput"], 
div[data-testid="stTextInput"] > div, 
div[data-testid="stTextInput"] input {
    background: #121212 !important;
    background-color: #121212 !important;
    border: none !important;
    box-shadow: none !important;
    color: white !important;
    outline: none !important;
}

div[data-testid="stTextInput"] > div:focus-within,
div[data-testid="stTextInput"] > div:hover,
input[type="text"]:focus {
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<div class="cosmic-sidebar">
    <div class="top-icons">
        <a href="#" class="cosmic-icon"><i class="fa-solid fa-compass"></i></a>
        <a href="#" class="cosmic-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></a>
        <a href="#" class="cosmic-icon"><i class="fa-solid fa-shuttle-space"></i></a>
        <div class="dot-container">
            <a href="#" class="cosmic-icon"><i class="fa-solid fa-atom"></i></a>
        </div>
        <a href="#" class="cosmic-icon"><i class="fa-solid fa-grip"></i></a>
    </div>
    <div class="bottom-icons">
        <div class="dot-container">
            <a href="#" class="cosmic-icon"><i class="fa-solid fa-sliders"></i></a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



# ---------------- MAIN APP LAYOUT ----------------
st.markdown('<div class="cosmic-layout">', unsafe_allow_html=True)

chat_id = st.session_state.current_chat
messages = st.session_state.chats[chat_id]["messages"]

# ---------------- FRONT PAGE OR CHAT DISPLAY ----------------
if len(messages) == 0:
    st.markdown("""
    <div class='front-page-container'>
        <div class='cosmic-title'>How can I help you today?</div>
        <div class='cosmic-subtitle'>Explore data horizons, build pipelines, or unlock quantum insights.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- PROMPT SUGGESTIONS CARDS ---
    st.markdown('<div class="suggestions-grid">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("✨ Explore Star Clusters\n\nAnalyze stellar formations", use_container_width=True):
            st.session_state.suggestion_prompt = "Tell me about the latest discoveries in Star Clusters."
            st.rerun()
    with c2:
        if st.button("🎨 Generate Galaxy Art\n\nGet cosmic style ideas", use_container_width=True):
            st.session_state.suggestion_prompt = "Give me creative ideas for coding a futuristic galaxy visualizer."
            st.rerun()
    with c3:
        if st.button("🌌 Define Nebulae\n\nLearn quantum gas physics", use_container_width=True):
            st.session_state.suggestion_prompt = "Explain how Nebulae are formed in simple data terms."
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    for msg in messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


st.markdown("""
<div class="unified-capsule-bar">
    <div class="capsule-left-side">
        <div class="plus-container">
            <div class="plus-btn-custom" id="plusBtn"><i class="fa-solid fa-plus"></i></div>
            <div class="plus-dropdown-menu" id="plusDropdown">
                <label for="imgUpload"><i class="fa-solid fa-image" style="margin-right: 12px; color: #38bdf8;"></i> Photo</label>
                <label for="audioUpload"><i class="fa-solid fa-microphone-lines" style="margin-right: 12px; color: #a855f7;"></i> Audio</label>
                <label for="videoUpload"><i class="fa-solid fa-video" style="margin-right: 12px; color: #ec4899;"></i> Video</label>
                <label for="fileUpload"><i class="fa-solid fa-file-import" style="margin-right: 12px; color: #eab308;"></i> Add File</label>
            </div>
        </div>
    </div>
    <div class="capsule-right-side">
        <div class="model-selector-custom">
            <span class="blue-glow-dot"></span>
            <span>Cosmic-Llama 3 (Ultra)</span>
            <i class="fa-solid fa-chevron-down" style="font-size: 11px; color: #8a8a8a; margin-left: 3px;"></i>
        </div>
        <div class="mic-icon-custom"><i class="fa-solid fa-microphone"></i></div>
    </div>
</div>

<script>
const plusBtn = document.getElementById('plusBtn');
const plusDropdown = document.getElementById('plusDropdown');

plusBtn.addEventListener('click', function(e) {
    plusDropdown.classList.toggle('show-menu');
    e.stopPropagation();
});

document.addEventListener('click', function() {
    plusDropdown.classList.remove('show-menu');
});
</script>
""", unsafe_allow_html=True)



with st.sidebar:
    st.markdown("<style>.stFileUploader {display:none !important;}</style>", unsafe_allow_html=True)
    uploaded_photo = st.file_uploader("", type=["png", "jpg", "jpeg"], key="imgUpload")
    uploaded_audio = st.file_uploader("", type=["mp3", "wav", "ogg"], key="audioUpload")
    uploaded_video = st.file_uploader("", type=["mp4", "mov", "avi"], key="videoUpload")
    uploaded_file = st.file_uploader("", type=["pdf", "txt", "csv", "xlsx", "zip"], key="fileUpload")


# ---------------- 🚀 ACTIVE TEXT INPUT (WITH RESET LOGIC) ----------------
def handle_input():
    if st.session_state.actual_clean_input:
        st.session_state.temp_prompt = st.session_state.actual_clean_input
        st.session_state.actual_clean_input = "" 

if st.session_state.suggestion_prompt:
    st.session_state.actual_clean_input = st.session_state.suggestion_prompt
    st.session_state.suggestion_prompt = "" 

user_text = st.text_input(
    "", 
    placeholder="Ask the AI Cosmos...", 
    label_visibility="collapsed", 
    key="actual_clean_input",
    on_change=handle_input
)


# ---------------- LOGIC PROCESSING ----------------
final_prompt = ""

if uploaded_photo:
    final_prompt = f"📁 [Uploaded Photo]: {uploaded_photo.name}"
    st.session_state.imgUpload = None # रिसेट
elif uploaded_audio:
    final_prompt = f"🎵 [Uploaded Audio]: {uploaded_audio.name}"
    st.session_state.audioUpload = None
elif uploaded_video:
    final_prompt = f"🎬 [Uploaded Video]: {uploaded_video.name}"
    st.session_state.videoUpload = None
elif uploaded_file:
    final_prompt = f"📄 [Uploaded File]: {uploaded_file.name}"
    st.session_state.fileUpload = None
# २. जर फाईल नसेल तर टाईप केलेला प्रश्न वाचू
elif st.session_state.temp_prompt:
    final_prompt = st.session_state.temp_prompt
    st.session_state.temp_prompt = ""

if final_prompt:
    messages.append({"role": "user", "content": final_prompt})

    if st.session_state.chats[chat_id]["title"] == "⚡ New Cosmic Orbit":
        st.session_state.chats[chat_id]["title"] = final_prompt[:20] + "..."

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": m["role"], "content": m["content"]} for m in messages]
        )
        reply = response.choices[0].message.content
    except Exception:
        reply = "⚠️ Space connection lost. Verify your Groq API Key."

    messages.append({"role": "assistant", "content": reply})
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
