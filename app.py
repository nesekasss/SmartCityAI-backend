from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.data_loader import load_current_data, load_history_data
from services.analytics import analyze_city
from services.ai_module import generate_ai_report, generate_alerts, district_ranking
from services.formatter import build_overview, build_meta, build_summary

app = FastAPI(title="Smart City AI Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Smart City AI Backend is running",
        "status": "OK",
    }


@app.get("/api/overview")
def get_overview():
    current_data = load_current_data()
    analyzed = analyze_city(current_data)

    return {
        "meta": build_meta(),
        "overview": build_overview(analyzed),
        "summary": build_summary(analyzed),
    }


@app.get("/api/districts")
def get_districts():
    current_data = load_current_data()
    analyzed = analyze_city(current_data)

    return {
        "meta": build_meta(),
        "districts": analyzed,
    }


@app.get("/api/ai-report")
def get_ai_report():
    current_data = load_current_data()
    analyzed = analyze_city(current_data)

    return {
        "meta": build_meta(),
        "ai_report": generate_ai_report(analyzed),
    }


@app.get("/api/trends")
def get_trends():
    history = load_history_data()

    return {
        "meta": build_meta(),
        "history": history,
    }


@app.get("/api/alerts")
def get_alerts():
    current_data = load_current_data()
    analyzed = analyze_city(current_data)

    return {
        "meta": build_meta(),
        "alerts": generate_alerts(analyzed),
    }


@app.get("/api/ranking")
def get_ranking():
    current_data = load_current_data()
    analyzed = analyze_city(current_data)

    return {
        "meta": build_meta(),
        "ranking": district_ranking(analyzed),
    }


@app.get("/api/dashboard")
def get_dashboard():
    current_data = load_current_data()
    history = load_history_data()
    analyzed = analyze_city(current_data)

    return {
        "meta": build_meta(),
        "overview": build_overview(analyzed),
        "summary": build_summary(analyzed),
        "districts": analyzed,
        "ai_report": generate_ai_report(analyzed),
        "history": history,
        "alerts": generate_alerts(analyzed),
        "ranking": district_ranking(analyzed),
    }