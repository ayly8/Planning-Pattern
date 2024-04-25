from flask import Flask, render_template, request
import openai import OpenAI

app = Flask(__name__)

# OpenAI API key
api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
openai.api_key = api_key

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = []
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
        z = request.form['z']

        prompt = f"Plan {x} for {y} about {z}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )
        suggestions.append(response.choices[0].text.strip())

    return render_template('index.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)