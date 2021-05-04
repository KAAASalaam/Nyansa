import random
def command_list():#works
    print("Advice - recieve proverbial wisdom to assist you")
    print("Options - to see command list")
    print("Add - add your own proverb to our database")
    print("Game - play a game where you can learn and test your knowledge of proverbs")
    print("Learn - learn new proverbs and add wisdom to your life")
    print("Exit - end the program")
def add_proverbs():#works
    f = open("proverbs.text","r")
    add_proverb_input = input("Type the Proverb you would like to ADD. ")
    proverbs = f.readlines()
    for i in proverbs:
        if i == add_proverb_input:
            print("Your proverb is already in the system.")
        else:
            f.close()
            f = open("proverbs.text","a")
            f.write("\n")
            categorize = input("Choose one categroy that your proverb fits into.\nPatience, wisdom, love, family, good character, or strength.\n>> ")
            f.write(categorize.lower())
            f.write("-")
            f.write(add_proverb_input)
            print("Your proverb has been added.")
            break
    f.close()
def help_with_problem():#works
    f = open("proverbs.text","r+")
    problem_help = input("How can I help you? Describe your problem to me.\n>> ")
    categories = input("Our proverbs are grouped into a few categroies, type in one that your proverb fits into. \n The categories are -Good Character-Wisdom-Strength-Family-Patience-Love-. \n Choose the category that best fits your problem.\n>> ") 
    proverbs = f.readlines()
    categories = categories.lower()
    temp_proverb_set = []
    for i in proverbs:
        if categories == i.split('-')[0]:
            temp_proverb_set.append(i.split('-')[1])
    match_count = 0
    for i in temp_proverb_set:
        for word in problem_help:
            if i == word:
                match_count += 1
    #random.randint(0,len(temp_proverb_set)-1)
    count  = 0
    while match_count <= 0:
        num = random.randint(0,len(temp_proverb_set))
        if count < 1:
            recieved_proverb = input(temp_proverb_set[num])
            count += 1
            #num += 1
            match_count -= 1
        re_ask = input("Would yo like another related proverb?\n>> ")
        num += 1
        if re_ask.lower() == "yes":
            match_count -= 1
            if count >= len(temp_proverb_set):
              return("no more proverbs in this category")
            else:
              print(temp_proverb_set[num])
        elif re_ask.lower() == "no":
            break
        else:
          print("Choose an option")
          break
    f.close()
    temp_proverb_set.clear()
def complete_the_proverb():#works
    print("In this game we test our proverbial knowledge by entering the second half of the proverb prompt.")
    f = open("proverbs.text", "r+")
    proverbs = f.readlines()
    index = random.randint(0,len(proverbs)-1)
    get_half = proverbs[index].split("-")[1].strip('\n')
    #get_half[1] = get_half[1].strip('\n')
    half = get_half.split(" ")
    half_length = len(half)//2
    first_half = " ".join(half[:half_length])
    game = input(first_half)
    #print(first_half + game)
    #print(type(half[0]))
    #print(type(" ".join(half[:half_length])+game))
    abc = first_half + game
    cde = " ".join(half)
    if abc == cde:
        print("Great Job You know this one!!!")
    else:
        print("Not quite. Here is the full proverb - " + " ".join(half))
    f.close()
def learn_a_proverb():#works
    print("LET'S LEARN A PROVERB")
    f = open("proverbs.text", "r+")
    index = random.randint(0,5)#len(f.readlines()))
    proverbs = f.readlines()
    proverb_to_learn = proverbs[index].split("-")[1].strip('\n')
    while True:
        print("Here is your proverb\n",proverb_to_learn)
        ask = input("Type YES when you are ready.\n>> ")
        if ask.lower() == "yes":
            print("///////////////FIVE//////////////////////////////")
            print("//////////////////FOUR///////////////////////////")
            print("////////////////////THREE////////////////////////")
            print("//////////////////////TWO////////////////////////")
            print("/////////////////////////ONE/////////////////////")
            print("///////////////////////////GOOOO/////////////////")
            check = input("Now, Without looking, type the proverb you just learned back to me. \n")
            if check == proverb_to_learn:
                print("Great job!!! You Nailed it.")
                return False
            else:
                print("Not Quite.")
                ask_again = input("Last Try. Retype it.\n")
                if check == proverb_to_learn:
                    print("Great job!!! You Nailed it.")
                    return False 
                else:
                    print("Good Effort.")
                    print(proverb_to_learn)
                    print(type(proverb_to_learn))
                    print(ask_again)
                    print(type(ask_again))
                    print(proverb_to_learn==ask_again)
                    return False
        else:
            return False
    f.close()
prompt_user = input("Welcome to Nyansa. Type \"options\" to see your list of commands.\n>> ")
if prompt_user:
    command_list()
def Nyansa_Function():#works
  while True:
      Nyansa_input = input(">> ")
      if Nyansa_input.lower() == "advice":
          help_with_problem()
      if Nyansa_input.lower() == "options":
          command_list()
      if Nyansa_input.lower() == "add":
          add_proverbs()
      if Nyansa_input.lower() == "game":
          complete_the_proverb()
      if Nyansa_input.lower() == "learn":
          learn_a_proverb()
      if Nyansa_input.lower() == "exit":
          "Thank You for Interacting with Nyansa."
          return False
Nyansa_Function()
