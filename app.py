"""
Career Guidance System – Flask Backend
Deploy on Render (or any WSGI host).
"""

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# ── Career data (ported from main.py) ─────────────────────────────────────
CAREERS = [
    {
        "id": 1,
        "icon": "🏛️",
        "label": "Government",
        "name": "Civil Services (UPSC)",
        "clr": "#e07b00",
        "bgLight": "#fff7ed",
        "sub": "UPSC · IAS · IPS · IFS",
        "qualification": "Any Degree",
        "age": "21 – 32 years",
        "gender": "Both Male & Female",
        "eligibility": "Must be Indian citizen and graduate from a recognised university",
        "documents": [
            "Aadhar Card",
            "Degree Certificate",
            "Passport Size Photos",
            "Caste Certificate (if applicable)",
        ],
        "books": [
            "Indian Polity – M. Laxmikanth",
            "Indian Economy – Ramesh Singh",
            "Modern History",
            "Geography of India",
            "NCERT Books (6–12)",
        ],
        "notification": "UPSC Notification released every year in February",
    },
    {
        "id": 2,
        "icon": "🏦",
        "label": "Finance",
        "name": "Banking Jobs (IBPS, SBI)",
        "clr": "#0284c7",
        "bgLight": "#eff8ff",
        "sub": "IBPS PO · Clerk · SBI · RRB",
        "qualification": "Any Degree",
        "age": "20 – 30 years",
        "gender": "Both Male & Female",
        "eligibility": "Graduate from recognised university with basic computer knowledge",
        "documents": [
            "Aadhar Card",
            "Degree Certificate",
            "Photo & Signature",
            "Caste Certificate (if applicable)",
        ],
        "books": [
            "Quantitative Aptitude – R.S. Aggarwal",
            "Verbal & Non-Verbal Reasoning",
            "Objective English",
            "Banking Awareness",
        ],
        "notification": "IBPS Notifications released between June – August every year",
    },
    {
        "id": 3,
        "icon": "📋",
        "label": "Central Govt",
        "name": "SSC Jobs",
        "clr": "#7c3aed",
        "bgLight": "#f5f3ff",
        "sub": "CGL · CHSL · MTS · GD",
        "qualification": "12th / Degree",
        "age": "18 – 27 years",
        "gender": "Both Male & Female",
        "eligibility": "Must have completed 12th or degree depending on the post applied",
        "documents": [
            "Aadhar Card",
            "10th & 12th Certificates",
            "Passport Photos",
            "Caste Certificate (if applicable)",
        ],
        "books": [
            "Arithmetic – R.S. Aggarwal",
            "General English – S.P. Bakshi",
            "Lucent's GK",
            "Reasoning by Arihant",
        ],
        "notification": "SSC Notifications are released throughout the year on ssc.nic.in",
    },
    {
        "id": 4,
        "icon": "💻",
        "label": "Tech Industry",
        "name": "Software / IT Jobs",
        "clr": "#059669",
        "bgLight": "#ecfdf5",
        "sub": "Developer · Engineer · Analyst",
        "qualification": "B.Sc / B.Tech (CS / IT)",
        "age": "No strict age limit",
        "gender": "Both Male & Female",
        "eligibility": "Good programming skills and knowledge of data structures & algorithms",
        "documents": [
            "Updated Resume",
            "Degree Certificate",
            "Project Portfolio",
            "Government ID Proof",
        ],
        "books": [
            "Let Us C – Yashwant Kanetkar",
            "Data Structures – Narasimha Karumanchi",
            "Python Crash Course",
            "Introduction to Algorithms (CLRS)",
        ],
        "notification": "Job openings available year-round on LinkedIn, Naukri, and company career portals",
    },
]


# ── Routes ─────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Serve the main HTML page."""
    return render_template("index.html")


@app.route("/api/careers")
def get_careers():
    """Return all career records as JSON."""
    return jsonify(CAREERS)


@app.route("/api/careers/<int:career_id>")
def get_career(career_id):
    """Return a single career record by id."""
    career = next((c for c in CAREERS if c["id"] == career_id), None)
    if career is None:
        return jsonify({"error": "Career not found"}), 404
    return jsonify(career)


# ── Entry point ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # For local testing only – Render uses gunicorn
    app.run(debug=True)
