## Text Processor
A Python program that runs Python's spaCy library to analyze and separate the names of real places that appear in a particular text, along with the frequency of their occurence.

### Features
- uses chunking method making it capable of analysing large texts that surpass spaCy's 1,000,000 characters per text string constraint. 
- cuurently parses strings using ASCII compatible utf-8 with the english language library and can be expanded to include other language libraries and utf-16 support.
- Easy to extend for geocoding hereafter
### How to Run
1. Clone this repository: ``` git clone https://github.com/heeahcodes/Text_processor.git```
2. Run the script: python Text_processor.py
3. Example output:
   London | 36 times
