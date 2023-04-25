from machinetranslation import translator
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    englishToFrench('Good morning')

@app.route("/frenchToEnglish")
def frenchToEnglish():
    frenchToEnglish('Bonjour, bonjour')

@app.route("/")
def renderIndexPage():
    return "Wayne's Translator"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
