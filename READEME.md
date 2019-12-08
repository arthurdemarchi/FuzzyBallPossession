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


Git(optional) and python 3.

```
$ sudo dnf install python37
$ sudo dnf install git
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
           

Put desired file in the right path
```
$ mv path/to/file/file_name.csv ~/ballpossession/data
```

Run program
```
$ python3 -m ballpossession
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
