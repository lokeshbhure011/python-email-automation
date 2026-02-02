Python Email Automation 📧
------------------------------------------------------

A Python-based email automation tool that sends emails using Gmail SMTP with secure authentication.
The script supports user input, optional file attachments, and environment-based credentials.

🚀 Features
------------------------------------------------------

Send emails using Gmail SMTP

Secure login using Gmail App Password

User input for subject and message

Optional file attachment support

Error handling for failed email attempts

Clean and reusable function-based code

## 🛠 Tech Stack

| Technology / Platform | Purpose / Usage                              |
|------------------------|----------------------------------------------|
| Windows               | `python` — default Python interpreter         |
| Linux / macOS         | `python3` — explicitly use Python 3           |
| `smtplib` (built-in)  | Send emails via SMTP                         |
| `email.message` (built-in) | Construct email content and headers     |
| `python-dotenv`       | Load environment variables from `.env` file   |


📂 Project Structure
------------------------------------------------------
email_automation/

├── send_email.py

├── .env

├── .gitignore

├── requirements.txt

└── README.md

🔐 Environment Setup
------------------------------------------------------

Create a .env file in the project root:

SENDER_EMAIL= ```your_email@gmail.com```

APP_PASSWORD=```your_app_password```

RECEIVER_EMAIL=```receiver@gmail.com```


⚠️ Do not upload .env to GitHub.


📦 Installation
------------------------------------------------------

Create and activate virtual environment:

```
python -m venv venv
venv\Scripts\activate
```


Install dependencies:

```
pip install -r requirements.txt
```

▶️ How to Run
------------------------------------------------------

```python send_email.py ```

You will be prompted to:

Enter email subject

Enter message

Provide attachment path (or press Enter to skip)

⚠️ Common Issues
------------------------------------------------------

Authentication failed → Ensure Gmail App Password is used

Attachment error → Check file path

Email not received → Check spam folder

📌 Future Enhancements
------------------------------------------------------

HTML email templates

Multiple recipients support

Email scheduling

Logging instead of print statements

📄 License
------------------------------------------------------

This project is for learning and personal use.
