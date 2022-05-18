# def kbc(questions,options):
#     i=0
#     solutions=[3,4,1]
#     while i<len(questions):
#         print("Q.",i+1,questions[i])
#         j=0
#         while j<len(options[i]):
#             print(j+1,".",options[i][j])
#             j+=1
#         user=int(input("choose answer:"))
#         if user==solutions[i]:
#             print("congrats!your answer is correct")
#         else:
#             print("sorry! wrong answer. You are out of the game.")
#             break
#         i+=1
# questions=["how many continents are there?",
#     "what is the capital of India?",
#     "what course do they teach at NG?"]
# options=[["four","nine","seven","eight"],
#     ["chandigarh","bhopal","chennai","delhi"],
#     ["software engineering","counselling","tourism","agriculture"]]
# kbc(questions,options)



# questions=["how many continents are there?",
#     "what is the capital of India?",
#     "what course do they teach at NG?"]
# answers=[["four","nine","seven","eight"],
#     ["chandigarh","bhopal","chennai","delhi"],
#     ["software engineering","counselling","tourism","agriculture"]]
# solutions=[3,4,1]
# def kbc(questions):
#     def kbc(answers):
#             i=0
#             while i<len(questions):
#                 print("Q.",i+1,questions[i])
#                 j=0
#                 while j<len(answers[i]):
#                     print(j+1,".",answers[i][j])
#                     j+=1
#                 user=int(input("enter answer choice:"))
#                 if user==solutions[i]:
#                     print("correct answer!")
#                 else:
#                     print("wrong answer!")
#                     break
#                 i+=1
#     kbc(answers)
# kbc(questions)
