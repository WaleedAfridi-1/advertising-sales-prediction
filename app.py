import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Custom CSS for professional and modern styling
st.markdown("""
    <style>
    /* General Styling */
    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #1f2937;
    }
    .main {
        background-color: #ffffff;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
        max-width: 800px;
        margin: 2rem auto;
        animation: fadeIn 0.5s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .stTitle {
        color: #1e3a8a;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
    }
    .stMarkdown {
        color: #4b5563;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2.5rem;
        line-height: 1.6;
    }
    /* Input Section Styling */
    .input-container {
        background: #f8fafc;
        padding: 2rem;
        border-radius: 12px;
        border-left: 4px solid #3b82f6;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .input-header {
        color: #1e3a8a;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e5e7eb;
    }
    .stNumberInput > label {
        color: #374151;
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .stNumberInput input {
        border: 2px solid #d1d5db;
        border-radius: 8px;
        padding: 0.8rem;
        font-size: 1rem;
        background-color: #ffffff;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stNumberInput input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
        outline: none;
    }
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #1e40af 100%);
        color: white;
        font-weight: 600;
        padding: 0.9rem 2rem;
        border-radius: 8px;
        border: none;
        width: 100%;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        margin-top: 1.5rem;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    /* Result Styling */
    .prediction-card {
        background: linear-gradient(135deg, #dbeafe 0%, #eff6ff 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.15);
        border: 1px solid #bfdbfe;
        position: relative;
        overflow: hidden;
        animation: slideIn 0.7s ease-out;
    }
    .prediction-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #3b82f6, #1e40af);
    }
    .prediction-title {
        color: #1e40af;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }
    .prediction-value {
        color: #1e3a8a;
        font-size: 2.8rem;
        font-weight: 800;
        margin: 1rem 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .prediction-unit {
        color: #4b5563;
        font-size: 1.1rem;
        font-weight: 500;
    }
    .prediction-breakdown {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        text-align: left;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .breakdown-title {
        color: #374151;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #e5e7eb;
    }
    .breakdown-item {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid #f3f4f6;
    }
    .breakdown-item:last-child {
        border-bottom: none;
    }
    .breakdown-label {
        color: #6b7280;
        font-weight: 500;
    }
    .breakdown-value {
        color: #1f2937;
        font-weight: 600;
    }
    @keyframes slideIn {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    /* Footer Styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #6b7280;
        font-size: 0.9rem;
    }
    /* Responsive Design */
    @media (max-width: 768px) {
        .main {
            padding: 1.8rem;
            margin: 1.2rem;
        }
        .stTitle {
            font-size: 2rem;
        }
        .stMarkdown {
            font-size: 1rem;
        }
        .input-container {
            padding: 1.5rem;
        }
        .input-header {
            font-size: 1.2rem;
        }
        .prediction-value {
            font-size: 2.2rem;
        }
    }
    @media (max-width: 480px) {
        .main {
            padding: 1.2rem;
            margin: 0.8rem;
        }
        .stTitle {
            font-size: 1.8rem;
        }
        .input-container {
            padding: 1.2rem;
        }
        .prediction-card {
            padding: 1.5rem;
        }
        .prediction-value {
            font-size: 1.8rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("📈 Advertising Sales Prediction")
st.markdown("Enter your advertising budgets below to predict potential sales performance.")

# Input section
st.markdown('<div class="input-container">', unsafe_allow_html=True)
st.markdown('<div class="input-header">Ad Budget Inputs</div>', unsafe_allow_html=True)

# Create two columns for better layout on wider screens
col1, col2 = st.columns(2)

with col1:
    tv = st.number_input(
        "TV Advertising Budget (in thousands)",
        min_value=0.0,
        step=1.0,
        value=100.0,
        format="%.1f",
        help="Enter TV ad budget in thousands."
    )
    radio = st.number_input(
        "Radio Advertising Budget (in thousands)",
        min_value=0.0,
        step=1.0,
        value=25.0,
        format="%.1f",
        help="Enter Radio ad budget in thousands."
    )

with col2:
    newspaper = st.number_input(
        "Newspaper Advertising Budget (in thousands)",
        min_value=0.0,
        step=1.0,
        value=30.0,
        format="%.1f",
        help="Enter Newspaper ad budget in thousands."
    )

st.markdown('</div>', unsafe_allow_html=True)

if st.button("Predict Sales"):
    # Scale input
    features = scaler.transform([[tv, radio, newspaper]])
    
    # Prediction
    prediction = model.predict(features)[0]
    
    # Display result with enhanced styling
    st.markdown(f"""
        <div class="prediction-card">
            <div class="prediction-title">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
                Predicted Sales
            </div>
            <div class="prediction-value">${prediction:.2f}</div>
            <div class="prediction-unit">thousand units</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Display budget breakdown
    st.markdown(f"""
        <div class="prediction-breakdown">
            <div class="breakdown-title">Budget Breakdown</div>
            <div class="breakdown-item">
                <span class="breakdown-label">TV Advertising:</span>
                <span class="breakdown-value">${tv:.1f}k</span>
            </div>
            <div class="breakdown-item">
                <span class="breakdown-label">Radio Advertising:</span>
                <span class="breakdown-value">${radio:.1f}k</span>
            </div>
            <div class="breakdown-item">
                <span class="breakdown-label">Newspaper Advertising:</span>
                <span class="breakdown-value">${newspaper:.1f}k</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 Sales Prediction Analytics | All Rights Reserved</div>', unsafe_allow_html=True)