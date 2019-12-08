# Fuzzy Ball Possession for Simulated Robot Soccer 2D

As the Titles specifies is a fuzzy logic application that, based on a game situation, will classifie which player have ball possession in a simualted
robot soccer game, data will be retrieved from Robocup.

## Getting Started

```
$ cd ~
$ git clone https://github.com/arthurdemarchi/FuzzyEPCs.git
$ python3 -m ballpossession
```

### Prerequisites


Git(optional) and python 3, Python Libs (pandas)

```
$ sudo dnf install python37
$ sudo dnf install git
$ pip3 install --user pandas
```



### Installing

Clone repository

```
$ cd ~
$ git clone https://github.com/arthurdemarchi/FuzzyEPCs.git
```

Prepare desired file to analise:
    File must be in CSV format
    File must have the header:
    * "cycle,team_name,player_num,ball_x,ball_y,ball_vx,ball_vy,player_x,player_y,player_vx,player_vy,playmode"
    data must be relative to header

Put desired file in the right path
```
$ mv path/to/file/file_name.csv ~/ballpossession/data
```

Run program
```
$ python3 -m ballpossession
```

## Running the tests

There are no atuomated tests yet.


## Authors

* **Arthur Demarchi** - *Initial work* - [arthurdemarchi](https://github.com/arthurdemarchi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Robocup for archiving logs
* Thanks to zenoyang for the 2DLogMining Tool