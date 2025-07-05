from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Sample data - you can modify this with your own information
portfolio_data = {
    'name': 'Geetika Panda',
    'title': 'Full Stack Developer',
    'email': 'geetikapanda4@gmail.com',
    'phone': '8917200716',
    'location': 'Berhampur,Odisha',
    'bio': 'Passionate developer with experience in web development, machine learning, and software engineering. I love creating innovative solutions and learning new technologies.',
    'skills': ['Python', 'JavaScript', 'Flask', 'HTML/CSS', 'SQL', 'Git'],
    'projects': [
        {
            'title': 'E-commerce Website',
            'description': 'A full-stack e-commerce platform built with Flask and JavaScript',
            'technologies': ['Flask', 'SQLite', 'JavaScript', 'Bootstrap'],
            "image_filename": "ecommerce.jpeg",
            'github': 'https://github.com/yourusername/ecommerce',
            'demo': '#',
            "category": "web"
            
        },
        {
            'title': 'Task Management App',
            'description': 'A responsive task management application with real-time updates',
            'technologies': ['React', 'Node.js', 'MongoDB', 'Socket.io'],
            "image_filename": "task management.jpg",
            'github': 'https://github.com/yourusername/taskmanager',
            'demo': '#',
            "category": "web"
        },
        {
            'title': 'Data Visualization Dashboard',
            'description': 'Interactive dashboard for analyzing sales data with charts and graphs',
            'technologies': ['Python', 'Plotly', 'Pandas', 'Flask'],
            "image_filename": "data visualization.jpg",
            'github': 'https://github.com/yourusername/dashboard',
            'demo': '#',
            "category": "web"
        },
        {
            'title': 'Weather App',
            'description': 'A mobile weather application with real-time updates and beautiful UI',
            'technologies': ['React Native', 'Weather API', 'Redux'],
            "image_filename": "weather app.jpg", # Ensure you have this image in your static/images folder
            'github': '#', # Replace with actual GitHub link
            'demo': '#', # Replace with actual demo link
            "category": "mobile"
        },
        {
            'title': 'ML Prediction Model',
            'description': 'Machine learning model for predicting market trends with 95% accuracy',
            'technologies': ['Python', 'Scikit-learn', 'Pandas', 'Jupyter'],
            "image_filename": "ml prediction1.jpg", # Ensure you have this image in your static/images folder
            'github': '#', # Replace with actual GitHub link
            'demo': '#', # Replace with actual demo link
            "category": "data"
        }
    ],
    'social_links': {
        'github': 'https://github.com/mydemonicarc',
        'linkedin': 'https://linkedin.com/in/geetika-panda-b82745346',
        'twitter': 'https://twitter.com/yourusername'
    }
}

@app.route('/')
def home():
    return render_template('home.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just flash a success message
        if name and email and message:
            flash(f'Thank you {name}! Your message has been sent successfully.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all required fields.', 'error')
    
    return render_template('contact.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)