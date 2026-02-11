#Create a program capable of displaying questions to the user like KBC.
#Use List data type to store the questions and their correct answers.
#Display the final amount the person is taking home after playing the game.

questions = ["What is the capital of India?", "Who is the current president of India?", "What is the national animal of India?"]
answers = ["New Delhi", "Ram Nath Kovind", "Tiger"]
score = 0

for x in questions:
    print(x)
    y = input("Your answer: ")
    if(y.lower() == answers[0].lower() or y.lower() == answers[1].lower() or y.lower() == answers[2].lower()):
        print("Correct answer!")
        score  = score + 1
    else:
        print("Wrong answer!")
print("Your final score is: ", score)


# 2nd solution using for loop and index
# for i in range(len(questions)):
#     print(questions[i])
#     y = input("Your answer: ")
#     if(y.lower() == answers[i].lower()):
#         print("Correct answer!")
#         score  = score + 1
#     else:
#         print("Wrong answer!")
# print("Your final score is: ", score)

Total_amount = score * 10000
print("You are taking home: ", Total_amount)