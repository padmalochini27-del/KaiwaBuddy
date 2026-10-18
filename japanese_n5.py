
# ============================================================
# KaiwaBuddy - Japanese N5 Learning Engine
# ============================================================

import re
import random


# ============================================================
# LESSON 1 VOCABULARY
# ============================================================

LESSON_1_VOCABULARY = [
    {"japanese": "watashi", "english": "I"},
    {"japanese": "watashitachi", "english": "we"},
    {"japanese": "anata", "english": "you"},
    {"japanese": "ano hito", "english": "that person / he / she"},
    {"japanese": "minasan", "english": "everyone"},
    {"japanese": "sensei", "english": "teacher / instructor"},
    {"japanese": "kyoushi", "english": "teacher / instructor"},
    {"japanese": "gakusei", "english": "student"},
    {"japanese": "kaishain", "english": "company employee"},
    {"japanese": "shain", "english": "employee"},
    {"japanese": "ginkouin", "english": "bank employee"},
    {"japanese": "isha", "english": "doctor"},
    {"japanese": "kenkyuusha", "english": "researcher"},
    {"japanese": "enjinia", "english": "engineer"},
    {"japanese": "daigaku", "english": "university"},
    {"japanese": "byouin", "english": "hospital"},
    {"japanese": "denki", "english": "electricity / electric light"},
    {"japanese": "dare", "english": "who"},
    {"japanese": "sai", "english": "years old"},
    {"japanese": "nansai", "english": "how old"},
    {"japanese": "hai", "english": "yes"},
    {"japanese": "iie", "english": "no"},
]


# ============================================================
# LESSON 1 GRAMMAR
# ============================================================

LESSON_1_PATTERNS = [
    {
        "pattern": "N は N です",
        "meaning": "N is N.",
        "example": "Watashi wa gakusei desu."
    },
    {
        "pattern": "N は N じゃありません",
        "meaning": "N is not N.",
        "example": "Watashi wa gakusei ja arimasen."
    },
    {
        "pattern": "N は N ですか",
        "meaning": "Is N N?",
        "example": "Anata wa gakusei desu ka."
    },
    {
        "pattern": "N も N です",
        "meaning": "N is also N.",
        "example": "Watashi mo gakusei desu."
    },
    {
        "pattern": "N1 の N2",
        "meaning": "N2 related to / belonging to N1.",
        "example": "Daigaku no gakusei."
    },
]


LESSON_1_GRAMMAR = [
    {
        "title": "N は N です",
        "explanation": (
            "は (wa) marks the topic. "
            "です makes a polite statement after a noun."
        )
    },
    {
        "title": "N は N じゃありません",
        "explanation": (
            "じゃありません is the negative form of です "
            "for noun sentences."
        )
    },
    {
        "title": "S か",
        "explanation": (
            "か is used at the end of a sentence to make a question."
        )
    },
    {
        "title": "N も",
        "explanation": (
            "も means 'also' and can replace は."
        )
    },
    {
        "title": "N1 の N2",
        "explanation": (
            "の connects two nouns and shows a relationship between them."
        )
    },
]


# ============================================================
# KNOWN NOUNS
# ============================================================

LESSON_1_NOUNS = {
    "watashi": "I",
    "watashitachi": "we",
    "anata": "you",
    "ano hito": "that person / he / she",
    "minasan": "everyone",
    "sensei": "teacher / instructor",
    "kyoushi": "teacher / instructor",
    "gakusei": "student",
    "kaishain": "company employee",
    "shain": "employee",
    "ginkouin": "bank employee",
    "isha": "doctor",
    "kenkyuusha": "researcher",
    "enjinia": "engineer",
    "daigaku": "university",
    "byouin": "hospital",
    "denki": "electricity / electric light",
    "dare": "who",
}


# ============================================================
# KNOWN SENTENCES
# ============================================================

