<h1>Language Translation</h1>

<h3>This project provides an efficient way to translate English to French.</h3>

<pre>
Two ways are used to solve the problem:
1. Simple Encoder and Decoder with the help of the LSTM model.
2. Pretrained model from hugging face library.

In the early stage, we have visualized the data, for example, the length of words in both the languages.
We also plotted the most common words from both languages discarding stopwords.

After getting one with the data we are heading towards model building. At first, we are building a simple encoder-decoder model with LSTM.
We are training the model for only 4 epochs and the accuracy is 91%. Of course, we can make a model bit more complex by stacking several LSTM models but again it will take a lot of time to train the model.

Then we use the pre-trained model from hugging face which is already been trained on the data (English to French).
We are using it to translate the user input.

The UI includes the text area to type your message and then the corresponding translated text would be shown next to it.


</pre>