new_idea = open("ideas.txt", 'a')
z = new_idea.write(input("What is your new idea? "))
new_idea = open("ideas.txt", 'r+')
for idea in enumerate(new_idea, 1):
    print(idea)
#print('\n')
print(new_idea.readlines())
new_idea.close()