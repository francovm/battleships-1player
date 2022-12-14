<h1 align="center">Welcome to Battleships-Single Player 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Simplified game of Battleships using text input and output.


## Prerequisites

``` 
Python 3.9
```

## Install


Download the source

```
   $ git clone git@github.com:Refactorahau/Battleships-Franco-Vega-Mercado.git
   $ cd Battleships-Franco-Vega-Mercado
```
and
 
```
make install
```

or 

```sh
$ python setup.py install
```
Add sudo in the beginning if you met problem.

## Usage

```sh
$ make run
```
or

```
$ python ./src/main.py
```

## Run tests

```sh
$ make test
```
or 

```
$ python -m unittest discover -v -s . -p "*_test.py"
```

## Author

👤 **Franco Vega Mercado**

* Github: [@francovm](https://github.com/francovm)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/franco-vega\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/franco-vega\/)

## Comments

The solution can be improved by adding complete testing coverage and adding continuous deployment. Due to time constraints, I created a simple battleship_test.py. A complete solution in a real production enviroment should be rigorously tested. 

# Original Instructions

Simplified game of Battleships using text input and output.

The computer randomly chooses the location of two single-cell "ships" on a board of 8 by 8 cells.  The user then has 20 guesses to find the two ships.

The user enters a co-ordinate, for example `3,5`, and the computer locates the nearest ship to that co-ordinate and tells them they're "hot" if they're 1 to 2 cells away, "warm" if they're 3 to 4 cells away, or "cold" if they're further away.

As an example, `3,5` is three cells away from `2,7` because (3 - 2) + (7 - 5) = 3, so they'd be told they were "warm".

If the user correctly guesses a ship's location, they're told they've got a hit and that ship is removed from the board.  The game ends when both ships have been hit by the user, or the user has used up their 20 guesses.

