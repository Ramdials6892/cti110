def main():
    user_text = input()
    counter = 0
    for x in user_text: 
        if not(x in " .,"):
            counter += 1
    print(counter)
main()
