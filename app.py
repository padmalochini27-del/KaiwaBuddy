
import streamlit as st
import ollama

from japanese_n5 import (
    LESSON_1_VOCABULARY,
    LESSON_1_PATTERNS,
    LESSON_1_GRAMMAR,
    analyze_vocabulary,
    analyze_noun_desu,
    analyze_no_pattern,
    analyze_mo_pattern,
    analyze_noun_janai,
    analyze_question,
    check_common_mistake,
    analyze_conversation_answer,
    check_known_sentence,
    get_practice_questions,
    check_practice_answer,
    get_vocabulary_questions,
    check_vocabulary_answer,
    analyze_japanese_script,
)

# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="KaiwaBuddy",
    page_icon="🌸",
    layout="wide",
)

# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>
    /* Main application */
    .stApp {
        background: #FBF8F3 !important;
        color: #493F43;
        font-family: "Segoe UI", "Noto Sans", sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(251, 248, 243, 0.96) !important;
    }

    .block-container {
        max-width: 940px;
        padding-top: 1.5rem;
        padding-bottom: 7rem;
    }

    h1, h2, h3, h4 {
        color: #493F43 !important;
        letter-spacing: -0.02em;
    }

    p, li, label,
    [data-testid="stMarkdownContainer"] {
        color: #5F5558;
    }

    [data-testid="stCaptionContainer"] {
        color: #8A7C80;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #F3EFE8 !important;
        border-right: 1px solid #E7DED7;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.25rem;
    }

    .brand-row {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 0 18px;
    }

    .brand-flower {
        width: 48px;
        height: 48px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #F1DFDB;
        font-size: 26px;
    }

    .brand-name {
        color: #493F43;
        font-size: 1.42rem;
        font-weight: 760;
        line-height: 1.2;
    }

    .brand-subtitle {
        color: #87777B;
        font-size: 0.78rem;
        margin-top: 4px;
    }

    .sidebar-label {
        color: #9A777B;
        font-size: 0.72rem;
        font-weight: 750;
        letter-spacing: 0.11em;
        text-transform: uppercase;
        margin: 6px 0 10px;
    }

    /* Welcome banner */
    .welcome-card {
        background: linear-gradient(
            125deg,
            #F6E9E4 0%,
            #F8F1E8 54%,
            #EEF2E8 100%
        );
        border: 1px solid #EADBD5;
        border-radius: 23px;
        padding: 25px 28px;
        margin: 0 0 22px;
    }

    .welcome-eyebrow {
        color: #9A6B73;
        font-size: 0.73rem;
        font-weight: 750;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .welcome-title {
        color: #493F43;
        font-size: clamp(1.8rem, 4vw, 2.45rem);
        font-weight: 780;
        line-height: 1.2;
        margin-bottom: 9px;
    }

    .welcome-copy {
        color: #74666A;
        font-size: 0.98rem;
        line-height: 1.7;
        max-width: 650px;
    }

    .welcome-japanese {
        color: #9A6B73;
        font-size: 1.1rem;
        font-weight: 650;
        margin-top: 15px;
    }

    .pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 17px;
    }

    .soft-pill {
        display: inline-block;
        padding: 7px 11px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 650;
    }

    .pill-lilac {
        background: #F0E6F5;
        color: #765E83;
    }

    .pill-sage {
        background: #DFEADF;
        color: #4D6A50;
    }

    /* Home feature cards */
    .feature-card {
        background: #FFFFFF;
        border: 1px solid #EDE3DE;
        border-radius: 17px;
        padding: 18px;
        min-height: 135px;
        box-shadow: 0 4px 14px rgba(91, 66, 70, 0.035);
    }

    .feature-icon {
        font-size: 1.45rem;
        margin-bottom: 8px;
    }

    .feature-title {
        color: #493F43;
        font-weight: 730;
        margin-bottom: 7px;
    }

    .feature-copy {
        color: #827479;
        font-size: 0.88rem;
        line-height: 1.6;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        min-height: 42px;
        font-weight: 620;
        border: 1px solid #E4D6D1;
    }

    .stButton > button[kind="primary"] {
        background: #9A6B73 !important;
        color: #FFFFFF !important;
        border-color: #9A6B73 !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: #855861 !important;
        border-color: #855861 !important;
        color: #FFFFFF !important;
    }

    .stButton > button[kind="secondary"] {
        background: #FFFFFF !important;
        color: #594B4F !important;
    }

    .stButton > button[kind="secondary"]:hover {
        background: #F7EEEA !important;
        border-color: #D9BFC0 !important;
        color: #493F43 !important;
    }

    /* Regular text inputs */
    .stTextInput input,
    .stTextArea textarea {
        background: #FFFFFF !important;
        color: #493F43 !important;
        border: 1px solid #E5D9D4 !important;
        border-radius: 13px !important;
        caret-color: #9A6B73 !important;
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #9A8C90 !important;
        opacity: 1 !important;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        border: 1px solid #EADFD9;
        border-radius: 18px;
        padding: 14px 17px;
        margin-bottom: 12px;
        background: #FFFFFF;
    }

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {
        background: #E3EEE2;
        border-color: #D4E2D2;
    }

    /* ========================================================
       CHAT INPUT: REMOVE THE DARK BLUE/BLACK BACKGROUND
       ======================================================== */

    /* Bottom fixed input region */
    [data-testid="stBottom"],
    [data-testid="stBottomBlockContainer"],
    .stChatInput {
        background: #FBF8F3 !important;
        background-color: #FBF8F3 !important;
        box-shadow: none !important;
    }

    [data-testid="stBottom"] {
        border-top: none !important;
    }

    [data-testid="stBottomBlockContainer"] {
        padding-top: 12px !important;
        padding-bottom: 18px !important;
    }

    /* Chat input outer wrapper */
    [data-testid="stChatInput"] {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Inner input container */
    [data-testid="stChatInput"] > div {
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border: 1px solid #D8CBBE !important;
        border-radius: 22px !important;
        box-shadow: none !important;
    }

    /* Actual typing field */
    [data-testid="stChatInput"] textarea {
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #51483F !important;
        caret-color: #82977B !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }

    /* Placeholder */
    [data-testid="stChatInput"] textarea::placeholder {
        color: #A7978B !important;
        opacity: 1 !important;
    }

    /* Focus state */
    [data-testid="stChatInput"]:focus-within,
    [data-testid="stChatInput"] > div:focus-within {
        border-color: #9CAF91 !important;
        box-shadow: 0 0 0 2px rgba(156, 175, 145, 0.15) !important;
    }

    /* Send button */
    [data-testid="stChatInput"] button {
        background: #82977B !important;
        background-color: #82977B !important;
        color: #FFFFFF !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: none !important;
    }

    [data-testid="stChatInput"] button:hover {
        background: #6F8768 !important;
        background-color: #6F8768 !important;
        color: #FFFFFF !important;
    }

    [data-testid="stChatInput"] button:disabled {
        background: #DCE5D8 !important;
        color: #FFFFFF !important;
    }

    /* Prevent dark backgrounds on chat composer descendants */
    [data-testid="stBottom"] div,
    [data-testid="stBottomBlockContainer"] div {
        scrollbar-color: #D8CBBE #FBF8F3;
    }

    /* Other elements */
    [data-testid="stAlert"] {
        border-radius: 13px;
    }

    [data-baseweb="tab-list"] {
        gap: 7px;
    }

    [data-baseweb="tab"] {
        color: #74666A;
    }

    [aria-selected="true"][data-baseweb="tab"] {
        color: #8C5F67 !important;
    }

    [data-testid="stProgressBar"] > div {
        background: #F0E4DF;
        border-radius: 99px;
    }

    [data-testid="stProgressBar"] > div > div {
        background: #A8B99F;
        border-radius: 99px;
    }

    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #EDE3DE;
        padding: 15px;
        border-radius: 15px;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"] {
        color: #493F43;
    }

    hr {
        border-color: #E8DDD7;
    }

    @media (max-width: 700px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }

        .welcome-card {
            padding: 21px 18px;
            border-radius: 18px;
        }

        .feature-card {
            min-height: 0;
            padding: 15px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "messages": [],
    "conversation_topic": None,
    "practice_mode": False,
    "practice_questions": [],
    "practice_index": 0,
    "practice_score": 0,
    "practice_checked": False,
    "practice_result": None,
    "vocabulary_mode": False,
    "vocabulary_questions": [],
    "vocabulary_index": 0,
    "vocabulary_score": 0,
    "vocabulary_checked": False,
    "vocabulary_result": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div class="brand-row">
            <div class="brand-flower">🌸</div>
            <div>
                <div class="brand-name">KaiwaBuddy</div>
                <div class="brand-subtitle">Your Japanese study space</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-label">YOUR LEARNING PATH</div>',
        unsafe_allow_html=True,
    )

    st.write("JLPT N5")
    st.write("Minna no Nihongo 1")
    st.write("Lesson 1")

    st.divider()

    st.markdown(
        '<div class="sidebar-label">LEARNING MODES</div>',
        unsafe_allow_html=True,
    )

    if st.button("💬 Conversation Mode", use_container_width=True):
        st.session_state.practice_mode = False
        st.session_state.vocabulary_mode = False
        st.rerun()

    if st.button("🎯 Practice Mode", use_container_width=True):
        st.session_state.practice_mode = True
        st.session_state.vocabulary_mode = False

        if not st.session_state.practice_questions:
            st.session_state.practice_questions = get_practice_questions()

        st.rerun()

    if st.button("📚 Vocabulary Mode", use_container_width=True):
        st.session_state.vocabulary_mode = True
        st.session_state.practice_mode = False

        if not st.session_state.vocabulary_questions:
            st.session_state.vocabulary_questions = get_vocabulary_questions()

        st.rerun()

    st.divider()

    st.markdown(
        '<div class="sidebar-label">POWERED BY</div>',
        unsafe_allow_html=True,
    )

    st.caption("Gemma 3 1B · Ollama · Streamlit")
    st.caption("AI responses can run locally through Ollama.")

    st.divider()

    st.info("🔒 AI inference can run locally through Ollama.")

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.conversation_topic = None
        st.rerun()

# ============================================================
# WELCOME HEADER
# ============================================================

st.markdown(
    """
    <div class="welcome-card">
        <div class="welcome-eyebrow">A LITTLE JAPANESE, EVERY DAY</div>
        <div class="welcome-title">こんにちは！</div>
        <div class="welcome-copy">
            Let's practice Japanese together. Write a sentence,
            explore its meaning, and learn one small grammar point
            at a time.
        </div>
        <div class="welcome-japanese">
            Konnichiwa · Let's learn together 🌸
        </div>
        <div class="pill-row">
            <span class="soft-pill pill-lilac">📖 Lesson 1</span>
            <span class="soft-pill pill-sage">🌱 Beginner · N5</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# PRACTICE MODE
# ============================================================

if st.session_state.practice_mode:
    st.subheader("🎯 Practice Mode")

    questions = st.session_state.practice_questions

    if not questions:
        questions = get_practice_questions()
        st.session_state.practice_questions = questions

    total = len(questions)

    if st.session_state.practice_index >= total:
        st.success("🎉 Practice completed!")

        score = st.session_state.practice_score
        st.metric("Your Score", f"{score} / {total}")

        percentage = score / total * 100 if total else 0

        if percentage >= 80:
            st.success("Excellent! 🌟")
        elif percentage >= 60:
            st.info("Good job! Keep practicing.")
        else:
            st.warning("Keep practicing!")

        if st.button("🔄 Restart Practice"):
            st.session_state.practice_questions = get_practice_questions()
            st.session_state.practice_index = 0
            st.session_state.practice_score = 0
            st.session_state.practice_checked = False
            st.session_state.practice_result = None
            st.rerun()

        st.stop()

    question = questions[st.session_state.practice_index]

    st.progress((st.session_state.practice_index + 1) / total)

    st.write(
        f"Question {st.session_state.practice_index + 1} / {total}"
    )

    st.subheader(question["question"])
    st.write(f"🇯🇵 **{question['japanese']}**")

    answer = st.text_input(
        "Your answer:",
        key=f"practice_{st.session_state.practice_index}",
    )

    if not st.session_state.practice_checked:
        if st.button("Check Answer", use_container_width=True):
            result = check_practice_answer(answer, question)

            st.session_state.practice_result = result
            st.session_state.practice_checked = True

            if result["correct"]:
                st.session_state.practice_score += 1

            st.rerun()

    else:
        result = st.session_state.practice_result

        if result["correct"]:
            st.success(result["message"])
        else:
            st.error(result["message"])
            st.info(f"Correct answer: {result['correct_answer']}")

        st.write(result["explanation"])

        if st.button("➡️ Next Question", use_container_width=True):
            st.session_state.practice_index += 1
            st.session_state.practice_checked = False
            st.session_state.practice_result = None
            st.rerun()

    st.stop()

# ============================================================
# VOCABULARY MODE
# ============================================================

if st.session_state.vocabulary_mode:
    st.subheader("📚 Vocabulary Mode")

    questions = st.session_state.vocabulary_questions

    if not questions:
        questions = get_vocabulary_questions()
        st.session_state.vocabulary_questions = questions

    total = len(questions)

    if st.session_state.vocabulary_index >= total:
        st.success("🎉 Vocabulary practice completed!")

        score = st.session_state.vocabulary_score
        st.metric("Your Score", f"{score} / {total}")

        percentage = score / total * 100 if total else 0

        if percentage >= 80:
            st.success("Excellent vocabulary! 🌟")
        elif percentage >= 60:
            st.info("Good work!")
        else:
            st.warning("Review Lesson 1 vocabulary.")

        if st.button("🔄 Restart Vocabulary"):
            st.session_state.vocabulary_questions = get_vocabulary_questions()
            st.session_state.vocabulary_index = 0
            st.session_state.vocabulary_score = 0
            st.session_state.vocabulary_checked = False
            st.session_state.vocabulary_result = None
            st.rerun()

        st.stop()

    question = questions[st.session_state.vocabulary_index]

    st.progress((st.session_state.vocabulary_index + 1) / total)

    st.write(
        f"Question {st.session_state.vocabulary_index + 1} / {total}"
    )

    mode = question.get("mode", "jp_to_en")

    if mode == "jp_to_en":
        st.subheader(f"🇯🇵 {question['japanese']}")
        st.caption("Translate this Japanese word into English.")
    else:
        st.subheader(f"🇬🇧 {question['english']}")
        st.caption("Translate this English word into Japanese.")

    answer = st.text_input(
        "Your answer:",
        key=f"vocab_{st.session_state.vocabulary_index}",
    )

    if not st.session_state.vocabulary_checked:
        if st.button("Check Answer", use_container_width=True):
            result = check_vocabulary_answer(answer, question)

            st.session_state.vocabulary_result = result
            st.session_state.vocabulary_checked = True

            if result["correct"]:
                st.session_state.vocabulary_score += 1

            st.rerun()

    else:
        result = st.session_state.vocabulary_result

        if result["correct"]:
            st.success(result["message"])
        else:
            st.error(result["message"])
            st.info(f"Correct answer: {result['correct_answer']}")

        if st.button("➡️ Next Question", use_container_width=True):
            st.session_state.vocabulary_index += 1
            st.session_state.vocabulary_checked = False
            st.session_state.vocabulary_result = None
            st.rerun()

    st.stop()

# ============================================================
# HOME
# ============================================================

if not st.session_state.messages:
    st.markdown("### Your learning space")

    st.caption(
        "Choose a mode from the sidebar, or start a conversation below."
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">💬</div>
                <div class="feature-title">Conversation practice</div>
                <div class="feature-copy">
                    Explore meaning, grammar, corrections, and follow-up
                    questions with your Japanese learning partner.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🌸</div>
                <div class="feature-title">A gentle learning pace</div>
                <div class="feature-copy">
                    Start with simple sentences and build confidence
                    one lesson at a time.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("📖 Open the Lesson 1 quick reference"):
        tab1, tab2, tab3 = st.tabs(
            ["Vocabulary", "Grammar patterns", "Grammar notes"]
        )

        with tab1:
            for item in LESSON_1_VOCABULARY:
                st.write(
                    f"**{item['japanese']}** — {item['english']}"
                )

        with tab2:
            for item in LESSON_1_PATTERNS:
                st.markdown(f"**{item['pattern']}**")
                st.write(item["meaning"])
                st.caption(f"Example: {item['example']}")
                st.divider()

        with tab3:
            for item in LESSON_1_GRAMMAR:
                st.markdown(f"**{item['title']}**")
                st.write(item["explanation"])
                st.divider()

# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.write(message["content"])
        else:
            data = message.get("data")

            if data:
                if data.get("meaning"):
                    st.markdown("**🇬🇧 Meaning**")
                    st.write(data["meaning"])

                if data.get("grammar"):
                    st.markdown("**🧩 Grammar**")
                    st.write(data["grammar"])

                if data.get("explanation"):
                    st.markdown("**💡 Explanation**")
                    st.write(data["explanation"])

                if data.get("correction"):
                    st.markdown("**✏️ Correction**")
                    st.code(data["correction"])

                if data.get("followup"):
                    st.markdown("**💬 Try this next**")
                    st.info(data["followup"])

# ============================================================
# CHAT INPUT AND JAPANESE ANALYSIS
# ============================================================

user_input = st.chat_input(
    "Type your Japanese or English message… 例：わたしはがくせいです"
)

if user_input:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    result = None

    # 1. Conversation answer
    if st.session_state.conversation_topic:
        result = analyze_conversation_answer(
            user_input,
            st.session_state.conversation_topic,
        )

        if result:
            st.session_state.conversation_topic = result.get("next_topic")

    # 2. Common mistake detection
    if result is None:
        result = check_common_mistake(user_input)

    # 3. Known sentence
    if result is None:
        result = check_known_sentence(user_input)

    # 4. Vocabulary
    if result is None:
        result = analyze_vocabulary(user_input)

    # 5. N は N です
    if result is None:
        result = analyze_noun_desu(user_input)

    # 6. N1 の N2
    if result is None:
        result = analyze_no_pattern(user_input)

    # 7. N も N です
    if result is None:
        result = analyze_mo_pattern(user_input)

    # 8. N は N じゃありません
    if result is None:
        result = analyze_noun_janai(user_input)

    # 9. N は N ですか
    if result is None:
        result = analyze_question(user_input)

    # 10. Japanese script recognition
    if result is None:
        result = analyze_japanese_script(user_input)

    # 11. Local AI fallback
    if result is None:
        prompt = f"""
You are KaiwaBuddy, a beginner Japanese learning assistant.

The learner is studying beginner JLPT N5 Japanese.

User sentence:
{user_input}

Give a short and careful explanation.

Return:

MEANING:
The likely English meaning.

GRAMMAR:
A short grammar observation.

EXPLANATION:
A simple explanation.

FOLLOWUP:
One simple practice question.

Rules:
- Do not invent Japanese meanings.
- Do not claim uncertain meanings as facts.
- Keep explanations beginner-friendly.
- Do not pretend everything is from Minna no Nihongo Lesson 1.
"""

        try:
            response = ollama.chat(
                model="gemma3:1b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            ai_text = response["message"]["content"]

            result = {
                "type": "ai",
                "meaning": ai_text,
                "grammar": "Gemma 3 1B fallback",
                "explanation": (
                    "This sentence was not recognized by the Lesson 1 "
                    "rule engine, so the local AI model provided a "
                    "general explanation."
                ),
                "followup": None,
            }

        except Exception:
            result = {
                "type": "error",
                "meaning": "I couldn't connect to the local AI model.",
                "grammar": "Ollama connection",
                "explanation": (
                    "Check that Ollama is running and that the "
                    "gemma3:1b model is installed."
                ),
                "followup": "Make sure Ollama is running, then try again.",
            }

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "",
            "data": result,
        }
    )

    st.rerun()
