# Vanguard - AI-Powered Phishing Detection System

![Vanguard Logo](./assets/vanguard-logo.png)

## Overview
Vanguard is an AI-powered phishing detection system designed to identify and mitigate phishing attacks. It utilizes machine learning to analyze email content, URLs, and website data, offering real-time threat intelligence and scalable security solutions for organizations and individuals.

## Features
- **Phishing Email Detection**: Analyzes email content, sender reputation, and embedded URLs.
- **Malicious Website Detection**: Identifies fraudulent websites using advanced content and URL analysis.
- **Real-Time Threat Intelligence**: Leverages threat intelligence feeds and domain reputation databases.
- **Scalability**: Efficiently processes large volumes of emails and websites.
- **Seamless Integration**: Compatible with email security tools, SIEMs, and web security platforms.

## Installation
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vanguard.git
   cd phishing-detection-system/ 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the environment:
   - Create a `.env` file in the root directory and add your API keys and configurations:
     ```
     THREAT_INTEL_API_KEY=your_api_key
     EMAIL_API_KEY=your_email_api_key
     ```
4. Run the API:
   ```bash
   cd src/api
   uvicorn main:app --reload
   ```

## Usage
### API Endpoints
- **Detect Phishing in a Single Email**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/detect-phishing" \
  -H "Content-Type: application/json" \
  -d '{"content": "Dear user, please click this link: http://malicious-site.com"}'
  ```
- **Detect Phishing in a Batch of Emails**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/detect-phishing-batch" \
  -H "Content-Type: application/json" \
  -d '{"emails": ["Email 1 content", "Email 2 content"]}'
  ```
- **Health Check**:
  ```bash
  curl "http://127.0.0.1:8000/health"
  ```

### Training the Model
To train the phishing detection model:
```bash
python src/models/train.py
```

### Updating Threat Intelligence
To update the blacklist:
```bash
python src/threat_intelligence/blacklist_updater.py
```

## Documentation
For detailed technical documentation, refer to [TechnicalDocumentation.pdf](./docs/TechnicalDocumentation.pdf).

## Evaluation Metrics
- **Detection Accuracy**:
  - Precision: 0.94
  - Recall: 0.96
  - F1 Score: 0.95
  - AUC-ROC: 0.98
- **False Positive Rate**: 2%
- **False Negative Rate**: 1%

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

## Contact
For questions or feedback, please contact:
- **Runtime Terrors**: devayanee999@gmail.com
