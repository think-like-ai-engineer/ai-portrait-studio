# AI Portrait Studio

An AI-powered portrait studio that removes backgrounds and applies creative transformations using a modular inference pipeline — built to demonstrate real-world AI product design.

Part of the **Think Like an AI Engineer** ecosystem.

---

## 🚀 Project Vision

AI Portrait Studio is not just an image tool.

It is a systems-first AI project designed to teach:

- How models become products
- How to structure AI inference pipelines
- How to separate UI from logic
- How to design modular, replaceable AI components

This project represents **Stage 1: Builder → Engineer** in the AI Engineer journey.

---

## 🧠 What This System Does

- Upload a human portrait
- Remove the background using an open-source segmentation model
- Optionally apply artistic style transformations
- Return a studio-style output image

---

## 🏗 System Architecture

```

User Upload
↓
Validation Layer
↓
Background Removal Module
↓
Style Transformation Module (Optional)
↓
Output Rendering

```

### Design Principles

- UI contains no business logic
- Pipeline orchestrates modules
- Each module does one thing
- Models are swappable
- Clean separation of concerns

---

## 📂 Project Structure

```

ai-portrait-studio/
│
├── app/                    # Streamlit UI layer
│   └── streamlit_app.py
│
├── src/                    # Core AI system logic
│   ├── pipeline.py
│   ├── background_removal.py
│   ├── style_transfer.py
│   └── utils.py
│
├── models/                 # Local or downloaded model files
├── data/                   # Sample inputs / outputs
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app/streamlit_app.py
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* rembg (U2Net-based background removal)
* Pillow
* Modular pipeline architecture

---

## 🎯 Learning Objectives

By building this project, you will understand:

* How to turn a model into a usable product
* Why inference architecture matters
* How modular design improves scalability
* How UX impacts perceived AI quality

---

## 📘 Related Book

This project accompanies the book:

**Think Like an AI Engineer**

It supports chapters in:

Part II — From Model to Product

---

## 🔭 Future Roadmap

* Improved segmentation models
* GPU acceleration support
* Batch processing
* Docker deployment
* Cloud hosting
* Model monitoring

---

## 📜 License

MIT License

