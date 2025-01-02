# Git Profile Manager

## Installation

To install the Git Profile Manger with Hombrew follow the steps:

```console
brew tap kujov/tap 
```

and

```console
brew install git-profile-manager              
```

verify with 

```console
gpm
```

and you should see your current git user and the availible actions for the tool.

## Usage

The Git Profile Manager includes the following actions:
- get: shows active profile
- set: switches profiles to predefined ones in the config
- edit: opens config file with ```vi```
- list: lists all the profiles in the config

Create a new profile:
either edit the config with ```gpm edit```

## Development

To build the package use:
```console
pip install -e .
```

Also install the requirements and create a venv.

## Bugs & Feature Requests

Create an Issue [on the issue page](https://github.com/kujov/git-profile-manager/issues/new).