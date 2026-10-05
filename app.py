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
)


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="KaiwaBuddy",
    page_icon="🇯🇵",
    layout="wide",
)


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #777;
        margin-bottom: 2rem;
    }

    .feature-card {
        padding: 1.4rem;
        border-radius: 16px;
        border: 1px solid #ddd;
        min-height: 150px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# STATE
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

    st.header("🇯🇵 KaiwaBuddy")

    st.caption(
        "Your Local AI Japanese Conversation Partner"
    )

    st.divider()

    st.subheader("📚 Learning")

    st.write("JLPT N5")
    st.write("Minna no Nihongo 1")
    st.write("Lesson 1")

    st.divider()

    st.subheader("🎯 Modes")

    if st.button(
        "💬 Conversation Mode",
        use_container_width=True
    ):

        st.session_state.practice_mode = False
        st.session_state.vocabulary_mode = False
        st.rerun()

    if st.button(
        "🎯 Practice Mode",
        use_container_width=True
    ):

        st.session_state.practice_mode = True
        st.session_state.vocabulary_mode = False

        if not st.session_state.practice_questions:

            st.session_state.practice_questions = (
                get_practice_questions()
            )

        st.rerun()

    if st.button(
        "📚 Vocabulary Mode",
        use_container_width=True
    ):

        st.session_state.vocabulary_mode = True
        st.session_state.practice_mode = False

        if not st.session_state.vocabulary_questions:

            st.session_state.vocabulary_questions = (
                get_vocabulary_questions()
            )

        st.rerun()

    st.divider()

    st.subheader("🤖 Technology")

    st.write("• Gemma 3 1B")
    st.write("• Ollama")
    st.write("• Streamlit")
    st.write("• Local inference")

    st.divider()

    st.info(
        "🔒 AI inference can run locally through Ollama."
    )

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.session_state.conversation_topic = None
        st.rerun()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🇯🇵 KaiwaBuddy</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your Local AI Japanese Conversation Partner'
    '</div>',
    unsafe_allow_html=True
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

        st.metric(
            "Your Score",
            f"{score} / {total}"
        )

        percentage = score / total * 100

        if percentage >= 80:
            st.success("Excellent! 🌟")

        elif percentage >= 60:
            st.info("Good job! Keep practicing.")

        else:
            st.warning("Keep practicing!")

        if st.button("🔄 Restart Practice"):

            st.session_state.practice_questions = (
                get_practice_questions()
            )

            st.session_state.practice_index = 0
            st.session_state.practice_score = 0
            st.session_state.practice_checked = False
            st.session_state.practice_result = None

            st.rerun()

        st.stop()

    question = questions[
        st.session_state.practice_index
    ]

    st.progress(
        (st.session_state.practice_index + 1)
        / total
    )

    st.write(
        f"Question "
        f"{st.session_state.practice_index + 1} / {total}"
    )

    st.subheader(question["question"])

    st.write(
        f"🇯🇵 **{question['japanese']}**"
    )

    answer = st.text_input(
        "Your answer:",
        key=f"practice_{st.session_state.practice_index}"
    )

    if not st.session_state.practice_checked:

        if st.button(
            "Check Answer",
            use_container_width=True
        ):

            result = check_practice_answer(
                answer,
                question
            )

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

            st.info(
                f"Correct answer: "
                f"{result['correct_answer']}"
            )

        st.write(result["explanation"])

        if st.button(
            "➡️ Next Question",
            use_container_width=True
        ):

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

        st.metric(
            "Your Score",
            f"{score} / {total}"
        )

        percentage = score / total * 100

        if percentage >= 80:
            st.success("Excellent vocabulary! 🌟")

        elif percentage >= 60:
            st.info("Good work!")

        else:
            st.warning("Review Lesson 1 vocabulary.")

        if st.button("🔄 Restart Vocabulary"):

            st.session_state.vocabulary_questions = (
                get_vocabulary_questions()
            )

            st.session_state.vocabulary_index = 0
            st.session_state.vocabulary_score = 0
            st.session_state.vocabulary_checked = False
            st.session_state.vocabulary_result = None

            st.rerun()

        st.stop()

    question = questions[
        st.session_state.vocabulary_index
    ]

    st.progress(
        (st.session_state.vocabulary_index + 1)
        / total
    )

    st.write(
        f"Question "
        f"{st.session_state.vocabulary_index + 1} / {total}"
    )

    mode = question.get(
        "mode",
        "jp_to_en"
    )

    if mode == "jp_to_en":

        st.subheader(
            f"🇯🇵 {question['japanese']}"
        )

        st.caption(
            "Translate this Japanese word into English."
        )

    else:

        st.subheader(
            f"🇬🇧 {question['english']}"
        )

        st.caption(
            "Translate this English word into Japanese."
        )

    answer = st.text_input(
        "Your answer:",
        key=f"vocab_{st.session_state.vocabulary_index}"
    )

    if not st.session_state.vocabulary_checked:

        if st.button(
            "Check Answer",
            use_container_width=True
        ):

            result = check_vocabulary_answer(
                answer,
                question
            )

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

            st.info(
                f"Correct answer: "
                f"{result['correct_answer']}"
            )

        if st.button(
            "➡️ Next Question",
            use_container_width=True
        ):

            st.session_state.vocabulary_index += 1
            st.session_state.vocabulary_checked = False
            st.session_state.vocabulary_result = None

            st.rerun()

    st.stop()


# ============================================================
# HOME
# ============================================================

if not st.session_state.messages:

    st.markdown("### 👋 Welcome to KaiwaBuddy!")

    st.write(
        "Practice beginner Japanese with a local AI "
        "conversation partner."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="feature-card">
            <h3>💬 Conversation Mode</h3>
            <p>
            Practice Japanese and receive meaning,
            grammar, explanations, corrections and
            follow-up questions.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="feature-card">
            <h3>🎯 Practice Mode</h3>
            <p>
            Test your Lesson 1 knowledge with
            interactive questions and scoring.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col3, col4 = st.columns(2)

    with col3:

        st.markdown(
            """
            <div class="feature-card">
            <h3>📚 Vocabulary Mode</h3>
            <p>
            Practice Japanese ↔ English vocabulary.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            """
            <div class="feature-card">
            <h3>🔒 Local AI</h3>
            <p>
            Powered by Gemma 3 1B through Ollama.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("📖 Lesson 1")

    tab1, tab2, tab3 = st.tabs(
        [
            "Vocabulary",
            "Grammar Patterns",
            "Grammar Notes"
        ]
    )

    with tab1:

        for item in LESSON_1_VOCABULARY:

            st.write(
                f"**{item['japanese']}** — "
                f"{item['english']}"
            )

    with tab2:

        for item in LESSON_1_PATTERNS:

            st.markdown(
                f"**{item['pattern']}**"
            )

            st.write(item["meaning"])

            st.caption(
                f"Example: {item['example']}"
            )

    with tab3:

        for item in LESSON_1_GRAMMAR:

            st.markdown(
                f"**{item['title']}**"
            )

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

                    st.markdown("### 🇬🇧 Meaning")

                    st.write(
                        data["meaning"]
                    )

                if data.get("grammar"):

                    st.markdown("### 🧩 Grammar")

                    st.write(
                        data["grammar"]
                    )

                if data.get("explanation"):

                    st.markdown("### 💡 Explanation")

                    st.write(
                        data["explanation"]
                    )

                if data.get("correction"):

                    st.markdown("### ✏️ Correction")

                    st.code(
                        data["correction"]
                    )

                if data.get("followup"):

                    st.markdown("### 💬 Follow-up")

                    st.info(
                        data["followup"]
                    )


# ============================================================
# CHAT
# ============================================================

user_input = st.chat_input(
    "Type a Japanese sentence..."
)


if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    result = None

    # --------------------------------------------------------
    # 1. Conversation answer
    # --------------------------------------------------------

    if st.session_state.conversation_topic:

        result = analyze_conversation_answer(
            user_input,
            st.session_state.conversation_topic
        )

        if result:

            st.session_state.conversation_topic = (
                result.get("next_topic")
            )

    # --------------------------------------------------------
    # 2. Mistake detector
    # --------------------------------------------------------

    if result is None:

        result = check_common_mistake(
            user_input
        )

    # --------------------------------------------------------
    # 3. Known sentence
    # --------------------------------------------------------

    if result is None:

        result = check_known_sentence(
            user_input
        )

    # --------------------------------------------------------
    # 4. Vocabulary
    # --------------------------------------------------------

    if result is None:

        result = analyze_vocabulary(
            user_input
        )

    # --------------------------------------------------------
    # 5. N は N です
    # --------------------------------------------------------

    if result is None:

        result = analyze_noun_desu(
            user_input
        )

    # --------------------------------------------------------
    # 6. N1 の N2
    # --------------------------------------------------------

    if result is None:

        result = analyze_no_pattern(
            user_input
        )

    # --------------------------------------------------------
    # 7. N も N です
    # --------------------------------------------------------

    if result is None:

        result = analyze_mo_pattern(
            user_input
        )

    # --------------------------------------------------------
    # 8. N は N じゃありません
    # --------------------------------------------------------

    if result is None:

        result = analyze_noun_janai(
            user_input
        )

    # --------------------------------------------------------
    # 9. N は N ですか
    # --------------------------------------------------------

    if result is None:

        result = analyze_question(
            user_input
        )

    # --------------------------------------------------------
    # 10. Gemma fallback
    # --------------------------------------------------------

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
                        "content": prompt
                    }
                ]
            )

            ai_text = response[
                "message"
            ][
                "content"
            ]

            result = {
                "type": "ai",
                "meaning": ai_text,
                "grammar": "Gemma 3 1B fallback",
                "explanation": (
                    "This sentence was not recognized "
                    "by the Lesson 1 rule engine, so "
                    "the local AI model provided a "
                    "general explanation."
                ),
                "followup": None,
            }

        except Exception as e:

            result = {
                "type": "error",
                "meaning": (
                    "I couldn't connect to the local AI model."
                ),
                "grammar": "Ollama connection",
                "explanation": str(e),
                "followup": (
                    "Make sure Ollama is running."
                ),
            }

    # --------------------------------------------------------
    # Save result
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "",
            "data": result
        }
    )

    st.rerun()