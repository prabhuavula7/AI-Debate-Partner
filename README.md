# Rhea - an Intellectual AI Debate Partner

Rhea, from "rhetoric" is a transformer-based NLP project designed to generate logically structured arguments for and against real-world debate topics. The system was developed to explore the capabilities of large language models in reasoning, ethical analysis, and dialogue generation.

---

### 🧠 Model Architecture

The foundation of the model is a fine-tuned version of `facebook/bart-large`, trained on a custom-curated dataset that now includes **10,000 high-quality debate samples**. The initial dataset consisted of 2,500 rows, manually extracted and parsed from two reputable sources:

- **Perspectrum**
- Reddit's own **Change My View (CMV)**

These sources provided labeled, real-world argument pairs with diverse perspectives. I parsed and merged the raw formats into a normalized CSV schema tailored for sequence-to-sequence training. Each sample was structured with:
- A unique debate topic
- A concise **argument in favor**
- A logically sound **counterargument**

---

### 📈 Dataset Expansion & Curation

To scale beyond the seed data, I designed a system to generate additional high-quality samples using:
- Topic templating
- Domain categorization
- Reusable logical structures

This added 7,500 unique debate entries with diverse phrasing, structure, and argument logic to ensure generalization.

The expanded dataset spans **8 thematic domains**:

- Ethics & Morals  
- Science & Technology  
- Education  
- Environment  
- Politics  
- Society & Culture  
- Religion & Belief Systems  
- Public Health & Wellbeing  

Output lengths were statistically balanced (mean: ~26 words) for consistent behavior.

---

### ⚙️ Training Details

Model training was optimized for limited hardware (**Apple M2 Mac, 8GB RAM**) using Hugging Face Transformers. Key training optimizations:

- Truncated input/output to 128 tokens
- `beam_search=6` with `no_repeat_ngram_size=4`
- `batch_size=8`, `num_train_epochs=3`
- Early stopping and learning rate scheduling

---

### 🖥️ Interactive Gradio Interface

The final model was deployed with **Gradio**, offering an interactive UI to:

- Select or enter custom debate topics
- Generate structured arguments in real time
- Refresh topics across domains

---

### 🛠️ Highlights

This project demonstrates full-stack AI capabilities, including:

- ✅ Dataset creation & preprocessing  
- ✅ Argument mining & domain expansion  
- ✅ Transformer fine-tuning (BART)  
- ✅ Prompt engineering for logical generation  
- ✅ Gradio UI for public-facing deployment  

It showcases my ability to work across **data engineering**, **NLP research**, and **production UI prototyping** to build technically rigorous, user-centric systems.
