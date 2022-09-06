<h1 align="center">Welcome to Battleships-Franco-Vega-Mercado 👋</h1>
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

```sh
make install
```
Or, you can download the source and

```
   $ git clone git@github.com:Refactorahau/Battleships-Franco-Vega-Mercado.git
   $ cd Battleships-Franco-Vega-Mercado
   $ python setup.py install
```

Add sudo in the beginning if you met problem.

## Usage

```sh
make run
```

## Run tests

```sh
make test
```

## Author

👤 **Franco Vega Mercado**

* Github: [@francovm](https://github.com/francovm)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/franco-vega\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/franco-vega\/)

## Comments

The solution can be improved by adding complete testing coverage and adding continuous deployment. Due to time constraints, I created a simple battleship_test.py. A complete solution in a real production enviroment should be rigorously tested. 

# Original Instructions

Your challenge is to implement this simplified game of Battleships using text input and output.

The computer randomly chooses the location of two single-cell "ships" on a board of 8 by 8 cells.  The user then has 20 guesses to find the two ships.

The user enters a co-ordinate, for example `3,5`, and the computer locates the nearest ship to that co-ordinate and tells them they're "hot" if they're 1 to 2 cells away, "warm" if they're 3 to 4 cells away, or "cold" if they're further away.

As an example, `3,5` is three cells away from `2,7` because (3 - 2) + (7 - 5) = 3, so they'd be told they were "warm".

If the user correctly guesses a ship's location, they're told they've got a hit and that ship is removed from the board.  The game ends when both ships have been hit by the user, or the user has used up their 20 guesses.

Some things to note:
* Write your code in a style that you consider to be production quality. 
* We're more interested in your logical thinking, process and coding style. Show us what you know about writing great software.
* Feel free to use your language of choice. We prefer C#, Java, JavaScript, TypeScript, or Python.
* Please include guidance on how to install and execute your solution.
* Please create a merge request when you are done.  