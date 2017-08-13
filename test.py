from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
import nltk
from nltk.corpus import stopwords

nltk.download()

#intro = "Mehmet Kerem Tunçeri (born April 14, 1979) is a Turkish former professional basketball player who played at the point guard and shooting guard positions. He is 194 cm (6 ft 4 in) in height and 86 kg (190 lbs.) in weight."
#intro = "Hello World. It's good to see you. Thanks for buying this book."
#intro = "Aleksandar Tunchev (Bulgarian: Александър Тунчев; born 10 July 1981 in Pazardzhik) is a Bulgarian former footballer who played as a defender. He is currently assistant coach of Lokomotiv Plovdiv.[2]"
#intro = "Esmeral Özçelik Tunçluer (born April 7, 1980)[1] is a Dutch-Turkish basketball player for Fenerbahçe İstanbul. The 1.75 m (5 ft 9 in) national competitor plays in the guard position. Mert Tunço (born 17 May 1995) is a Turkish male badminton player.[1][2]"
intro = "Tünde Handó (Salgótarján, 1 May 1962 – ) Hungarian jurist, judge, President of the OBH (National Judiciary Office) since 2011."
sent = sent_tokenize(intro)
print(sent)

word = word_tokenize(sent[0])
print(word)

wordpunct = wordpunct_tokenize(sent[0])
print(wordpunct)

english_stops = set(stopwords.words('english'))
print([word for word in wordpunct if word not in english_stops])

new_words = []
words_set = []

for word in wordpunct:
    if word not in english_stops:
        new_words.append(word)
    else:
        if len(new_words) is not 0:
            words_set.append(new_words)
            new_words = []
#print(words_set)

print(' '.join(words_set[0]))
print(' '.join(words_set[1]))
#print(words_set[0].index("born"))

print("\n=====================")
start_pos = words_set[0].index("born")
if ")" in words_set[0]:
    end_pos = words_set[0].index(")")
elif ")[" in words_set[0]:
    end_pos = words_set[0].index(")[")

full_name = words_set[0][:start_pos-1]
if len(full_name) >=3:
    print('First Name: ', full_name[0])
    print('Middel Name: ', full_name[1])
    print('Last Name: ', full_name[2])
else:
    print('First Name: ', full_name[0])
    print('Middel Name: ', '')
    print('Last Name: ', full_name[1])
birthday = words_set[0][start_pos+1:end_pos]
print('Birthday: ', ' '.join(birthday))
category = words_set[1]
print('Category: ', ' '.join(category))





