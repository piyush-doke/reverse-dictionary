# Reverse Dictionary

NOTE: Created in Python 2.

## Description

A Python search engine which, given any sentence, finds the most semantically equivalent word for it. It helps solve the tip of the tongue problem.

## Resources

Download and place this [pre-trained Word2Vec model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) in the same folder alongside revDict.py and dictionary.json.

## Repository Tree

```
./reverse-dictionary
├── dictionary.json
└── revDict.py                      # Script to run
```

## Usage

### How to Execute

```
python revDict.py                   # Run the script using python 2
```

### Inputs

- Sentence - Sentence whose semantically equivalent word is required.
- First Alphabet - First alphabet of the word expected as output (specifically done to restrict the search space and can be removed if computational resources are not a problem).

### Outputs

- Prints a list to the terminal (of length 20, but can be adjusted) of suggestions in decreasing order of similarity.

