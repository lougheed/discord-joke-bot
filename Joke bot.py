"""
Python discord bot to tell jokes v0.2
Be sure to update the variables  
"api_key" & "BotToken" with the needed keys. 

Use the code however and enjoy (-_-) 

Updates to came: 
*Update the code to post GPT voice and pics
*Find a meme api and deploy it here
*Add a schedule code code block
*Find server hosting for the bot
"""
#Libs needed
from discord.ext import commands 
import discord
import requests
import json
from openai import OpenAI
# joke API site: https://v2.jokeapi.dev/joke/Dark

def get_joke():#ping the website API and requst any joke, while retruning the outout. 
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    # Store JSON data in API_Data
    API_Data = response.json()
    #Grab the val we want
    setup = API_Data["setup"]
    delivery = API_Data["delivery"]
    Output = f"{setup}: {delivery}"#format the string
    return Output

def ChatGPTRequest(text):#useing the openAi lib send a text string to GPT and retrun its output for later use.     
    api_key = "Your key here"
    client = OpenAI(api_key=api_key)    
    completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
            messages=[
                        {"role": "user", "content": text}
                          ]
                      )
    Output= completion.choices[0].message.content
    return Output  

#House keeping
BotToken = "Bot token here"
ChannelID = "ID goes here"
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all()) 

@bot.event
async def on_ready():#what will happen when the bot goes online, in this case print out some info 
    print("Connected...")
    Channel = bot.get_channel(ChannelID)
    await Channel.send("ahhh after 10,000 years I'm free! Its time to tell some jokes!")
    await Channel.send("Use !list to see what i can do.")

@bot.command(name="joke")#call the joke get api request form above and print it out
async def joke(ctx):
    joke = get_joke()
    await ctx.send(joke)   

@bot.command()#call the GPT request the suers text input in the payload 
async def gpt(ctx, *text): # take in user input  
    text = ' '.join(text)# Split it as it comes as a list, this turns it into a str
    print(text)#for logging in the cmd 
    GPTRequest = ChatGPTRequest(text)#pass the str to a GPT def
    await ctx.send(f"ChatGPT: {GPTRequest} ")# Print out to dis    
   
@bot.command()#list of how to call the bot 
async def list(ctx):         
    await ctx.send("!joke to get a random joke")
    await ctx.send("!gpt to talk to/access chatGPT")  

bot.run(BotToken)#bot runs     

"""
                T\ T\
                | \| \
                |  |  :
           _____I__I  |
         .'            '.
       .'                '
       |   ..             '
       |  /__.            |
       :.' -'             |
      /__.                |
     /__, \               |
        |__\        _|    |
        :  '\     .'|     |
        |___|_,,,/  |     |    _..--.
     ,--_-   |     /'      \../ /  /\\
    ,'|_ I---|    7    ,,,_/ / ,  / _\\
  ,-- 7 \|  / ___..,,/   /  ,  ,_/   '-----.
 /   ,   \  |/  ,____,,,__,,__/            '\
,   ,     \__,,/                             |
| '.       _..---.._                         !.
! |      .' z_M__s. '.                        |
.:'      | (-_ _--')  :          L            !
.'.       '.  Y    _.'             \,         :
 .          '-----'                 !          .
 .           /  \                   .          .

 Batman approves this code 
           _____       _____
     ,-'``_.-'` \   / `'-._``'-.
   ,`   .'      |`-'|      `.   `.
 ,`    (    /\  |   |  /\    )    `.
/       `--'  `-'   `-'  `--'       \
|                                   |
\      .--.  ,--.   ,--.  ,--.      /
 `.   (    \/ lt.\ /    \/    )   ,'
   `._ `--.___    V    ___.--' _,'
      `'----'`         `'----'`
"""
