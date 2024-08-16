from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']

        # Tokenize the texts into words
        words1 = set(text1.split())
        words2 = set(text2.split())

        # Find the differences
        words_in_text1_not_in_text2 = words1 - words2
        words_in_text2_not_in_text1 = words2 - words1

        # Convert sets to strings
        words_in_text1_not_in_text2_str = ' '.join(words_in_text1_not_in_text2)
        words_in_text2_not_in_text1_str = ' '.join(words_in_text2_not_in_text1)

        # Create a DataFrame
        df = pd.DataFrame({
            "Text 1": [text1],
            "Text 2": [text2],
            "Words in Text 1 not in Text 2": [words_in_text1_not_in_text2_str],
            "Words in Text 2 not in Text 1": [words_in_text2_not_in_text1_str]
        })

        # Convert DataFrame to HTML table
        result_table = df.to_html(index=False, classes='table table-bordered table-hover')

        return render_template('index.html', result_table=result_table)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)