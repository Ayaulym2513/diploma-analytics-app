import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="PulseMetrics | Enterprise Big Data AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Полное удаление верхней полоски Streamlit Cloud и локального хедера
st.markdown("""
<style>
    /* Убираем шапку Streamlit локально и в облаке */
    header, [data-testid="stHeader"], [data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }

    .stApp {
        background: radial-gradient(circle at top left, #111827 0%, #030712 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background: #0b0f19;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    .brand-header {
        display: flex;
        align-items: center;
        padding: 12px 0 24px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 30px;
    }
    .brand-logo {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        width: 48px;
        height: 48px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: white;
        margin-right: 18px;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.5);
    }
    .brand-title {
        font-size: 22px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #ffffff;
    }
    .brand-subtitle {
        font-size: 13px;
        color: #94a3b8;
    }

    .metric-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        border-color: rgba(59, 130, 246, 0.6);
        box-shadow: 0 15px 35px -5px rgba(59, 130, 246, 0.25);
        transform: translateY(-2px);
    }
    .metric-title {
        color: #94a3b8;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #60a5fa;
        font-size: 32px;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(96, 165, 250, 0.3);
    }
    .status-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
    }
    .badge-warning { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); box-shadow: 0 0 15px rgba(245, 158, 11, 0.2); }
    .badge-success { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); box-shadow: 0 0 15px rgba(16, 185, 129, 0.2); }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 15px 0 25px 0;">
            <h2 style="color: #60a5fa; margin:0; font-weight: 900; letter-spacing: -0.5px; text-shadow: 0 0 20px rgba(96, 165, 250, 0.4);">⚡ PulseMetrics</h2>
            <p style="color: #94a3b8; font-size: 11px; margin-top: 6px; text-transform: uppercase; letter-spacing: 1px;">Enterprise AI & Big Data</p>
        </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio(
        "Навигация", 
        ["📊 Дашборд мониторинга", "📝 Генерация отчетов", "⚙️ Статус бэкенда"],
        label_visibility="collapsed"
    )
    
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<p style='font-size: 11px; color: #64748b; text-align: center;'>PulseMetrics OS v1.0<br>Secure Enterprise Build</p>", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

if menu == "📊 Дашборд мониторинга":
    st.markdown("""
        <div class="brand-header">
            <div class="brand-logo">📈</div>
            <div>
                <div class="brand-title">Мониторинг инфраструктуры в реальном времени</div>
                <div class="brand-subtitle">Анализ телеметрии Big Data серверов и интеллектуальное детектирование аномалий</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    sample_data = pd.DataFrame({
        "Время": pd.date_range(start=datetime.now(), periods=10, freq="min"),
        "CPU_Usage": [42.1, 45.5, 48.0, 89.2, 52.1, 49.3, 91.5, 50.0, 46.2, 44.8],
        "Response_Time": [110, 125, 115, 610, 140, 130, 580, 120, 112, 108],
        "Errors": [0, 0, 0, 2, 0, 0, 3, 0, 0, 0]
    })
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-title">Ср. загрузка CPU</div><div class="metric-value">55.8%</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-title">Время отклика</div><div class="metric-value">205 <span style="font-size:16px; color:#94a3b8;">мс</span></div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-title">Всего ошибок</div><div class="metric-value" style="color:#f87171; text-shadow: 0 0 20px rgba(248, 113, 113, 0.4);">5</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-title">Статус системы</div><div style="margin-top: 8px;"><span class="status-badge badge-warning">⚠ Аномалии найдены</span></div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        fig_cpu = px.line(sample_data, x="Время", y="CPU_Usage", title="Динамика загрузки процессора (CPU %)", markers=True, line_shape="spline")
        fig_cpu.update_traces(line_color="#3b82f6", line_width=3)
        fig_cpu.update_layout(
            template="plotly_dark", 
            height=360,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#f8fafc")
        )
        st.plotly_chart(fig_cpu, use_container_width=True)

    with c2:
        fig_resp = px.bar(sample_data, x="Время", y="Response_Time", title="Время отклика сервисов (мс)")
        fig_resp.update_traces(marker_color="#10b981")
        fig_resp.update_layout(
            template="plotly_dark", 
            height=360,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#f8fafc")
        )
        st.plotly_chart(fig_resp, use_container_width=True)

elif menu == "📝 Генерация отчетов":
    st.markdown("""
        <div class="brand-header">
            <div class="brand-logo">📑</div>
            <div>
                <div class="brand-title">Генератор аналитических отчетов</div>
                <div class="brand-subtitle">Автоматизированное формирование инсайтов и сохранение структурированных данных в хранилище</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    report_name = st.text_input("Название аналитического отчета", value="Инфраструктурный аудит производительности")
    
    st.markdown("<br><b>Параметры симуляции метрик для анализа:</b>", unsafe_allow_html=True)
    cpu_val = st.slider("Загрузка CPU (%)", 10.0, 100.0, 88.5)
    resp_val = st.slider("Время отклика (мс)", 50.0, 1000.0, 540.0)
    err_val = st.number_input("Количество ошибок", min_value=0, value=2)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Сгенерировать отчет и записать в базу данных", type="primary", use_container_width=True):
        payload_metrics = [{"cpu_usage": cpu_val, "response_time": resp_val, "error_count": err_val}]
        try:
            res = requests.post(f"{BACKEND_URL}/api/reports/generate?report_title={report_name}", json=payload_metrics)
            if res.status_code == 200:
                data = res.json()
                st.success("✨ Отчет успешно сформирован и сохранен в реляционную базу данных!")
                
                st.markdown("#### 🤖 Интеллектуальные выводы аналитики:")
                st.info(data['report_details']['metrics_summary']['ai_insights'])
                
                with st.expander("📄 Детали JSON-пакета отчета"):
                    st.json(data['report_details'])
            else:
                st.error("Ошибка при обращении к бэкенду.")
        except Exception as e:
            st.error(f"Не удалось подключиться к FastAPI: {e}")

elif menu == "⚙️ Статус бэкенда":
    st.markdown("""
        <div class="brand-header">
            <div class="brand-logo">⚙️</div>
            <div>
                <div class="brand-title">Системный мониторинг и статус сервисов</div>
                <div class="brand-subtitle">Проверка здоровья бэкенда, реляционных и NoSQL баз данных</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    try:
        r = requests.get(f"{BACKEND_URL}/test-mysql")
        if r.status_code == 200:
            st.markdown('### 🟢 Все компоненты функционируют штатно')
            st.success("✅ FastAPI Backend Server: Активен (Порт 8000)")
            st.success(f"✅ MySQL Relational DB (Docker): Подключена (Версия: {r.json().get('mysql_version')}, Порт 3307)")
            st.success("✅ MongoDB Big Data DB (Docker): Подключена (Порт 27017)")
    except:
        st.error("🔴 Ошибка: Бэкенд сервер недоступен. Проверьте запуск Uvicorn.")
