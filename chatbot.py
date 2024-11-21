
from groq import Groq

API_KEY = "<YOUR_GROQ_API_KEY>"

client = Groq(api_key=API_KEY)


def chat_response(conversation_history):

    chat_completion = client.chat.completions.create(
    messages=conversation_history,  
    model="llama3-8b-8192", 
    )
    ai_response = chat_completion.choices[0].message.content
    return ai_response
     