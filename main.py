import streamlit as st
index = 0

class team:
    points = 0
    name: str
    bet: int


def give_round():
    rounds = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
    return rounds[index]


def increment_round():
    global index
    index = index+1


def make_bet(team, x):
    team.bet = x

def show_points(team1, team2, team3):
    print(team1.name, 'has ', team1.points)
    print(team2.name, 'has ', team2.points)
    print(team3.name, 'has ', team3.points)


def update_points(team, x):
    board = False

    if give_round() == team.bet:
        board = True

    if board:
        if x == give_round():
            team.points = team.points + (10 * team.bet)
        else:
            team.points = team.points - (10 * team.bet)
    else:
        extra = team.bet - x
        if x == 0:
            team.points = team.points + (4 * team.bet)
        elif x > 0:
            team.points = team.points - (4 * team.bet)
        else:
            team.points = team.points + ((4 * team.bet) - extra)

t1 = team()
t2 = team()
t3 = team()

"""
# Welcome to 🔙 alley 🌉
"""
t1.name = input('Enter team one name:')
t2.name = input('Enter team two name:')
t3.name = input('Enter team three name:')

if t1 and t2 and t3:
    print('Welcome to the game: ', t1.name, ', ', t2.name, ', and ', t3.name, '!')
    input()

while True:
    print('It is now round: ' , give_round(), ' please distribute ', give_round(), ' cards to everyone!')
    input()
    t1.bet = input (' team 1 how many bets? ')
    t2.bet = input(' team 2 how many bets? ')
    t3.bet = input (' team 3 how many bets? ')

    print ('Begin play!')
    t1_made = int (input('team 1 how many hands did you make?'))
    t2_made = int (input('team 2 how many hands did you make?'))
    t3_made = int (input('team 3 how many hands did you make?'))
    make_bet(t1, t1_made)
    make_bet(t2, t2_made)
    make_bet(t3, t3_made)

    update_points(t1, t1_made)
    update_points(t2, t2_made)
    update_points(t3, t3_made)
    show_points(t1,t2,t3)

    increment_round()







