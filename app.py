from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Using a list of dicts so we can support id, completed status, etc.
tasks = []
_next_id = 1

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    global _next_id
    title = request.form.get("task", "").strip()
    if title:
        tasks.append({"id": _next_id, "title": title, "done": False})
        _next_id += 1
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("home"))

@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
            break
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
