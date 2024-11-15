import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)

# Initialize Gemini model
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
llm = Gemini(model="models/gemini-1.5-flash")


@app.route("/ask", methods=["POST"])
def ask_bot():
    """Endpoint to ask the bot a question."""
    data = request.get_json()
    question = data.get("question")

    SWITCHHIGH_PROMPT = """
You are a bot in swithchigh website and you answer the questions that are asked to you as a bot assisstant.
Your job is to sell the services on our websites and pitch form them in very prompt manner and short responses.
Answer user queries nicely and politely.

Here is information about switchhigh services for your reference :

About Switchhigh
Mastering Challenges in Digital Technology is Our Expertise
SwitchHigh is an innovative digital consulting house established to improve business growth and innovation in this fast-pace era of digital. Our solutions are offered to the B2B and B2C clients from all industries to enhance their online presence and push them toward business success.

Switchhigh’s Commitment to Success. Unlock Excellence in Web Development, and more !

Dedicated Towards Customer Satisfaction
30 Days Money-Back Guarantee
Discover More
about-us-three__thumb
about-us-three__thumb__award__inner
Digital Consultancy
Company

Our Digital Marketing Services In India
We Offer the Best
Consultancy and IT Services

Here is the question asked by user: {question}

INSTRUCTIONS FOR OUTPUT:-
- Give one or two liner answers.
- Do not give very lengthy responses.
- Do not entertain any query that does not resonates with switchhigh's services.
- company website: https://switchhigh.com/ company contact :- 7626936858
"""

    # Generate response from LLM
    response = llm.complete(SWITCHHIGH_PROMPT.format(question=question))
    return jsonify({"response": str(response)})


@app.route("/")
def home():
    """Home endpoint."""
    return jsonify({"message": "Welcome to SwitchHigh bot!"})


if __name__ == "__main__":
    app.run(debug=True)
