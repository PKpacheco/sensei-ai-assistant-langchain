import json
from pathlib import Path

from src.chains import generate_smart_response
from src.agents.triage_agent import classify_email


BASE_DIR = Path(__file__).resolve().parent.parent
TEST_CASES_PATH = BASE_DIR / "evals" / "test_cases.json"


def contains_any(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)


def contains_forbidden(text: str, forbidden_terms: list[str]) -> list[str]:
    text_lower = text.lower()
    found = []

    for term in forbidden_terms:
        if term.lower() in text_lower:
            found.append(term)

    return found


def run_evals():
    with open(TEST_CASES_PATH, "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    total = len(test_cases)
    passed = 0

    print("\nRunning Sensei AI Assistant evals...\n")

    for test in test_cases:
        name = test["name"]
        user_input = test["input"]
        expected_category = test["expected_category"]
        must_include_any = test.get("must_include_any", [])
        must_not_include = test.get("must_not_include", [])

        actual_category = classify_email(user_input)
        response = generate_smart_response(user_input)

        category_ok = actual_category == expected_category
        includes_ok = contains_any(response, must_include_any)
        forbidden_found = contains_forbidden(response, must_not_include)
        forbidden_ok = len(forbidden_found) == 0

        test_passed = category_ok and includes_ok and forbidden_ok

        if test_passed:
            passed += 1
            status = "PASS"
        else:
            status = "FAIL"

        print(f"Test: {name}")
        print(f"Status: {status}")
        print(f"Expected category: {expected_category}")
        print(f"Actual category: {actual_category}")

        if not includes_ok:
            print(f"Missing expected keywords. Expected one of: {must_include_any}")

        if forbidden_found:
            print(f"Forbidden terms found: {forbidden_found}")

        print("Generated response:")
        print(response)
        print("-" * 80)

    print(f"\nEval result: {passed}/{total} passed\n")


if __name__ == "__main__":
    run_evals()