while True:
    cmyk = input("Enter your parameters  for the CMYK format (4 numbers on a real scale from 0.0 "
                       "to 1.0 split by space character): ")
    if cmyk == "e" or cmyk == "exit":
        print("See ya!")
        break
    elif (cmyk.replace(" ", "").replace(".", "")).isnumeric():
        cmyk = cmyk.split(" ")
        cyan = float(cmyk[0])
        magenta = float(cmyk[1])
        yellow = float(cmyk[2])
        black = float(cmyk[3])
        if (cyan >= 0 and cyan <= 1) and (magenta >= 0 and magenta <= 1) and (yellow >= 0 and yellow <= 1) and (black >= 0 and black <= 1):
            white = 1 - black
            red = 255 * white * (1 - cyan)
            green = 255 * white * (1 - magenta)
            blue = 255 * white * (1 - yellow)
            print(f"red = {int(red)}\ngreen = {int(green)}\nblue = {int(blue)}")
        else:
            print("Wrong input!!!\nEnter 4 numbers on a real scale from 0.0 to 1.0 split by space character")
