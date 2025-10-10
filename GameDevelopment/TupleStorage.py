x = 0
for i in range(5):
    x += 1
    group_name = input("\nWhat is the name of Group #" + str(x) + "? ")
    group_size = input("How many people are in your group? ")
    competition_date = input("When did you compete in the tournament? ")
    competition_venue = input("Where was the competition held? ")
    medal_type = input("What medal did you receive? ")
    print("")
    if x == 1:
        group_1 = group_name, group_size, competition_date, competition_venue, medal_type
        print(group_1)
    elif x == 2:
        group_2 = group_name, group_size, competition_date, competition_venue, medal_type
        print(group_2)
    elif x == 3:
        group_3 = group_name, group_size, competition_date, competition_venue, medal_type
        print(group_3)
    elif x == 4:
        group_4 = group_name, group_size, competition_date, competition_venue, medal_type
        print(group_4)
    else:
        group_5 = group_name, group_size, competition_date, competition_venue, medal_type
        print(group_5)
