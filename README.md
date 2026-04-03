# SmartCityAI – Backend

## Overview
SmartCityAI is an AI-powered system for monitoring urban conditions and supporting decision-making.

This backend provides:
- real-time city analytics
- anomaly detection
- risk scoring
- AI-generated recommendations
- forecasting

## Features
- Transport and environmental analysis
- Risk scoring system
- AI decision engine
- Forecasting module
- REST API

## API Endpoints

- `/api/overview` – city KPI
- `/api/districts` – district data
- `/api/ai-report` – AI insights
- `/api/trends` – historical data
- `/api/dashboard` – full dataset

## How to run

```bash
pip install -r requirements.txt
python3 mock_data_generator.py
python3 -m uvicorn app:app --reload