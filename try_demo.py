is_not_valid = True
while is_not_valid:
    user_input = input("gimme a number ")
    try:
        user_int = int(user_input)
        is_not_valid = False
        print ("You gave me the number %d" % (user_int,))
    except:
        print("boooooooooooo get outtta here! %s is not a number" % user_input)
        pass 