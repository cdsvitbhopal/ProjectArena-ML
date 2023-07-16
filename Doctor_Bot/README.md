Aditya Khamitkar   Doctor bot’s Chat bot. 
 
The code above uses the RASA framework to create a simple chatbot. The RASA framework is divided 
into two main components: 
 
RASA NLU: This component is responsible for understanding the user's intent. It does this by using a 
natural language processing (NLP) model to parse the user's message and identify the intent of the 
message. 
RASA Core: This component is responsible for deciding what to do next in the conversation. It does 
this by using a dialogue management model to track the conversation state and determine the next 
action to take. 
In the code above, the greet_user() function uses the RASA NLU component to identify the intent of 
the user's message. If the user's message is a greeting, the function then uses the RASA Core 
component to decide to send a greeting message back to the user. 
 
The architecture of the chatbot is as follows: 
 
Code snippet 
User -> RASA NLU -> RASA Core -> User 
 
The user sends a message to the chatbot. The RASA NLU component then parses the message and 
identifies the intent of the message. The RASA Core component then decides what to do next in the 
conversation. This could involve sending a message back to the user, performing an action, or 
transitioning to a new state in the conversation. 
 
The code above is a very simple example of a chatbot. However, it shows the basic principles of how 
a chatbot using RASA works. To learn more: https://rasa.com/. 
 
Here are some additional details about the code: 
 
The Session class is used to track the state of the conversation. 
The ActionExecuted event is used to indicate that an action has been executed. 
The DialogueTracker class is used to track the conversation history. 
 
 
 
 
 
Aditya Khamitkar   Doctor bot’s Chat bot. 
 
This code will create a simple chatbot that greets the user when they first interact with it. The 
greet_user() function takes the user's ID as input and returns a string containing the greeting 
message. The main() function is the entry point for the code and it calls the greet_user() function 
with the user's ID. 
 
To run this code on VS Code, you will need to install the following packages: 
 
rasa 
rasa-sdk 
Once you have installed the packages, you can run the code by opening the file in VS Code and 
pressing F5. 
 
The code should output the greeting message to the console. For example, if the user's ID is 
"user_1", the code will output the following message: 
 
Code snippet 
Hello, user_1! 
You can also test the chatbot by using the rasa CLI. To do this, run the following command from the 
command line: 
 
Code snippet 
rasa run 
This will start the chatbot in a development server. You can then interact with the chatbot by sending 
it messages through the command line. For example, to greet the chatbot, you would type the 
following command: 
 
Code snippet 
rasa interactive greet 
The chatbot will then greet you back.