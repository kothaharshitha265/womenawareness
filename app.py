from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq
from ai_agent import SocialAwarenessAgent
from report_generator import ReportGenerator
import os

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise Exception("GROQ API KEY NOT FOUND")

client = Groq(api_key=api_key)

agent = SocialAwarenessAgent(client)
report_generator = ReportGenerator()

os.makedirs("reports", exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_report():

    topic = request.form['topic']

    content = agent.generate_awareness_content(topic)

    word_count = report_generator.count_words(content)

    # enforce minimum words
    if word_count < 2000:
        extra = agent.generate_awareness_content(
            f"Expand and add more details to: {topic}"
        )
        content += "\n" + extra
        word_count = report_generator.count_words(content)

    # enforce max words
    if word_count > 4000:
        content = " ".join(content.split()[:4000])
        word_count = 4000

    text_file = report_generator.save_text_report(topic, content)
    pdf_file = report_generator.save_pdf_report(topic, content)

    return jsonify({
        "topic": topic,
        "word_count": word_count,
        "text_report": text_file,
        "pdf_report": pdf_file,
        "preview": content[:1000]
    })

if __name__ == "__main__":
    app.run(debug=True)