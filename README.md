# Reverse Dictionary

NOTE: Created in Python 2.

## Objective

A Python search engine which, given any sentence, finds the most semantically equivalent word for it. It helps solve the tip of the tongue problem.

## About the Repository

```
./reverse-dictionary
├── dictionary.json
└── revDict.py
```

## Resources

Download and place this [pre-trained Word2Vec model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) in the same folder alongside revDict.py and dictionary.json.

## Instructions to Run

```
python revDict.py                   # Run the script using python 2
```

## Inputs

- Sentence - Sentence whose semantically equivalent word is required.
- First Alphabet - First alphabet of the word you are expecting as output (specifically done to restrict the search space and can be removed if computational limitations are not a problem).

## Outputs

```
To the Terminal                     # Printed as a list (of length 20, which can be adjusted) of suggestions in decreasing order of similarity
```
