import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {client.user}")

@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return
    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "Hello":
        await message.channel.send("Hello, world!")
        return
    
    if message.content == "愛你":
        await message.channel.send("<3")
        return
    

    if message.content == "!":
        with open("money.txt", "r") as money:
            F = money.readline()
            sentence = "目前宗翰欠薇昕： " + str(F)
            await message.channel.send(sentence)
            return
    
    if message.content.startswith("!="):
        num = message.content.strip().split(" ")
        a = int(num[1])
        with open("money.txt", "w") as money:
            money.write(str(a))
            sentence = "目前宗翰欠薇昕： " + str(a)
            await message.channel.send(sentence)
            return

    if message.content.startswith("!"):
        num = message.content.strip().split(" ")
        a = int(num[1])
        
        money = open("money.txt", "r")
        b = int(money.readline().strip())
        money.close()

        money = open("money.txt", "w")
        money.write(str(a + b))
        sentence = "目前宗翰欠薇昕： " + str(a + b)
        await message.channel.send(sentence)
        money.close()
        return

client.run("MTE5Nzg5ODgzNTUzNjY1ODU2Mg.GGm7BG.ksugwhInIOrhVH3qZ8CaJ79rlGC9bhLym87Aqc")
