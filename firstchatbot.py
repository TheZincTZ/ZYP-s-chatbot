variable = False

while not variable:
    print("Hello Ying Ying, this is a chatbot made for you. Type Y to continue:)")
    print("=" * 100)
    
    answer = input("Type 'Y' here: ")
    
    while answer.lower() != "y":
        print("=" * 100)
        print("Wrong input, try again:) Type 'Y': ")
        print("=" * 100)
        answer = input("Type 'Y' here: ")
    
    print("=" * 100)
    print("Why not type 'show me to see a surprise?:>")
    print("=" * 100)
    
    showme = input("Type 'Show Me' to see the surprise: ")
    
    while showme.lower() != "show me":
        print("=" * 100)
        print("Wrong input, try again:) Type 'Show Me': ")
        print("=" * 100)
        showme = input("Type 'Show Me' to see the surprise: ")
    
    print("=" * 100)
    print("Happy 1 month of knowing each other:>")
    print("Can we continue to know each other better and walk through the year together?")
    print("=" * 100)
    
    youranswer = input("Yes or No?: ")
    
    while youranswer.lower() != "yes":
        print("=" * 100)
        print("Wrong input, try again:) Type 'Yes': ")
        print("=" * 100)
        youranswer = input("Yes or No?: ")
    
    print("=" * 100)
    print("I promise I'll treat you right this year")
    print("Give us one more month and I promise that I am genuine to you")
    print("I will be there through your Ups and Downs")
    variable = True

print("=" * 100)
print("Once again, Happy 1 month!:)")
print("Hope you find this chatbot interesting:) Next time, I'll show you something else that is better")