KNOWN_SENTENCES = {
    "watashi wa gakusei desu": {
        "meaning": "I am a student.",
        "grammar": "N は N です",
        "explanation": (
            "Watashi means 'I' and gakusei means 'student'. "
            "は marks the topic and です makes a polite statement."
        ),
    },

    "watashi wa sensei desu": {
        "meaning": "I am a teacher.",
        "grammar": "N は N です",
        "explanation": (
            "Watashi means 'I' and sensei means 'teacher / instructor'."
        ),
    },

    "watashi wa isha desu": {
        "meaning": "I am a doctor.",
        "grammar": "N は N です",
        "explanation": (
            "Watashi means 'I' and isha means 'doctor'."
        ),
    },

    "watashi wa kaishain desu": {
        "meaning": "I am a company employee.",
        "grammar": "N は N です",
        "explanation": (
            "Watashi means 'I' and kaishain means 'company employee'."
        ),
    },
}


# ============================================================
# NORMALIZATION
# ============================================================

def normalize(text):
    text = text.lower().strip()

    text = text.replace(",", "")
    text = text.replace("。", "")
    text = text.replace("?", "")
    text = text.replace("？", "")
    text = text.replace(".", "")

    text = re.sub(r"\s+", " ", text)

    return text


def _script_normalize(text):
    return re.sub(r"[\s。！!？?、,]", "", str(text).strip())


# ============================================================
# SAFE FOLLOW-UP QUESTIONS
# ============================================================

def get_safe_followup(topic):
    options = {
        "gakusei": [
            "Anata wa gakusei desu ka?",
            "Gakusei desu ka?",
        ],
        "sensei": ["Anata wa sensei desu ka?"],
        "isha": ["Anata wa isha desu ka?"],
        "kaishain": ["Anata wa kaishain desu ka?"],
    }

    return random.choice(
        options.get(
            topic,
            ["Can you make another simple Japanese sentence?"],
        )
    )


# ============================================================
# VOCABULARY ANALYSIS
# ============================================================

def analyze_vocabulary(text):
    normalized = normalize(text)

    for item in LESSON_1_VOCABULARY:
        if normalized == normalize(item["japanese"]):
            return {
                "type": "vocabulary",
                "meaning": item["english"],
                "grammar": "Vocabulary",
                "explanation": (
                    f"{item['japanese']} means "
                    f"'{item['english']}'."
                ),
                "followup": (
                    f"Try using '{item['japanese']}' in a sentence."
                ),
            }

    return None


# ============================================================
# N は N です
# ============================================================

def analyze_noun_desu(text):
    normalized = normalize(text)

    match = re.fullmatch(
        r"(.+?) wa (.+?) desu",
        normalized,
    )

    if not match:
        return None

    subject, predicate = match.groups()

    if (
        subject not in LESSON_1_NOUNS
        or predicate not in LESSON_1_NOUNS
    ):
        return None

    return {
        "type": "grammar",
        "meaning": (
            f"{LESSON_1_NOUNS[subject]} is "
            f"{LESSON_1_NOUNS[predicate]}."
        ),
        "grammar": "N は N です",
        "explanation": (
            f"'{subject}' is the topic and "
            f"'{predicate}' describes it. "
            "は (wa) marks the topic; です makes "
            "a polite statement."
        ),
        "followup": get_safe_followup(predicate),
        "next_topic": None,
    }


# ============================================================
# N は N じゃありません
# ============================================================

def analyze_noun_janai(text):
    normalized = normalize(text)

    match = re.fullmatch(
        r"(.+?) wa (.+?) "
        r"(?:ja arimasen|jaarimasen|dewa arimasen)",
        normalized,
    )

    if not match:
        return None

    subject, predicate = match.groups()

    if (
        subject not in LESSON_1_NOUNS
        or predicate not in LESSON_1_NOUNS
    ):
        return None

    return {
        "type": "grammar",
        "meaning": (
            f"{LESSON_1_NOUNS[subject]} is not "
            f"{LESSON_1_NOUNS[predicate]}."
        ),
        "grammar": "N は N じゃありません",
        "explanation": (
            "じゃありません is the polite negative form "
            "used in noun sentences. "
            "ではありません (dewa arimasen) is a more "
            "formal alternative."
        ),
        "followup": get_safe_followup(predicate),
        "next_topic": None,
    }

# ============================================================
# N は N ですか
# ============================================================

