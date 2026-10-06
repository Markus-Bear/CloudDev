# CloudDev

Python code from the Cloud Development module at SETU Carlow, written in JupyterLab. The repository moves from introductory exercises to a small web application built with **Flask**.

## Repository layout

```
CloudDev/
├── intro/          Introductory Python exercises from the early labs
├── flask/
│   └── xword/      Flask web application
└── README.md
```

## Getting started

1. Install Python 3 and clone the repository:

   ```bash
   git clone https://github.com/Markus-Bear/CloudDev.git
   cd CloudDev
   ```

2. Create and activate a virtual environment, then install Flask:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install flask
   ```

3. Run the Flask application:

   ```bash
   cd flask/xword
   flask run
   ```

   The app is then served at `http://127.0.0.1:5000`.

4. To work through the introductory exercises, install JupyterLab and open the `intro` folder:

   ```bash
   pip install jupyterlab
   jupyter lab intro
   ```

## Author

Mark Mukiiza, Software Development student at SETU Carlow. [LinkedIn](https://www.linkedin.com/in/mukiiza-mark)
