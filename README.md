# Credit Card Fraud Detection System 🔒

A comprehensive fraud detection system built with machine learning and deployed using Streamlit. This application analyzes transaction patterns to identify potentially fraudulent activities in real-time.

## 🌟 Features

- **Real-time Fraud Detection**: Analyze transactions instantly
- **Interactive Web Interface**: User-friendly Streamlit application
- **Multiple Transaction Types**: Support for PAYMENT, TRANSFER, CASH_OUT, DEPOSIT
- **Risk Assessment**: Visual indicators for risk levels
- **Professional UI**: Modern design with color-coded alerts

## 🚀 Live Demo

Experience the fraud detection system in action through our interactive web interface!

## 📊 Dataset

This project uses a comprehensive dataset containing transaction records with the following features:
- Transaction type (PAYMENT, TRANSFER, CASH_OUT, DEPOSIT)
- Transaction amount
- Account balances (sender and receiver)
- Balance changes

*Note: Due to file size limitations, the dataset is not included in this repository. Please contact for access to the full dataset.*

## 🛠️ Technology Stack

- **Python 3.12+**
- **Streamlit** - Web application framework
- **Scikit-learn** - Machine learning algorithms
- **Pandas** - Data manipulation
- **Joblib** - Model serialization

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akriti-e/CreditCard-Fraud-Detection.git
   cd CreditCard-Fraud-Detection
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install streamlit scikit-learn pandas joblib
   ```

## 🔧 Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run fraud_detection.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Enter transaction details**:
   - Select transaction type
   - Enter transaction amount
   - Provide sender and receiver balance information

4. **Analyze the transaction** by clicking the "Analyze Transaction" button

5. **Review results**: The system will display whether the transaction is legitimate or potentially fraudulent

## 🎯 How It Works

1. **Data Input**: User enters transaction details through the web interface
2. **Feature Processing**: The system processes the input data
3. **Model Prediction**: A trained machine learning model analyzes the transaction
4. **Risk Assessment**: The system provides a risk level and recommendation
5. **Visual Feedback**: Color-coded alerts and metrics display the results

## 📈 Model Performance

The fraud detection model has been trained on comprehensive transaction data and provides:
- High accuracy in fraud detection
- Low false positive rates
- Real-time processing capabilities

## 🔐 Security Features

- **Risk Level Assessment**: Visual indicators for transaction risk
- **Confidence Metrics**: Shows model confidence in predictions
- **Action Recommendations**: Clear guidance on whether to approve or block transactions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👩‍💻 Author

**Akriti** - [GitHub Profile](https://github.com/akriti-e)

## 🙏 Acknowledgments

- Thanks to the open-source community for the amazing tools and libraries
- Special thanks to Streamlit for making web deployment simple and elegant

---

⭐ **Star this repository if you found it helpful!** ⭐
