class SocialAwarenessAgent:

    def __init__(self, client):
        self.client = client

    def generate_awareness_content(self, topic):

        prompt = f"""
        You are an expert AI social awareness writer.

        Write a detailed report on: {topic}

        Requirements:
        - 2000 to 4000 words
        - Structured headings
        - Introduction, Problems, Solutions, AI Role, Future Scope, Conclusion
        - Simple English
        """

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content