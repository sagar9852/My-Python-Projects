print("=============================")
print(f" \t Python Quiz App")
print("=============================")
while True:
    user_score = 0
    incorrect_score = 0
    print("1. Play Quiz \n2. Main menu \n3. Exit")
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
        general_knowledge = {
            "Question": {
                1: "Q1. Which planet in our solar system is known as the 'Red Planet'?",
                2: "Q2. What is the capital city of Australia?",
                3: "Q3. Which gas do plants primarily absorb from the atmosphere during photosynthesis?",
                4: "Q4. Who painted the famous artwork 'The Starry Night'?",
                5: "Q5. In computer science, what does 'RAM' stand for?",
                6: "Q6. Which is the largest ocean on Earth?",
                7: "Q7. What is the chemical symbol for Gold?",
                8: "Q8. Who is widely credited with inventing the World Wide Web (WWW) in 1989?",
                9: "Q9. Which organ in the human body is primarily responsible for filtering blood?",
                10: "Q10. Which country is known as the 'Land of the Rising Sun'?",
            },
            "Options":{

            },
            "Answers":{

            },
        }
        python = {
            "Question": {
                1: "Q1. What is the correct syntax to output 'Hello World' in Python?",
                2: "Q2. Which of the following is NOT a valid variable name in Python?",
                3: "Q3. Which data type is used to store a sequence of immutable objects?",
                4: "Q4. Which collection is ordered, changeable, and allows duplicate members?",
                5: "Q5. What does the lst.pop() method do by default if no index is specified?",
                6: "Q6. What is the correct way to create a function in Python?",
                7: "Q7. What is the main purpose of the is operator in Python?",
                8: "Q8. Which operator is used for floor division (integer division) in Python?",
                9: "Q9. How do you add a comment in Python?",
                10: "Q10. Which of the following built-in collection types in Python strictly prohibits duplicate elements?",
            },
            "Options": {

            },
            "Answers": {

            },
        }
        science = {
            "Question": {
                1: "Q1. Which gas do plants primarily absorb during photosynthesis?",
                2: "Q2. What is the powerhouse of the cell?",
                3: "Q3. What is the chemical symbol for water?",
                4: "Q4. Which planet is known as the Red Planet?",
                5: "Q5. What is the hardest natural substance on Earth?",
                6: "Q6. Sound waves travel fastest through which of the following?",
                7: "Q7. Which vitamin is produced when human skin is exposed to sunlight?",
                8: "Q8. What is the boiling point of pure water at standard atmospheric pressure?",
                9: "Q9. Which organ in the human body filters blood to produce urine?",
                10: "Q10. Newton's first law of motion is also known as the law of what?"
            },
            "Options": {

            },
            "Answers": {

            },
        }
        maths = {
            "Question": {
                1: "Q1. What is the value of x in the equation 3x - 7 = 14?",
                2: "Q2. What is the area of a triangle with a base of 8 cm and a height of 5 cm?",
                3: "Q3. Which of the following is a prime number?",
                4: "Q4. If a car travels at a constant speed of 60 km/h, how far will it travel in 2.5 hours?",
                5: "Q5. What is the value of 5^3 - 4^2?",
                6: "Q6. What is the median of the following dataset: 3, 11, 7, 9, 15?",
                7: "Q7. If 15% of a number is 45, what is the number?",
                8: "Q8. What is the sum of the interior angles of a regular hexagon?",
                9: "Q9. Solve the following expression using the correct order of operations (BODMAS/PEMDAS): 12 + 4 * (8 - 5)",
                10: "Q10. What is the least common multiple (LCM) of 8 and 12?",
            },
            "Options": {

            },
            "Answers": {

            },
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
                print(f"Your answer: {user_option.upper()}")
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
        percentage=(user_score/10)*100
        print(f"Percentage: {round(percentage,1)}%git")
        if user_score>=5:
            print("Excellent Work")
        elif user_score==0:
            print("Tere se nhi ho payega")
        else:
            print("Better luck next time")
    elif user_opt=="2":
        while True:
            print("1.General Knowledge \n2.Python \n3.Science \n4.Maths \n5.Exit ")
            user_choice=input("Enter your choice(1-5): ")
            if user_choice=="1":
                pass
            elif user_choice=="2":
                pass
            elif user_choice=="3":
                pass
            elif user_choice=="4":
                pass
            elif user_choice=="5":
                print("OK! NO PROBLEM.")
                break
    elif user_opt=="3":
        print("Have a Good Day!")
        break
    else:
        print("Invalid Option")
        continue

