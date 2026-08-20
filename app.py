from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Danish Editing Studio</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;scroll-behavior:smooth}
body{font-family:Arial,sans-serif;background:#070707;color:#fff}
nav{position:fixed;top:0;width:100%;z-index:10;padding:16px 7%;display:flex;justify-content:space-between;
align-items:center;background:rgba(7,7,7,.88);backdrop-filter:blur(15px);border-bottom:1px solid #222}
.logo{font-size:22px;font-weight:800;letter-spacing:2px}
nav a{color:#aaa;text-decoration:none;margin-left:18px;font-size:14px}
nav a:hover{color:#fff}
.hero{min-height:100vh;padding:130px 7% 70px;display:flex;align-items:center;justify-content:center;text-align:center;
background:radial-gradient(circle at top,#242424,#070707 55%)}
.hero h1{font-size:clamp(42px,10vw,82px);line-height:1.05}
.hero h1 span{color:#888}
.hero p{color:#aaa;margin:18px auto 28px;max-width:600px;line-height:1.7}
.btn{display:inline-block;background:#fff;color:#000;padding:14px 24px;border-radius:30px;text-decoration:none;font-weight:bold}
section{padding:85px 7%}
.title{text-align:center;font-size:36px;margin-bottom:40px}
.title span{color:#777}
.services{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;max-width:900px;margin:auto}
.service{background:#111;border:1px solid #242424;border-radius:18px;padding:28px;transition:.3s}
.service:hover{transform:translateY(-5px);border-color:#555}
.icon{font-size:32px;margin-bottom:15px}
.service h3{margin-bottom:10px}.service p{color:#888;line-height:1.6}
.price{margin-top:15px;color:#ddd;font-weight:bold}
.order{max-width:650px;margin:auto;background:#101010;border:1px solid #242424;border-radius:20px;padding:25px}
input,select,textarea{width:100%;padding:15px;margin-bottom:14px;border:1px solid #292929;border-radius:10px;
background:#080808;color:#fff;outline:none}
textarea{height:130px;resize:none}
button{width:100%;padding:15px;border:0;border-radius:10px;background:#fff;color:#000;font-weight:bold;font-size:15px}
.note{text-align:center;color:#666;font-size:12px;margin-top:12px;line-height:1.5}
footer{text-align:center;border-top:1px solid #222;padding:28px;color:#666}
@media(max-width:650px){
nav{padding:14px 5%}nav a{font-size:11px;margin-left:7px}
section{padding:70px 5%}.services{grid-template-columns:1fr}
}
</style>
</head>
<body>

<nav>
<div class="logo">DANISH. EDITS</div>
<div>
<a href="#home">Home</a>
<a href="#services">Services</a>
<a href="#order">Order</a>
</div>
</nav>

<section class="hero" id="home">
<div>
<p>WELCOME TO DANISH EDITING STUDIO</p>
<h1>Make Your <span>Visuals</span> Better.</h1>
<p>Professional photo editing, video editing, cinematic color grading and Instagram reels editing.</p>
<a class="btn" href="#order">ORDER AN EDIT ✦</a>
</div>
</section>

<section id="services">
<h2 class="title">Editing <span>Services</span></h2>
<div class="services">

<div class="service">
<div class="icon">🎬</div>
<h3>Video Editing</h3>
<p>Cinematic cuts, transitions, effects and polished storytelling.</p>
<div class="price">999 ₹</div>
</div>

<div class="service">
<div class="icon">🖼️</div>
<h3>Photo Editing</h3>
<p>Professional retouching, lighting, background and Instagram-ready edits.</p>
<div class="price">99 ₹</div>
</div>

<div class="service">
<div class="icon">🎨</div>
<h3>Color Grading</h3>
<p>Cinematic color correction and premium mood-based grading.</p>
<div class="price">149 ₹</div>
</div>

<div class="service">
<div class="icon">📱</div>
<h3>Instagram Reels</h3>
<p>Short-form edits designed for reels, status and social media.</p>
<div class="price">249 ₹</div>
</div>

</div>
</section>

<section id="order">
<h2 class="title">Order <span>Your Edit</span></h2>
<div class="order">

<form action="https://formsubmit.co/danisheram416@gmail.com" method="POST">
<input type="hidden" name="_subject" value="New Editing Order - Danish Edits">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_template" value="table">

<input name="name" type="text" placeholder="Your Name" required>
<input name="email" type="email" placeholder="Your Email" required>

<select name="service" required>
<option value="">Select Editing Service</option>
<option>Video Editing</option>
<option>Photo Editing</option>
<option>Cinematic Color Grading</option>
<option>Instagram Reels Editing</option>
</select>

<textarea name="details" placeholder="Tell me about your project..." required></textarea>

<button type="submit">SEND EDITING REQUEST 🚀</button>
</form>

<p class="note">After submitting, your request will be sent to the email connected in app.py.</p>
</div>
</section>

<footer>© 2026 Danish Edits • Creator & Editor</footer>

</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
