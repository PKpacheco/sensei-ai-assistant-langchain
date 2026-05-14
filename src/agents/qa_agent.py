def clean_response(response: str) -> str:
    """
    Cleans common LLM formatting issues before displaying the final response.
    """

    replacements = {
        "Dear [Customer's Name],": "Hello,",
        "Dear [User],": "Hello,",
        "Dear [Name],": "Hello,",
        "[Customer's Name]": "",
        "[User]": "",
        "[Name]": "",
    }

    cleaned = response

    for old, new in replacements.items():
        cleaned = cleaned.replace(old, new)

    return cleaned.strip()