import pathlib
import random
from string import ascii_lowercase
import tomli as tomllib

NUMBER_OF_QUESTIONS = 15
QUESTIONS = pathlib.Path(__file__).parent / "topicWiseQuestions.toml"

def start_quiz():
    total_questions = question_preparation(
        QUESTIONS, num_questions=NUMBER_OF_QUESTIONS
    )

    num_correct = 0
    for num, question in enumerate(total_questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += question_asked(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")
    print(f"\nYour got {num_correct * 2} out of {num * 2} marks")

def question_preparation(path, num_questions):
    topic_name = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["questions"] for topic in topic_name.values()
    }
    topic_label = answers_of_questions(
        question="Which topic do you want to be quizzed about",
        alternatives=sorted(topics),
    )[0]

    questions = topics[topic_label]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

def question_asked(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = answers_of_questions(
        question=question["question"],
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )
    if correct := (set(answers) == set(correct_answers)):
        print("⭐ Correct! ⭐")
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))

    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    return 1 if correct else 0

def answers_of_questions(question, alternatives, num_choices=1, hint=None):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    if hint:
        labeled_alternatives["?"] = "Hint"

    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hints
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle invalid answers
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]

if __name__ == "__main__":
    start_quiz()
