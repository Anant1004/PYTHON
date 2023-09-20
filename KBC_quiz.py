Questions =[
    ["What is the capital of France?","1) London","2) Berlin","3) Paris","4) Madrid", 4],
    ["What is the capital of india", "1) London","2) New delhi","3) Mumbai","4) Goa", 2],
    ["What is the capital of Italy?", "1) Rome","2) Paris","3) Berlin","4) Madrib", 1],
    ["Which gas do plants absorb from the atmosphere during photosynthesis?", "1) Oxygen","2) Carbon dioxide","3) Nitrogen","4) Hydrogen", 2],
    ["What is the largest planet in our solar system?", "1) Earth","2) Venus","3) Mars","4) Jupiter", 4],
    ["Who is known as the inventor of the telephone? ?","1)  Thomas Edison","2) Alexander Graham Bell","3)  Nikola Tesla","4)  Isaac Newton",2],
    ["What is the chemical symbol for water? ?","1) H2O","2) CO2","3) O2","4) NaCl",1],
    ["Which planet is called the 'Red Planet' ?","1) Venus","2) Jupiter","3) Mars","4) Saturn",3],
    ["Who painted the Mona Lisa? ?","1) Vincent van Gogh","2) Leonardo da Vinci","3)  Pablo Picasso","4) Michelangelo",2],
    [" Who wrote the play 'Romeo and Juliet'?","1) Charles Dickens","2) Jane Austen","3) William Shakespeare","4) Mark Twain",1],
    ] 
levels = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
money = 0
for i in range(len(Questions)):
    Question = Questions[i]
    print(f"Question for $ ->{levels[i]}")
    print(Question[0])
    print(f"{Question[1]}       {Question[2]}")
    print(f"{Question[3]}       {Question[4]}")
    reply = int(input("Enter your choice (1-4)")) 
    if(reply ==Question[-1]):
        print("!!!Congrats!!!")
        print("Correct answer")
        if(i==2):
            money = 2000
        elif(i==4):
            money = 4000
        elif(i==6):
            money = 6000
        elif(i==8):
            money = 8000
        print(f"you won -> {levels[i]}")
    else:
        print("!!!Alas!!!")
        print("Wrong answer")
        break
    print(f"Your take home money is -> {money} ")