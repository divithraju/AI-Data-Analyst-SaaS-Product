from fastapi import FastAPI
from analyzer import analyze_csv
from llm import ask_llm

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Data Analyst SaaS running"}


@app.post("/analyze")
def analyze(question: str):
    explanation = ask_llm(f"Explain this analysis in simple terms: {question}")
    result = analyze_csv("data.csv", question)
    return {
       "question": question,
       "analysis": result,
       "ai_explanation": explanation
   }
