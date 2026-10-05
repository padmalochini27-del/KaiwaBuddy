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
        "example": "SJIT no gakusei."
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


# ============================================================
# VOCABULARY
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
# SAFE FOLLOW-UPS
# ============================================================

CONVERSATION_FOLLOWUPS = {
    "gakusei": [
        "Gakusei desu ka?",
        "Anata wa gakusei desu ka?",
    ],
    "sensei": [
        "Sensei desu ka?",
        "Anata wa sensei desu ka?",
    ],
    "isha": [
        "Isha desu ka?",
        "Anata wa isha desu ka?",
    ],
    "kaishain": [
        "Kaishain desu ka?",
        "Anata wa kaishain desu ka?",
    ],
    "shain": [
        "Shain desu ka?",
    ],
}


def get_safe_followup(topic):

    if topic in CONVERSATION_FOLLOWUPS:
        return random.choice(CONVERSATION_FOLLOWUPS[topic])

    return "Can you make another simple Japanese sentence?"


# ============================================================
# N は N です
# ============================================================

def analyze_noun_desu(text):

    normalized = normalize(text)

    match = re.fullmatch(
        r"(.+?) wa (.+?) desu",
        normalized
    )

    if not match:
        return None

    subject = match.group(1).strip()
    predicate = match.group(2).strip()

    if subject not in LESSON_1_NOUNS:
        return None

    if predicate not in LESSON_1_NOUNS:
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
            "は (wa) marks the topic and です makes "
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
        r"(.+?) wa (.+?) (?:ja arimasen|jaarimasen)",
        normalized
    )

    if not match:
        return None

    subject = match.group(1).strip()
    predicate = match.group(2).strip()

    if subject not in LESSON_1_NOUNS:
        return None

    if predicate not in LESSON_1_NOUNS:
        return None

    return {
        "type": "grammar",
        "meaning": (
            f"{LESSON_1_NOUNS[subject]} is not "
            f"{LESSON_1_NOUNS[predicate]}."
        ),
        "grammar": "N は N じゃありません",
        "explanation": (
            "じゃありません is the negative form "
            "of です for noun sentences."
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
        normalized
    )

    if not match:
        return None

    subject = match.group(1).strip()
    predicate = match.group(2).strip()

    if subject not in LESSON_1_NOUNS:
        return None

    if predicate not in LESSON_1_NOUNS:
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
        normalized
    )

    if not match:
        return None

    subject = match.group(1).strip()
    predicate = match.group(2).strip()

    if subject not in LESSON_1_NOUNS:
        return None

    if predicate not in LESSON_1_NOUNS:
        return None

    return {
        "type": "grammar",
        "meaning": (
            f"{LESSON_1_NOUNS[subject]} is also "
            f"{LESSON_1_NOUNS[predicate]}."
        ),
        "grammar": "N も N です",
        "explanation": (
            "も means 'also' and replaces は."
        ),
        "followup": get_safe_followup(predicate),
    }


# ============================================================
# N1 の N2
# ============================================================

def analyze_no_pattern(text):

    normalized = normalize(text)

    match = re.fullmatch(
        r"(.+?) wa (.+?) no (.+?) desu",
        normalized
    )

    if not match:
        return None

    subject = match.group(1).strip()
    organization = match.group(2).strip()
    noun = match.group(3).strip()

    if subject not in LESSON_1_NOUNS:
        return None

    if noun not in LESSON_1_NOUNS:
        return None

    return {
        "type": "grammar",
        "meaning": (
            f"{LESSON_1_NOUNS[subject]} is a "
            f"{LESSON_1_NOUNS[noun]} of {organization}."
        ),
        "grammar": "N1 は N2 の N3 です",
        "explanation": (
            "の connects two nouns and shows a relationship "
            "between them."
        ),
        "followup": (
            f"Can you make another sentence using "
            f"'{organization} no {noun}'?"
        ),
    }


# ============================================================
# COMMON MISTAKE DETECTOR
# ============================================================

