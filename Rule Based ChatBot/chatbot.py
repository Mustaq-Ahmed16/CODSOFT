from nltk.chat.util import Chat,reflections
#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)(Robot|robot|Bot|bot)",
        ["hi Human, how can I help you "]
    ],
    [
        r"(.*)question",
        ["I am here for you"]
    ],
    
    [
        r"(.*)developed ",
        ["Mr.Mustaq Ahmed created me using Python"]
    ],
    [
        r"(.*)alive",
        ["I am a Rule-Based ChatBot, I am just a computer program . Created by Mustaq"]
    ],


    [
        r"(.*)help|Help",
        ["How can I help you ",]
    ],
    [
        r"(.*)whats your name|Who are you?|who|Who you are?|Your name|Good name(.*)",
        ["My name is Chitti Bot, but you can just call me Bot and I'm a chatbot ."]
    ],
    [
        r"(.*)how are you|How are you|How are you?",
        ["I'm doing very well,what about you?", "i am great !, what about you?"]
    ],
    [
        r"(.*)sorry",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"(.*)good|well|okay|ok",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(.*)(hi|hey|hello|hola|holla|Hello|Helo|Hola|Holla|Hi|Hii)(.*)",
        ["Hello...", "Hey there",]
    ],
    [
        r"(.*)what| want?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created",
        ["Mr.Mustaq Ahmed created me using Python's NLTK library ","Its top secret........... ;)",]
    ],
    [
        r"(.*)(location|city)",
        ['Kurnool, Andhra Pradesh India',]
    ],
    
    [
        r"(.*)Health|health",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    
    [
        r"(.*)(quit|Bye|Byee|Good Bye|good bye|Good bye|good Bye)",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
    
]


my_dummy_reflections= {
    "go"     : "gone",
    
}
chat = Chat(pairs, reflections)
print(chat)
chat.converse()