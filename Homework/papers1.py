"""
Homework #3
Description: Strings, list, and functions
"""
from string import punctuation
import constants
WIDTH = 25
SCREENLEN = constants.SCREENLEN
STOPWORDS = constants.STOPWORDS

def processcitation(citation):
    type, year, authors, title, outlet, vol, issue, pp, article = "","","","","","","","",""
    #write your code here
    return type, year, authors, title, outlet, vol, issue, pp, article

def processauthors(authors):
    result = "{"
    # write your code here

    return result[:-2] + "}"

def initial(firstname):
    '''
    This is a supporting function to extrac first name initial
    It should return the initial
    '''
    # write your code here
    pass

def processtitle(title):
    # write your code here
    return title.capitalize()

def abstractstats(abstract):
    numsent, numwords, numchars, numstopwords = 0, 0, 0, 0
    #write your code here

    return numsent, numwords, numstopwords, round(numwords/numsent, 2), round(numchars/numwords, 2)

def removepunc(word):
    # write your code here
    return word


def printlongtext(text, attribute = "Abstract"):
    #attribute is an optional parameter with the default value of "Abstract"
    #This function can be used to print any long text. For example,
    #when you set attribute to be "Title", this function can be used to print a long title

    line = " "*(25-len(attribute)-1) + attribute + ": "

    # write your code here

    print(line + text)

#  helping functions - do not modify

def printcitation(type, year, authors, title, outlet, vol, issue, pp, article):
    print(f"{'Publication Type:':>{WIDTH}} {type}")
    print(f"{'Publication Year:':>{WIDTH}} {year}")
    printlongtext(authors, "Authors")
    printlongtext(title, "Title")
    printlongtext(outlet, "Publication Venue")
    print(f"{'Volume:':>{WIDTH}} {vol}")
    print(f"{'Issue:':>{WIDTH}} {issue}")
    print(f"{'Pages:':>{WIDTH}} {pp}")
    print(f"{'Article No.:':>{WIDTH}} {article}")

def printabstract(abstract, numsent, numwords, numstopwords, avgsentlen, avgwordlen):
    printlongtext(abstract, "Abstract")
    print(f"{'# sentences:':>{WIDTH}} {numsent}")
    print(f"{'# words:':>{WIDTH}} {numwords}")
    print(f"{'# stop words:':>{WIDTH}} {numstopwords}")
    print(f"{'Average sentence length:':>{WIDTH}} {avgsentlen}")
    print(f"{'Average word length:':>{WIDTH}} {avgwordlen}")
    print()

# main function - run after testing the functions you write

def main():
    count = 0
    f = open("../Supplemental exercises/input.txt", 'r')
    lines = f.read().split('\n')

    for line in lines:
        line = line.strip()
        if len(line) != 0:
            count += 1

            if count % 2 == 1:
                print("=" * ((SCREENLEN-8)//2) + "Paper #" + str(count//2+1) + "=" * ((SCREENLEN-8)//2))

            if line.startswith("Citation"):
                type, year, authors, title, outlet, vol, issue, pp, article = processcitation(line[10:])
                printcitation(type, year, authors, title, outlet, vol, issue, pp, article) # [10:] - To strip off "Citation:"
            else:
                numsent, numwords, numstopwords, avgsentlen, avgwordlen = abstractstats(line[10:])
                printabstract(line[10:], numsent, numwords, numstopwords, avgsentlen, avgwordlen) # [10:] - To strip off "Abstract:"


def test():
    # set SCREENLEN = 40 in constants.py for testing
    print("\nremovepunc tests")
    word1 = removepunc("Prediction:")  # check for punctuation at end of word
    # change "your test" to add additional test cases and comment them
    word2 = removepunc("your test")
    word3 = removepunc("your test")

    print(word1, word2, word3, sep="\n")

    print("\nprocessauthors tests")
    authors1 = processauthors("Messeri, L. & Crockett, M.J.")  # two authors
    authors2 = processauthors("add another author test")  # change this test case
    authors3 = processauthors("add another author test")  # change this test case

    print(authors1, authors2, authors3, "\n", sep="\n")

    print("\nprocesstitle tests")
    title1 = processtitle("Harnessing Python: Transforming Business Analytics in Education")
    title2 = processtitle("add another title test case")
    title3 = processtitle("add another title test case")

    print(title1, title2, title3, "\n", sep="\n")

    print("\nprintlongtext tests")
    outlet = "International Journal of Innovative Practices in Business Education and Technology Integration"
    # a long journal name
    printlongtext(authors1, "Authors")
    printlongtext(title1, "Title")
    printlongtext(outlet, "Publication Venue")

    print("\nprocesscitation tests")
    type, year, authors, title, outlet, vol, issue, pp, article = \
        processcitation(
            "Messeri, L. & Crockett, M.J. (2024). Artificial intelligence and illusions of understanding in scientific research, Nature, 627, 49-58.")
    printcitation(type, year, authors, title, outlet, vol, issue, pp, article)

    # add your own citation for a conference proceeding

    print("\nabstract test")
    abstract = "This is a very long sentence. It could be the abstract of an article. It describes a summary of the article."
    numsent, numwords, numstopwords, avgsentlen, avgwordlen = abstractstats(abstract)
    printabstract(abstract, numsent, numwords, numstopwords, avgsentlen, avgwordlen)

# for testing, run the test function so you can determine if your functions are running properly.
# once your functions work properly, comment out the call to test(), then run main()
# and make sure the entire program works.

#main()

test()
