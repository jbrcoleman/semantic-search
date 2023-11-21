# semantic-search
Use vector database qdrant to setup semantic search on dataset. Install the requirements file to install dependencies.

In the search.txt file update the phrase for search that needs to be used for the semantic search. The data to search agains should go in the data.json file.

The output of the search will give you the top searches based on the phrase. For example searching for the phrase alien invasion with the book data given in the example will create the output below:

```
{'name': 'The War of the Worlds', 'description': 'A Martian invasion of Earth throws humanity into chaos.', 'author': 'H.G. Wells', 'year': 1898} score: 0.5700933246392614
{'name': "The Hitchhiker's Guide to the Galaxy", 'description': 'A comedic science fiction series following the misadventures of an unwitting human and his alien friend.', 'author': 'Douglas Adams', 'year': 1979} score: 0.5040468254505261
{'name': 'The Three-Body Problem', 'description': 'Humans encounter an alien civilization that lives in a dying system.', 'author': 'Liu Cixin', 'year': 2008} score: 0.4590293503775251
```

The ne