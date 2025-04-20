from dotenv import load_dotenv
import os
import requests
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

# Function to translate text
def translate_text(subscription_key, endpoint, region, text, to_language):
    try:
        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': region,
            'Content-type': 'application/json'
        }
        body = [{'text': text}]
        url = f"{endpoint}/translate?api-version=3.0&to={to_language}"
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()[0]['translations'][0]['text']
    except Exception as e:
        return None

# Function to detect the input language
def detect_language(subscription_key, endpoint, region, text):
    try:
        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': region,
            'Content-type': 'application/json'
        }
        body = [{'text': text}]
        url = f"{endpoint}/detect?api-version=3.0"
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()[0]['language']
    except Exception as e:
        return None

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')
        translator_key = os.getenv('TRANSLATOR_KEY')
        translator_endpoint = os.getenv('TRANSLATOR_ENDPOINT')
        translator_region = os.getenv('TRANSLATOR_REGION')
        
        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)
        
        print("Welcome to ABC's FAQ chatbot! Type 'quit' to exit.\n")
        
        # Multilingual chatbot loop
        while True:
            user_question = input("You: ")
            if user_question.lower() == 'quit':
                print("Chatbot: Thank You for using ABC's Services. Goodbye!")
                break

            # Detect input language
            user_language = detect_language(
                translator_key,
                translator_endpoint,
                translator_region,
                user_question
            )
            if not user_language:
                print("Chatbot: I'm sorry, I couldn't detect your language. Please try again.")
                continue

            # Translate user question to English
            translated_question = translate_text(
                translator_key,
                translator_endpoint,
                translator_region,
                user_question,
                'en'
            )
            if not translated_question:
                print("Chatbot: I'm sorry, I couldn't understand your question. Please try again.")
                continue

            # Get response from Question Answering service
            response = ai_client.get_answers(
                question=translated_question,
                project_name=ai_project_name,
                deployment_name=ai_deployment_name
            )

            # Handle QnA response
            if response.answers:
                best_answer = response.answers[0]

                # Translate answer back to the user's language
                translated_answer = translate_text(
                    translator_key,
                    translator_endpoint,
                    translator_region,
                    best_answer.answer,
                    user_language  # Respond in detected language
                )
                if translated_answer:
                    print(f"Chatbot: {translated_answer}")
                else:
                    print("Chatbot: I'm sorry, I couldn't translate the response.")
            else:
                print("Chatbot: I'm sorry, I couldn't find an answer to your question.")

    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()
