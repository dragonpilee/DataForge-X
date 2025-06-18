import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import re  # for cleaning numbering

# -------------------------------------------------------------
# Helper: call local LM-Studio model (Gemma 3-4B)
# -------------------------------------------------------------

def ask_phi4(prompt: str) -> str:
    """Send a prompt to the local model and return the reply text.

    If anything goes wrong we return an error string that can be shown in the UI.
    """
    try:
        res = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json={
                "model": "gemma-3-4b",
                "messages": [
                    {"role": "system", "content": "You are a data analyst AI. Analyze data and provide clear, concise answers."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.5,
                "max_tokens": 512,
            },
            timeout=30,
        )
        res.raise_for_status()
        data = res.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as exc:  # noqa: BLE001
        return f"❌ Error: {exc}"


# -------------------------------------------------------------
# Streamlit UI
# -------------------------------------------------------------

st.set_page_config(page_title="DataForge X", layout="wide")
st.title("📊 DataForge X\n(by Alan Cyril Sunny)")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if not uploaded_file:
    st.info("Upload a CSV file to get started.")
    st.stop()

# -----------------------------------------------------------------
# Load the CSV and basic preview
# -----------------------------------------------------------------

df = pd.read_csv(uploaded_file)
st.subheader("📋 Dataset Preview")
st.dataframe(df.head(20))

# -----------------------------------------------------------------
# Question → AI answer
# -----------------------------------------------------------------

st.subheader("🤖 Ask Questions")
query = st.text_input("", placeholder="Ask a question about the data (e.g., 'Which product sold the most?')")

if not query:
    st.stop()

# -------- 1. Textual answer --------------------------------------------------

with st.spinner("🔍 Generating answer ..."):
    prompt_text_answer = f"""You are a data analyst AI. Here's the data:\n\n{df.head(10).to_string(index=False)}\n\nQuestion: {query}\n\nProvide a direct answer only. Format:\n\n1. Answer only (no code, no data, no explanation)\n2. Key insights (brief bullet points)\n\nBe extremely concise. No code, no data, no thinking process.\n\nAnswer:"""
    answer = ask_phi4(prompt_text_answer)

# -------- Display the textual insight neatly -------------------
clean_line = lambda s: re.sub(r'^(?:\d+\.|[-•])\s*', '', s.strip())
insight_sections = [clean_line(s) for s in answer.split("\n") if s.strip()]

if insight_sections:
    st.markdown("### 💡 AI Insight")
    st.write(insight_sections[0])  # main answer
    if len(insight_sections) > 1:
        st.markdown("#### • Key Insights")
        for bullet in insight_sections[1:]:
            bullet = bullet.lstrip("-• ")  # remove any residual bullet chars
            st.write(f"- {bullet}")

# -----------------------------------------------------------------
# -------- 2. Plot suggestion & generation ------------------------
# -----------------------------------------------------------------

st.markdown("---")
st.markdown("### 📊 AI-Driven Insights")

with st.spinner("🔍 Analyzing data & preparing plot ..."):
    prompt_plot = f"""Data:\n{df.head(10).to_string(index=False)}\n\nQuestion: {query}\n\nSuggest a general plot format to answer this question:\nFormat: PlotType: [bar/pie], Category: [column], Value: [column], Description: [text]\n\nNote: Do not include specific values or regions in the description. Keep it general."""
    plot_reply = ask_phi4(prompt_plot)


# ---------------- Parse reply ------------------------------------

def parse_plot_reply(reply: str):
    default = ("bar", "Product", "TotalSales", "Total sales by category")
    parts = [p.strip() for p in reply.split(",") if p.strip()]
    if not parts:
        return default
    try:
        plot_type = parts[0].split(":")[1].strip() if ":" in parts[0] else default[0]
        category = parts[1].split(":")[1].strip() if len(parts) > 1 and ":" in parts[1] else default[1]
        value = parts[2].split(":")[1].strip() if len(parts) > 2 and ":" in parts[2] else default[2]
        desc = parts[3].split(":")[1].strip() if len(parts) > 3 and ":" in parts[3] else default[3]
        return plot_type, category, value, desc
    except Exception:  # noqa: BLE001
        return default

plot_type, category_col, value_col, description = parse_plot_reply(plot_reply)

# Validate columns
if category_col not in df.columns:
    category_col = df.columns[0]
if value_col not in df.columns:
    # choose first numeric column as fallback
    num_cols = df.select_dtypes("number").columns
    value_col = num_cols[0] if len(num_cols) else df.columns[1]

# ------------------- Plot ----------------------------------------

st.markdown(f"#### 📈 {description}")
fig, ax = plt.subplots()

try:
    if plot_type.lower() == "pie":
        grouped = df.groupby(category_col)[value_col].sum()
        ax.pie(grouped, labels=grouped.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
    else:
        df.plot(kind="bar", x=category_col, y=value_col, ax=ax)
        plt.xticks(rotation=45)
except Exception as exc:  # noqa: BLE001
    st.error(f"Plotting failed, showing fallback bar chart. Error: {exc}")
    df.plot(kind="bar", x=category_col, y=value_col, ax=ax)
    plt.xticks(rotation=45)

plt.tight_layout()
st.pyplot(fig)

# -----------------------------------------------------------------
# Footer
# -----------------------------------------------------------------

st.markdown("---")
st.markdown("Made with ❤️ by Alan Cyril Sunny")
