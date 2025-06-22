# Simple Twitter

#### Video Demo:  <https://youtu.be/your_video_id_here>
#### Description:

Simple Twitter is a web application as my final project for CS50x. It is a minimalist clone of Twitter, focusing on the core functionality: user authentication, post creation, and a real-time global feed. The application is built from the ground up using Python and the Flask web framework on the backend, with a SQLite database for data persistence. The frontend is crafted with HTML, custom CSS, and the Bootstrap 5 framework to ensure a responsive, modern, and intuitive user interface.

---

#### Core Features
*   **Full User Authentication:** Users can register for a new account with a unique username and a securely hashed password. Existing users can sign in and sign out of their sessions.
*   **Post Creation:** Authenticated users can create and publish short text posts (up to 150 characters).
*   **Global Feed:** The homepage displays all posts from all users in a single, reverse-chronological feed, making it a public timeline.
*   **Dynamic UI with Theme Switching:** The website features a clean, responsive design with a fully functional light/dark mode toggle. The user's choice is saved and automatically applied on their next visit.
*   **Flash Messaging:** Users receive clear, non-intrusive feedback for actions like successful logins, logouts, or post creation through Bootstrap alerts.

### Project Structure

The project is organized into a standard Flask application structure.

```
├── app.py                  # Main Flask application, routes, and logic
├── simple_twitter.db       # SQLite database file
├── requirements.txt        # List of Python dependencies for pip
├── static/
│   └── css/
│       └── styles.css      # Custom CSS for styling, theming, and dark mode
└── templates/
    ├── create_post.html    # Page for creating a new post
    ├── index.html          # Homepage/Global feed
    ├── layout.html         # Base HTML template with navbar and structure
    ├── login.html          # User sign-in page
    └── register.html       # User sign-up page
```

### How to Run Locally

To run this project on your own machine, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [<your-repository-url>](https://github.com/samtong0425/simple-twitter-app.git)
    cd simple-twitter-app
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    flask run
    ```

5.  Open your web browser and navigate to the link provided by Flask.