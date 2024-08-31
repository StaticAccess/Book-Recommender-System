<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Recommender System</title>
</head>
<body>
    <h1>Book Recommender System</h1>
    <p>The Book Recommender System is a web application built with Flask that allows users to search for books and receive personalized recommendations based on collaborative filtering. The system also includes a popularity-based recommendation feature. The app is deployed at <a href="https://book-recommender-system-qpiz.onrender.com/">Book Recommender System</a>.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Search for Books</strong>: Users can search for books by title and see relevant details such as author and rating.</li>
        <li><strong>Get Recommendations</strong>: Users can receive book recommendations based on a specific book they enter.</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>Flask</li>
        <li>Pandas</li>
        <li>NumPy</li>
        <li>Gunicorn (for Linux deployment)</li>
        <li>Waitress (for Windows deployment)</li>
    </ul>

    <h2>Setup</h2>

    <h3>1. Clone the Repository</h3>
    <p>Clone the repository to your local machine:</p>
    <pre><code>git clone https://github.com/yourusername/book-recommender-system.git
cd book-recommender-system</code></pre>

    <h3>2. Create and Activate a Virtual Environment</h3>
    <p><strong>On Windows:</strong></p>
    <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>

    <p><strong>On macOS/Linux:</strong></p>
    <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>

    <h3>3. Install Dependencies</h3>
    <p>Install the required Python packages:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>Running the Application Locally</h2>

    <h3>On Windows</h3>
    <p>Activate the Virtual Environment:</p>
    <pre><code>venv\Scripts\activate</code></pre>

    <p>Run the Flask Application:</p>
    <pre><code>python app.py</code></pre>

    <p>Open your web browser and visit <a href="http://localhost:5000">http://localhost:5000</a>.</p>

    <h3>On Linux</h3>
    <p>Activate the Virtual Environment:</p>
    <pre><code>source venv/bin/activate</code></pre>

    <p>Run the Flask Application using Gunicorn:</p>
    <pre><code>gunicorn -w 4 app:app</code></pre>

    <p>Open your web browser and visit <a href="http://localhost:8000">http://localhost:8000</a>.</p>

    <h2>WSGI Setup for Production</h2>

    <h3>On Windows (Using Waitress)</h3>
    <p>Create a <code>serve.py</code> file in the project root:</p>
    <pre><code>from waitress import serve
from app import app

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)</code></pre>

    <p>Run the server:</p>
    <pre><code>python serve.py</code></pre>

    <h3>On Linux (Using Gunicorn with Nginx)</h3>
    <p>Install Nginx:</p>
    <pre><code>sudo apt-get install nginx</code></pre>

    <p>Configure Nginx:</p>
    <p>Create a configuration file in <code>/etc/nginx/sites-available/book_recommender</code>:</p>
    <pre><code>server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}</code></pre>

    <p>Enable the Configuration:</p>
    <pre><code>sudo ln -s /etc/nginx/sites-available/book_recommender /etc/nginx/sites-enabled/</code></pre>

    <p>Restart Nginx:</p>
    <pre><code>sudo systemctl restart nginx</code></pre>

    <p>Run the Flask Application using Gunicorn:</p>
    <pre><code>gunicorn -w 4 app:app</code></pre>

    <h2>Deployment</h2>
    <p>The application is deployed at <a href="https://book-recommender-system-qpiz.onrender.com/">Book Recommender System</a>. This deployment uses a cloud platform that can be configured similarly to the local setup but optimized for production environments.</p>

    <h2>File Structure</h2>
    <ul>
        <li><code>app.py</code> - Contains the Flask application code, routes, and recommendation logic.</li>
        <li><code>templates/</code> - Contains the HTML templates for rendering web pages.</li>
        <li><code>static/</code> - Contains static files like CSS, JavaScript, and images.</li>
        <li><code>requirements.txt</code> - Lists project dependencies.</li>
        <li><code>serve.py</code> - Script to run the application using Waitress (Windows only).</li>
    </ul>

    <h2>How it Works</h2>

    <h3>Popularity-Based Recommendations</h3>
    <p>The application loads a dataset (<code>popular.pkl</code>) containing popular books based on the number of ratings and average rating scores. This data is used to display popular books on the homepage.</p>

    <h3>Collaborative Filtering Recommendations</h3>
    <p>The application uses a collaborative filtering approach. When a user inputs a book, the system calculates similarity scores (<code>sc.pkl</code>) with other books. The top 10 similar books are recommended to the user.</p>

    <h2>Notes</h2>
    <ul>
        <li>Make sure to properly configure your production environment, including security settings and proper handling of static files.</li>
        <li>For local development, the Flask server is sufficient, but for production, using Gunicorn (on Linux) or Waitress (on Windows) with Nginx is recommended for better performance and security.</li>
    </ul>
</body>
</html>
