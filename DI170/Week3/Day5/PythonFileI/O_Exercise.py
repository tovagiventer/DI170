# Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps

# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word into letters
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

with open(r"C:\Users\tova_\code\DI170\DI170\Week3\Day5\PythonFileI\nameslist.txt", "r") as f:
    for line in f:
        print(line.strip())
    # f.readlines()

    lines= f.readlines()
    fifth_line = lines[4]
    print(fifth_line)

    first_five_chars = f.read[5]
    print(first_five_chars)

    names = f.read().splitlines()
    letters = [list(name) for name in names]
    print (letters)

    names = [line.strip() for line in f]

    count_darth = names.count("Darth")
    count_luke = names.count("Luke")
    count_lea = names.count("Lea")

    print("Darth:", count_darth)
    print("Luke:", count_luke)
    print("Lea:", count_lea)

    f.write("\n Tova")

    lines = [line.rstrip("\n") for line in f]
    for name in lines:
        if name == "Luke":
            f.write("Luke Skywalker")
        else:
            f.write(name + "\n")