def analyze_question(text):
    normalized = normalize(text)

    match = re.fullmatch(
        r"(.+?) wa (.+?) desu ka",
        normalized,
    )

    if not match:
        return None

    subject, predicate = match.groups()

    if (
        subject not in LESSON_1_NOUNS
        or predicate not in LESSON_1_NOUNS
    ):
        return None

    return {
        "type": "question",
        "meaning": (
            f"Is {LESSON_1_NOUNS[subject]} "
            f"{LESSON_1_NOUNS[predicate]}?"
        ),
        "grammar": "N は N ですか",
        "explanation": (
            "か at the end of the sentence makes it a question."
        ),
        "followup": get_safe_followup(predicate),
        "next_topic": None,
    }


# ============================================================
# N も N です
# ============================================================

def analyze_mo_pattern(text):
    normalized = normalize(text)

    match = re.fullmatch(
        r"(.+?) mo (.+?) desu",
        normalized,
    )

    if not match:
        return None

    subject, predicate = match.groups()

    if (
        subject not in LESSON_1_NOUNS
        or predicate not in LESSON_1_NOUNS
    ):
        return None

    return {
        "type": "grammar",
        "meaning": (
            f"{LESSON_1_NOUNS[subject]} is also "
            f"{LESSON_1_NOUNS[predicate]}."
        ),
        "grammar": "N も N です",
        "explanation": (
            "も (mo) means 'also' or 'too' and replaces は "
            "when saying something is also true."
        ),
        "followup": get_safe_followup(predicate),
        "next_topic": None,
    }


# ============================================================
# N1 の N2
# ============================================================

def analyze_no_pattern(text):
    normalized = normalize(text)

    match = re.fullmatch(r"(.+?) no (.+)", normalized)

    if not match:
        return None

    first, second = match.groups()

    if (
        first not in LESSON_1_NOUNS
        or second not in LESSON_1_NOUNS
    ):
        return None

    return {
        "type": "grammar",
        "meaning": (
            f"{LESSON_1_NOUNS[second]} related to "
            f"{LESSON_1_NOUNS[first]}."
        ),
        "grammar": "N1 の N2",
        "explanation": (
            "の (no) connects nouns and can show possession, "
            "affiliation, or another relationship."
        ),
        "followup": "Try making another sentence using 'no'.",
        "next_topic": None,
    }


# ============================================================
# COMMON MISTAKE CHECKER
# ============================================================

def check_common_mistake(text):
    normalized = normalize(text)

    if (
        "gakusei ja arimasen" in normalized
        and "watashi wa" in normalized
    ):
        return {
            "type": "grammar",
            "meaning": "I am not a student.",
            "grammar": "N は N じゃありません",
            "explanation": (
                "じゃありません is the polite negative form "
                "of です for noun sentences."
            ),
            "followup": "Anata wa gakusei desu ka?",
            "next_topic": None,
        }

    if (
        "gakusei desu" in normalized
        and "watashi mo" in normalized
    ):
        return {
            "type": "grammar",
            "meaning": "I am also a student.",
            "grammar": "N も N です",
            "explanation": (
                "も means 'also' or 'too' and replaces は "
                "in this pattern."
            ),
            "followup": "Anata mo gakusei desu ka?",
            "next_topic": None,
        }

    return None


# ============================================================
# CONVERSATION ANSWERS
# ============================================================

def analyze_conversation_answer(text, expected_topic):
    normalized = normalize(text)

    for item in LESSON_1_VOCABULARY:
        word = normalize(item["japanese"])

        if (
            word
            and word in normalized
            and (
                normalized.startswith("hai")
                or normalized.startswith("watashi wa")
                or normalized == word
            )
        ):
            return {
                "type": "conversation",
                "meaning": f"Yes, {item['english']}.",
                "grammar": "Conversation answer",
                "explanation": (
                    f"'{item['japanese']}' means "
                    f"'{item['english']}'."
                ),
                "followup": get_safe_followup(word),
                "next_topic": None,
            }

    if normalized == "iie":
        return {
            "type": "conversation",
            "meaning": "No.",
            "grammar": "はい / いいえ",
            "explanation": "いいえ (iie) means 'no'.",
            "followup": "Try another simple answer.",
            "next_topic": None,
        }

    return None

# ============================================================
# KNOWN ROMAJI SENTENCES
# ============================================================

