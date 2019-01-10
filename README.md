Swedish lemmatizer
==================

I looked online for a swedish lemmatizer to use with pandas dataframes but couldn't find any so I put this naive solution together.

The file in this repo with swedish words key value pairs is extracted from the `svwiktionary-20190101-pages-meta-current.xml.bz2` file that can be found here https://dumps.wikimedia.org/svwiktionary/20190101/.

The solution seems to work fine for my usecase but I have only tested it briefly so please let me know if you use it and notice any unexpected behaviour.

### Example - Lemmatize:
```python
import json
from lemmatizer import lemmatize


f = open('data/swedish_words.json')
word_list = json.load(f)
f.close()

# Swedish poem. Excerpt from here: http://web.comhem.se/humanistgruppen/dikter/ekeloef_eufori.htm
sentence = "Du sitter i trädgården ensam med anteckningsboken, en " \
"smörgås, pluntan och pipan. " \
"Det är natt men så lugnt att ljuset brinner utan att fladdra " \
"sprider ett återsken över bordet av skrovliga plankor " \
"och glänser i flaska och glas."

sentence = sentence.replace(".", "").replace(",", "").lower()

lemmatize(sentence, word_list)

# Output

# du sitta i trädgård ensam med anteckningsbok
# en smörgås plunta och pipa
# det vara natt men så # lugn att ljus brinna utan att fladdra
# sprida ett återsken över bord av skrovlig planka
# och glänsa i flaska och glas

```

### Example - Extract words from a Wiktionary XML dump file:
```python
from lemmatizer import extract_words


wiktionary_file = "/path/to/your/file/svwiktionary-20190101-pages-meta-current.xml"
extract_words(wiktionary_file, "data/swedish_words.json")
```
