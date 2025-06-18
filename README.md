# DataForge X

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)
![Python](https://img.shields.io/badge/Language-Python%203.10+-blue)
![Gemma 3 4B](https://img.shields.io/badge/Model-Gemma%203%204B-purple)
![LM Studio](https://img.shields.io/badge/Serving-LM%20Studio-orange)
![CUDA RTX](https://img.shields.io/badge/GPU-RTX%202050%2B-green)
![MIT License](https://img.shields.io/badge/License-MIT-blue)

> **Developed by ALAN CYRIL SUNNY**  
> If you find this project helpful, please ⭐ [star the repository](https://github.com/yourusername/dataforge-x)!

---

## 📊 DataForge X

A powerful data analysis tool that uses your local AI model (Gemma 3 4B) to provide intelligent insights and visualizations.

- 🤖 AI-powered data analysis using Gemma 3 4B  
- 📈 Automatic plot generation (bar / pie) based on AI suggestions  
- 🥧 Supports both bar charts and pie charts  
- 🖥️ Local deployment with no external dependencies  
- ⚡ GPU-accelerated with CUDA (RTX 2050+)  
- 🔒 100% local processing for privacy and control  

---

## ✨ Features

- **AI Data Analysis**: Ask questions in natural language and get intelligent insights.
- **Automatic Visualization**: The AI suggests and generates bar or pie charts.
- **Streamlit UI**: Simple, modern, and interactive interface.
- **Local & Private**: All processing is done locally—your data never leaves your machine.
- **Fast GPU Inference**: Optimized for NVIDIA RTX GPUs via CUDA.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Processing**: [Pandas](https://pandas.pydata.org/)
- **Visualization**: [Matplotlib](https://matplotlib.org/)
- **AI Model**: Gemma 3 4B (via [LM Studio](https://lmstudio.ai/))
- **Model Serving**: LM Studio (REST API)
- **GPU Acceleration**: CUDA (RTX 2050+)
- **API Communication**: REST API (HTTP)

---

## 💻 Requirements

- Python 3.10 or higher
- LM Studio with Gemma 3 4B model
- CUDA-compatible GPU (RTX 2050 or better)

---

## 🚀 Installation

1. *(Optional)* Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```

2. Install the required Python packages:
   ```bash
   pip install streamlit pandas matplotlib requests
   ```

3. Start LM Studio with the Gemma 3 4B model and keep it listening on `http://localhost:1234`.

---

## ⚡ Quick Start

With LM Studio running, launch the app:
```bash
streamlit run insight_ai_clean.py
```

---

## 📝 Usage

1. **Upload your CSV file** using the file uploader.
2. **Ask questions** about your data in natural language.
3. **AI analyzes your data** and provides insights.
4. **Automatic plots** are generated based on the insights.

---

## 💡 Example Questions

- "What's the total sales by region?"
- "Which product has the highest sales?"
- "Show sales distribution by product"
- "What's the trend over time?"

---

## 🔒 Note

This application uses your local Gemma 3 4B model through LM Studio for all AI processing, ensuring complete privacy and control over your data.

---

## 👨‍💻 Developer

**Alan Cyril Sunny**

---

Feel free to fork, star ⭐, and contribute!
