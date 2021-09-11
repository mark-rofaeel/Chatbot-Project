from wit import Wit 
from pprint import pprint 
import random

access_token = "Q3OPXGBDBTTQUW25L7JHEN5R2A55DVGJ"
client = Wit(access_token = access_token)

def get_wit_response(message_text):
     wit_response = client.message(message_text)
     pprint(wit_response)
     entity = None
     value = None
     intent = None
     try:
          entities = list(wit_response['entities'].keys())
          intent = wit_response['intents'][0]['name']
          for key in entities:
               entity = list(wit_response['entities'])[0]
               value = wit_response['entities'][key][0]['value']
     except:
          pass
          
     
     print(intent,entity,value)
     return (intent,entity,value)

def generate_user_response(messaging_text):
     intent,entity,value = get_wit_response(messaging_text)
     
     quotes = {"love":
["Love is friendship that has caught fire. It is quiet understanding, mutual confidence, sharing and forgiving. It is loyalty through good and bad times. It settles for less than perfection and makes allowances for human weaknesses."
,"Absence is to love as wind is to fire; it extinguishes the small and enkindles the great."
,"Love is composed of a single soul inhabiting two bodies."
,"Love is a fruit in season at all times, and within reach of every hand."
,"Love is a canvas furnished by Nature and embroidered by imagination."]
, "hope":
["Hope is a good breakfast but a bad supper."
,"If it were not for hope, the heart would break."
,"Hope is to keep your eyes on the sun and you will not see the shadows."
,"We must accept finite disappointment, but never lose infinite hope."
,"Walk on with hope in your heart, and you'll never walk alone."]
, "life":
["Life isn't complicated if you don't break your concentration on your true vision."
,"Life is given to us, we earn it by giving it."
,"Life is a divine adventure."
,"Life is holy endured faith."
,"Life is never free of contradictions."]
, "leadership":
["The higher the monkey climbs, the more he shows his tail."
,"Even the largest army is nothing without a good general."
,"The master of the people is their servant."
,"If your actions inspire others to dream more, learn more, do more and become more, you are a leader."
,"A man who wants to lead the orchestra must turn his back on the crowd."]
, "positive":
["Optimism is a happiness magnet. If you stay positive, good things and good people will be drawn to you."
,"Stay positive, all other choices are pointless punishments to your psyche"
,"If you are positive, you'll see opportunities instead of obstacles."
,"When it rains, it pours? but soon, the sun shines again. Stay positive. Better days are on their way.   "
,"Positive thinking is empowering, positive action is achieving."]
, "friendship":
["Hold a true friend with both your hands."
,"A real friend is one who walks in when the rest of the world walks out."
,"Friendship is always a sweet responsibility, never an opportunity."
,"Friendship is the only cement that will ever hold the world together."
,"The language of friendship is not words but meanings."]
, "time":
["Time is what we want most, but... what we use worst."
,"Time is the most valuable thing a man can spend."
,"Time is the longest distance between two places."
,"Time is like the wind, it lifts the light and leaves the heavy."
,"Time flies over us, but leaves its shadow behind."]
, "trust":
["You may be deceived if you trust too much, but you will live in torment if you don't trust enough."
,"Trust is the fruit of a relationship in which you know you are loved."
,"A man who doesn't trust himself can never truly trust anyone else."
,"It is an equal failing to trust everybody, and to trust nobody."
,"Trust is always earned, never given."]
, "sacrifice":
["Some day you will find out that there is far more happiness in another's happiness than in your own."
,"Doing the right thing for someone else occasionally means doing something that feels wrong to you"
,"Sometimes we have to step down to help somebody up, not because we failed to go up, but as a humble sacrifice to save a great soul"
,"Whenever you feel compelled to put others first at the expense of yourself, you are denying your own reality, your own identity"
,"As soon as sacrifice becomes a duty and necessity to mankind. I see no limit to the horizon which opens before him"]
, "wisdom":
["Give a man a fish and you feed him for a day; teach a man to fish and he'll eat forever."
,"When you say one thing, the clever person understands three."
,"Silence is often misinterpreted but never misquoted."
,"The wise understand by themselves; fools follow the reports of others."
,"One should speak little with others and much with oneself"]
, "funny":
["If you think nobody cares about you, try missing a couple of payments.",
"Do not take life too seriously. You will never get out of it alive.",
"Doing nothing is hard, you never know when you're done",
"When life gives you lemons, squirt someone in the eye.",
"Everything is funny, as long as it's happening to somebody else."]
, "dreams":
["All our dreams can come true, if we have the courage to pursue them.",
 "Hold fast to dreams, for if dreams die, life is a broken-winged bird that cannot fly.",
 "The future belongs to those who believe in the beauty of their dreams.",
 "There is only one thing that makes a dream impossible to achieve: the fear of failure.",
 "A dream you dream alone is only a dream. A dream you dream together is reality."]
, "family":
["Home is where you are loved the most and act the worst.",
 "The most important thing a father can do for his children is to love their mother.",
 "While we try to teach our children all about life, our children teach us what life is all about.",
 "Parents were the only ones obligated to love you; from the rest of the world you had to earn it.",
 "The best inheritance a parent can give to his children is a few minutes of their time each day."]
, "sea":
["Smell the sea and feel the sky. Let your soul and spirit fly.",
"Dance with the waves, move with the sea. Let the rhythm of the water set your soul free.",
"Follow the river and you will find the sea.",
"Friends, sun, sand and sea. That sounds like a summer to me",
"The sea is an underwater museum still awaiting its visitors"]
, "survival":
["To survive it is often necessary to fight and to fight you have to dirty yourself.",
"Survival is nothing more than recovery.",
"The ability to delude yourself may be an important survival tool.",
"Every day I run scared. That's the only way I can stay ahead.",
"In truth, we exist and survive, not because of the ego, but in spite of it."]
,"alone":
["I love to be alone. I never found the companion that was so companionable as solitude."
,"It is better to be alone than in bad company."
,"People who cannot bear to be alone are generally the worst company."
,"Sometimes life is too hard to be alone, and sometimes life is too good to be alone."
,"The trouble is not really in being alone, it's being lonely. One can be lonely in the midst of a crowd, don't you think?"]
,"movies":
["I'm going to make him an offer he can't refuse. - The Godfather, 1972",
"They may take our lives but they will never take our freedom!  - Braveheart, 1995",
"The first rule of Fight Club is: You do not talk about Fight Club. - Fight Club, 1999",
"Why so serious? - The Dark Knighet, 2008",
"Gentlemen, you had my curiosity. But now you have my attention - Django Unchained, 2012"]
,"series":
["Leave one wolf alive and the sheep are never safe - Game of Thrones, 2017",
"I Am The One Who Knocks - Breaking Bad, 2011",
"I wanted to save the world - Mr.robot, 2017",
"After all, what’s more human than the fight for survival? - Money Heist, 2017",
"Glitch in the matrix - Dark, 2017"]}
     
     response = None    
     if intent=="send_greetings":
          response="Hello, how are you :D"
     elif intent =="send_thanks":
         response = "It was a pleasure helping you ^_^"
     elif intent =="get_quotes" and entity=="topic_name:topic_name":
          if value in quotes.keys():
              x = random.randint(0, 4)
              response = quotes[value][x]
          else:
              response = "Sure, This is quotes about {}".format(str(value))+" https://www.wisesayings.com/{}".format(str(value))+"-quotes/"
     else:
          response = "Sorry, i didn't understand you!"
     return response
    
