import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

# create Flask server
app = Flask(__name__)
# hide API key
load_dotenv(find_dotenv())
api_key = os.environ.get("API_KEY")

# set up OpenAI API key
client = OpenAI(api_key=api_key)

# create api endpoint for home/base page to handle GET requests
@app.route('/', methods=['GET'])
def render_homepage():
   return render_template('index.html')

# create api endpoint called generate_plan to handle POST requests
@app.route('/generate_plan', methods=['POST'])
def generate_plan():
   # receives the user input
   data = request.get_json()
   x = data['x']
   y = data['y']
   z = data['z']
   # puts the xyz into the prompt
   prompt = f"Plan {x} for {y} about {z}"
   # call the chatgpt api to get the suggested result
   response = client.chat.completions.create(
               model="gpt-3.5-turbo",
               messages=[{"role": "user", 
                        "content": prompt}],
               temperature=0.6,
               max_tokens=4096,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0
            )
   # store the result into variable suggested_plan
   suggested_plan = response.choices[0].message.content
   
   # returns suggested plan in form of js dictionary (key: value) format
   return jsonify({'suggestion': suggested_plan})

# run Flask server
if __name__ == '__main__':
    app.run(debug=True)