from multiprocessing import Pool
from src.preprocessing.email_preprocessor import EmailPreprocessor

def process_email(email: str) -> dict:
    """Process a single email."""
    preprocessor = EmailPreprocessor()
    cleaned_email = preprocessor.clean_email(email)
    return {"email": email, "cleaned": cleaned_email}

def process_emails_in_parallel(emails: list) -> list:
    """Process emails in parallel using multiprocessing."""
    with Pool() as pool:
        results = pool.map(process_email, emails)
    return results