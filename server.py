from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'Berries_and_cream'

# answer_int = random.randint(1, 2)

@app.route('/')
def index():
    if 'answer_int' not in session:
        session['answer_int'] = random.randint(1, 100)
    else:
        pass
    return render_template('home_page.html', answer_int = session["answer_int"])

@app.route('/guess_int', methods=['POST'])
def user_guess ():
    session['number_guessed'] = int(request.form['number_guessed'])
    answer_right = False
    if 'num_of_guess' not in session:
        session['num_of_guess'] = 5
        return redirect('/guess')
    else:
        if session['number_guessed'] == session["answer_int"]:
            answer_right = True
            return redirect ('/game_over')
        elif session['num_of_guess'] <= 0 :
            return redirect('game_over')    
        else:
            session['num_of_guess'] = session['num_of_guess'] - 1
            return redirect('/guess')


@app.route('/guess')
def guess_page():
    return render_template('guess.html', number_guessed = session["number_guessed"], answer_int = session['answer_int'], num_of_guess =session['num_of_guess']) 

@app.route('/game_over_reset', methods=['POST'])
def end_of_game ():
    session.clear()
    
    return redirect('/')

@app.route('/game_over')
def game_over():
    return render_template('game_over.html', answer_int= session['answer_int'])


if __name__ == "__main__":
    app.run(debug=True)