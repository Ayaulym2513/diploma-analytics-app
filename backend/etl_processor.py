import pandas as pd
import numpy as np

def process_system_logs(data: list[dict]):
    """
    ETL-процесс: очистка данных, агрегация и поиск аномалий
    """
    if not data:
        return {"total_records": 0, "avg_cpu_usage": 0.0, "avg_response_time": 0.0, "total_errors": 0, "ai_insights": "No data provided."}

    df = pd.DataFrame(data)
    
    # 1. Очистка данных (удаление пустых строк)
    df = df.dropna()
    
    total_records = len(df)
    
    # 2. Расчет базовых метрик
    avg_cpu = float(df['cpu_usage'].mean()) if 'cpu_usage' in df.columns else 0.0
    avg_response = float(df['response_time'].mean()) if 'response_time' in df.columns else 0.0
    total_errors = int(df['error_count'].sum()) if 'error_count' in df.columns else 0
    
    # 3. Интеллектуальный анализ (выявление аномалий для ИИ-модуля)
    anomalies = []
    if 'cpu_usage' in df.columns:
        high_cpu = df[df['cpu_usage'] > 85.0]
        if len(high_cpu) > 0:
            anomalies.append(f"Выявлено {len(high_cpu)} критических пиков загрузки CPU (>85%).")
            
    if 'response_time' in df.columns:
        slow_requests = df[df['response_time'] > 500.0]
        if len(slow_requests) > 0:
            anomalies.append(f"Зафиксировано {len(slow_requests)} запросов с высоким временем отклика (>500мс).")

    if anomalies:
        insights = "Внимание: " + " ".join(anomalies) + " Рекомендуется оптимизация инфраструктуры."
    else:
        insights = "Параметры системы в норме. Критических аномалий и отклонений не обнаружено."

    return {
        "total_records": total_records,
        "avg_cpu_usage": round(avg_cpu, 2),
        "avg_response_time": round(avg_response, 2),
        "total_errors": total_errors,
        "ai_insights": insights
    }
