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

    parts = citation.split(").")
    author_year = parts[0].split("(")
    authors = author_year[0]
    year = author_year[1]

    parts2 = parts[1].split(",")
    title = parts2[0].strip()
    outlet = parts2[1].strip()
    vol = parts2[2]
    #issue = parts2[3]
    pp = parts2[-1].rstrip(".")
    return "Journal", year, authors, title, outlet, vol, issue, pp, article


def processauthors(authors):
    result = "{"
    author_list = authors.split(" ; ")
    return "{" + "; ".join(author_list) + "}"
    #return result[:-2] + "}"


def initial(firstname):
    '''
     This is a supporting function to extrac first name initial
     It should return the initial
     '''
    # write your code here
    return firstname[0].upper() if firstname else ""


def processtitle(title):
    return title.capitalize()


def abstractstats(abstract):
    numsent, numwords, numchars, numstopwords = 0, 0, 0, 0
    # write your code here
    numsent = abstract.count(".") + abstract.count("!") + abstract.count("?")
    words = abstract.split()
    numwords = len(words)
    numchars = sum(len(word.strip(punctuation)) for word in words)
    numstopwords = sum(1 for word in words if word.lower() in STOPWORDS)

    return numsent, numwords, numstopwords, round(numwords/numsent, 2), round(numchars/numwords, 2)


def removepunc(word):
    return word


def printlongtext(text, attribute="Abstract"):
    # attribute is an optional parameter with the default value of "Abstract"
    # This function can be used to print any long text. For example,
    # when you set attribute to be "Title", this function can be used to print a long title

    line = " " * (25 - len(attribute) - 1) + attribute + ": "
    # write your code here
    start = 0
    text2 = ""
    while start < len(text):
        # Determine end position
        end = start + SCREENLEN - WIDTH
        if end < len(text) and text[end] != ' ':
            end = text.rfind(' ', start, end)
        if end == -1:  # No space found, force wrap
            end = start + SCREENLEN - WIDTH

        # Extract and print the line
        line = " " * WIDTH + text[start:end].strip()
        text2 += line + '\n'

        # Update the start position for the next iteration
        start = end + 1
    print(f'{text2}')
    # print(f"{'Abstract:':>{WIDTH}} {text2}")
    ''''
    start = 0
    while start < len(text):
        # Determine the end position
        end = start + SCREENLEN - WIDTH
        if end < len(text) and text[end] != ' ':
            end = text.rfind(' ', start, end)
        if end == -1:  # If no space is found, wrap at SCREENLEN
            end = start + SCREENLEN - WIDTH

        # Extract the line and format it
        line = " " * WIDTH + text[start:end].strip()
        print(line)

        # Move the start pointer to the next position
        start = end + 1

    start = 0
    while start < len(text):
        end = start + SCREENLEN - WIDTH
        if end < len(text) and text[end] != ' ':
            end = text.rfind(' ', start, end)
        if end == -1:  # If no space is found, wrap at SCREENLEN
            end = start + SCREENLEN - WIDTH
        # print(line + text[start:end].strip())
        line = " " * WIDTH
        start = end + 1
        print(line + text)
'''

# Helping functions - do not modify
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
    with open("../Supplemental exercises/input.txt", 'r') as f:
        lines = f.read().split('\n')

    for line in lines:
        line = line.strip()
        if len(line) != 0:
            count += 1

            if count % 2 == 1:
                print("=" * ((SCREENLEN - 8) // 2) + "Paper #" + str(count // 2 + 1) + "=" * ((SCREENLEN - 8) // 2))

            if line.startswith("Citation"):
                type, year, authors, title, outlet, vol, issue, pp, article = processcitation(line[10:])
                printcitation(type, year, authors, title, outlet, vol, issue, pp, article)   # [10:] - To strip off "Citation:"
            else:
                numsent, numwords, numstopwords, avgsentlen, avgwordlen = abstractstats(line[10:])
                printabstract(line[10:], numsent, numwords, numstopwords, avgsentlen, avgwordlen)   # [10:] - To strip off "Abstract:"


def test():
    """
    Test each function to verify it performs as expected.
    """
    print("\nremovepunc tests")
    word1 = removepunc("Prediction:")
    word2 = removepunc("Prediction1/")
    word3 = removepunc("Predication2!")

    print(word1, word2, word3, sep="\n")

    print("\nprocessauthors tests")
    authors1 = processauthors("Messeri, L. & Crockett, M.J.")
    authors2 = processauthors("Stieber, S. & Heber, L.")
    authors3 = processauthors("Yang, Y. & Qin Y.")

    print(authors1, authors2, authors3, "\n", sep="\n")

    print("\nprocesstitle tests")
    title1 = processtitle("Harnessing Python: Transforming Business Analytics In Education")
    title2 = processtitle("Artificial Intelligence and Illusions of Understanding in Scientific Research")
    title3 = processtitle("Control of Composite Manufacturing Processes Through Deep Reinforcement Learning")

    print(title1, title2, title3, "\n", sep="\n")

    print("\nprintlongtext tests")
    outlet = "International Journal of Innovative Practices in Business Education and Technology Integration"
    printlongtext(authors1, "Authors")
    printlongtext(title1, "Title")
    printlongtext(outlet, "Publication Venue")

    print("\nprocesscitation tests")
    type, year, authors, title, outlet, vol, issue, pp, article = \
        processcitation(
            "Messeri, L. & Crockett, M.J. (2024). Artificial intelligence and illusions of understanding in scientific research, Nature, 627, 49-58.")
    printcitation(type, year, authors, title, outlet, vol, issue, pp, article)
    # add your own citation for a conference proceeding
    type2, year2, authors2, title2, outlet2, vol2, issue2, pp2, article2 = \
        processcitation(
            "Conference Article: Stieber, S. & Heber, L. (2023). Control of composite manufacturing processes through deep reinforcement learning, the International Conference on Machine Learning and Applications (ICMLA), , 17-22.")
    printcitation(type2, year2, authors2, title2, outlet2, vol2, issue2, pp2, article2)

    type3, year3, authors3, title3, outlet3, vol3, issue3, pp3, article3 = \
        processcitation(
            "Journal Paper: Yang, Y. & Qin, Y. (2023). Unlocking the power of voice for financial risk prediction: A theory-driven deep learning design approach, MIS Quarterly, 63-96.")
    printcitation(type3, year3, authors3, title3, outlet3, vol3, issue3, pp3, article3)


    print("\nabstract test")
    abstract = "This is a very long sentence. It could be the abstract of an article. It describes a summary of the article."
    numsent, numwords, numstopwords, avgsentlen, avgwordlen = abstractstats(abstract)
    printabstract(abstract, numsent, numwords, numstopwords, avgsentlen, avgwordlen)

# for testing, run the test function so you can determine if your functions are running properly.
# once your functions work properly, comment out the call to test(), then run main()
# and make sure the entire program works.

main()

# test()
