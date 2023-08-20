
#the is_no() function is used to evaluate whether the user says no to a question
#It outputs True if the user said no. Otherwise, it outputs False.

import streamlit as st
#To be used to evaluate user input
def is_no(string):
  substring_list = ("no", "No", "NO", "nO", "nah")
  output = False
  for substring in substring_list:
    if substring in string:
      output = True
      return output
  return output


#First we will greet the user with something friendly and inviting then
#ask them if they want to open a relevant PDF for what this is based on :)

first_message = ("\n" +
    "\nHelp lines:\n" +
    "If you or others are in immediate danger, or fear for your safety: " +
    "please call 911\nEmergency on Caltech campus: please call: 626 395 5000" +
    "\nNational Suicide hotline: call 1-800-273-8255" +
    "\nLifeline Crisis chat:" +
    "http://chat.suicidepreventionlifeline.org/GetHelp/LifelineChat.aspx\n" +
    "If you are feeling suicidal, threatened, or need someone " +
    "to talk to please please\nseek help from the following resources:\n" +
    "Counseling Center, 24/7 phone number: (626) 395-8331"
    "\nTitle IX Office https://equity.caltech.edu/" +
    "\nDiversity Center https://diversity.caltech.edu/"
)
print("Hello! " +"\n" +
    "Let's do cognitive behavioral therapy to make you feel better.")
print("You're a good person and you have value :)")
print("\nPlease read this message first:", first_message)
st.text_input("Please hit enter when you are ready to continue with CBT")


url = ("https://www.colorado.edu/herbst/sites/default/files/attached-files/" +
    "how_to_do_cbt.pdf")
google_drive_url = ("https://drive.google.com/file/d/" +
           "1-hKJEgfNDixWbKuvTYMhCK379RD3y7Du/view?usp=sharing")
tiny_url = ("https://tinyurl.com/how2cbtpdf")
st.echo("\nPlease click on at least one of the following links for a free access"
      + " PDF of \"How to Do CBT\"\n" + tiny_url + "\n" + url + "\n" +
      google_drive_url +"\n" )
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
prompt1 = ( "What thoughts are making you depressed and anxious?" )
prompt2 = ( "What is your level of distress on a scale from 1 to 10? Where " +
    "10 is the worst you could ever feel in your life ")
prompt3 = ( "What happened? What were your automatic thoughts?")
prompt4 = ( "Based on the PDF, is this a cognitive distortion?" )
prompt5 = ( "Write down the cognitive distrotions you notice")
prompt6 = ( "Look at the evidence for and against your thought. You can " +
    "write it here if you like" )
prompt7 = ( "What would someone say if they disagree with you. Is there " +
    "merit in their opinion?")
prompt8 = ("Consider again what happened and reevaluate the situation without" +
    "the cognitive distrotions")
prompt9 = "Write down your new thoughts and feelings"
prompt10 = ("Write down again using the same scale from 1 to 10 how anxious" +
    "depressed, or otherwise distressed you feel")
list_of_prompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6,
    prompt7, prompt8, prompt9]
dict_of_prompts = {}
for prompt in list_of_prompts:
        st.echo(prompt)
        long_input = st.text_input("Type any character if the answer to the above" +
        " question " + "is a long input. Otherwise, just hit enter:\n")
        #this works because any non empty string in Python is True
        if(long_input and (not is_no(long_input))):
            print("Just enter nothing when you are done")
            lines = []
            while True:
                line = st.text_input(prompt + "\nplease type here: ")
                if (line and not (line == "nothing" or line == "Nothing")):
                    lines.append(line)
                else:
                    break
            multi_line_input = '\n'.join(lines)
            dict_of_prompts[prompt] = multi_line_input
        else:
            if not "?" in prompt:
              dict_of_prompts[prompt] = st.text_input(prompt + ":\n")
            else:
               dict_of_prompts[prompt] = st.text_input(prompt + "\n")

print("\nYou're a good person and you have value")
