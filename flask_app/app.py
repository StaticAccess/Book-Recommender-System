from flask import Flask, render_template, request
import pickle
import numpy as np

# Load your data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('sc.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    user_input = user_input.strip().lower() 
    
    pt_index_lower = [title.lower() for title in pt.index]
    if user_input not in pt_index_lower:
        return render_template('recommend.html', data=[], message="Book not found. Please try again.")
    
    index = pt_index_lower.index(user_input)
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:11]
    
    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'].str.lower() == pt.index[i[0]].lower()]
        if not temp_df.empty:
            item = [
                temp_df['Book-Title'].iloc[0],
                temp_df['Book-Author'].iloc[0],
                temp_df['Image-URL-M'].iloc[0]
            ]
            data.append(item)

    if not data:
        return render_template('recommend.html', data=[], message="No recommendations available. Please try a different book.")
    
    return render_template('recommend.html', data=data)
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = []

    for _, row in books.iterrows():
        if query.lower() in row['Book-Title'].lower():
            results.append([
                row['Book-Title'],
                row['Book-Author'],
                row['Image-URL-M'],
                row.get('num_rating', 'N/A'),
                row.get('avg_rating', 'N/A')
            ])

    if not results:
        return render_template('search_results.html', results=[], message="No books found. Please try another search.")

    return render_template('search_results.html', results=results)



if __name__ == '__main__':
    app.run(debug=True)
