#main.py

from fastapi import FastAPI, HTTPException
from src.models.email_model import EmailPhishingDetector
from src.feature_extraction.email_features import EmailFeatureExtractor
from src.preprocessing.email_preprocessor import EmailPreprocessor
from src.utils.logger import logger
from .schemas import EmailRequest, PhishingResponse, BatchEmailRequest, BatchPhishingResponse

# Initialize FastAPI app
app = FastAPI()

# Initialize components
email_preprocessor = EmailPreprocessor()
feature_extractor = EmailFeatureExtractor()
phishing_detector = EmailPhishingDetector()

# API Endpoints
@app.post("/detect-phishing", response_model=PhishingResponse)
async def detect_phishing(email: EmailRequest):
    """Detect phishing in a single email."""
    try:
        # Preprocess email
        cleaned_email = email_preprocessor.clean_email(email.content)
        if not cleaned_email:
            raise HTTPException(status_code=400, detail="Failed to preprocess email.")

        # Extract features
        features = feature_extractor.extract_features([cleaned_email])
        if features is None:
            raise HTTPException(status_code=400, detail="Failed to extract features.")

        # Predict phishing
        prediction = phishing_detector.model.predict(features)[0]
        confidence = phishing_detector.model.predict_proba(features)[0][1]

        return {
            "is_phishing": bool(prediction),
            "confidence": float(confidence)
        }
    except Exception as e:
        logger.error(f"Error in detect-phishing: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detect-phishing-batch", response_model=BatchPhishingResponse)
async def detect_phishing_batch(emails: BatchEmailRequest):
    """Detect phishing in a batch of emails."""
    try:
        # Preprocess emails
        cleaned_emails = [email_preprocessor.clean_email(email) for email in emails.emails]
        if not cleaned_emails:
            raise HTTPException(status_code=400, detail="Failed to preprocess emails.")

        # Extract features
        features = feature_extractor.extract_features(cleaned_emails)
        if features is None:
            raise HTTPException(status_code=400, detail="Failed to extract features.")

        # Predict phishing
        predictions = phishing_detector.model.predict(features)
        confidences = phishing_detector.model.predict_proba(features)[:, 1]

        results = [
            {"is_phishing": bool(pred), "confidence": float(conf)}
            for pred, conf in zip(predictions, confidences)
        ]

        return {"results": results}
    except Exception as e:
        logger.error(f"Error in detect-phishing-batch: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

# Run the API
if __name__ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)