def check_known_sentence(text):
    normalized = normalize(text)

    if normalized not in KNOWN_SENTENCES:
        return None

    result = KNOWN_SENTENCES[normalized].copy()
    result["type"] = "known_sentence"

    if "gakusei" in normalized:
        result["followup"] = get_safe_followup("gakusei")
    elif "sensei" in normalized:
        result["followup"] = get_safe_followup("sensei")
    elif "isha" in normalized:
        result["followup"] = get_safe_followup("isha")
    else:
        result["followup"] = get_safe_followup("kaishain")

    return result


# ============================================================
# PRACTICE MODE
# ============================================================

PRACTICE_QUESTIONS = [
    {
        "question": "What is your name?",
        "japanese": "おなまえは？",
        "accepted": [
            "watashi wa padma desu",
            "watashi wa padma lochini desu",
        ],
    },
    {
        "question": "Are you a student?",
        "japanese": "がくせいですか。",
        "accepted": [
            "hai",
            "hai desu",
            "hai gakusei desu",
            "watashi wa gakusei desu",
        ],
    },
    {
        "question": "Are you a teacher?",
        "japanese": "せんせいですか。",
        "accepted": [
            "hai",
            "hai desu",
            "hai sensei desu",
            "watashi wa sensei desu",
        ],
    },
    {
        "question": "Are you a doctor?",
        "japanese": "いしゃですか。",
        "accepted": [
            "hai",
            "hai desu",
            "hai isha desu",
            "watashi wa isha desu",
        ],
    },
    {
        "question": "Are you a company employee?",
        "japanese": "かいしゃいんですか。",
        "accepted": [
            "hai",
            "hai desu",
            "hai kaishain desu",
            "watashi wa kaishain desu",
        ],
    },
]


def get_practice_questions():
    return PRACTICE_QUESTIONS.copy()


def check_practice_answer(answer, question):
    normalized = normalize(answer)
    accepted = [normalize(x) for x in question["accepted"]]

    if normalized in accepted:
        return {
            "correct": True,
            "message": "Correct! 🎉",
            "explanation": "Your answer is accepted.",
        }

    return {
        "correct": False,
        "message": "Not quite.",
        "correct_answer": question["accepted"][-1],
        "explanation": "Try using the answer shown above.",
    }

# ============================================================
# VOCABULARY PRACTICE
# ============================================================

VOCABULARY_PRACTICE = LESSON_1_VOCABULARY.copy()


def get_vocabulary_questions():
    questions = []

    for item in VOCABULARY_PRACTICE:
        questions.append({
            "japanese": item["japanese"],
            "english": item["english"],
            "mode": "jp_to_en",
        })

        questions.append({
            "japanese": item["japanese"],
            "english": item["english"],
            "mode": "en_to_jp",
        })

    random.shuffle(questions)
    return questions


def check_vocabulary_answer(answer, question):
    if question["mode"] == "jp_to_en":
        expected = question["english"]
    else:
        expected = question["japanese"]

    correct = normalize(answer) == normalize(expected)

    return {
        "correct": correct,
        "message": "Correct! 🎉" if correct else "Not quite.",
        "correct_answer": expected,
    }


# ============================================================
# JAPANESE SCRIPT RECOGNITION
# ============================================================

