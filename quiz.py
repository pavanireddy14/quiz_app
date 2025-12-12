import json, random, time
from utils import colored, progress_bar

class QuizApp:
    def __init__(self):
        with open("questions.json") as f:
            self.questions = json.load(f)
        self.score = 0
        self.player = ""

    def welcome(self):
        print(colored("\n🎉 Welcome to the Advanced Quiz App! 🎉\n", "cyan"))
        self.player = input("Enter your name: ")
        progress_bar()

    def choose_category(self):
        print(colored("\nAvailable Categories:", "yellow"))
        for cat in self.questions.keys():
            print(f" - {cat}")
        return input("\nChoose a category: ")

    def choose_level(self):
        levels = ["Easy", "Medium", "Hard"]
        print(colored("\nDifficulty Levels:", "yellow"))
        for lvl in levels:
            print(f" - {lvl}")
        return input("\nChoose a difficulty level: ")

    def start_quiz(self, category, level):
        q_list = self.questions[category][level]
        random.shuffle(q_list)

        for q in q_list:
            print(colored(f"\n{q['question']}", "cyan"))
            options = q['options']
            random.shuffle(options)

            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")

            start = time.time()
            answer = input("\nYour answer (1–4): ")
            end = time.time()

            # Timer of 10 seconds
            if end - start > 10:
                print(colored("⏳ Time’s up!", "red"))
                continue

            if options[int(answer)-1] == q["answer"]:
                print(colored("✔ Correct!", "green"))
                self.score += 1
            else:
                print(colored(f"❌ Wrong! Correct answer: {q['answer']}", "red"))

    def save_score(self):
        with open("scoreboard.txt", "a") as f:
            f.write(f"{self.player} - Score: {self.score}\n")

    def show_result(self):
        print(colored(f"\nYour final score: {self.score}\n", "yellow"))
        self.save_score()
        print(colored("Score saved in scoreboard.txt 📂", "cyan"))

    def run(self):
        self.welcome()
        category = self.choose_category()
        level = self.choose_level()
        print(colored(f"\nStarting quiz on {category} [{level}]...\n", "yellow"))
        self.start_quiz(category, level)
        self.show_result()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
