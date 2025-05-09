# 🌐 Website Summarizer

A Django-based web application that allows users to input a URL of a public website, extracts readable text from it, and generates a concise summary using a pre-trained NLP model from Hugging Face.

---

## 🚀 Features

- 🔗 Accepts public article URLs.
- 🧠 Extracts paragraph content using BeautifulSoup.
- ✂️ Summarizes text using the `facebook/bart-large-cnn` transformer.
- 📋 Displays both original and summarized content.
- ⬇️ Allows users to download the summarized output as a `.txt` file.

---

## 🛠️ Tech Stack

| Component       | Technology                  |
|----------------|----------------------------- |
| Backend         | Django                      |
| NLP Model       | Hugging Face Transformers   |
| Summarizer      | BART (`facebook/bart-large-cnn`) |
| Web Scraping    | BeautifulSoup4              |
| Frontend        | HTML + Bootstrap (optional) |
| Deployment Ready| Localhost / Render / Heroku |

---
#Query :
![image](https://github.com/user-attachments/assets/d85a1107-222c-46c2-a63e-f9ce8b0bb1f8)
#Summary Result :
![image](https://github.com/user-attachments/assets/3bca1fc7-8d02-4790-9b9b-3d018a6eaffa)
#Result in Dark Mode :
![image](https://github.com/user-attachments/assets/8825d131-7458-4094-94d4-8bd9fcd171f3)


## ⚙️ How to Run Locally
1. Clone the Repository

git clone https://github.com/your-username/website-summarizer.git
cd website-summarizer

2. Create and Activate Virtual Environment

Windows : python -m venv env

env\Scripts\activate

macOS/Linux : python3 -m venv env

source env/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Django Server

python manage.py runserver

5. Open in Browser

Go to: http://127.0.0.1:8000

##📝 Example Use Case

Input URL:

https://www.ndtv.com/india-news/operation-sindoor-what-is-anti-tank-guided-missile-india-used-to-destroy-pakistani-posts-across-loc-8368992

What Happens:

    Text is scraped and parsed from the webpage.

    Summarized using the BART model.

    Both original and summarized versions are displayed.

    Option to download the summary as a .txt file.

📦 Example requirements.txt

Django>=5.2

transformers>=4.41.2

torch>=2.3.0

beautifulsoup4>=4.12.3

requests>=2.31.0

📄 License

This project is licensed under the MIT License — feel free to use and modify it for personal or commercial purposes.

🙌 Credits

    Hugging Face — Pre-trained BART Model

    BeautifulSoup4 — Web Scraping

    Django — Backend Framework

    All contributors and testers 🙏



