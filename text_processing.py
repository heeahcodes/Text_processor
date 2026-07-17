def main():
    import spacy
    from collections import Counter #to count the frequency of a named entity

    nlp = spacy.load("en_core_web_sm") #loads the english language module for spacy
    #loads the novel with utf-8 encoding to process both regular and special characters safely
    with open("Bleak House.txt", "r",
              encoding = "utf-8") as file:
        #spilts texts by double newlines to separate content into smaller chunks
        text_chunks = file.read().split("\n\n")
        #cleans whitespace, removes empty strings
        text_chunks = [chunk.strip() for chunk in text_chunks if chunk.strip()]

    """ The pipe method was used to chunk the text [ Bleak House by Charles Dickens] as the character count
    exceeded spaCy's character limit of 1000000 characters
    """
    location_list = [] #list to append all the recognized entities in the text
    #n_process unlocks all cores for faster processing, surpasses GIL
    for doc in nlp.pipe(text_chunks, batch_size = 30, n_process = -1): #parsing size limited to chunks of 30
        for ent in doc.ents:
            if ent.label_ in ["GPE", "LOC"]: #entity labels for geopolitical entities and non-GPE locations
                location_list.append(ent.text)
    location_counts = Counter(location_list)

    #displays output in the form of a list with names and the frequency of appearance
    print(f"found locations --- ")
    for location, count in location_counts.most_common(30):
        print(f"{location}:{count} mentions")

if __name__ == '__main__':  # boilerplate
    main()