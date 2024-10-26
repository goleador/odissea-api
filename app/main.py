from fastapi import FastAPI
from twilio.rest import Client
from app.core.config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/send")
def send():
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        to="whatsapp:+4152970252",
        from_="whatsapp:+18446206093",
        body="Hello from from Odissea AI!")
    return {"message": "SMS sent successfully"}

@app.get("/receive")
def receive(message: str):
    # Process the received message
    # ...

    # Parse the intent of the message using ChatGPT
    intent = parse_intent(message)
    print(f"Intent: {intent}")

    # Perform actions based on the intent
    if intent == "greeting":
        response = "Hello! How can I assist you?"
    elif intent == "farewell":
        response = "Goodbye! Have a great day!"
    elif intent == "question":
        response = "I'm sorry, I don't have the answer to that question."
    elif intent == "list of food items":
        response = "I'm sorry, I don't have the answer to that question."
    else:
        response = "I'm sorry, I didn't understand your message."

    return {"message": response}

import os
import openai

# Load the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

openai_client = openai.Client(api_key=openai.api_key)


system_prompt = """"You are an assistant for a life coaching application focused on weight loss. Users will send you messages about logging food, logging exercise, or requesting nutritional information. Your job is to:
1. Detect the intent of the user’s message (log_food, log_exercise, request_nutritional_info, general_query).
2. Respond using the appropriate JSON schema based on the detected intent.
3. If you detect that the user wants to log food, check if the user has provided the meal type (breakfast, lunch, dinner), food items and if the user did not provide quantity and unit estimate it based on tipical portion sizes (e.g. 1 glass of wine, 1 egg, 1 service of pasta).

Here are the required JSON structures for each intent:

- For log_food:
{
  "intent": "log_food",
  "meal": "breakfast/lunch/dinner",
  "food_items": [
    {
      "name": "food_name",
      "quantity": number,
      "unit": "unit",
      "calories": number
    }
  ],
  "time_of_day": "time_of_day"
}

- For log_exercise:
{
  "intent": "log_exercise",
  "exercise": {
    "name": "exercise_name",
    "duration": number,
    "unit": "minutes"
  },
  "time_of_day": "morning/afternoon/evening"
}

- For request_nutritional_info:
{
  "intent": "request_nutritional_info",
  "food_item": "food_name",
  "portion_size": {
    "quantity": number,
    "unit": "unit",
    "calories": number
  }
}

If the message is ambiguous or you need more details, ask a clarifying question."""

def parse_intent(message: str) -> str:
    """
    Use ChatGPT to parse the intent of the message.
    """
    # Define the prompt you will use to get the intent from ChatGPT
    prompt = f"Identify the intent of the following message: '{message}'. Respond with the intent in JSON format."
    
    try:
        # Make the request to OpenAI API with ChatGPT model
        chat_completion = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the intent from the response
        intent = chat_completion.choices[0].message.content
        
        # Return the parsed intent
        return intent
    except Exception as e:
        print(f"Error parsing intent: {e}")
        return "unknown"
