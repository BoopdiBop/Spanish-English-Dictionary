import requests
from bs4 import BeautifulSoup
        

class SearchBot:
    def __init__(self, query):
        self.query = query
        self.grammar_dict = {}
        
    def search_query(self):
        URL = "https://www.spanishdict.com/translate/" + self.query
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        
        green_text = soup.find_all(class_=["_2VBIE8Jw", "_2-ylzxko", "_1vjZoH4D", "_3nHbP_Tm", "_3AjVTHH0", "_2vd6M2gR"])
        
        lru_grammar_word = ""
        lru_green_text = ""
        definition = ""
        sentence_pair = []

        for element in green_text:
            # we are adding in the grammar words 1st tier
            if element['class'][0] == "_2VBIE8Jw" or element['class'][0] == "_3AjVTHH0":
                if element.text not in self.grammar_dict:
                    # this dictionary will have the general uses as the key (text in ()), with values being an tuple of tuples (eng - es translation)
                    self.grammar_dict[element.text] = {}
                lru_grammar_word = element.text
            # general use (text in ())
            elif element['class'][0] == "_2-ylzxko":
                # assuming this general use text is not used more than once
                if element.text not in self.grammar_dict[lru_grammar_word]:
                    self.grammar_dict[lru_grammar_word][element.text] = {}
                lru_green_text = element.text
            elif element['class'][0] =="_2vd6M2gR":
                #definition = definition + " | " + element.text
                if definition != "":
                    definition += (" | " + element.text)
                else:
                    definition += (" " + element.text)
            elif element['class'][0] =="_1vjZoH4D":
                sentence_pair.append(element.text)
            elif element['class'][0] =="_3nHbP_Tm":
                sentence_pair.append(element.text)
            
            
            if len(sentence_pair) == 2:
                self.grammar_dict[lru_grammar_word][lru_green_text][definition] = (sentence_pair[0], sentence_pair[1])
                definition = ""
                sentence_pair.clear()
                
    def display_info(self):
        if self.grammar_dict: 
            for grammar, meanings in self.grammar_dict.items():
                print(grammar)
                for meaning, definitions in meanings.items():
                    print("\t" + meaning)
                    for definition, sentences in definitions.items():
                        print("\t\t" + definition)
                        print("\t\t\t" + str(sentences))
                        
                            
                print()
        else:
            print("must perform search_query method first.")
            
    def output_message(self):
        message = ''
        if self.grammar_dict: 
            for grammar, meanings in self.grammar_dict.items():
                message += ("\t" + grammar + "\n")
                for meaning, definitions in meanings.items():
                    message += ("\t\t" + meaning + "\n")
                    for definition, sentences in definitions.items():
                        message += ("\t\t\t" + definition + "\n")
                        message += ("\t\t\t\t" + str(sentences[0]) + "\n")
                        message += ("\t\t\t\t" + str(sentences[1]) + "\n")
                        
                            
                message += "\n"
        else:
            message = "must perform search_query method first."
            
        return message





"""        
# function to get request from website
# TESTING - cat, el gato, el monóculo, el monóculo
query = "aguantar"
URL = "https://www.spanishdict.com/translate/" + query
page = requests.get(URL)

# page.content is better than page.text in terms of character encoding
soup = BeautifulSoup(page.content, "html.parser")


# typing in 'Christmas' showed that not all grammar words have the class "_2VBIE8Jw" 
# grammar | class = "_2VBIE8Jw" OR "_3AjVTHH0"
# (green text) | class = "_2-ylzxko"  
# no direct translation | class = "_2_pex0Ik"
# spanish english sentence (one line) | class = "_1KfMZ02u"
# spanish sentence | class = "_1vjZoH4D"
# english sentence | class = "_3nHbP_Tm" OR _1vjZoH4D
# _2vd6M2gR | direct translation

green_text = soup.find_all(class_=["_2VBIE8Jw", "_2-ylzxko", "_1vjZoH4D", "_3nHbP_Tm", "_3AjVTHH0", "_2vd6M2gR"])



  
grammar_dict = {}
# last recently used grammar word
lru_grammar_word = ""
lru_green_text = ""
definition = ""
sentence_pair = []

for element in green_text:
    # we are adding in the grammar words 1st tier
    if element['class'][0] == "_2VBIE8Jw" or element['class'][0] == "_3AjVTHH0":
        if element.text not in grammar_dict:
            # this dictionary will have the general uses as the key (text in ()), with values being an tuple of tuples (eng - es translation)
            grammar_dict[element.text] = {}
        lru_grammar_word = element.text
    # general use (text in ())
    elif element['class'][0] == "_2-ylzxko":
        # assuming this general use text is not used more than once
        if element.text not in grammar_dict[lru_grammar_word]:
            grammar_dict[lru_grammar_word][element.text] = {}
        lru_green_text = element.text
    elif element['class'][0] =="_2vd6M2gR":
        #definition = definition + " | " + element.text
        if definition != "":
            definition += (" | " + element.text)
        else:
            definition += (" " + element.text)
    elif element['class'][0] =="_1vjZoH4D":
        # grammar_dict[lru_grammar_word][lru_green_text][definition] = []
        sentence_pair.append(element.text)
    elif element['class'][0] =="_3nHbP_Tm":
        sentence_pair.append(element.text)
    
    
    if len(sentence_pair) == 2:
        grammar_dict[lru_grammar_word][lru_green_text][definition] = (sentence_pair[0], sentence_pair[1])
        definition = ""
        sentence_pair.clear()
    #print(sentence_pair)
    
        

for grammar, meanings in grammar_dict.items():
    print(grammar)
    for meaning, definitions in meanings.items():
        print("\t" + meaning)
        for definition, sentences in definitions.items():
            print("\t\t" + definition)
            print("\t\t\t" + str(sentences))
        
            
    print()

























grammar_words = {} # key is grammar word
green_text = {} # inside of grammar_words, value of grammar_words' keys
definiton = "" # key of green_text, keep adding to it until you hit a sentence
sentences = [] # value of green text dictionary, consists of tuples
sentence_pair = () # tuple of english and spanish sentnece

# query the websity
query = "cat"
URL = "https://www.spanishdict.com/translate/" + query
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

grams = soup.find_all(class_=["_2VBIE8Jw", "_3AjVTHH0", "o9Q4V2vd"])


for gram in grams:
    if gram["class"][0] == "_2VBIE8Jw" or gram["class"][0] == "_3AjVTHH0":
        print("Grammar word: " + gram.text)
    elif gram['class'][0] == "o9Q4V2vd":
        def_box = gram.find_all(class_=["_2-ylzxko", "_1vjZoH4D", "_3nHbP_Tm", "_2vd6M2gR"])
        for element in def_box:
            if element['class'][0] == "_2-ylzxko":
                print("general meaning: " + element.text)
            elif element['class'][0] == "_2vd6M2gR":
                print("Definition: " + element.text)
            elif element['class'][0] == "_1vjZoH4D":
                print("Sample setence: " + element.text)
            elif element['class'][0] == "_3nHbP_Tm":
                print("Translated sentence: " + element.text)
                
    print()
"""

