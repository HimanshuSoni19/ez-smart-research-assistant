import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

#  Load local NLP pipelines
@st.cache_resource
def load_pipelines():
    summarizer = pipeline("summarization", model="google/flan-t5-small")
    qna = pipeline("question-answering", model="deepset/roberta-base-squad2")
    generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
    return summarizer, qna, generator

summarizer, qna, generator = load_pipelines()

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def summarize_text(text):
    input_text = text[:1000]  # Keep within model limit
    result = summarizer(input_text, max_length=150, min_length=30, do_sample=False)
    return result[0]['summary_text']

def answer_question(doc_text, question):
    input_text = doc_text[:1000]
    result = qna(question=question, context=input_text)
    answer = result['answer']
    start = result['start']
    end = result['end']
    snippet = input_text[start:end+1]
    return answer, snippet


def generate_questions(doc_text):
    prompt = (
        f"Read the following text and generate 3 clear, reasoning-based questions to test understanding:\n\n"
        f"{doc_text[:1000]}\n\n"
        f"Questions:"
    )
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text'].split('\n')


def evaluate_answer(doc_text, question, user_answer):
    return f"Thanks for your answer! Based on the document, here's a suggestion: Make sure to support your response using key terms like those in the document such as '{question.split()[0]}' or '{doc_text.split()[0]}'."

st.title("EZ Smart Research Assistant(Offline Mode)")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")
    with st.spinner("Reading and summarizing..."):
        doc_text = extract_text_from_pdf(uploaded_file)
        summary = summarize_text(doc_text)
    st.subheader("Auto Summary (≤150 words):")
    st.write(summary)

    mode = st.radio("Choose a Mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Ask a question based on the document:")
        if question:
            with st.spinner("Thinking..."):
                answer, snippet = answer_question(doc_text, question)
                st.markdown("**Answer:**")
                st.write(answer)
                st.markdown("**Supporting Snippet:**")
                st.code(snippet)


    elif mode == "Challenge Me":
        st.write("Generating logic-based questions...")
        questions = generate_questions(doc_text)
        for i, q in enumerate(questions):
            if q.strip() == "":
                continue
            st.markdown(f"**Q{i+1}:** {q}")
            user_ans = st.text_input(f"Your Answer {i+1}")
            if user_ans:
                with st.spinner("Evaluating..."):
                    feedback = evaluate_answer(doc_text, q, user_ans)
                st.markdown(f"**Feedback:** {feedback}")
