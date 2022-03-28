#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("Input/Letters/starting_letter.txt") as f_starting_letter:
    starting_letter = f_starting_letter.read()

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp

with open ("Input/Names/invited_names.txt") as f_names:
    invited_names = f_names.readlines()

for name in invited_names:
    new_letter = starting_letter.replace("[name]", name.strip())
    with open(f"Output/{name}_invitation.txt", mode="w") as f_invitation:
        f_invitation.write(new_letter)

    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp