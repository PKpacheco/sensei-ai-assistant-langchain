def requires_human_review(user_email: str) -> bool:
    """
    It detects whether requests should be forwarded to a human agent
    """

    human_review_keywords = [
        "discount",
        "discounts",
        "loyalty",
        "loyalty program",
        "special pricing",
        "promotion",
        "promotional offer",
        "promo",
        "lifetime discount",
        "long-term customer",
        "special price",
    ]

    email_lower = user_email.lower()

    return any(keyword in email_lower for keyword in human_review_keywords)


def human_review_response() -> str:
    """
    Standard response for requests that require human review
    """

    return (
        "Hello,\n\n"
        "Thank you for reaching out. A human support agent will follow up to "
        "review your request and provide the most accurate information.\n\n"
        "Best regards,\n"
        "Sensei AI - Support Team"
    )