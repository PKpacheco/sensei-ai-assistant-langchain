from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def load_skill(skill_name: str) -> str:
    """
    Loads the correct skill instructions from the skills folder.
    """

    skill_path = BASE_DIR / "skills" / skill_name / "SKILL.md"

    if not skill_path.exists():
        raise FileNotFoundError(f"Skill file not found: {skill_path}")

    return skill_path.read_text(encoding="utf-8")