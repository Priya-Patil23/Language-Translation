
from flask import Flask , render_template , request

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("PaulineSanchez/autotrain-translation_food_english_to_french-52830124391")
model = AutoModelForSeq2SeqLM.from_pretrained("PaulineSanchez/autotrain-translation_food_english_to_french-52830124391")

app = Flask(__name__)

@app.route("/")
def greet():
    return  render_template("index.html")

@app.route("/predict" , methods = ["POST"])
def predict():
    input = request.form.get('text').strip()
    src_text = [
        f">>fra<< {input} "
    ]
    translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
    answer = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return render_template("index.html" , result = answer[0])


if "__main__" == __name__:
    app.run(debug = True , host = "0.0.0.0" , port = 5000)