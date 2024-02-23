from record import record_audio
from chat import make_client, get_transcript, ask_question
from output import read_text
import json


def detect_key_word(transcript):
    transcript_words = transcript.split(" ")

    for i in range(len(transcript_words) - 1):
        current_word = transcript_words[i]
        next_word = transcript_words[i + 1]

        current_word = current_word.lower().strip(",").strip(" ").strip(".")
        next_word = next_word.lower().strip(",").strip(" ").strip(".")

        if (current_word == "hey") and (next_word == "chat"):
            try:
                return ' '.join(transcript_words[i+2:])
            except IndexError:
                return



def main():
    # _KEY = "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"

    with open("config.json", "r") as config:
        _KEY = json.load(config)["GPT_KEY"]


    while True:
        record_audio()
        with open("output.wav", "rb") as wav:

            read_text("Let me see")

            client = make_client(_KEY)

            transcript = get_transcript(client, wav)

            result = detect_key_word(transcript)

            if result == None:
                continue

            if result.strip(",").strip(" ").strip(".") == "exit":
                read_text("goodbye")
                break

            answer = ask_question(client, result)

            read_text(answer)


if __name__ == "__main__":
    main()
