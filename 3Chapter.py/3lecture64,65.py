
import random
isRunning = True
while isRunning:
    winning_number = random.randint(1,100)
    # while True:
    guess_number=0
    play_times=0
    print("\n")
    while guess_number!=winning_number:
        play_times+=1
        guess_number=int(input("\nguess the winning number : "))
        if winning_number>guess_number:
            print("to low "   "\n guess again")
        elif winning_number<guess_number:
            print("to high "   "\n guess again")
        elif winning_number==guess_number :
            print(f"YOu are winner , you win in {play_times} times")
    ans=input("\npress q for quit or r for replay : ")
    if ans=="q":
        isRunning = False
    elif ans == "r":
        pass

print("\n\n you are quiting...")
print("\n")
