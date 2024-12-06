"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Assignment 3)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
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
    # Split authors and year from the rest of the citation
    if "(" in citation:
        authors_part, rest = citation.split(" (", 1)
        authors = processauthors(authors_part.strip())
        if ")." in rest:
            year_part, rest = rest.split("). ", 1)
            year = year_part.strip()
        else:
            year = ""
            rest = rest.strip()
    # Determine type of publication and process remaining details
    if "Proceedings of" in rest:
        type = "Conference Article"
        title_part, outlet_part = rest.split(" in ", 1)
        title = processtitle(title_part.strip())
        if ", " in outlet_part:
            outlet, pp = outlet_part.rsplit(", ", 1)
            outlet = outlet.strip()
            pp = pp.strip()
        else:
            outlet = outlet_part.strip()
            pp = ""
    else:
        type = "Journal Paper"
        # Split remaining parts of the journal citation
        remaining_parts = rest.rsplit(", ", 3)
        if len(remaining_parts) >= 1:
            title = processtitle(remaining_parts[0].strip())
        if len(remaining_parts) >= 2:
            outlet = remaining_parts[1].strip()
        if len(remaining_parts) >= 3:
            vol = remaining_parts[2].strip()
            vol = vol.split("(")[0].strip()
        if len(remaining_parts) >= 4:
            pp = remaining_parts[3].strip().replace(".", "")  # Extract and clean page numbers

    return type, year, authors, title, outlet, vol, issue, pp, article

def processauthors(authors):
    result = "{"
    # write your code here

    if " &" in authors and not authors[authors.index(" &") - 1] == ",":
        authors = authors.replace(" &", ", &")
   # Split authors into a list
    authors = authors.replace("&", "").strip()
    authors_list = [author.strip() for author in authors.split(",")]

    i = 0
    while i < len(authors_list):
        if i + 1 < len(authors_list):
            last_name = authors_list[i].strip().capitalize()
            first_name = authors_list[i + 1].strip()

            initials = initial(first_name)
            result += f"{initials} {last_name}; "
            i += 2
        else:
            last_name = authors_list[i].strip().capitalize()
            result += f"{last_name}; "
            i += 1

    return result[:-2] + "}"  # Remove trailing "; " and close the brace

def initial(firstname):
    '''
    This is a supporting function to extrac first name initial
    It should return the initial
    '''
    # write your code here
    parts = firstname.strip().split()
    if "." in firstname:
        return firstname.upper()  # Return uppercase for names already in initial format

    return parts[0][0].upper() + "."  # Capitalize the first letter and append a dot

def processtitle(title):
    result = []
    capitalize_next = True

    for i, char in enumerate(title):
        if capitalize_next and char.isalpha():
            result.append(char.upper())  # Capitalize alphabetic characters
            capitalize_next = False
        else:
            result.append(char.lower())

        if char in ":?":
            result.append(' ')
            capitalize_next = True

    return ''.join(result).replace('  ', ' ')


def abstractstats(abstract):
    numsent, numwords, numchars, numstopwords = 0, 0, 0, 0
    #write your code here
    sentences = []
    sentence = ""
    # Split abstract into sentences
    for char in abstract:
        sentence += char
        if char in ".!?":
            sentences.append(sentence.strip())
            sentence = ""

    if sentence:
        sentences.append(sentence.strip())

    numsent = len(sentences)
    words = abstract.split()
    numwords = len(words)
    numstopwords = sum(1 for word in words if word.lower().strip(punctuation) in STOPWORDS)
    numchars = sum(len(removepunc(word)) for word in words)

    return numsent, numwords, numstopwords, round(numwords/numsent, 2), round(numchars/numwords, 2)

def removepunc(word):
    # write your code here
    word = word.strip(punctuation)
    return word


def printlongtext(text, attribute = "Abstract"):
    #attribute is an optional parameter with the default value of "Abstract"
    #This function can be used to print any long text. For example,
    #when you set attribute to be "Title", this function can be used to print a long title

    line = " "*(25-len(attribute)-1) + attribute + ": "

    # write your code here
    available_space = SCREENLEN - len(line)

    first_line = line
    # Print text, wrapping lines as needed
    while len(text) > available_space:
        cut = text.rfind(" ", 0, available_space)
        if cut == -1:
            cut = available_space
        print(first_line + text[:cut])

        first_line = " " * len(line)

        text = text[cut:].strip()

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
    with open("../Supplemental exercises/input.txt", 'r') as f:
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

#test()

