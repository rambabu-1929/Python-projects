def Suit():
    Suits = ('Heart','Diamond','Club','Spade')
    return Suits

def Rank():
    Ranks = ('One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')
    return Ranks

def rank_value():
    Rank_Value = {
        "One" : 1,
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
        "Six" : 6,
        "Seven" : 7,
        "Eight" : 8,
        "Nine" : 9,
        "Ten" : 10,
        "Jack" : 11,
        "Queen" : 12,
        "King" : 13,
        "Ace" : 14
    }
    return Rank_Value