# Create a .txt file name Trans.txt(any-other name will be fine)

with open('Trans.txt', 'r+') as file:      # reference file name
    read = file.readline()

print(read)     #Printing the lines in the file

replace = input("What you want to replace ? ")  # prompting the user, what they want to replace
letter = input("With what ? ")      # prompting the user, what they want to replace with

read = read.replace(replace, letter)

with open('Trans.txt', 'w') as file:
    file.write(read)
