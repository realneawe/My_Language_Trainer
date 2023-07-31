from english_data import english_word_dictionary
import random

word_self = []
word_mean = []
for i in range(0, len(english_word_dictionary)):
    word_self.append(english_word_dictionary[i]["word"])
    word_mean.append(english_word_dictionary[i]["mean"])

all_quiz = len(word_self)
print(f"🥳 Welcome to English ---> Turkish word exam! 🥳"
      f"\nThe total number of words in this section; {all_quiz} words!"
      f"\nIf you want exit the code, input one of these words; 'exit', 'quit' or 'stop'.\n"
      f"\nLet's started with first word;")

score = 0
quiz_step = 0
end = False
while not end:
    randomize = random.randint(0, (len(word_self) - 1))
    print("---------------------------------------------------------------------------------")
    print("👇What does it mean?👇")
    user_answer = input(f"{word_self[randomize]}: ").lower()
    if user_answer == word_mean[randomize].lower():
        print("\nYou're goddamn right!")
        score += 1
        quiz_step += 1
        del word_mean[randomize]
        del word_self[randomize]
        print(f"Your earn 1.0 point in score. Your new score is; 🔺{score}🔺\n")
        if score == all_quiz:
            print("You are amazing, you have completed the exam with full marks.\n"
                  "🎉🎉 !!! AWESOME DUDE 🎉 REALLY AWESOME !!! 🎉🎉")
        if quiz_step == all_quiz:
            end = True
            if score <= 0:
                print("📝You should more study!📝")
            elif score >= 25:
                print("👏You are really good dude, congratulations!👏")
            else:
                print("👍You are OK but not enough!👌")
    elif user_answer == "quit" or user_answer == "exit" or user_answer == "stop":
        end = True
        print(f"\nYour final score is; {score}")
        if score <= 0:
            print("📝You should more study!📝")
        elif score >= 25:
            print("👏You are really good dude, congratulations!👏")
        else:
            print("👍You are OK but not enough!👌")
    else:
        print("\nOK, maybe you are thinking you answer right, but this answer wrong dude. sorry 😞")
        print(f"Correct word mean is;👉 {word_mean[randomize]} 👈")
        score -= 0.5
        print(f"\nYour lost 0.5 point in score. Your new score is; 🔻{score}🔻\n")