# Twitter Tweet Collector 
Twitter Tweet Collector is a tool that allows you pull tweets posted in a given location, and save them on a firebase realtime 
database. This will be useful for research and predicting the behavior of people in any given location.

## Getting Started

To use this tool, you need twitter api credentials.
- Create a `config.json` file in the current directory in the format shown below and 
add your twitter credentials. File si 
```
{
  "c_key": "fkdkdkdkd",
  "c_sec": "dkdkkdkdkd",
  "a_token": "1111111111-ldkdkdkdkdk",
  "a_sec": "kdkdkdkd",
  "firebase_url": "https://<firebase_url>.firebaseio.com/"
}

```
- Create a firebase realtime database and add the firebase database url above
- Install dependencies in requirements.txt
- Run code and watch the log when tweet is saved to database

The `firebase_url` is the url to your firebase realtime database to store the data in.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
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

* Hat tip to anyone who's code was used
* Inspiration
* etc

