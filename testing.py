import streamlit as st

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

first_message_list = ["Help lines:", 
    "If you or others are in immediate danger, or fear for your safety please call 911",
    "\nIf this is on the Caltech campus please call: 626 395 5000",
    "\nNational Suicide hotline: call 1-800-273-8255",
    "\nLifeline Crisis chat:",
    "http://chat.suicidepreventionlifeline.org/GetHelp/LifelineChat.aspx",
    "\nIf you are feeling suicidal, threatened, or need someone to talk to please please seek help from the following resources:",
    "\nCaltech Counseling Center 24/7 phone number: (626) 395-8331",
    "\nTitle IX Office https://equity.caltech.edu/ Diversity Center https://diversity.caltech.edu/"]
st.write("Hello! " +"\n" +
    "Let's do cognitive behavioral therapy to make you feel better.")
st.write("You're a good person and you have value :)")
st.write("\nPlease read this message first:")
for message in first_message_list:
    st.write(message)
st.text_input("Please hit enter when you are ready to continue with CBT")

url = ("https://www.colorado.edu/herbst/sites/default/files/attached-files/" +
    "how_to_do_cbt.pdf")
google_drive_url = ("https://drive.google.com/file/d/" +
           "1-hKJEgfNDixWbKuvTYMhCK379RD3y7Du/view?usp=sharing")
tiny_url = ("https://tinyurl.com/how2cbtpdf")
st.write("\nPlease click on at least one of the following links for a free access"
      + " PDF of \"How to Do CBT\"\n" + tiny_url + "\n" + url + "\n" +
      google_drive_url +"\n" )

# This is writing directly to the main body. Since the form container is
# defined above, this will appear below everything written in the form.

prompt1 = ( "What thoughts are making you depressed and anxious?" )
prompt2 = ( "What is your level of distress on a scale from 1 to 10? Where " +
    "10 is the worst you could ever feel in your life.")
prompt3 = ( "What happened? What were your automatic thoughts?")
prompt4 = ( "Based on the PDF, is this a cognitive distortion?" )
prompt5 = ( "Please write the cognitive distrotions you notice.")
prompt6 = ( "Look at the evidence for and against your thought. You can " +
    "write it here if you like" )
prompt7 = ( "What would someone say if they disagree with you? Is there " +
    "merit in their opinion?")
prompt8 = ("Consider again what happened and reevaluate the situation without " +
    "the cognitive distrotions.")
prompt9 = "Write down your new thoughts and feelings."
prompt10 = ("Write down again using the same scale from 1 to 10 how anxious, " +
    "depressed, or otherwise distressed you feel.")
list_of_prompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6,
    prompt7, prompt8, prompt9]
dict_of_prompts = {}

def main():
    question = st.form('my_question')
    current_index = -1
    # These methods called on the form container, so they appear inside the form.
    submit = question.form_submit_button('Click here to proceed.')
    if submit:
        current_index += 1
        ask(current_index, question)

def ask(current_index, question):
    if not current_index < len(list_of_prompts):
        st.stop()
    prompt, text_input_key = list_of_prompts[current_index], current_index+1
    if current_index == len(list_of_prompts) - 1:
        submit_text = question.text_area(prompt + 
            " Please reload the page or go to this website again if you need to continue.", 
            key = text_input_key*-1)   
        st.write("\nYou're a good person and you have value")
    else:
        submit_text = question.text_area(prompt + 
            " Please click the button at the top or hit ctrl+enter to proceed.", 
            key = text_input_key*-1)
    #submit_button = question.form_submit_button(
    #    f'Click here to or hit ctrl+enter to enter your response')
    if submit_text:# or submit_button:
        #new_question = st.form('my_question' + str(current_index))
        ask(current_index+1, question)
main()