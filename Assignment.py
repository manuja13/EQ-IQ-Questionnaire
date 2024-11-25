# Welcome
print("...Welcome to the Test...\n")
name = input("Enter your Name: ")
age = str(input("Enter your Age: "))
gender = input("Enter your Gender: ")
print("")
print("Read the instructions carefully.\n")
# Score
def main():
    IQ_Score = 0
    EQ_Score = 0
    start = input("Write down a) or b) what you want to do now ?\n\n a) IQ Test\n b) EQ Test\n\n Type Here: ").lower()
    print()
    if start == "a":
        print("IQ Questions")
        print("")
        IQ01 = print("01) How many continents are there on Earth?\n a.20\n b.7\n c.15\n d.50\n")
        ANS01 = "b"
        answer = input("Answer: ")
        if answer == ANS01:
            IQ_Score = IQ_Score + 10

        IQ02 = print("\n02) Who was the 23rd president of the US?\n a.Abraham lincoln\n b.George washington\n c.Barack Obama\n d.Benjamin Harrison\n")
        ANS02 = "d"

        answer = input("Answer: ")
        if answer == ANS02:
            IQ_Score = IQ_Score + 10

        IQ03 = print("\n03) What year was NASA founded?\n a.2009\n b.1948\n c.1958\n d.1960\n")
        ANS03 = "c"

        answer = input("Answer: ")
        if answer == ANS03:
            IQ_Score = IQ_Score + 10

        IQ04 = print("\n04) Who was the first man on the moon?\n a.Lance Armstrong\n b.George Washington\n c.Neil Armstrong\n d.Alan Shepard\n")
        ANS04 = "c"

        answer = input("Answer: ")
        if answer == ANS04:
            IQ_Score = IQ_Score + 10

        IQ05 = print("\n05) How many men does it take to dig half a hole?\n a.10\n b.1\n c.Not enough info\n d.0-you cant dig half a hole\n")
        ANS05 = "d"

        answer = input("Answer: ")
        if answer == ANS05:
            IQ_Score = IQ_Score + 10

        IQ06 = print("\n06) Spinach is high in?\n a.Iron \n b.Vitamin C\n c.Biotin\n d.None of the above\n")
        ANS06 = "a"

        answer = input("Answer: ")
        if answer == ANS06:
            IQ_Score = IQ_Score + 10

        IQ07 = print("\n07) How many months in a year have 28 days?\n a.1 \n b.3\n c.1- but not every year but once in every 4 years\n d.4\n")
        ANS07 = "a"

        answer = input("Answer: ")
        if answer == ANS07:
            IQ_Score = IQ_Score + 10

        IQ08 = print("\n08) Which one out of the following produces honey?\n a.Wasp C\n b.Bee \n c.Hornet\n d.Flying ants\n")
        ANS08 = "b"

        answer = input("Answer: ")
        if answer == ANS08:
            IQ_Score = IQ_Score + 10

        IQ09 = print("\n09) 0 multiplied by any number gives the result as _______.\n a.0 \n b.The same number \n c.1\n d.Undefined\n")
        ANS09 = "a"

        answer = input("Answer: ")
        if answer == ANS09:
            IQ_Score = IQ_Score + 10

        IQ10 = print("\n10) How many zeroes are there in 1 million?\n a.6 \n b.5 \n c.3\n d.4\n")
        ANS10 = "a"

        answer = input("Answer: ")
        if answer == ANS10:
            IQ_Score = IQ_Score + 10
        print("\nIQ Questions are over.\n")
        print("Your Name: ", name)
        print("Your Age: ", age, "years old")
        print("Your Gender: ", gender)
        print("\nCongratulation,Your total IQ score is " + str(IQ_Score) + " /100 ")
        print()
    elif start == "b":
        print("EQ Questions\n")
        EQ01 = print(" 01) Some people tend to be disconnected from their emotions.What can be a reason for this?\n a.A dominant personality\n b.Unhappy childhood experiences\n c.Poor academic performance\n d.Lack of parental attachment\n")
        EQans01 = "b"

        answer = input("Answer: ")
        if answer == EQans01:
            EQ_Score = EQ_Score + 10

        EQ02 = print("\n 02) Which of the following statements is true about emotional intelligence?\n a.One is born with emotional intelligence.\n b.Emotional intelligence does not concern other people.\n c.Emotional intelligence is developed.\n d.One needs formal schooling to have emotional intelligence.\n")
        EQans02 = "c"

        answer = input("Answer: ")
        if answer == EQans02:
            EQ_Score = EQ_Score + 10

        EQ03 = print("\n 03) What is an indicator of emotional awareness?\n a.Keeping quiet when conflicts are happening.\n b.Letting emotions shift from negative to positive and vice versa, depending on the situation.\n c.Recognizing and experiencing distinct emotions.\n d.Channeling negative emotions to physical activities.\n")
        EQans03 = "c"

        answer = input("Answer: ")
        if answer == EQans03:
            EQ_Score = EQ_Score + 10

        EQ04 = print("\n 04) Which attribute of emotional intelligence pertains to one's own emotions and how they affect thoughts and behavior,knowing strengths and weaknesses, and having self-confidence?\n a.Social awareness\n b.Self-awareness\n c.Self management\n d.Relationship management\n")
        EQans04 = "b"

        answer = input("Answer: ")
        if answer == EQans04:
            EQ_Score = EQ_Score + 10

        EQ05 = print("\n 05) How can emotional intelligence help individuals?\n a.It can increase one’s salary.\n b.It can decrease depression.\n c.It can increase IQ.\n d.It is a major predictor of financial success.\n")
        EQans05 = "b"

        answer = input("Answer: ")
        if answer == EQans05:
            EQ_Score = EQ_Score + 10

        EQ06 = print("\n 06) What entails the attribute of social awareness?\n a.You can understand the emotions, needs, and concerns of other people, pick up on emotional cues,feel comfortable socially, and recognize the power dynamics in a group or organization.\n b.You’re able to control impulsive feelings and behaviors, manage your emotions in healthy ways,take the initiative, follow through on commitments, and adapt to changing circumstances.\n c.You recognize your own emotions and how they affect your thoughts and behavior,know your strengths and weaknesses, and have self-confidence.\n d.You know how to develop and maintain good relationships, communicate clearly,inspire and influence others, work well in a team, and manage conflict.\n")
        EQans06 = "a"

        answer = input("Answer: ")
        if answer == EQans06:
            EQ_Score = EQ_Score + 10

        EQ07 = print("\n 07) Which of the following skills is needed to enhance emotional intelligence?\n a.Increasing leadership skills to control your followers.\n b.Directing peers and colleagues to express what is on their minds.\n c.Being honest in all situations, even if it will result in conflicts.\n d.Use of nonverbal behavior in connecting with others.\n")
        EQans07 = "d"

        answer = input("Answer: ")
        if answer == EQans07:
            EQ_Score = EQ_Score + 10

        EQ08 = print("\n 08) Which of the following is a technique in reducing stress in the heat of a moment?\n a.Identifying and maximizing sensory stimuli that soothe and energizes a person.\n b.By excessively indulging in a favorite hobby.\n c.Confronting the person who is a source of your stress.\n d.Letting all anger out by shouting, hitting something, or engaging in sports.\n")
        EQans08 = "a"

        answer = input("Answer: ")
        if answer == EQans08:
            EQ_Score = EQ_Score + 10

        EQ09 = print("\n09) What should be the first consideration when feeling agitated in a specific situation?\n a.Realizing that you are stressed.\n b.Identifying how you cope with stress.\n c.Indulging in soothing or relaxing activities.\n d.Maintaining physical and emotional health at all times.\n")
        EQans09 = "a"

        answer = input("Answer: ")
        if answer == EQans09:
            EQ_Score = EQ_Score + 10

        EQ10 = print("\n10) A visual person is likely to relieve stress by:\n a.Listening to music.\n b.Playing basketball.\n c.Enjoy a movie.\n d.Going on a food binge.\n")
        EQans10 = "c"

        answer = input("Answer: ")
        if answer == EQans10:
            EQ_Score = EQ_Score + 10

        print("\nEQ Questions are over. \n")
        print("Your Name: ", name)
        print("Your Age: ", age, "years old")
        print("Your Gender: ", gender)
        print("\nCongratulation,Your total EQ score is " + str(EQ_Score) + " /100 \n")

    print("If you want to retry or select a next question type, Type (r).")
    print("To save your result as a text file, Type (s).")
    print("If you want to Exit, Type (q).")
    select = input("\nType Here : ")
    print()
    if select == "r":
     main()
    elif select =="s":
      Result = open("EQ-IQ Results.txt", "w")
      ResultFile = "Name :     " + name + "\n" + "Age :      " + age + "\n" + "Gender :   " + gender + "\n"
      ResultFileMarks = "IQ Score : " + str(IQ_Score) + "/100" + "\n" + "EQ Score : "+ str(EQ_Score) + "/100"
      Result.write(ResultFile)
      Result.write(ResultFileMarks)
      Result.close()
    else:
      select ="q"
      print("You quit your game")
      print("###### Thank You #####")
main()