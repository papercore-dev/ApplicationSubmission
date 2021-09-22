# Config 파일은 수정할 수 없으며 수정을 위해서는 다른 py파일을 생성해 주세요. (config-app.py 참고) EMBEDCOLOR는 "0x00FFFF"로, PREFIX는 "리크봇"으로 고정되어 있습니다.
# 사용할 수 있는 Config은 PREFIX,EMBEDCOLOR,ERRORCOLOR,PINGPONGCALL,MUTEROLEID입니다.
# TOKEN,PINGPONGURL,PINGPONGAUTHORIZATION은 존재하긴 하나, 토큰이나 secret에 관련한 내용으로, 사용하지 않습니다.
from config import EMBEDCOLOR, PREFIX

# import에 관련한 것들은 여기에 모두 입력해 주세요.
# ex) "import discord"
# discord.py==1.7.3,EZPaginator,lxml,discord-components,aiosqlite,jishaku,PingPongTool,bs4,psutil은
# 이미 선탑재 되어 있으므로 추가로 로드하시면 PR이 거절당할수도 있으며 위의 모듈들만을 사용한다면 추가적인 requirements 파일은 삭제하셔도 됩니다.
import discord 

# from [모듈명] import [서브 모듈명] 꼴로 작성해 주세요.
from discord.ext import commands

# 많은 데스크톱 및 앱 개발 언어에서 사용하는 패키지네임과 비슷한 용도의 Class입니다. name란에는 해당 앱의 이름을 작성해 주세요.
class SampleApp(commands.Cog, name="샘플 어플리케이션"):
  
  # 봇의 시작 스크립트로, 제거하면 안 됩니다.
    def __init__(self, bot): 
        self.bot = bot
        
  # 본 명령어는 PREFIX+name값으로 부를수 있으며, PREFIX+도움에서 help값으로 소개됩니다.
    @commands.command(name="helloworld", help="환영합니다.")
    # 중복되지 않는 값으로만 async를 구현해 주세요.
    async def hworld(self, ctx):
        # 본 부분부터는 일반적인 Discord.py 스크립트처럼 구현하시면 됩니다.
        await ctx.reply('Hello, World!')

# 봇을 load할 때 해당 Class명의 앱을 동시에 로드하는 역할입니다. 만약 본 부분이 적혀있지 않으면 앱의 작동을 중단합니다.
def setup(bot):
    bot.add_cog(SampleApp(bot))
