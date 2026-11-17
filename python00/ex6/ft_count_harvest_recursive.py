def ft_count_harvest_recursive(day: int = 1) -> None:
    if day == 1:
        days = int(input("Days until harvest: "))
        ft_count_harvest_recursive.days = days

    print("Day", day)

    if day < ft_count_harvest_recursive.days:
        ft_count_harvest_recursive(day + 1)
    else:
        print("Harvest time!")
