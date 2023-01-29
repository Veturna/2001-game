

move = roll()
    user_points = 0
    computer_points = 0

    input("Click enter to roll the dice!")
    user_points += move
    computer_points += move

    while computer_points < 2001 and user_points < 2001:
        print(f"""Your points: {user_points}
Computer points: {computer_points}""")

        input("Click enter to roll the dice!")
        user_points = add_points(user_points)
        computer_points = add_points(computer_points)

    print(f"""Your points: {user_points}
Computer points: {computer_points}""")

    if user_points > computer_points:
        print("You win!")
    if computer_points > user_points:
        print("Computer win!")
    else:
        print("Draw!")
