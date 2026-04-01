import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class StoryEngine:
    def __init__(self, model="gpt-3.5-turbo"):
        self.story = []
        self.model = model

    def generate(self, system_prompt, user_prompt, temperature=0.7, max_tokens=300):
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            response = client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

    def continue_story(self, genre, user_text="", temperature=0.7):
        if user_text:
            self.story.append(user_text)

        system_prompt = f"""
You are a master collaborative storyteller.
Rules:
- Stay strictly in {genre} genre
- Maintain consistency with all previous events and characters
- Never contradict earlier story
- Write vivid, engaging narrative
"""
        full_story = "\n".join(self.story)
        user_prompt = f"Continue the story:\n{full_story}"
        result = self.generate(system_prompt, user_prompt, temperature)
        self.story.append(result)
        return result

    def give_choices(self, genre, temperature=0.7):
        system_prompt = f"""
You are a storyteller generating branching story options.
Rules:
- Stay in {genre} genre
- Keep consistency with previous story
- Provide 3 possible next events
"""
        full_story = "\n".join(self.story)
        user_prompt = f"Story so far:\n{full_story}\n\nProvide 3 choices, each on a new line."
        result = self.generate(system_prompt, user_prompt, temperature)
        choices = [c for c in result.split("\n") if c.strip()]
        return choices[:3]
