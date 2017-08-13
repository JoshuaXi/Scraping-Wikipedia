from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize

def splitByStopWords(sent):
    wordpunct = wordpunct_tokenize(sent)
    english_stops = set(stopwords.words("english"))
    new_words = []
    words_set = []

    for word in wordpunct:
        if word not in english_stops:
            new_words.append(word)
        else:
            if len(new_words) is not 0:
                words_set.append(" ".join(new_words))
                new_words = []

    if new_words is not None:
        words_set.append(" ".join(new_words))

    return words_set

def splitByBorn(sent):

    result = []

    if "(" in sent and ")" in sent:
        #start_pos = sent.index("(")
        #end_pos = sent.index(")")

        indices_left = [i for i in range(len(sent)) if sent[i] == "("]
        indices_right = [i for i in range(len(sent)) if sent[i] == ")"]

        start_pos = indices_left[0]
        end_pos = indices_right[-1]

        first_element = sent[:start_pos]
        result.append(first_element)
        second_element = sent[start_pos + 1:end_pos]
        result.append(second_element)
        third_element = sent[end_pos + 1:]
        result.append(third_element)

    return result

def remove_bracket(sent):
    while "[" in sent and "]" in sent:
        start_pos = sent.index("[")
        end_pos = sent.index("]")
        if end_pos < start_pos:
            sent = sent.replace("]", "")
        pattern = sent[start_pos:end_pos+1]
        sent = sent.replace(pattern, "")
    return sent

def remove_pattern(sent, patterns):
    for pattern in patterns:
        while pattern in sent:
            sent = sent.replace(pattern, "")

    return sent

def remove_before_born(sent):
    if "born" in sent:
        start_pos = sent.index("born")
        sent = sent[start_pos+4:]

    return sent



class profile_parser():
    def __init__(self, profile):
        self.isProfile = False
        self.profile = None
        if profile is None or len(profile) is 0:
            self.isProfile = False
        else:
            self.isProfile = True
            self.profile = sent_tokenize(profile)[0]
        self.existBorn = False
        self.first_name = []
        self.middle_name = []
        self.last_name = []
        self.birthday = []
        self.birthplace = ""
        self.category = []

    def parse(self):
        parsed = splitByBorn(self.profile)
        self.parsed = []
        if len(parsed) is 0:
            self.existBorn = False

            parsed = splitByStopWords(self.profile)
            try:
                self.parsed.append(parsed[0])
                self.parsed.append("")
                self.parsed.append(parsed[1])
            except:
                self.isProfile = False

        else:
            self.existBorn = True
            self.parsed = parsed

        if self.isProfile:
            self.get_full_names()
            self.get_category()
            self.get_birthday()
            
        #print(self.parsed)

    def get_full_names(self):
        self.parsed[0] = remove_bracket(self.parsed[0])

        full_name = self.parsed[0].split(" ")
        if "" in full_name:
            full_name.remove("")

        if len(full_name) >= 3:
            self.first_name = full_name[0]
            self.middle_name = full_name[1]
            self.last_name = full_name[2]
        elif len(full_name) == 2:
            self.first_name = full_name[0]
            self.middle_name = ""
            self.last_name = full_name[1]
        elif len(full_name) == 1:
            self.first_name = full_name[0]
            self.middle_name = ""
            self.last_name = ""
        else:
            self.first_name = ""
            self.middle_name = ""
            self.last_name = ""

        self.first_name = remove_pattern(self.first_name, ["."])
        self.middle_name = remove_pattern(self.middle_name, ["."])
        self.last_name = remove_pattern(self.last_name, ["."])

        print("First Name: ", self.first_name)
        print("Middel Name: ", self.middle_name)
        print("Last Name: ", self.last_name)

    def get_birthday(self):
        self.parsed[1] = remove_before_born(self.parsed[1])
        self.birthday = self.parsed[1]
        self.birthday = " ".join(self.birthday.split(" "))
        print("Birthday: ", self.birthday)

    def get_category(self):
        self.parsed[2] = remove_bracket(self.parsed[2])
        self.parsed[2] = remove_pattern(self.parsed[2], [".", ";", "]", "["])

        category = splitByStopWords(self.parsed[2])[0]
        self.category = category
        if len(self.category) >=2 and self.category[0] == ",":
            self.category = self.category[1:]
        print("Category: ", self.category)


if __name__ == "__main__":

    profile = "Tun Dato' Sri Haji Abdullah bin Haji Ahmad Badawi ( pronunciation (help·info) " \
              "/ˈɑːbduːlɑː ˈɑːmʌd bʌˈdɑːwiː/ Arabic: عبد الله بن حاجّ أحمد بدوي‎‎ ʿAbdullāh ibn ḥaajj " \
              "Aḥmad Badawī; born 26 November 1939) is a Malaysian politician who served as Prime " \
              "Minister of Malaysia from 2003 to 2009. He was also the President of the United Malays " \
              "National Organisation (UMNO), the largest political party in Malaysia, and led the governing " \
              "Barisan Nasional parliamentary coalition. He is informally known as Pak Lah, 'Pak' meaning " \
              "'Uncle' while 'Lah' is taken from his name 'Abdullah'. He is also referred to as the 'Father of " \
              "Human Capital Development' (Bapa Pembangunan Modal Insan) The Hague from 2008 to 2017."
    app = profile_parser(profile)
    app.parse()


