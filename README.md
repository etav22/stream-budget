## About The Project

This project is a basic dashboard for viewing financial transactions. After mint was shut-down, I needed a way to view all my transactions in one place and figured I could use my programming skills to make it happen 😊

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

To run the project locally, you will need to have the following installed on your machine:

- [just](https://github.com/casey/just)
- [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
- [docker](https://docs.docker.com/get-docker/)

Additionally, you will need a `transactions.csv` file in a `data` folder which is git ignored. This file should contain all your transactions. You can export this file from your bank's website. In the future, I would like to use a financial API to get this data instead of a CSV file (see [Roadmap](#roadmap)).

### Installation

To install the project, run the following commands:

```sh
just install
```

This will install all the dependencies and the `pre-commit` hooks.

<!-- USAGE EXAMPLES -->
## Usage

To run the project, you have two options:

1. Run the project with poetry:

```sh
just run
```

2. Run the project with docker:

```sh
just docker
```

<!-- ROADMAP -->
## Roadmap

- [ ] Clean up filters
- [ ] Add monthly spending chart
- [ ] Add monthly income chart
- [ ] Modularize code within `stream_budget` directory
- [ ] Use financial API over CSV files
- [ ] Create some sort of time-series prediction model to predict future spending
- [ ] Add database to store categorized transactions
