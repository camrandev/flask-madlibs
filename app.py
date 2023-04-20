from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import excited_story, silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

#add route to serve selection box at the start
@app.get('/')
def serve_home_page():
    """serves the story selection page for the user"""

    return render_template('selectStory.html', silly=silly_story, excited=excited_story)



#route to handle the root/serve up the basic page
@app.get('/select')
def serve_prompts():
    """serves up the home page for the player to enter choices"""
    story = request.args
    print(f"{story}")
    # prompts = story.prompts

    # return render_template("questions.html", prompts=prompts)
    return 'hi'

#rout to process the story and send it back
@app.get('/results')
def serve_results():
    """returns a story to the user from the text they entered"""
    story = excited_story.get_result_text(request.args)

    return render_template("results.html", story=story)
