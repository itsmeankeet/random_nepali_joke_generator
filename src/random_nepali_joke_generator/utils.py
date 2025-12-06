from google import genai
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from google.genai import types

load_dotenv()


client = genai.Client()


def generate_prompt(topic):
    prompt = """
    You are a humorous Nepali comedian. Generate a short, funny, and clever joke in Nepali based on the following topic: "{topic}". 
    Make sure the joke is culturally relevant, easy to understand, and does not contain offensive content. 
    Keep it under 2 sentences.

    """

    prompt_template = PromptTemplate(template=prompt, input_variables=["topic"])
    prompt = prompt_template.format(topic=topic)
    return prompt


def generate_joke(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="""
    You are a Nepali comedian AI. You take a topic provided by the user and generate a short, funny, clever, and culturally relevant joke in Nepali. 
    The joke should be easy to understand, safe for all audiences, and preferably include emojis. 
    Always keep it under 2 sentences. 
    Do not explain the joke, just output the punchline."""),
        contents=prompt
    )

    return response.text
