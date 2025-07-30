import gradio as gr
from fastai.learner import load_learner
from fastai.vision.core import PILImage

learn_inf = load_learner("recycling_classifier_12class.pkl")
categories = learn_inf.dls.vocab

def classify_image(img):
    pred, idx, probs = learn_inf.predict(img)
    return {categories[i]: float(probs[i]) for i in range(len(categories))}

title = "Recycling Waste Classifier (12 Classes)"
description = (
    "Upload a photo of waste and the model will classify it as one of: "
    + ", ".join(categories)
    + ".<br>Powered by fastai + Gradio.<br>"
    "<b>Example classes:</b> battery, biological, brown-glass, cardboard, clothes, green-glass, metal, paper, plastic, shoes, trash, white-glass."
)

gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title=title,
    description=description,
    allow_flagging="never"
).launch()