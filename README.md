# DataForge X

A powerful data analysis tool that uses your local AI model (Gemma 3 4B) to provide intelligent insights and visualizations.

## Tech Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Matplotlib
- **AI Model**: Gemma 3 4B
- **Model Serving**: LM Studio
- **GPU Acceleration**: CUDA (RTX 2050)
- **API Communication**: REST API (HTTP)

## Features

- AI-powered data analysis using Gemma 3 4B
- Automatic plot generation based on AI-suggested formats (bar / pie)
- Support for both bar charts and pie charts
- Local deployment with no external dependencies
- Developed by Alan Cyril Sunny

## Requirements

- Python 3.10 or higher
- LM Studio with Gemma 3 4B model
- CUDA-compatible GPU (RTX 2050 or better)

## Installation

1. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```
2. Install the required Python packages:
   ```bash
   pip install streamlit pandas matplotlib requests
   ```
3. Start LM Studio with the Gemma 3 4B model and keep it listening on `http://localhost:1234`.

## Quick Start

With LM Studio running, launch the app:
```bash
streamlit run insight_ai_clean.py
```

## Usage

1. Upload your CSV file using the file uploader
2. Ask questions about your data in natural language
3. The AI will analyze your data and provide insights
4. Automatic plots will be generated based on the insights

## Example Questions

- "What's the total sales by region?"
- "Which product has the highest sales?"
- "Show sales distribution by product"
- "What's the trend over time?"

## Note

This application uses your local Gemma 3 4B model through LM Studio for all AI processing, ensuring complete privacy and control over your data.

## Developer

Alan Cyril Sunny
