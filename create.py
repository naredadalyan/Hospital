import requests
import random

BASE_URL = "http://127.0.0.1:8000"

def generate_patients(n):
    for _ in range(n):
        patient = {
            "name": f"Пациент {_}",
            "birth_year": random.randint(1950, 2010),
            "social_status": random.choice(["работающий", "учащийся", "пенсионер"])
        }
        response = requests.post(f"{BASE_URL}/patients", json=patient)
        print(response.json())

def generate_doctors(n):
    for _ in range(n):
        doctor = {
            "name": f"Врач {_}",
            "specialization": random.choice(["терапевт", "хирург", "кардиолог"]),
            "experience": random.randint(1, 40)
        }
        response = requests.post(f"{BASE_URL}/doctors", json=doctor)
        print(response.json())

def generate_treatments(n, num_patients, num_doctors):
    for _ in range(n):
        treatment = {
            "start_date": "2025-01-01",
            "end_date": "2025-01-15",
            "diagnosis": "Грипп",
            "status": random.choice(["средней тяжести", "тяжелое"]),
            "patient_id": random.randint(1, num_patients),
            "doctor_id": random.randint(1, num_doctors)
        }
        response = requests.post(f"{BASE_URL}/treatments", json=treatment)
        print(response.json())

generate_patients(10)
generate_doctors(5)
generate_treatments(20, num_patients=10, num_doctors=5)
