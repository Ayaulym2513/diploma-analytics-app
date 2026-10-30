from fastapi import FastAPI, HTTPException
from backend.database import get_mysql_connection, logs_collection
from backend.etl_processor import process_system_logs
from datetime import datetime

app = FastAPI(
    title="AI-Driven Big Data Analytics & Reporting Platform",
    description="Дипломный проект: Мониторинг Big Data и автоматическая генерация отчетов",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "success", "message": "Backend system is running successfully!"}

@app.get("/test-mysql")
def test_mysql():
    try:
        connection = get_mysql_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION() as version;")
            result = cursor.fetchone()
        connection.close()
        return {"status": "connected", "mysql_version": result["version"]}
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.post("/api/logs")
def receive_bigdata_log(log_data: dict):
    """Сбор сырых логов (Big Data хранилище в MongoDB)"""
    inserted_id = logs_collection.insert_one(log_data).inserted_id
    return {"status": "saved", "mongo_id": str(inserted_id)}

@app.post("/api/analytics/process")
def analyze_metrics(metrics: list[dict]):
    """Запуск ETL-пайплайна и анализ метрик"""
    analysis_result = process_system_logs(metrics)
    return {"status": "success", "analysis": analysis_result}

@app.post("/api/reports/generate")
def generate_analytical_report(report_title: str, metrics: list[dict]):
    """
    Генерация готового аналитического отчета и сохранение в MySQL 
    (сокращает рутину аналитиков на 70-80%)
    """
    # 1. Обрабатываем данные через ETL и ИИ-анализ
    analysis = process_system_logs(metrics)
    
    # 2. Сохраняем готовый отчет в реляционную базу данных MySQL
    try:
        connection = get_mysql_connection()
        with connection.cursor() as cursor:
            # Создаем таблицу отчетов, если она еще не создана
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS analytical_reports (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total_records INT,
                    avg_cpu FLOAT,
                    avg_response_time FLOAT,
                    total_errors INT,
                    insights TEXT
                )
            """)
            
            # Вставляем сгенерированный отчет
            cursor.execute(
                """
                INSERT INTO analytical_reports 
                (title, total_records, avg_cpu, avg_response_time, total_errors, insights) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    report_title, 
                    analysis["total_records"], 
                    analysis["avg_cpu_usage"], 
                    analysis["avg_response_time"], 
                    analysis["total_errors"], 
                    analysis["ai_insights"]
                )
            )
            connection.commit()
        connection.close()
        
        return {
            "status": "success",
            "message": "Analytical report successfully generated and stored!",
            "report_details": {
                "title": report_title,
                "timestamp": str(datetime.now()),
                "metrics_summary": analysis
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
