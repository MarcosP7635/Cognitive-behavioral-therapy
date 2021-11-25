import os
import webbrowser
'''
First we will greet the user with something friendly and inviting then
ask them if they want to open a relevant PDF :)
'''
print("Hello! " +"\n" +
    "Let's do cognitive behavioral therapy to make you feel better :)")
path = 'C:/Users/engin/Downloads/how_to_do_cbt.pdf'
want_PDF = input("Please type something if you would like to see a " +
    "\n releveant PDF :)    ")
url = ("https://www.colorado.edu/herbst/sites/default/files/attached-files/" +
    "how_to_do_cbt.pdf")
'''
Change the filepath in this line to correspond to the file path of a downloaded
relevant PDF. Commented out for now
'''
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//"
        + "Application//chrome.exe"))
if(want_PDF and (not ((want_PDF =="no") or (want_PDF=="No")))):
    webbrowser.get('chrome').open(url)
if(want_PDF and (not ((want_PDF =="no") or (want_PDF=="No")))):
    os.system(path)
'''
The plan is to write all of the prompts and put them in a list.
Then we loop through the list and add each input to a dictionary.
At the end, the dictionary of responses will be added to text file
with the time and date for me to look at when I'm sad.
The idea is to build up responses because I think the cognitive behavior
therapy will get repetitive, and I think it will be good to read it at the end
and track progress.
'''
'''
This is the template for each prompt I can copy paste to add new prompts.
Remember to add it to the list named list_of_prompts too!
promptn = ("  " +
    "\n ")
'''
prompt1 = ( "What thoughts are making you depressed and anxious " )
prompt2 = ( "What is your level of distress on a scale from 1 to 10? Where " +
    "\n 10 is the worst you could ever feel in your life ")
prompt3 = ( "What happened? What were your automatic thoughts")
prompt4 = ( "Based on the PDF, is this a cognitive distortion" )
prompt5 = ( "Write down the cognitive distrotions you notice")
prompt6 = ( "Look at the evidence for and against your thought. You can " +
    "\n write it here if you like" )
prompt7 = ( "What would someone say if they disagree with you. Is there " +
    "\n merit in their opinion?")
prompt8 = ("Consider again what happened and reevaluate the situation without" +
    "\n the cognitive distrotions")
prompt9 = "Write down your new thoughts and feelings"
prompt10 = ("Write down again using the same scale from 1 to 10 how anxious" +
    "\n depressed, or otherwise distressed you feel")
list_of_prompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6,
    prompt7, prompt8, prompt9]
dict_of_prompts = {}
for prompt in list_of_prompts:
        print(prompt)
        long_input = input("Type any character if the answer to the above" +
        " question " + "\n is a long input. Otherwise, just hit enter       ")
        #this works because any non empty string in Python is True
        if(long_input and (not ((input=="no") or (input=="No")))):
            print("Just enter nothing when you are done")
            lines = []
            while True:
                line = input(prompt + ":         ")
                if (line and not (line == "nothing" or line == "Nothing")):
                    lines.append(line)
                else:
                    break
            multi_line_input = '\n'.join(lines)
            dict_of_prompts[prompt] = multi_line_input
        else:
            dict_of_prompts[prompt] = input(prompt + ":         ")
'''
Now we will ask the user if they want a text file. Then if it's a new textfile
or an old one. Same with the folder they want it in. Then the script will
automatically open both the folder and the text file.
'''
want_text_file = input("Would you like to save your responses as a text file?" +
    "\n This would automatically be saved in the folder C:\Therapy\ "
    "\n If so, using underscores instead of spaces, please enter what would you " +
    "\n like to name the file. If not, just hit Enter:         ")
if(want_text_file and (not ((want_text_file=="no") or (want_text_file=="No")))):
    new_cd = input("If you would like to pick the folder it goes in, please " +
        "\n enter the name of it using underscores instead of spaces:         ")
    if(new_cd):
        folder = new_cd
    else:
        folder = "C:\Therapy\_"
    file_name = (folder + "" + want_text_file + ".txt")
    file = open(file_name, "w+")
    for prompt in list_of_prompts:
        line = prompt + ": \n " + dict_of_prompts.get(prompt) + " \n"
        file.write(line)
    file.close()
    os.system(folder)
    os.system(file_name)
print("\n You're a good person and you have value :)")
