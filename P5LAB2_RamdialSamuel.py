def miles_to_laps(user_miles):
    user_laps = user_miles / 0.25
    return user_laps

if __name__ == '__main__':
    input_val = float(input())
    user_laps = miles_to_laps(input_val)
    print('{:.2f}'.format(user_laps))