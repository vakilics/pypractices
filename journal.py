today_date = input("Enter today's date: ")
today_rating = input("How do you rate your mood today: from 1 to 10? ")
your_thaughts = input("Let your thoughts flow: \n")

with open(f"{today_date}.txt", 'w') as file:
    file.write(today_rating + 2*'\n')
    file.write(your_thaughts)