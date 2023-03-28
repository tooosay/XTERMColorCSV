# this program just prints colors with hex code and color numbers


from dict import NUMBER_RGB, NUMBER_HEX, NUMBER_NAME

# color reset
reset = "\033[0m"

# print all colors
for i in range(0,256):
    R,G,B = NUMBER_RGB[i]
    background = f"\033[48;2;{R};{G};{B}m"
    hexcode = NUMBER_HEX[i]
    print(background+hexcode+reset, end="")
    if (i+1) % 16 == 0:
        print()

print()

# print 16 system colors
for i in range(2):
    for j in range(0,16):
        R,G,B = NUMBER_RGB[j]
        fgcolor = f"\033[38;2;{R};{G};{B}m"
        bgcolor = f"\033[48;2;{R};{G};{B}m"
        if not i:
            print(str(j).center(5)+reset,end="")
        else:
            print(bgcolor+"     "+reset,end="")
    print()
print()


# print color cubes
start = 16
max_chunk = 3
line_of_start = start+6
for i in range(2):
    count = 0
    for j in range(6*6*3):
        R,G,B = NUMBER_RGB[start+count]
        bgcolor = f"\033[48;2;{R};{G};{B}m"
        #if start+count >= 226:
        #    bgcolor = bgcolor+f"\033[38;2;150;150;150m"
        print(bgcolor+str(start+count).center(5)+reset, end="")
        count += 1
        if count == 6:
            print("   ",end="")
            start = start + 6*6
            count = 0
            max_chunk -= 1

        if max_chunk == 0:
            print()
            max_chunk = 3
            start = line_of_start
            line_of_start += 6
    start = 124
    line_of_start = start+6
    print()

# print 24 shades of gray        
for i in range(2):
    for j in range(232,256):
        R,G,B = NUMBER_RGB[j]
        fgcolor = f"\033[38;2;{R};{G};{B}m"
        bgcolor = f"\033[48;2;{R};{G};{B}m"
        if not i:
            print(str(j).center(5)+reset,end="")
        else:
            print(bgcolor+"     "+reset,end="")
    print()



