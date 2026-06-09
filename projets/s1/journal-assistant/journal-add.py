#!/usr/bin/env python3
import datetime
import os

MOIS = {
    1: "janvier", 2: "février", 3: "mars", 4: "avril",
    5: "mai", 6: "juin", 7: "juillet", 8: "août",
    9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre",
}

JOURNAL_PATH = os.path.join(os.getcwd(), "journal", "journal.md")

QUESTIONS = [
    "1. Qu'as-tu fait aujourd'hui pendant cette session ?",
    "2. Quels wins / ce qui a marché ?",
    "3. Qu'est-ce qui t'a bloqué ou semblé difficile ?",
    "4. Qu'est-ce que tu as appris ?",
    "5. Quel est ton plan pour la prochaine session ?",
]

SECTIONS = [
    "Fait aujourd'hui",
    "Wins",
    "Blocages",
    "Appris",
    "Plan suivant",
]


def ask(prompt):
    print(f"\n{prompt}")
    return input("> ").strip()


def format_date():
    today = datetime.date.today()
    return f"{today.day} {MOIS[today.month]} {today.year}"


def build_entry(semaine, answers):
    date_str = format_date()
    lines = [f"## 📌 {semaine} — {date_str} — Session", ""]
    for section, answer in zip(SECTIONS, answers):
        lines.append(f"### {section}")
        lines.append(f"- {answer}")
        lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def prepend_to_journal(entry):
    existing = ""
    if os.path.exists(JOURNAL_PATH):
        with open(JOURNAL_PATH, "r", encoding="utf-8") as f:
            existing = f.read()
    os.makedirs(os.path.dirname(JOURNAL_PATH), exist_ok=True)
    with open(JOURNAL_PATH, "w", encoding="utf-8") as f:
        f.write(entry + existing)


def main():
    print("=== Journal de bord — nouvelle entrée ===")
    semaine = ask("Quelle semaine / session ? (ex: S1, S2…)") or "S?"
    answers = [ask(q) for q in QUESTIONS]
    entry = build_entry(semaine, answers)
    prepend_to_journal(entry)
    print(f"\n✓ Entrée ajoutée en haut de {JOURNAL_PATH}")


if __name__ == "__main__":
    main()
