from openai import OpenAI
import json

def make_client(API_key):
    client =  OpenAI(api_key= API_key)
    return client


def get_transcript(client, audio_file):
    transcript = client.audio.transcriptions.create(model = "whisper-1", file= audio_file)
    return transcript.text


def ask_question(client, question):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "Answer user's question politely in JSON with your response as the 'response' field."},
        {"role": "user", "content": question}
    ]
    )

    json_response = json.loads(response.choices[0].message.content)
    try: 
        return json_response["response"]
    except:
        print(json_response)
        return "ERROR"
