from flask import Flask, render_template_string

app = Flask(__name__)

contact_form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f7f7f7;
            padding: 40px;
        }
        .container {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input, textarea {
            width: 100%;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background: #007BFF;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            width: 100%;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Contact Me</h2>
        <form action="https://formspree.io/f/mgvkjdbr" method="POST">
            <label>Your Name</label>
            <input type="text" name="name" required>
            
            <label>Your Email</label>
            <input type="email" name="_replyto" required>
            
            <label>Message</label>
            <textarea name="message" rows="5" required></textarea>
            
            <button type="submit">Send Message</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def contact():
    return render_template_string(contact_form_html)

if __name__ == '__main__':
    app.run(debug=True)