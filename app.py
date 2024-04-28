from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = ""

# create api endpoint called generate_plan to handle POST and GET requests
@app.route('/generate_plan', methods=['POST', 'GET'])
def generate_plan():
   if (request.method == 'POST'):
      data = request.get_json()
      x = data['x']
      y = data['y']
      z = data['z']
    
      prompt = f"Plan {x} for {y} about {z}"
      response = openai.Completion.create(
         model="gpt-3.5-turbo",
         messages=[{"role": "user",
                  "content": prompt}],
         temperature=0.6,
         max_tokens=500,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0
      )
      suggested_plan = response.choices[0].text
      
      return jsonify({'suggested_plan': suggested_plan})
   
if __name__ == '__main__':
    app.run(debug=True)