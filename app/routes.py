from flask import render_template, request
import random

from app import app

@app.route('/')
def index():
    return render_template('rosc.html')

@app.route('/play', methods=['POST'])
def play():
    choices = ['rock', 'paper', 'scissors']
    player_choice = request.form.get('choice')
    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)

    return render_template('rosc.html', player_choice=player_choice, computer_choice=computer_choice, result=result)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'scissors' and computer_choice == 'paper') or
        (player_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    elif (
        (computer_choice == 'rock' and player_choice == 'scissors') or
        (computer_choice == 'scissors' and player_choice == 'paper') or
        (computer_choice == 'paper' and player_choice == 'rock')
    ):
        return "You lose!"
    else:
        return "Invalid choices. Please try again."
