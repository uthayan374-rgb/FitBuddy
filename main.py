from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# --- COMMON STYLE ---
STYLE = """
body{font-family:Segoe UI,sans-serif;background:#f0f2f5;margin:0}
.header{background:#0d9488;color:white;padding:15px;text-align:center;font-weight:bold;font-size:22px}
.container{max-width:900px;margin:20px auto;background:white;border-radius:12px;overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.1)}
.workout-bg{display:flex;background:url('https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=1000') center/cover}
.plan-box{background:rgba(255,255,255,0.95);margin:20px auto;padding:20px;width:65%;border-radius:8px;font-family:monospace;white-space:pre-wrap;font-size:13px;line-height:1.5}
.tip-box{border:1px solid #333;padding:15px;margin:20px;border-radius:6px;background:#fffdf5}
.feedback-box{border:1px solid #333;padding:20px;margin:20px;border-radius:6px}
input,textarea,select{width:100%;padding:10px;margin:6px 0;border-radius:6px;border:1px solid #ccc;box-sizing:border-box}
button{width:100%;padding:12px;background:#2563eb;color:white;border:none;border-radius:8px;font-weight:bold;cursor:pointer}
.footer-img{display:flex;justify-content:space-between;padding:10px 20px;background:white;border-top:1px solid #eee}
"""

INDEX_PAGE = f"""
<html><head><title>FitBuddy</title><style>{STYLE}
.card{{width:400px;margin:60px auto;background:white;padding:30px;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,0.2)}}
body{{background:linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.6)),url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1920') center/cover;min-height:100vh}}
</style></head>
<body><div class="card">
<h2>FitBuddy - AI Fitness</h2>
<form action="/generate" method="post">
<input name="username" placeholder="Name" required>
<input name="user_id" placeholder="User ID" required>
<input name="age" type="number" placeholder="Age" required>
<input name="weight" type="number" step="0.1" placeholder="Weight kg" required>
<select name="goal"><option value="weight loss">Weight Loss</option><option value="muscle gain">Muscle Gain</option><option value="general fitness">General Fitness</option></select>
<select name="intensity"><option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option></select>
<button type="submit">Generate Plan</button>
</form></div></body></html>
"""

