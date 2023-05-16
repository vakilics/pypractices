import json

with open("questions.json", 'r') as file:
    content = file.read()
data = json.loads(content)

for question in data:
    print()
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    print()

    user_choice = int(input("Enter choice: "))
    question["user_choice"] = user_choice  #save user answer



score = 0
percent = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer!"
        percent = percent + 50 #here two questions, so 2 * 50 = 100 if both answers are correct

    else:
        result = "Wrong Answer!"

    message = f"Q_{index +1}: {result}  - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"

    with open("files/Multiple-Choice-Result.txt", 'a') as f:
        f.write(message + "\n" * 2)

with open("files/Multiple-Choice-Result.txt", 'a') as f:
    f.write("#==========SCORE==================#" + "\n")
    f.write(f"Score : , {score}, /, {len(data)}, Total:, {percent}, %")

#print(data)
print("Score :", score, "/", len(data), "Total: ", percent, "%")


