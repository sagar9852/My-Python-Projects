print("=============================")
print(f" \t Python Quiz App")
print("=============================")
while True:
    user_score = 0
    incorrect_score = 0
    print("1. Play Quiz \n2. View High Score \n3. Exit")
    user_opt=input("Choose an option(1-3): ")
    if user_opt=="1":
        question = {
            "Questions": {
                1: "1.Which gas makes up the largest percentage of Earth's atmosphere?",
                2: "2.Which of the following rivers is the longest in the world?",
                3: "3.What is the primary function of the red blood cells in the human body?",
                4: "4.Which planet in our solar system is known for having a giant, persistent storm called the 'Great Red Spot'?",
                5: "5.Who was the first President of the United States?",
                6: "6.What is the chemical symbol for the element Gold?",
                7: "7.Who wrote the famous play Romeo and Juliet?",
                8: "8.If a triangle has angles that measure 50 degrees and 60 degrees, what must the measure of the third angle be?",
                9: "9.What does 'URL' stand for in web terminology?",
                10: "10.Which of the following is a renewable energy source?",

            },
            "Options": {
                1: " A)Oxygen \n B)Nitrogen \n C)Carbon Dioxide \n D)Hydrogen ",
                2: " A) The Amazon River \n B) The Yangtze River \n C) The Nile River \n D) The Mississippi River ",
                3: " A) To fight off infections \n B) To help the blood clot after an injury \n C) To carry oxygen from the lungs to the rest of the body \n D) To digest nutrients from food ",
                4: " A) Mars \n B) Saturn \n C) Jupiter \n D) D) Neptune",
                5: " A) Thomas Jefferson \n B) Abraham Lincoln \n C) George Washington \n D) Benjamin Franklin ",
                6: " A) Gd \n B) Go \n C) Ag \n D) Au ",
                7: " A) Charles Dickens \n B) William Shakespeare \n C) Mark Twain \n D) Jane Austen ",
                8: " A) 50 degrees \n B) 70 degrees \n C) 90 degrees \n D) 110 degrees ",
                9: " A) Uniform Resource Locator \n B) Universal Real Link \n C) Unified Resource Line \n D) User Route Locator ",
                10: " A) Coal \n B) Natural Gas \n C) Solar Power \n D) Petroleum ",
            },
            "Answers": {
                1: "B",
                2: "C",
                3: "C",
                4: "C",
                5: "C",
                6: "D",
                7: "B",
                8: "B",
                9: "A",
                10: "C",
            }
        }
        for i in range(1, 11):
            correct_answer = question["Answers"][i]
            print("=========================")
            print(f"Question {i} out of 10.")
            print("=========================")
            print(question["Questions"][i])
            print(question["Options"][i])
            user_option = input("Your answer(A/B/C/D): ")
            if user_option.upper() == correct_answer:
                print("Correct answer!")
                user_score += 1
                print()
                print(f"Current Score: {user_score}/10")
            else:
                incorrect_score+=1
                print("Incorrect answer!")
                print()
                print(f"Correct answer:{correct_answer}")
                print(f"Current Score: {user_score}/10")
        print("=========================")
        print(" \t Quiz Over")
        print("=========================")
        print("Total Question: 10")
        print(f"Correct answer: {user_score}")
        print(f"Incorrect answer: {incorrect_score}")
        print()
        print(f"Final Score:{user_score}/10")
        if user_score>=5:
            print("Excellent Work")
        elif user_score==0:
            print("Tere se nhi ho payega")
        else:
            print("Better luck next time")
    elif user_opt=="2":
        print(f"High score {user_score}")
    elif user_opt=="3":
        print("Have a Good Day!")
        break
    else:
        print("Invalid Option")
        continue

