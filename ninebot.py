import discord
import datetime
import openpyxl
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game(":thinking: 테스트 :thinking:")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("나인봇 맵깨짐 오류"):
        await message.channel.send("`esc -> 설정 -> 그래픽 에서 텍스쳐품질을 보통으로 설정해주세요!`")
    if message.content.startswith("나인봇 캐릭터 초기화"):
        await message.channel.send("`#복구문의 에 양식에 맞게 문의해주세요!`")

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)
        await message.channel.send("전송이 완료됬습니다!")

client.run("NjYzMzQ4MzgwMzk5MDQyNTgw.XhHN9Q.vnkGNwgyPxUCt1P2E5rYVXqGcrk")