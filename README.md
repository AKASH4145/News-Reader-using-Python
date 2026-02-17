##  AI News Reader using Python

This project is a Python-based news reader that fetches the latest headlines from online news sources and converts them into readable or spoken output.  
It demonstrates API integration and data processing in Python.

---

##  Features

- Fetch latest news headlines  
- Filter news by category or keyword  
- Clean and parse news content  
- (Optional) Convert news text to speech  
- Simple CLI or basic UI  

---

##  Tech Stack

- Python
- News API
- Requests
- JSON

---

## Project Structure

```text
news-reader/
├── main.py              # App entry point
├── config.py            # API keys / configuration
├── fetch_news.py        # News API logic
├── reader.py            # News formatting / TTS logic
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup and Run

git clone https://github.com/<Akash4145>/News Reader.git >> 
cd news-reader >> 
python -m venv venv 
source venv/bin/activate   (Linux or  macOS) or 
venv\Scripts\activate      ( Windows ) >> 
pip install -r news_req.txt >>
API setup e = "your api key here" >> 
python main.py

---

## Limitations

- Free news APIs may have rate limits
- Headlines depend on API availability
- TTS quality depends on the selected engine

---

## Future Improvements

- Add GUI or web interface
- Add sentiment analysis on headlines
- Save articles for offline reading
- Text to Speech conversion

---

## Author

Akash GS | Mechanical Engineering student exploring AI, computer vision, and applied Python development