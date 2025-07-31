# HTML Parser Web App

This is a simple web application for parsing and displaying HTML content. The app is built with Python using Flask, and provides a basic web interface for users to interact with HTML parsing functionality.

## Features

- Web interface for submitting a URL to view HTML content
- Simple, clean UI with custom CSS styling
- Easy to run locally

## Project Structure

```
html-parser/
│
├── app.py                # Main application file (Flask app)
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   └── css/
│       └── style.css     # Custom CSS styles
```

## Getting Started

### Prerequisites

- Python 3.x
- (Optional) Virtual environment tool (e.g., `venv`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:erinmyoung/html-parser.git
   cd html-parser
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install flask
   ```

### Running the App

1. **Start the Flask server:**
   ```bash
   python app.py
   ```
2. **Open your browser and go to:**
   [http://localhost:5000](http://localhost:5000)
3. **Type in a URL and see displayed details**

## Customization

- Edit `templates/index.html` to change the web page layout.
- Edit `static/css/style.css` to update the styling.
- Modify `app.py` to add new routes or logic.

## License

This project is provided for educational purposes. Feel free to modify and use it as needed.