def analyze_japanese_script(text):
    """
    Recognize selected Japanese Lesson 1 sentences.
    This is a limited rule-based recognizer, not a full translator.
    """

    normalized = _script_normalize(text)

    # --------------------------------------------------------
    # I am NOT a student.
    # --------------------------------------------------------
    negative_student_sentences = {
        "わたしはがくせいじゃありません",
        "私は学生じゃありません",
        "わたしは学生じゃありません",
        "私はがくせいじゃありません",
        "わたしはがくせいではありません",
        "私は学生ではありません",
        "わたしは学生ではありません",
        "私はがくせいではありません",
    }

    if normalized in negative_student_sentences:
        return {
            "type": "known_sentence",
            "meaning": "I am not a student.",
            "romaji": "Watashi wa gakusei ja arimasen.",
            "grammar": "N は N じゃありません",
            "explanation": (
                "わたし / 私 (watashi) means 'I'. "
                "は (wa) marks the topic. "
                "がくせい / 学生 (gakusei) means 'student'. "
                "じゃありません (ja arimasen) is the polite "
                "negative form used in noun sentences. "
                "ではありません (dewa arimasen) is a more "
                "formal alternative."
            ),
            "followup": (
                "わたしはせんせいじゃありません。 "
                "(Watashi wa sensei ja arimasen.) "
                "— I am not a teacher."
            ),
        }

    # --------------------------------------------------------
    # I am ALSO a student.
    # --------------------------------------------------------
    also_student_sentences = {
        "わたしもがくせいです",
        "私も学生です",
        "わたしも学生です",
        "私もがくせいです",
    }

    if normalized in also_student_sentences:
        return {
            "type": "known_sentence",
            "meaning": "I am also a student.",
            "romaji": "Watashi mo gakusei desu.",
            "grammar": "N も N です",
            "explanation": (
                "わたし / 私 (watashi) means 'I'. "
                "も (mo) means 'also' or 'too' and replaces は "
                "when expressing that something is also true. "
                "がくせい / 学生 (gakusei) means 'student'. "
                "です (desu) makes the statement polite."
            ),
            "followup": (
                "あなたもがくせいですか。 "
                "(Anata mo gakusei desu ka?) "
                "— Are you also a student?"
            ),
        }

    # --------------------------------------------------------
    # I am a student.
    # --------------------------------------------------------
    student_sentences = {
        "わたしはがくせいです",
        "私は学生です",
        "わたしは学生です",
        "私はがくせいです",
    }

    if normalized in student_sentences:
        return {
            "type": "known_sentence",
            "meaning": "I am a student.",
            "romaji": "Watashi wa gakusei desu.",
            "grammar": "N は N です",
            "explanation": (
                "わたし / 私 (watashi) means 'I'. "
                "は (wa) marks the topic. "
                "がくせい / 学生 (gakusei) means 'student'. "
                "です (desu) makes the sentence polite."
            ),
            "followup": (
                "あなたはがくせいですか。 "
                "(Anata wa gakusei desu ka?) "
                "— Are you a student?"
            ),
        }

    # --------------------------------------------------------
    # Self-introductions: I am Padma.
    # --------------------------------------------------------
    introductions = {
        "わたしはパドマです",
        "私はパドマです",
        "わたしはパドマロチニです",
        "私はパドマロチニです",
        "こんにちはわたしはパドマです",
        "こんにちは私はパドマです",
        "こんにちはわたしはパドマロチニです",
        "こんにちは私はパドマロチニです",
    }

    if normalized in introductions:
        name = (
            "Padma Lochini"
            if "パドマロチニ" in normalized
            else "Padma"
        )

        has_greeting = normalized.startswith("こんにちは")

        if has_greeting:
            romaji = (
                "Konnichiwa. Watashi wa Padma Lochini desu."
                if name == "Padma Lochini"
                else "Konnichiwa. Watashi wa Padma desu."
            )
        else:
            romaji = (
                "Watashi wa Padma Lochini desu."
                if name == "Padma Lochini"
                else "Watashi wa Padma desu."
            )

        return {
            "type": "known_sentence",
            "meaning": (
                f"Hello. I am {name}."
                if has_greeting
                else f"I am {name}."
            ),
            "romaji": romaji,
            "grammar": "N は N です",
            "explanation": (
                "わたし / 私 (watashi) means 'I'. "
                "は (wa) marks the topic of the sentence. "
                "パドマ is Padma written in katakana. "
                "です (desu) makes the statement polite. "
                "です is not a possessive particle."
            ),
            "followup": (
                "はじめまして。どうぞよろしくお願いします。 "
                "(Hajimemashite. Douzo yoroshiku onegaishimasu.) "
                "— Nice to meet you."
            ),
        }

    # --------------------------------------------------------
    # Greeting only
    # --------------------------------------------------------
    if normalized == "こんにちは":
        return {
            "type": "known_sentence",
            "meaning": "Hello. / Good afternoon.",
            "romaji": "Konnichiwa.",
            "grammar": "Greeting",
            "explanation": (
                "こんにちは (konnichiwa) is a common "
                "Japanese greeting."
            ),
            "followup": (
                "おげんきですか。 "
                "(Ogenki desu ka?) — How are you?"
            ),
        }

    return None

