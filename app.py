from openai import OpenAI
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up OpenAI API key
client = OpenAI(api_key="")

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
   data = request.get_json()
   x = data['x']
   y = data['y']
   z = data['z']
    
   prompt = f"Plan {x} for {y} about {z}"
   response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user",
                 "content": prompt}],
      temperature=0.6,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
   )
   suggested_plan = response.choices[0].message.content()
    
   return jsonify({'suggested_plan': suggested_plan})

if __name__ == '__main__':
    app.run(debug=True)