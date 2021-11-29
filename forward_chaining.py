import string

basic_propositions = string.ascii_uppercase

# Helper
def check_proposition(symbol):
    if symbol in basic_propositions:
        return True
    return False

def check_implies(symbol):
    if symbol == '>':
        return True
    return False

# Return all propositions
def get_propostions(rule):
    propositions = []

    for symbol in rule:
        if check_proposition(symbol):
            propositions.append(symbol)
        if check_implies(symbol):
            break

    return propositions

# Check if the rule matches with propositions in the database
def check_match(rule, database):
    propositions = get_propostions(rule)

    if set(propositions).issubset(database):
        return True
    return False
    

# search for matches between the rules and the database
def forward_chain(knowledge_base, database):
    x = 0
    turns = len(knowledge_base)

    print("init values")
    print("knowledge Base :", knowledge_base)
    print("Database :", database)

    # the while loop is neccesarry to truly use all rules, even if the rules are executed in a different order
    while x <= turns:
        print("---------------------------------------------")
        print("Turn :",x+1)
        for rule in knowledge_base:
            if check_match(rule, database):
                # if rule matches database add the result of the rule to the database
                # and remove the rule from the knowledge base (since it has already been used)
                database.append(rule[-1])
                knowledge_base.remove(rule)

                print("Matched Rule :", rule)
                print("New Knowledge Base:", knowledge_base)
                print("New Database:", database)

                break
        x+=1

    return database


if __name__ == "__main__":
    # Knowledge Base with Rules
    # knowledge_base = ['A&C>F', 'A&E>G', 'B>E', 'G>D']

    # Input sentence to prove > yields start database and hypothesis
    # sentence = 'A&B>D'

    # example
    # missle => weapon  
    # Col. west => american
    # american & sold & weapons & hostile = X criminal
    # nono = hostile
    # nono & missles => sold

    # sentence
    # West => criminal

    # 
    knowledge_base = ['M>W', 'C>A', 'A&S&W&H>X', 'N>H', 'N&M>S']

    sentence = 'C&M&N>X'


    init_database = get_propostions(sentence)
    hypothesis = sentence[-1]

    end_database = forward_chain(knowledge_base, init_database)

    if hypothesis in end_database:
        print("The sentence is proven correct")
    else:
        print("The sentence is wrong")

