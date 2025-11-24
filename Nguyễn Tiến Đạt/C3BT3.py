try:
    Score = input("Enter Score:")
    print("-----------------------------")
    Score = float(Score)
except:
    print("Enter Score:",Score)
    print("Bad Score")
    quit()
if Score >= 0.0 and Score <= 1.0:
    if Score >= 0.9:
        print("Enter Score:",Score)
        print("A")
    elif Score >= 0.8:
        print("Enter Score:",Score)
        print("B")
    elif Score >= 0.7:
        print("Enter Score:",Score)
        print("C")
    elif Score >= 0.6:
        print("Enter Score:",Score)
        print("D")
    else:
        print("Enter Score:",Score)
        print("F")
else:
    print("Enter Score:",Score)
    print("Bad Score")



