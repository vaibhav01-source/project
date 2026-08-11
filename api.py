from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client()

#common api handler
def generate_ai_response(prompt):
    try:
        response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
        )

        return True,response.text
    
    except Exception as e:
        print("Gemini API Error:",e)
        return False,None

def summarize_txt(text):
    prompt=f"summarize this text clearly and concisely:\n\n{text}"

    return generate_ai_response(prompt)


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

    return generate_ai_response(prompt)

def sentiment_analysis(text):
    prompt = f"""
    You are a professional sentiment analysis system.

    Analyze the sentiment of the user's text and classify it into exactly one of these categories:

    * Positive: The text expresses satisfaction, happiness, appreciation, approval, or other positive emotions.
    * Negative: The text expresses dissatisfaction, anger, disappointment, criticism, sadness, or other negative emotions.
    * Neutral: The text is factual, objective, unclear, or does not express a meaningful positive or negative emotion.

    Important rules:

    1. Consider the overall meaning and context of the text, not just individual words.
    2. Detect sarcasm, negation, and mixed emotions when possible.
    3. If the text contains both positive and negative opinions, classify it based on the dominant overall sentiment.
    4. Do not add assumptions that are not present in the text.
    5. Keep the explanation concise.
    6. Return ONLY valid JSON. Do not include Markdown, code fences, or additional text.

    Return exactly this JSON structure:

    {{
    "sentiment": "Positive | Negative | Neutral",
    "confidence": 0.0,
    "reason": "Brief explanation of the detected sentiment"
    }}

    The confidence value must be a number between 0 and 1.

    User text:
    "{text}"
    """

    return generate_ai_response(prompt)
