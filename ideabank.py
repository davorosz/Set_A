

Ideabank = open("ideas.txt", "r+")


lines = 0

for i in Ideabank.readlines():
    
    lines += 1

Ideabank = open("ideas.txt", "r+")

print(Ideabank.read())

Ideabank = open("ideas.txt", "a")

Idea = input("new idea: ")

    Ideabank.write("\n" + str(lines) + "." + Idea)

ideabank.close()
