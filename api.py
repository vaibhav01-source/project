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


def sentiment_analysis(text):
    prompt = f"""

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()
