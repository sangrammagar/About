from flask import Flask, render_template_string, url_for

app = Flask(__name__)

home_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sangram Magar - Portfolio</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        header { background: linear-gradient(135deg, #007bff, #6610f2); color: white; padding: 60px 20px; text-align: center; }
        header img { width: 150px; border-radius: 50%; border: 4px solid #fff; }
        section { padding: 60px 20px; }
        .project-card img { height: 200px; object-fit: cover; }
        footer { background: #222; color: #ddd; text-align: center; padding: 20px; }
        .timeline { border-left: 3px solid #007bff; padding-left: 20px; margin-top: 20px; }
        .timeline-item { margin-bottom: 20px; }
    </style>
</head>
<body>

    <!-- Hero Section -->
    <header>
        <img src="{{ url_for('static', filename='images/profile.jpg') }}" alt="Profile">
        <h1 class="mt-3">Sangram Magar</h1>
        <p>AI Engineer | Machine Learning Engineer |Data Scientist | Computer Vision Engineer | Generative AI Engineer | Data Analyst </p>
        <a href="#contact" class="btn btn-light btn-lg mt-3">Hire Me</a>
    </header>

    <!-- About -->
    <section id="about" class="container">
        <h2 class="mb-4">About Me</h2>
        <p>I have a strong background in Artificial Intelligence and Machine Learning with practical experience in Computer Vision, Deep Learning, and Time Series Forecasting. My academic journey and projects reflect a passion for applying AI to solve real-world challenges, including real-time object detection, financial forecasting, and renewable energy optimization. Skilled in Python, TensorFlow, Sklearn, and OpenCV, I enjoy exploring new technologies, building innovative solutions, and continuously learning to expand my knowledge. 
</p>
    </section>

    <!-- Education -->
    <section id="education" class="bg-light">
        <div class="container">
            <h2 class="mb-4">Education</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <h5>M.Tech in Artificial Intelligence</h5>
                    <p>Dr B.R. Ambedkar National Institute of Technology, Jalandhar (2023–2025)</p>
                </div>
                <div class="timeline-item">
                    <h5>B.Tech in Mechanical Engineering</h5>
                    <p>SMSMPITR, AKLUJ (PAHSU, Solapur)  (2020–2023)</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects -->
    <section id="projects" class="container">
        <h2 class="mb-4">Projects</h2>
        <div class="row">
            <div class="col-md-4">
                <div class="card project-card shadow-sm">
                    <img src="{{ url_for('static', filename='images/project1.jpg') }}" class="card-img-top" alt="Project 1">
                    <div class="card-body">
                        <h5 class="card-title">Real-Time Obstacle Detection</h5>
                        <p>I developed a real-time obstacle detection system designed for applications in autonomous navigation and robotics. The project involved collecting and annotating a custom dataset using Roboflow, exporting it in YOLO-compatible format, and training lightweight YOLOv8 models for efficient performance. The system achieved an accuracy of ~92% mAP@0.5, while maintaining responsiveness suitable for real-world deployment. This project provided hands-on experience in computer vision model training, fine-tuning, and evaluation for practical applications. </p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card project-card shadow-sm">
                    <img src="{{ url_for('static', filename='images/project2.jpg') }}" class="card-img-top" alt="Project 2">
                    <div class="card-body">
                        <h5 class="card-title">Tesla Stock Price Prediction</h5>
                        <p>In this project, I built a time-series forecasting model using Long Short-Term Memory (LSTM) networks to predict Tesla Inc. stock prices. I collected 720 days of hourly data using the yfinance API and processed it with Pandas and NumPy for model training. The dataset was normalized, transformed into sequences, and trained using TensorFlow/Keras with suitable loss functions and optimizers. The model’s performance was evaluated using MAE, RMSE, R², and MAPE, producing accurate predictions with strong alignment between actual and predicted price trends.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card project-card shadow-sm">
                    <img src="{{ url_for('static', filename='images/project3.jpg') }}" class="card-img-top" alt="Project 3">
                    <div class="card-body">
                        <h5 class="card-title">Thermal Performance prediction model for an Solar Air Heater</h5>
                        <p>This research project focused on predicting the thermal performance of an impinging jet solar air heater using Artificial Neural Networks (ANN). Experimental data was preprocessed with outlier removal and feature scaling to ensure reliability, and the ANN model was trained on parameters such as Reynolds number and geometric ratios. The ANN significantly outperformed traditional methods such as KNN and Decision Tree, demonstrating higher prediction accuracy. This work showcased the potential of AI in optimizing renewable energy systems and was presented at the SIESD-2025 Conference. </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills -->
    <section id="skills" class="bg-light">
        <div class="container">
            <h2 class="mb-4">Technical Skills</h2>
            <ul>
                <li>Python, NumPy, Pandas, Sklearn, TensorFlow, OpenCV,Huggingface,NLTK</li>
                <li>Deep Learning, YOLO, Transformers, Generative AI</li>
                <li>Data Visualization (Matplotlib, Seaborn)</li>
                <li>Database: MySQL</li>
                <li>Tools: Colab, Jupyter, Spyder,GitHub, VS Code</li>
            </ul>
        </div>
    </section>

    <!-- Certifications -->
    <section id="certifications" class="container">
        <h2 class="mb-4">Certifications</h2>
        <ul>
            <li>Python for Everybody — University of Michigan (Coursera)</li>
            <li>Advanced Learning Algorithms — Stanford University (Coursera)</li>
<li>International Conference on Smart Innovations, Engineering Systems & Design—Quantum University, Rorkee</li>
        </ul>
    </section>

    <!-- Contact -->
    <section id="contact" class="bg-light">
        <div class="container text-center">
            <h2 class="mb-4">Contact Me</h2>
            <p>📞 8806629761</p>
            <p>📧 <a href="mailto:sangrammagar812@gmail.com">sangrammagar812@gmail.com</a></p>
            <p>🔗 <a href="https://www.linkedin.com/in/sangram2751" target="_blank">https://www.linkedin.com/in/sangram2751</a></p>
            <p>💻 <a href="https://github.com/sangrammagar" target="_blank">https://github.com/sangrammagar</a></p>
            <form class="mt-4" style="max-width:500px;margin:auto;">
                <input class="form-control mb-2" type="text" placeholder="Your Name" required>
                <input class="form-control mb-2" type="email" placeholder="Your Email" required>
                <textarea class="form-control mb-2" rows="3" placeholder="Your Message"></textarea>
                <button class="btn btn-primary w-100">Send Message</button>
            </form>
        </div>
    </section>

    <footer>
        <p>© 2025 Sangram Magar. All rights reserved.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(home_page)

if __name__ == "__main__":
    app.run(debug=True)
