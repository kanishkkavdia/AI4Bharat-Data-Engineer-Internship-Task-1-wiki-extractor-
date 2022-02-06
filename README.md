# AI4Bharat-Data-Engineer-Internship-Task-1-wiki-extractor-
Task-1 for AI bharat internship.  Write a script (named “wiki_extractor.py”) that performs a Wikipedia search using the provided keyword, and returns urls of “n” related Wikipedia pages. Additionally, the script should also extract one paragraph from each such page and return the result as a json file (Details given below).


Libraries required :
Wikipedia: pip install wikipedia

There are 2 python files:

wiki_api.py: In this python file I have built Wikipedia_info class. It handles user's queries made through wiki_extractor.py and uses it to fetch data through python wikipedia api.

wiki_extractor.py: This file contains basic command to input user queries and send it to Wikipedia_info class created in wiki_api.py.
