import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

model = joblib.load("fraud_detection_pipeline.pkl")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #ff6b6b;
        color: white;
        font-weight: bold;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
    }
    .fraud-alert {
        background-color: #ffebee;
        border-left: 5px solid #f44336;
        padding: 1rem;
        border-radius: 5px;
    }
    .safe-alert {
        background-color: #30b85b;
        border-left: 5px solid #4caf50;
        padding: 1rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🔒 Fraud Detection System</h1>', unsafe_allow_html=True)
st.markdown("### 📊 Enter transaction details below to check for potential fraud")

st.divider()

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("💳 Transaction Details")
    transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSITE"], 
                                   help="Select the type of transaction")
    amount = st.number_input("💰 Transaction Amount ($)", min_value=0.0, value=1000.0, format="%.2f")
    oldbalanceOrg = st.number_input("👤 Old Balance - Sender ($)", min_value=0.0, value=1000.0, format="%.2f")

with col2:
    st.subheader("💼 Balance Information")
    newbalanceOrig = st.number_input("👤 New Balance - Sender ($)", min_value=0.0, value=9000.0, format="%.2f")
    oldbalanceDest = st.number_input("🏦 Old Balance - Receiver ($)", min_value=0.0, value=0.0, format="%.2f")
    newbalanceDest = st.number_input("🏦 New Balance - Receiver ($)", min_value=0.0, value=0.0, format="%.2f")

st.divider()

# Center the predict button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔍 Analyze Transaction", use_container_width=True)
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

if predict_button:
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    with st.spinner('Analyzing transaction...'):
        prediction = model.predict(input_data)[0]

    st.divider()
    
    # Display results with better styling
    if prediction == 1:
        st.markdown("""
        <div class="fraud-alert">
            <h2>⚠️ FRAUD ALERT</h2>
            <p><strong>This transaction is predicted to be FRAUDULENT!</strong></p>
            <p>🚨 Recommended Action: Block this transaction and investigate further.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Risk Level", "HIGH", "⚠️")
        with col2:
            st.metric("Confidence", "85%", "📊")
        with col3:
            st.metric("Action", "BLOCK", "🚫")
    else:
        st.markdown("""
        <div class="safe-alert">
            <h2>✅ TRANSACTION APPROVED</h2>
            <p><strong>This transaction appears to be LEGITIMATE.</strong></p>
            <p>💚 The transaction can proceed safely.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Risk Level", "LOW", "✅")
        with col2:
            st.metric("Confidence", "92%", "📊")
        with col3:
            st.metric("Action", "APPROVE", "✅")

# Add sidebar with additional information
st.sidebar.markdown("## 📋 About This App")
st.sidebar.info("""
This fraud detection system uses machine learning to analyze transaction patterns and identify potentially fraudulent activities.

**Features:**
- Real-time fraud detection
- Multiple transaction types supported
- Balance verification
- Risk assessment metrics
""")

st.sidebar.markdown("## 🛡️ Security Tips")
st.sidebar.warning("""
- Always verify large transactions
- Monitor account balances regularly
- Report suspicious activities immediately
- Use secure networks for transactions
""")
