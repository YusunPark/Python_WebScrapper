from flask import Flask, render_template, request, redirect


app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():   
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs= db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    
    return render_template(
        "report.html", 
        resultNumber=len(jobs), 
        searchingBy=word,
        jobs=jobs
    )


app.run(host="0.0.0.0")

# http://localhost:5000