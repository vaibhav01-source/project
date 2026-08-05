from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client()


def summarize_txt(text):
    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"summarize this text:\n\n{text}"
    )

    return response.text

'''
from openai import OpenAI
client2 = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def abuse_detn(text):
    response = client2.moderations.create(
        model="omni-moderation-latest",
        input=text)
    result=response.results[0]
    if result.flagged:
        return "⚠️ Abusive/Inappropriate content detected."
    else:
        return "✅ Content is safe."


'''

def abuse_detn(text):

    prompt = f"""
    Determine whether the following text contains abusive, hateful,
    offensive, or toxic language.

    Respond with only one word:
    ✅ SAFE
    or
    ⚠️ABUSIVE

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()