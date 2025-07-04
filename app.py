from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def madlib():
    if request.method == "POST":
        data = request.form
        madlib_story = f"""
Computer Programming is so {data['adjective']}!
It makes me so excited all the time because I love to {data['verb1']}.
Stay hydrated and {data['verb2']} like you're {data['famous_person']}!

I love to code and I love to learn {data['plural_noun']} every day.
I hope you do too! Let's keep {data['verb_ing']} together!

If you ever need help, just ask {data['person_in_room']}!
They are here to help you on your {data['adjective2']} coding journey.

Remember, coding is {data['adjective3']} and {data['adjective4']}.
So, keep practicing and never give up!

Happy coding, you awesome {data['animal_plural']}!

And don’t forget to subscribe to {data['channel_name']}!
"""
        return render_template("index.html", story=madlib_story)

    return render_template("index.html", story=None)

if __name__ == "__main__":
    app.run(debug=True)
