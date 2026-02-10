from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # needed to use sessions

# Set your password
PASSWORD = "Baltimar2026"

# ================= LOGIN PAGE =================
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        entered_password = request.form.get("password")
        if entered_password == PASSWORD:
            session["logged_in"] = True  # user is authenticated
            return redirect(url_for("accueil"))
        else:
            error = "Mot de passe incorrect"
    return render_template("login.html", error=error)

# ================= ROUTE ACCUEIL =================
@app.route("/", methods=["GET", "POST"])
def accueil():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":
        if "logo1" in request.form:
            return redirect(url_for("baltimar"))
        elif "logo2" in request.form:
            return redirect(url_for("revey"))
    return render_template("accueil.html")

# ================= PAGE BALTIMAR =================
@app.route("/baltimar", methods=["GET", "POST"])
def baltimar():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    result = None
    zones = []
    Type_Audit = ""
    if request.method == "POST":
        Type_Audit = request.form.get("type_audit")
        if Type_Audit in ["Audit GMP", "Audit Housekeeping"]:
            zones = ["zone1", "zone2", "zone3"]
        elif Type_Audit == "Audit GWP":
            zones = ["GWP agence", "GWP usines"]

        if "retour" in request.form:
            return redirect(url_for("accueil"))

    return render_template("baltimar.html", Type_Audit=Type_Audit, zones=zones)

# ================= PAGE REVEY =================
@app.route("/revey", methods=["GET", "POST"])
def revey():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    result = None
    zones = []
    Type_Audit = ""
    Atelier = ""
    if request.method == "POST":
        Atelier = request.form.get("atelier")
        Type_Audit = request.form.get("type_audit")
        if Type_Audit in ["Audit GMP", "Audit Housekeeping"]:
            zones = ["zone1", "zone2", "zone3"]
        elif Type_Audit == "Audit GWP":
            zones = ["GWP agence", "GWP usines"]

        if "retour" in request.form:
            return redirect(url_for("accueil"))

    return render_template("revey.html", Type_Audit=Type_Audit, zones=zones, Atelier=Atelier)

# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
