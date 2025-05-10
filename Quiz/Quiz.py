import random

class QuizGame:
    def __init__(self):
        self.quiz = {
            "What data structure uses key-value pairs in Python?": "Dictionary",
            "Which data structure is mutable and ordered in Python?": "List",
            "Which method adds an element to the end of a list?": "append",
            "What does the pop() method do in a list?": "Removes and returns last item",
            "Which data structure stores only unique elements?": "Set",
            "What keyword is used to define a function in Python?": "def",
            "What is the output of len('Hello')?": "5",
            "Which sorting algorithm has O(n^2) time in the worst case?": "Bubble sort",
            "What is recursion?": "A function calling itself",
            "Which Python keyword is used to loop over a sequence?": "for",
            "How do you get the first element of a list named 'nums'?": "nums[0]",
            "What is the time complexity of searching in a Python dictionary?": "O(1)",
            "What will list(range(5)) return?": "[0, 1, 2, 3, 4]",
            "What does the 'in' keyword check in a list?": "If an item exists in the list",
            "Which data structure is best for FIFO access?": "Queue",
            "Which function returns the maximum value in a list?": "max",
            "What is the result of 3 ** 2 in Python?": "9",
            "Which method is used to remove a specific item from a set?": "remove",
            "What will 'abc'.upper() return?": "ABC",
            "Which module provides heap operations in Python?": "heapq"
        }
        self.score = 0

    def shuffle_questions(self):
        """Shuffle the questions."""
        self.questions = list(self.quiz.items())
        random.shuffle(self.questions)

    def ask_question(self, question, correct_answer):
        """Ask a single question and check the answer."""
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!\n")
            return True
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")
            return False

    def run_quiz(self):
        """Run the full quiz."""
        self.shuffle_questions()
        
        # Ask user how many questions they want to answer
        num_questions = int(input(f"How many questions would you like to answer (max {len(self.quiz)}): "))

        # Ensure the user doesn't select more questions than available
        if num_questions > len(self.quiz):
            print(f"You can only answer up to {len(self.quiz)} questions. Setting it to {len(self.quiz)}.")
            num_questions = len(self.quiz)

        # Loop through only the number of questions the user requested
        for question, correct_answer in self.questions[:num_questions]:
            if self.ask_question(question, correct_answer):
                self.score += 1

        print(f"You got {self.score} out of {num_questions} correct!")

# Create a quiz object and run the quiz
quiz_game = QuizGame()
quiz_game.run_quiz()