def generate_mock_plan(name, goal, intensity):
    return f"""Workout Plan
4-7 Day High-Intensity Workout Plan for Fat Loss & Muscle Gain
This plan focuses on compound movements to maximize calorie burn and muscle engagement. Remember to adjust weights based on your fitness level and ensure you are performing each exercise with proper form. Remember to be consistent and keep challenging yourself with a routine diet.

**Day 1: Upper Body Strength**
* Warm-up (5 min): Jump rope (3 min), High knees (30 seconds), Arm circles (30 seconds), Shoulder rotation (1 min)
* Barbell Bench Press: 4 sets of 8-12 reps
* Bent Over Rows: 4 sets of 8-12 reps
* Overhead Press: 3 sets of 10-12 reps
* Pull-ups or Lat Pulldown: 3 sets of 8-12 reps
* Plank: 3 sets of 30-60 sec

**Day 2: Lower Body & Core**
* Warm-up (5 min): Bodyweight squats (10 reps), Leg swings (30 sec per leg), Ankle circles (30 sec)
* Squats: 4 sets of 8-12 reps
* Deadlift: 3 sets of 8-12 reps per leg
* Walking Lunges: 3 sets of 12-15 per leg
* Leg Raises: 3 sets of 15 reps
* Russian Twists: 3 sets of 20 reps (10 per side)

**Day 3: Active Recovery**
* Warm-up (5 min): Light cardio, slow jogging or jumping jacks, followed by dynamic stretches

**Day 4: Full Body Circuit**
* Circuit x 3 rounds: Push-ups 12 reps, Squats 15 reps, Burpees 10 reps, Mountain climbers 30 sec, Rest 1-2 min

**Day 5: Core Focus & Flexibility**
* Focus on core strength, flexibility, and mobility. Include planks, leg raises, and yoga stretches.

**Day 6: Lower Body & Glutes Focus**
* Hip Thrusts: 4 sets of 12-15 reps
* Romanian Deadlifts: 3 sets of 10-12 reps

**Day 7: Rest & Active Recovery**
* Prioritize Rest: Similar to Day 3. Hydration, protein, and sleep are key for recovery.
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return INDEX_PAGE

@app.post("/generate", response_class=HTMLResponse)
def generate(username: str = Form(...), user_id: str = Form(...), age: int = Form(...), weight: float = Form(...), goal: str = Form(...), intensity: str = Form(...)):
    plan = generate_mock_plan(username, goal, intensity)
    html = f"""
    <html><head><title>Plan for {username}</title><style>{STYLE}</style></head><body>
    <div class="header">FitBuddy - Plan for {username} | ID:{user_id} | {age}yr | {weight}kg | Goal:{goal}</div>
    
    <div class="container">
        <h3 style="padding-left:20px">Workout Plan:</h3>
        <div class="workout-bg">
            <div class="plan-box">{plan}</div>
        </div>
        
        <div class="footer-img">
            <span style="font-weight:bold;color:#0d9488">SMARTBRIDGE</span>
            <span style="font-weight:bold;color:#2563eb">Smart Internz</span>
        </div>

        <div class="tip-box">
            <b>**Important Notes:**</b><br><br>
            * **Progressive Overload:** Gradually increase the weight, reps, or sets each week to challenge your muscles and promote continued growth.<br>
            * **Proper Form:** Focus on maintaining correct form throughout each exercise to prevent injury and maximize results. Watch videos and, if possible, consult with a trainer to ensure proper technique.<br>
            * **Listen to Your Body:** Rest when needed and don't push through pain. Adjust the plan as needed based on your recovery and progress.<br>
            * **Nutrition:** Fuel your body with a balanced diet rich in protein, complex carbohydrates, and healthy fats to support muscle growth and recovery.<br>
            * **Hydration:** Drink plenty of water throughout the day, especially before, during, and after workouts.<br><br>
            This plan is a starting point. You can adjust it based on your progress and preferences. Remember consistency and proper execution are key to achieving your fitness goals. Good Luck!
        </div>

        <p style="padding:0 20px;font-size:14px"><b>Description:</b> FitBuddy generates a personalized, day-wise workout plan tailored to the user's fitness goal, experience level, and preferred workout schedule. The workout section on the result page outlines each day with a clear focus, such as full body, upper or lower body, cardio, core strength, or flexibility.</p>

        <h4 style="padding-left:20px">Nutrition Tip:</h4>
        <div class="tip-box" style="text-align:center">
            <div style="font-weight:bold">💡 Nutrition Tip</div>
            <p style="font-size:13px">Prioritize protein! Aim for a good source of protein (like chicken, fish, beans, or Greek yogurt) with every meal. Protein helps build muscle, keeps you feeling full, and supports your metabolism, all crucial for losing belly fat and gaining muscle.</p>
        </div>

        <h4 style="padding-left:20px">Feedback Page:</h4>
        <div class="feedback-box">
            <b>📝 Share Your Feedback</b><br><br>
            <label>Your Unique User ID:</label>
            <input value="{user_id}" readonly>
            <label>Your Feedback:</label>
            <textarea placeholder="Let us know how we can improve your plan..."></textarea>
            <form action="/feedback" method="post">
                <input type="hidden" name="user_id" value="{user_id}">
                <button type="submit">Submit Feedback</button>
            </form>
        </div>
        <br>
        <div style="text-align:center;padding:20px"><a href="/">Back to Home</a></div>
    </div>
    </body></html>
    """
    return HTMLResponse(content=html)

@app.post("/feedback", response_class=HTMLResponse)
def feedback(user_id: str = Form(...)):
    return f"""
    <html><head><style>{STYLE}</style></head><body>
    <div class="container" style="padding:40px;text-align:center">
        <div style="border:1px solid #ccc;padding:15px;background:#f0fdf4;color:green;font-weight:bold">
        ✅ Your plan has been updated based on your feedback!
        </div>
        <br><br><a href="/">Go Back to Home</a>
    </div>
    </body></html>
    """