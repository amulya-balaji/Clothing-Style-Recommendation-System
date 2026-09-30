from flask import Flask, render_template, request
import os

app = Flask(__name__)

# All possible selections
events = ["casual", "party", "interview", "college", "wedding"]
genders = ["male", "female"]
weathers = ["hot", "cold", "rainy"]
styles = ["modern", "trendy", "formal", "traditional"]
ages = ["teen", "adult"]

# Pre-build all product combinations
products = []
for event in events:
    for gender in genders:
        for weather in weathers:
            for style in styles:
                img_name = f"images/{event}_{gender}_{weather}_{style}_1.jpg"
                products.append({
                    "event": event,
                    "gender": gender,
                    "weather": weather,
                    "style": style,
                    "image": img_name
                })

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_event = request.form['event']
    user_gender = request.form['gender']
    user_weather = request.form['weather']
    user_style = request.form['style']
    user_age = request.form['age']

    # Filter matching products
    results = [item for item in products if
               item['event'] == user_event and
               item['gender'] == user_gender and
               item['weather'] == user_weather and
               item['style'] == user_style]

    if not results:
        return render_template('result.html', results=[], message="No image found!")

    # Add description
    for item in results:
        item['description'] = f"{user_age.capitalize()} outfit for {user_gender.capitalize()} - {user_event.capitalize()} event, {user_weather} weather, {user_style.capitalize()} style."

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)