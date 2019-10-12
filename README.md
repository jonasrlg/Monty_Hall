# Monty_Hall
Monty Hall problem generalization.

Here we can have as many goats shown on the game as we wish. (goats_shown <= number of doors-2)

The user can choose the number of doors, goats and simulations for every configuration.
(n°_doors >= 2, 0<= n°_goats <= 'n°_doors - 2', n°_simulations >= 1)

There are two main modes for the user to choose from: 'sampling' and 'graphical'. The sampling mode is very basic, here we have N iteratrions of the game and we see how the two players perfom under a certain set of doors and goats. One of the players knows the best strategy for playing this game works and always changes his/her first choice. The other always stays with the first door that he/she has choosen.

We have different graphical modes: Ngoats and Interval. In Ngoats we have the number of doors fixed; therefore, we change the number of goats after N simulations. In Interval we have the number of goats fixed (1 goat or 'n°_doors-2' goats) and we change the number of doors, beggining on a and ending on b (parameters passed by the user).