def check_common_mistake(text):

    normalized = normalize(text)

    # desuu / desuuu / desuuuu...
    if re.search(r"\bdesu{2,}\b", normalized):

        corrected = re.sub(
            r"\bdesu{2,}\b",
            "desu",
            normalized
        )

        corrected_result = analyze_noun_desu(corrected)

        if corrected_result:

            return {
                "type": "mistake",
                "meaning": corrected_result["meaning"],
                "grammar": corrected_result["grammar"],
                "explanation": (
                    "Small spelling mistake: "
                    "'desuu' should be written as 'desu' "
                    "in standard romanization."
                ),
                "correction": corrected,
                "followup": corrected_result["followup"],
            }

        return {
            "type": "mistake",
            "meaning": "Your sentence has a small spelling mistake.",
            "grammar": "です (desu)",
            "explanation": (
                "Use 'desu' in standard romanization."
            ),
            "correction": corrected,
            "followup": "Try the corrected sentence again.",
        }

    # des -> desu
    if re.search(r"\bdes\b", normalized):

        corrected = re.sub(
            r"\bdes\b",
            "desu",
            normalized
        )

        corrected_result = analyze_noun_desu(corrected)

        if corrected_result:

            return {
                "type": "mistake",
                "meaning": corrected_result["meaning"],
                "grammar": corrected_result["grammar"],
                "explanation": (
                    "Small spelling mistake: "
                    "'des' should be written as 'desu'."
                ),
                "correction": corrected,
                "followup": corrected_result["followup"],
            }

        return {
            "type": "mistake",
            "meaning": "Your sentence has a small spelling mistake.",
            "grammar": "です (desu)",
            "explanation": (
                "Use 'desu', not 'des'."
            ),
            "correction": corrected,
            "followup": "Try the corrected sentence again.",
        }

    # arimasn -> arimasen
    if "arimasn" in normalized:

        corrected = normalized.replace(
            "arimasn",
            "arimasen"
        )

        return {
            "type": "mistake",
            "meaning": "Your sentence has a small spelling mistake.",
            "grammar": "じゃありません",
            "explanation": (
                "The correct romanization is 'arimasen'."
            ),
            "correction": corrected,
            "followup": "Try the corrected sentence again.",
        }

    return None


# ============================================================
# CONVERSATION ANSWERS
# ============================================================

def analyze_conversation_answer(text, expected_topic):

    normalized = normalize(text)

    topic_data = {
        "student": ("gakusei", "student"),
        "teacher": ("sensei", "teacher"),
        "doctor": ("isha", "doctor"),
        "company_employee": ("kaishain", "company employee"),
    }

    if expected_topic not in topic_data:
        return None

    japanese_word, english_word = topic_data[expected_topic]

    if normalized in ["hai", "hai desu"]:

        return {
            "type": "conversation",
            "meaning": f"Yes, I am a {english_word}.",
            "grammar": "はい + N です",
            "explanation": (
                f"'{japanese_word}' means '{english_word}'."
            ),
            "followup": get_safe_followup(japanese_word),
            "next_topic": expected_topic,
        }

    positive_patterns = [
        f"hai {japanese_word} desu",
        f"watashi wa {japanese_word} desu",
    ]

    if normalized in positive_patterns:

        return {
            "type": "conversation",
            "meaning": f"Yes, I am a {english_word}.",
            "grammar": "N は N です",
            "explanation": (
                f"'{japanese_word}' means '{english_word}'."
            ),
            "followup": get_safe_followup(japanese_word),
            "next_topic": expected_topic,
        }

    if normalized == "iie":

        return {
            "type": "conversation",
            "meaning": "No.",
            "grammar": "はい / いいえ",
            "explanation": (
                "いいえ means 'no'."
            ),
            "followup": "Try another simple answer.",
            "next_topic": None,
        }

    return None


# ============================================================
# KNOWN SENTENCE
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

    elif "kaishain" in normalized:

        result["followup"] = get_safe_followup("kaishain")

    else:

        result["followup"] = (
            "Can you make another Japanese sentence?"
        )

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

    accepted = [
        normalize(x)
        for x in question["accepted"]
    ]

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
        "explanation": (
            "Try using the answer shown above."
        ),
    }


# ============================================================
# VOCABULARY MODE
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

    normalized = normalize(answer)

    if question["mode"] == "jp_to_en":

        correct = normalize(question["english"])

    else:

        correct = normalize(question["japanese"])

    if normalized == correct:

        return {
            "correct": True,
            "message": "Correct! 🎉",
            "correct_answer": (
                question["english"]
                if question["mode"] == "jp_to_en"
                else question["japanese"]
            ),
        }

    return {
        "correct": False,
        "message": "Not quite.",
        "correct_answer": (
            question["english"]
            if question["mode"] == "jp_to_en"
            else question["japanese"]
        ),
    }