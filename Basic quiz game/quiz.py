print("=============================")
print(f" \t Welcome to Quiz App")
print("=============================")
question ={
     "Questions" : {
         1: "1.Who is the prime minister of india?",
         2: "2.Who is the first prime minister of india?"
    },
     "Options" : {
        1:" A)Modi \n B)Yogi \n C)Lalu \n D)Mamta",
        2:" A)Modi \n B)Yogi \n C)Nehru \n D)Mamta"
     },
    "Answers": {
        1:"A",
        2:"C"
    }
}
user_score=0
for i in range(1,3):
    correct_answer=question["Answers"][i]
    print("=========================")
    print(question["Questions"][i])
    print(question["Options"][i])
    user_option = input("Enter your option(A/B/C/D): ")
    if user_option.upper()==correct_answer:
        print("Correct answer!")
        user_score+=1
    else:
        print("Incorrect answer!")
print(f"You have {user_score} correct answer.")