# semantic-search
Use vector database qdrant to setup semantic search on dataset. Install the requirements file to install dependencies. For this we will walkthrough two examples. One example will be using book dataset and the second example will be using a much large wikipedia summary dataset. Both examples take advantage of a pre-trained model called all-MiniLM-L6-v2 which will transform sentences to vector space so that it can be used for the semantic search.

In the search.txt file update the phrase for search that needs to be used for the semantic search. The data to search agains should go in the data.json file.

The output of the search will give you the top searches based on the phrase. For example searching for the phrase alien invasion with the book data given in the example will create the output below:

```
{'name': 'The War of the Worlds', 'description': 'A Martian invasion of Earth throws humanity into chaos.', 'author': 'H.G. Wells', 'year': 1898} score: 0.5700933246392614
{'name': "The Hitchhiker's Guide to the Galaxy", 'description': 'A comedic science fiction series following the misadventures of an unwitting human and his alien friend.', 'author': 'Douglas Adams', 'year': 1979} score: 0.5040468254505261
{'name': 'The Three-Body Problem', 'description': 'Humans encounter an alien civilization that lives in a dying system.', 'author': 'Liu Cixin', 'year': 2008} score: 0.4590293503775251
```

The second example is query that narrows down the results by searching only in the 2000s and should return:

```
{'name': 'The Three-Body Problem', 'description': 'Humans encounter an alien civilization that lives in a dying system.', 'author': 'Liu Cixin', 'year': 2008} score: 0.4590293503775251
```

## Wikipedia Summary Dataset

First download the stemmed wikipedia summary data set by running the extract_wiki_data.sh. This will download the data and transform it into json format. More wiki datasets can be found here if full summarizations are needed. This example uses stemmed text.

```
https://github.com/tscheepers/Wikipedia-Summary-Dataset/tree/master/src
```

Since this dataset is larger we will be using the qdrant docker container and upload data using the client. If needed the json file can be split up and files uploaded seperately.
```
docker run -p 6333:6333 \
    -v $(pwd)/qdrant_storage:/qdrant/storage \
    qdrant/qdrant
```

Then run
```
python wikipedia.py
```
Running this file will upload the wiki summary dataset into qdrant. This uses on disk storage instead of memory like the first example and uses bulk vector techniques available with the qdrant client. This process takes some time and will be looked into using rust or golang client alternitavely to python client in the future as uploads are much faster.

### Snapshot
Once complete a snapshot of the collection can be taken by running snapshot.py.


### Search Wiki Dataset

Finally we can search the wiki dataset using search.py. Here we will search for the phrase "a Nintendo fighting game allow you to play as Nintendo charachters like Mario to fight." It will return the following result.

```
{
    "name": "super smash bro",
    "summary": "super smash bros. seri crossov fight game publish nintendo primarili featur charact franchis establish system five game direct masahiro sakurai gameplay object differ tradit fighter aim knock oppon stage instead deplet life bar origin super smash bros. releas 1999 nintendo 64 small budget origin japan-onli releas domest success led worldwid releas seri achiev even greater success releas super smash bros. mele releas 2001 gamecub becam best-sel game system third instal super smash bros. brawl releas 2008 wii although hal laboratori develop first two titl third game develop collabor sever compani fourth fifth instal super smash bros. nintendo 3d wii u releas 2014 nintendo 3d wii u respect 3d instal first seri titl releas handheld platform seri featur mani charact nintendo 's popular franchis includ mario fox mccloud link kirbi samu aran pikachu origin super smash bros. 12 playabl charact roster count risen 26 charact mele 39 brawl 58 3ds/wii u seven download charact abl transform differ form differ style play set move game also featur non-play nintendo charact like ridley petey piranha brawl two third-parti charact ad solid snake sonic hedgehog addit third-parti charact mega man pac-man ryu cloud strife bayonetta appear 3d wii u solid snake remov line-up everi titl seri well receiv critic much prais given multiplay mode experi super smash bros. game spawn larg competit commun featur sever high-profil game tournament"
  }
```

## Future Improvements
- Upload data using Rust client
- Serve model for inference