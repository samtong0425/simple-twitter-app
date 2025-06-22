Of course! Based on the CS50 final project requirements and the detailed project plan you've provided, here is a complete `README.md` file ready for you to use. It incorporates all the necessary sections, explains the project's features and design choices, and details the file structure and how to run the application.

Just copy the text below and save it in a file named `README.md` in your project's main directory.

---

# Simple Twitter

#### Video Demo:  <https://youtu.be/your_video_id_here>
#### Description:

Simple Twitter is a dynamic web application developed as my final project for Harvard's CS50x. It is a streamlined, minimalist clone of Twitter, focusing on the core functionality that makes social media engaging: user authentication, post creation, and a real-time global feed. The application is built from the ground up using Python and the Flask web framework on the backend, with a SQLite database for data persistence. The frontend is crafted with HTML, custom CSS, and the Bootstrap 5 framework to ensure a responsive, modern, and intuitive user interface.

A key feature of this project is the custom, theme-aware design. The entire site supports both a light and a dark mode, with a seamless toggle that remembers the user's preference across sessions using `localStorage`. This was achieved by leveraging CSS custom properties (variables) and a small amount of JavaScript, demonstrating a commitment to a polished and user-centric design. The project serves as a comprehensive application of the concepts learned throughout CS50, from backend logic and database management with SQL to frontend development and user experience design.

---

### Features

The application is built around a Minimum Viable Product (MVP) model, with a clear roadmap for future enhancements.

#### Core Features (MVP)
*   **Full User Authentication:** Users can register for a new account with a unique username and a securely hashed password. Existing users can sign in and sign out of their sessions.
*   **Post Creation:** Authenticated users can create and publish short text posts (up to 150 characters).
*   **Global Feed:** The homepage displays all posts from all users in a single, reverse-chronological feed, making it a public timeline.
*   **Dynamic UI with Theme Switching:** The website features a clean, responsive design with a fully functional light/dark mode toggle. The user's choice is saved and automatically applied on their next visit.
*   **Flash Messaging:** Users receive clear, non-intrusive feedback for actions like successful logins, logouts, or post creation through Bootstrap alerts.

#### Potential Future Enhancements
*   **User Engagement:** Ability for users to "like" posts and view a like count.
*   **Post Management:** Allowing authors to edit or delete their own posts.
*   **User Profiles:** Dedicated pages to view all posts by a single user.
*   **Infinite Scroll:** Automatically loading older posts as the user scrolls down the feed.

### Project Structure

The project is organized into a standard Flask application structure to maintain a clean separation of concerns.

```
.
├── app.py                  # Main Flask application, routes, and logic
├── helpers.py              # Helper functions (e.g., login_required)
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

*   **`app.py`**: The heart of the application. It initializes the Flask app, configures the database, defines all the routes (e.g., `/`, `/login`, `/post`), and contains the logic for handling user requests, database queries, and rendering templates.
*   **`helpers.py`**: Contains helper functions, most notably the `login_required` decorator, which is used to protect routes that should only be accessible to authenticated users.
*   **`simple_twitter.db`**: The SQLite database file where all user and post data is stored. It is lightweight and ideal for a project of this scale.
*   **`requirements.txt`**: Specifies the necessary Python packages (Flask, Werkzeug for password hashing, etc.) required to run the application, allowing for easy setup in any environment.
*   **`static/css/styles.css`**: This file is central to the project's look and feel. It contains all custom styling, including the definitions for light and dark mode themes using CSS variables, and styles for the navbar, cards, buttons, and alerts to create a cohesive design.
*   **`templates/`**: This directory holds all the HTML files.
    *   **`layout.html`**: The master template that all other pages inherit from. It includes the HTML head, the navigation bar, the flash message container, and the JavaScript for the theme toggler.
    *   **`index.html`**: The homepage, which queries and displays the global post feed.
    *   **`login.html` & `register.html`**: The forms for user authentication.
    *   **`create_post.html`**: The form where users can write and submit a new post.

### Design Rationale

Several key decisions were made during the development of this project:

1.  **Framework Choice (Flask & SQLite):** Flask was chosen for its lightweight, "micro" nature, which provides flexibility and is an excellent tool for understanding web development fundamentals as taught in CS50. SQLite was selected as the database for its simplicity and serverless, file-based architecture, which is perfectly sufficient for this application's needs and avoids the overhead of setting up a larger database server.

2.  **Frontend Framework (Bootstrap 5):** Bootstrap was used to rapidly develop a responsive, mobile-first layout. Its grid system, pre-styled components (like cards, navbars, and buttons), and utility classes provided a solid foundation, allowing me to focus more on custom logic and styling.

3.  **Custom Theming and Dark Mode:** Instead of relying on Bootstrap's default dark mode, I chose to implement a custom theme using CSS variables (`--primary-color`, `--bg-color`, etc.). This approach provides complete control over the application's aesthetic. The `[data-bs-theme="dark"]` selector is used to swap the values of these variables, instantly changing the site's entire color palette. This demonstrates a more advanced and flexible approach to theming than simply linking to an alternate stylesheet.

### How to Run Locally

To run this project on your own machine, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows, use: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    flask run
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000` to see the application in action.