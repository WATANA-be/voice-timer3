import discord
client = discord.Client()

# 接続できたときに実行される
@client.event
async def on_ready():
    # 初期化処理などが行えるよ
    print("On ready")

if __name__ == "__main__":
    client.run("752707979177885808")
