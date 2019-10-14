# coding4kids/app.py --> web app starting point

"""
A portfolio web site to display a fictitious computer programming and STEM school for children. Built using Python Flask, JSON, the Bootstrap 4 CSS framework, FontAwesome 5 icons, Google Fonts, JavaScript, CSS, and HTML 5.  Includes a JSON data driven testimonials section, a JSON backed quiz system, and a number of Bootstrap 4 functionalities including an image carousel, and Courses tab UI, and much more.
Built by Ryan Hunter | GitHub handle SystemsVanguard | Web www.RyanHunter.org 
"""
# initial configurations
from flask import Flask, request, url_for, render_template , redirect 
import os, copy, random 
app = Flask(__name__)

# -----------------------------
# A JSON backed testimonials carousel. 

# -----------------------------
# routing 
@app.route('/')
def home():
    # return "Home Page - Coding4Kids"
    title = "Coding4Kids"
    subtitle = "We making coding fun for kids!"
    description = "Teaching children computer programming, web development, robotics, and STEM in a fun way"
    return render_template('home.html'  , title=title, subtitle=subtitle, description=description) 

@app.route('/courses/')
def courses():
    return render_template('courses.html') 

@app.route('/about/')
def about():
    return render_template('about.html') 

@app.route('/mission/')
def mission():
    return render_template('mission.html') 

@app.route('/volunteers/')
def volunteers():
    return render_template('volunteers.html') 

@app.route('/testimonials/')
def testimonials():
    return render_template('testimonials.html') 

@app.route('/contact/')
def contact():
    return render_template('contact.html') 
    
# see route for 'quizfun' far below.    


# ----------------------------- 
# JSON based Quiz of World City Capitals. #Format is 'question':[options].
# NOTE: The FIRST answer choice is the correct answer in the array.
original_questions = {
 'Nigeria':['Abuja','London','Rome','Luanda'],
 'Germany':['Berlin', 'Rome','Toronto','Durban'],
 'China':['Beijing','Amman','Nairobi','Singapore'],
 'Canada':['Ottawa','Madrid','Quebec City','Hamilton'],
 'India':['New Delhi','Cologne','Lima','Islamabad'],  
 'Spain':['Madrid','Bogotá','Milan','Cairo'], 
 'Russia':['Moscow','Canberra','Bucharest','Lisbon'],
 'Japan':['Tokyo','Ankara','Lagos','Hanoi'],  
 'Brazil':['Brasília','Nanjing','Baghdad','Belmopan'],
 'Thailand':['Bangkok','Tehran','Dongguan','Kingston']
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
 # shuffle the answer choices
 selected_keys = []
 i = 0
 while i < len(q):
  current_selection = random.choice(list(q.keys())) 
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys


@app.route('/quizfun/')
def quizfun():
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('quizfun.html', q = questions_shuffled, o = questions)


@app.route('/quiz_results/', methods=['POST'])
def quiz_results():
    total_questions = len(original_questions)
    your_score = your_percentage = 1 
    correct = 0
    for i in questions.keys():
        answered = request.form[i]
        if original_questions[i][0] == answered:
            correct = correct+1
            if correct >= 1:
              your_percentage = str(round(( correct / total_questions ) * 100 )) 
              your_score = 'Your Score: '+str(correct)+' of '+str(total_questions)+ ' or '+ your_percentage +'%. Let\'s Play Again'
            else: 
              #your_score = 'Let\'s Play The Quiz?'
              your_percentage = str(round(0))  
              your_score = 'Your Score: ' + your_percentage +'%. Let\'s Play Again'
    # return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'
    return render_template('quiz_results.html' , your_score=your_score)  

 

 
# ----------------------------- 


# start the web app --> default localhost:5000 
if __name__ == "__main__":
    app.run(debug=True)
