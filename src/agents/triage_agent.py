def classify_email(user_email: str) -> str:
    """
    Classifies the incoming email as technical or non-technical.
    """

    technical_keywords = [
        "api",
        "endpoint",
        "token",
        "authentication",
        "authorization",
        "database",
        "server",
        "server logs",
        "logs",
        "error code",
        "status code",
        "integration",
        "webhook",
        "json",
        "ssl",
        "timeout",
        "payload",
        "http",
        "401",
        "403",
        "404",
        "500",
    ]

    email_lower = user_email.lower()

    if any(keyword in email_lower for keyword in technical_keywords):
        return "technical_support"

    return "non_technical_support"