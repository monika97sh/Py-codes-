#LEAST COUNT. Between two players. 
count_for_bibek = 0
count_for_monika = 0
while True:
    who_won = input("Who won this round(B/M): ")
    if who_won.upper() == "B" :
        count_for_bibek += 1
    elif who_won.upper() == "M":
        count_for_monika +=1
    else:
        print("Bibek's score", count_for_bibek,"\nMonika's score", count_for_monika)
        if count_for_monika < count_for_bibek:
            print(f"The winner is Bibek by {count_for_bibek - count_for_monika} points")
        else:
            print(f"The winner is Monika by {count_for_monika- count_for_bibek} points")
        break