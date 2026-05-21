-----------.env-----------
is about the python package included in it so this contains the groq key
which is from the groq 


----------------agent.py----------------
i have imported the .env,groq and os from existing packages or libraries
loaded .env and loaded the api key using .getenv 
and also i gave that if api not found in .env give as error as not found output
here client creates a groq api client
and self gives a "llama-3.3-70b-versatile" model

-------------------app.py-----------------
This program imports ReportGenerator and creates a simple CLI app to generate AI reports.
It asks the user to enter a topic and 
then uses the generator to create a detailed report using AI.
The report is saved as a .txt file, and it also prints the word count, filename, and preview.
If any error occurs during generation, it catches and displays the error message.

-------------------------prompt.py-----------------------------

it gives the prompts like  while executing we can see the report of text format
REPORT_PROMPT = """
#Generate a detailed social awareness report on the topic: {topic}.

1. Introduction
2. Causes
3. Effects on Society
4. Real-world Examples
5. Government Initiatives
6. Solutions
7. Conclusion
"""

--------------------report_generator.py---------------

it imports agent as socialawarenessagent
and it also import the prompt file as report prompt
here we defined the agents model as we used and also limiting the word count as 2000 to 4000 words
and generates the report from it and we can get the report as womens_report.txt

---Generates and expands AI report for given topic

 
---Counts number of words in generated report

Sends a structured prompt to the AI model
Generates a detailed report using LLaMA model from Groq API
Limits the final report to 4000 words
Returns the final generated report



---------------------
so this is a basic project in which we have included the api key from groq and the report i have generated in this using "llama-3.3-70b-versatile" and i have also gave and several attempts like using versatile versions in it  
i have also build an agent an agent which behaves like a human it can be perform its tasks by not assisting to it and also generated the reports its all about the terminal output if we use frontend we can get a UI screen to it  i can also use the gemini api key to include the rag model to gemini but we need to buy the api key from them so i used the groq


Format prompt with topic  
Send request to Groq AI model  
Receive initial report  
Expand report if needed (up to 5 attempts)  
Trim report if it exceeds 4000 words  (like throwing a error to it if extends the words)
Return final report  

#to run a program

pip install google-genai(to install libraries)
pip install python-dotenv   -for api key usage packages
run using app.py
