% win conditions

win(brd, plyr) :- hor(brd, plyr).
win(brd, plyr) :- ver(brd, plyr).
win(brd, plyr) :- diag(brd, plyr).

hor(brd, plyr) :- brd = [plyr,plyr,plyr,_,_,_,_,_,_].
hor(brd, plyr) :- brd = [_,_,_,plyr,plyr,plyr,_,_,_].
hor(brd, plyr) :- brd = [_,_,_,_,_,_,plyr,plyr,plyr].

ver(brd, plyr) :- brd = [plyr,_,_,plyr,_,_,plyr,_,_].
ver(brd, plyr) :- brd = [_,plyr,_,_,plyr,_,_,plyr,_].
ver(brd, plyr) :- brd = [_,_,plyr,_,_,plyr,_,_,plyr].

diag(brd, plyr) :- brd = [plyr,_,_,_,plyr,_,_,_,plyr].
diag(brd, plyr) :- brd = [_,_,plyr,_,plyr,_,plyr,_,_].

other(x,o).
other(o,x).

% game initialization

game(brd, plyr) :- 
  win(brd, plyr),
  !,
  write([plyr, plyr, wins]).
game(brd, plyr) :- 
  other(plyr,otherplyr),
  move(brd,plyr,newbrd),
  !,
  print(newbrd),
  game(newbrd,otherplyr).

% move procdure

move([-,B,C,D,E,F,G,H,I], plyr, [plyr,B,C,D,E,F,G,H,I]).
move([A,-,C,D,E,F,G,H,I], plyr, [A,plyr,C,D,E,F,G,H,I]).
move([A,B,-,D,E,F,G,H,I], plyr, [A,B,plyr,D,E,F,G,H,I]).
move([A,B,C,-,E,F,G,H,I], plyr, [A,B,C,plyr,E,F,G,H,I]).
move([A,B,C,D,-,F,G,H,I], plyr, [A,B,C,D,plyr,F,G,H,I]).
move([A,B,C,D,E,-,G,H,I], plyr, [A,B,C,D,E,plyr,G,H,I]).
move([A,B,C,D,E,F,-,H,I], plyr, [A,B,C,D,E,F,plyr,H,I]).
move([A,B,C,D,E,F,G,-,I], plyr, [A,B,C,D,E,F,G,plyr,I]).
move([A,B,C,D,E,F,G,H,-], plyr, [A,B,C,D,E,F,G,H,plyr]).

print([A,B,C,D,E,F,G,H,I]) :- 
  write([A,B,C]), nl,
  write([D,E,F]), nl,
  write([G,H,I]), nl,
  nl.

x_can_win(brd) :- move(brd, x, newbrd), win(newbrd, x).

% respond: computers reponse

respond(brd,newbrd) :- 
  move(brd, o, newbrd),
  win(newbrd, o),
  !.
respond(brd,newbrd) :-
  move(brd, o, newbrd), 
  not(x_can_win(newbrd)).
respond(brd,newbrd) :-
  move(brd, o, newbrd).
respond(brd,newbrd) :-
  not(member(-,brd)),
  !, 
  write('Tie!'), nl,
  newbrd = brd.

% player turn

xmove([-,B,C,D,E,F,G,H,I], 1, [x,B,C,D,E,F,G,H,I]).
xmove([A,-,C,D,E,F,G,H,I], 2, [A,x,C,D,E,F,G,H,I]).
xmove([A,B,-,D,E,F,G,H,I], 3, [A,B,x,D,E,F,G,H,I]).
xmove([A,B,C,-,E,F,G,H,I], 4, [A,B,C,x,E,F,G,H,I]).
xmove([A,B,C,D,-,F,G,H,I], 5, [A,B,C,D,x,F,G,H,I]).
xmove([A,B,C,D,E,-,G,H,I], 6, [A,B,C,D,E,x,G,H,I]).
xmove([A,B,C,D,E,F,-,H,I], 7, [A,B,C,D,E,F,x,H,I]).
xmove([A,B,C,D,E,F,G,-,I], 8, [A,B,C,D,E,F,G,x,I]).
xmove([A,B,C,D,E,F,G,H,-], 9, [A,B,C,D,E,F,G,H,x]).
xmove(brd, _, brd) :- write('Invalid move.'), nl.

% game start

play :- howto, playon([-,-,-,-,-,-,-,-,-]).


% instructions on how to play the game

howto :-
  write('You play X.'),
  nl,
  write('Enter Integer where you want to place X: '),
  nl,
  print([1,2,3,4,5,6,7,8,9]).

% recursive procedure to play the game

playon(brd) :- win(brd, x), write('Player wins the game!').
playon(brd) :- win(brd, o), write('Computer wins the game!').
playon(brd) :- read(N),
  xmove(brd, N, newbrd), 
  print(newbrd),
  respond(newbrd, newnewbrd), 
  print(newnewbrd),
  playon(newnewbrd).