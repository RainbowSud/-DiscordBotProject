import discord
import random
import json
from discord.ext import commands
from datetime import datetime


class Wish(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x55a7f7

    @commands.command(aliases=['Wish'])
    async def wish(self, ctx, com = " "):
        user = ctx.message.author
        with open('wishPity.json', 'r') as f:
            pity = json.load(f)

        if str(user.id) not in pity:
            pity[str(user.id)] = {
                "standardPity": 10,
                "rateUpPity": 10,
                "allTimeWishes": 0,
                "fiveGuarantee": False,
                "fourGuarantee": False
            }

        rateUpFiveStar = ["null"]
        rateUpFourStar = ["null"]
        otherFourStar = ["null"]
        #Standard wish w/ standard logic
        if com == " ":
            # 5 Entries
            FiveSChar = ["☆☆☆☆☆ Keqing",
                         "☆☆☆☆☆ Mona",
                         "☆☆☆☆☆ QiQi",
                         "☆☆☆☆☆ Diluc",
                         "☆☆☆☆☆ Jean"]
            # 10 Entries
            FiveSWep = ["☆☆☆☆☆ Amos' Bow",
                        "☆☆☆☆☆ Skyward Harp",
                        "☆☆☆☆☆ Lost Prayer to the Sacred Winds",
                        "☆☆☆☆☆ Skyward Atlas",
                        "☆☆☆☆☆ Primordial Jade Winged-Spear",
                        "☆☆☆☆☆ Skyward Spine",
                        "☆☆☆☆☆ Wolf's Gravestone",
                        "☆☆☆☆☆ Skyward Pride",
                        "☆☆☆☆☆ Skyward Blade",
                        "☆☆☆☆☆ Aquila Favonia"]
            # 16 Entries
            FourSChar = ["☆☆☆☆ Xinyan",
                         "☆☆☆☆ Sucrose",
                         "☆☆☆☆ Diona",
                         "☆☆☆☆ Chongyun",
                         "☆☆☆☆ Noelle",
                         "☆☆☆☆ Bennett",
                         "☆☆☆☆ Fischl",
                         "☆☆☆☆ Ningguang",
                         "☆☆☆☆ Xingqiu",
                         "☆☆☆☆ Beidou",
                         "☆☆☆☆ Xiangling",
                         "☆☆☆☆ Amber",
                         "☆☆☆☆ Razor",
                         "☆☆☆☆ Kaeya",
                         "☆☆☆☆ Barbara",
                         "☆☆☆☆ Lisa"]
            # 18 Entries
            FourSWep = ["☆☆☆☆ Rust",
                        "☆☆☆☆ Sacrificial Bow",
                        "☆☆☆☆ The Stringless",
                        "☆☆☆☆ Favonius Warbow",
                        "☆☆☆☆ Eye of Perception",
                        "☆☆☆☆ Sacrificial Fragments",
                        "☆☆☆☆ The Widsith",
                        "☆☆☆☆ Favonius Codex",
                        "☆☆☆☆ Favonius Lance",
                        "☆☆☆☆ Dragon's Bane",
                        "☆☆☆☆ Rainslasher",
                        "☆☆☆☆ Sacrificial Greatsword",
                        "☆☆☆☆ The Bell",
                        "☆☆☆☆ Favonius Greatsword",
                        "☆☆☆☆ Lion's Roar",
                        "☆☆☆☆ Sacrificial Sword",
                        "☆☆☆☆ The Flute",
                        "☆☆☆☆ Favonius Sword"]
            # 13 Entries
            ThreeSWep = ["☆☆☆ Slingshot",
                         "☆☆☆ Sharpshooter's Oath",
                         "☆☆☆ Raven Bow",
                         "☆☆☆ Emerald Orb",
                         "☆☆☆ Thrilling Tales of Dragon Slayers",
                         "☆☆☆ Magic Guide",
                         "☆☆☆ Black Tassel",
                         "☆☆☆ Debate Club",
                         "☆☆☆ Bloodtainted Greatsword",
                         "☆☆☆ Ferrous Shadow",
                         "☆☆☆ Skyrider Sword",
                         "☆☆☆ Harbinger of Dawn",
                         "☆☆☆ Cool Steel"]
            # Actual Multi-Wish
            # This is the first wish, gonna write it to be a 4 or 5* 100%
            summon = []
            a = random.randint(1, 1000)
            if pity[str(user.id)]['standardPity'] == 90:
                b = random.randint(1, 2)
                if b == 1:
                    summon.append(random.choice(FiveSWep))
                    pity[str(user.id)]['standardPity'] = 0
                else:
                    summon.append(random.choice(FiveSChar))
                    pity[str(user.id)]['standardPity'] = 0
            else:
                if a <= 6:
                    b = random.randint(1, 2)
                    if b == 1:
                        summon.append(random.choice(FiveSWep))
                        pity[str(user.id)]['standardPity'] = 0
                    else:
                        summon.append(random.choice(FiveSChar))
                        pity[str(user.id)]['standardPity'] = 0
                else:
                    b = random.randint(1, 2)
                    if b == 1:
                        summon.append(random.choice(FourSWep))
                    else:
                        summon.append(random.choice(FourSChar))
            for i in range(9):
                d = random.randint(1, 1000)
                if pity[str(user.id)]['standardPity'] < 75:
                    if d <= 6:
                        e = random.randint(1, 2)
                        if e == 1:
                            summon.append(random.choice(FiveSWep))
                            pity[str(user.id)]['standardPity'] = 0
                        else:
                            summon.append(random.choice(FiveSChar))
                            pity[str(user.id)]['standardPity'] = 0
                    if 6 < d <= 57:
                        e = random.randint(1, 2)
                        if e == 1:
                            summon.append(random.choice(FourSWep))
                        else:
                            summon.append(random.choice(FourSChar))
                    else:
                        summon.append(random.choice(ThreeSWep))
                elif 75 <= pity[str(user.id)]['standardPity'] <= 89:
                    if d <= 200:
                        e = random.randint(1, 2)
                        if e == 1:
                            summon.append(random.choice(FiveSWep))
                            pity[str(user.id)]['standardPity'] = 0
                        else:
                            summon.append(random.choice(FiveSChar))
                            pity[str(user.id)]['standardPity'] = 0
                    if 200 < d <= 257:
                        e = random.randint(1, 2)
                        if e == 1:
                            summon.append(random.choice(FourSWep))
                        else:
                            summon.append(random.choice(FourSChar))
                    else:
                        summon.append(random.choice(ThreeSWep))
            summon.sort()
            summon.reverse()
            summonList = "\n".join(summon)
            g = summon.pop(0)
            if "☆☆☆☆☆" in g:
                self.color = 0xeeff00
            else:
                self.color = 0xaf4dff
            pity[str(user.id)]['allTimeWishes'] += 10
            embed = discord.Embed(color=self.color, timestamp=datetime.utcnow())
            embed.add_field(name="Your Wish",
                            value=f"{summonList}\n\nStandard Pity = {pity[str(user.id)]['standardPity']}",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            pity[str(user.id)]['standardPity'] += 10
            with open('wishPity.json', 'w') as f:
                json.dump(pity, f, indent=4)
            await ctx.send(embed=embed)
            return
        elif com == 'venti' or com == 'Venti':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Venti"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Xiangling",
                              "☆☆☆☆ Barbara",
                              "☆☆☆☆ Fischl"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Xinyan",
                             "☆☆☆☆ Sucrose",
                             "☆☆☆☆ Diona",
                             "☆☆☆☆ Chongyun",
                             "☆☆☆☆ Noelle",
                             "☆☆☆☆ Bennett",
                             "☆☆☆☆ Ningguang",
                             "☆☆☆☆ Xingqiu",
                             "☆☆☆☆ Beidou",
                             "☆☆☆☆ Razor"]
        elif com == 'klee' or com == 'Klee':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Klee"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Sucrose",
                              "☆☆☆☆ Xingqiu",
                              "☆☆☆☆ Noelle"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Xinyan",
                             "☆☆☆☆ Diona",
                             "☆☆☆☆ Chongyun",
                             "☆☆☆☆ Bennett",
                             "☆☆☆☆ Ningguang",
                             "☆☆☆☆ Beidou",
                             "☆☆☆☆ Razor",
                             "☆☆☆☆ Xiangling",
                             "☆☆☆☆ Barbara",
                             "☆☆☆☆ Fischl"]
        elif com == 'tartaglia' or com == 'Tartaglia':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Tartaglia"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Beidou",
                              "☆☆☆☆ Ningguang",
                              "☆☆☆☆ Diona"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Xinyan",
                             "☆☆☆☆ Sucrose",
                             "☆☆☆☆ Chongyun",
                             "☆☆☆☆ Noelle",
                             "☆☆☆☆ Bennett",
                             "☆☆☆☆ Xingqiu",
                             "☆☆☆☆ Razor",
                             "☆☆☆☆ Xiangling",
                             "☆☆☆☆ Barbara",
                             "☆☆☆☆ Fischl"]
        elif com == 'zhongli' or com == 'Zhongli':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Zhongli"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Razor",
                              "☆☆☆☆ Chongyun",
                              "☆☆☆☆ Xinyan"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Sucrose",
                             "☆☆☆☆ Diona",
                             "☆☆☆☆ Noelle",
                             "☆☆☆☆ Bennett",
                             "☆☆☆☆ Ningguang",
                             "☆☆☆☆ Xingqiu",
                             "☆☆☆☆ Beidou",
                             "☆☆☆☆ Xiangling",
                             "☆☆☆☆ Barbara",
                             "☆☆☆☆ Fischl"]
        elif com == 'albedo' or com == 'Albedo':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Albedo"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Bennett",
                              "☆☆☆☆ Sucrose",
                              "☆☆☆☆ Fischl"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Xinyan",
                             "☆☆☆☆ Diona",
                             "☆☆☆☆ Chongyun",
                             "☆☆☆☆ Noelle",
                             "☆☆☆☆ Ningguang",
                             "☆☆☆☆ Xingqiu",
                             "☆☆☆☆ Beidou",
                             "☆☆☆☆ Razor",
                             "☆☆☆☆ Xiangling",
                             "☆☆☆☆ Barbara", ]
        elif com == 'ganyu' or com == 'Ganyu':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Ganyu"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Xiangling",
                              "☆☆☆☆ Xingqiu",
                              "☆☆☆☆ Noelle"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Xinyan",
                             "☆☆☆☆ Sucrose",
                             "☆☆☆☆ Diona",
                             "☆☆☆☆ Chongyun",
                             "☆☆☆☆ Bennett",
                             "☆☆☆☆ Ningguang",
                             "☆☆☆☆ Beidou",
                             "☆☆☆☆ Razor",
                             "☆☆☆☆ Barbara",
                             "☆☆☆☆ Fischl"]
        elif com == 'xiao' or com == 'Xiao':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Xiao"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Xinyan",
                              "☆☆☆☆ Beidou",
                              "☆☆☆☆ Diona"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Sucrose",
                             "☆☆☆☆ Chongyun",
                             "☆☆☆☆ Noelle",
                             "☆☆☆☆ Bennett",
                             "☆☆☆☆ Ningguang",
                             "☆☆☆☆ Xingqiu",
                             "☆☆☆☆ Razor",
                             "☆☆☆☆ Xiangling",
                             "☆☆☆☆ Barbara",
                             "☆☆☆☆ Fischl"]
        elif com == 'keqing' or com == 'Keqing':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Keqing"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Bennett",
                              "☆☆☆☆ Ningguang",
                              "☆☆☆☆ Barbara"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Xinyan",
                             "☆☆☆☆ Sucrose",
                             "☆☆☆☆ Diona",
                             "☆☆☆☆ Chongyun",
                             "☆☆☆☆ Noelle",
                             "☆☆☆☆ Xingqiu",
                             "☆☆☆☆ Beidou",
                             "☆☆☆☆ Razor",
                             "☆☆☆☆ Xiangling",
                             "☆☆☆☆ Fischl"]
        elif com == 'hutao' or com == 'Hutao':
            # 1 Entry
            rateUpFiveStar = ["☆☆☆☆☆ Hutao"]
            # 3 Entry
            rateUpFourStar = ["☆☆☆☆ Xiangling",
                              "☆☆☆☆ Chongyun",
                              "☆☆☆☆ Xinqiu"]
            # 10 Entries
            otherFourStar = ["☆☆☆☆ Xinyan",
                             "☆☆☆☆ Sucrose",
                             "☆☆☆☆ Diona",
                             "☆☆☆☆ Noelle",
                             "☆☆☆☆ Bennett",
                             "☆☆☆☆ Ningguang",
                             "☆☆☆☆ Beidou",
                             "☆☆☆☆ Razor",
                             "☆☆☆☆ Barbara",
                             "☆☆☆☆ Fischl"]
        else:
            embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name="Error",
                            value=f"You used incorrect syntax, please refer to \"%help wish\" for more info",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)
            return
        # 5 Entries
        FiveSChar = ["☆☆☆☆☆ Keqing",
                     "☆☆☆☆☆ Mona",
                     "☆☆☆☆☆ QiQi",
                     "☆☆☆☆☆ Diluc",
                     "☆☆☆☆☆ Jean"]
        # 18 Entries
        FourSWep = ["☆☆☆☆ Rust",
                    "☆☆☆☆ Sacrificial Bow",
                    "☆☆☆☆ The Stringless",
                    "☆☆☆☆ Favonius Warbow",
                    "☆☆☆☆ Eye of Perception",
                    "☆☆☆☆ Sacrificial Fragments",
                    "☆☆☆☆ The Widsith",
                    "☆☆☆☆ Favonius Codex",
                    "☆☆☆☆ Favonius Lance",
                    "☆☆☆☆ Dragon's Bane",
                    "☆☆☆☆ Rainslasher",
                    "☆☆☆☆ Sacrificial Greatsword",
                    "☆☆☆☆ The Bell",
                    "☆☆☆☆ Favonius Greatsword",
                    "☆☆☆☆ Lion's Roar",
                    "☆☆☆☆ Sacrificial Sword",
                    "☆☆☆☆ The Flute",
                    "☆☆☆☆ Favonius Sword"]
        # 13 Entries
        ThreeSWep = ["☆☆☆ Slingshot",
                     "☆☆☆ Sharpshooter's Oath",
                     "☆☆☆ Raven Bow",
                     "☆☆☆ Emerald Orb",
                     "☆☆☆ Thrilling Tales of Dragon Slayers",
                     "☆☆☆ Magic Guide",
                     "☆☆☆ Black Tassel",
                     "☆☆☆ Debate Club",
                     "☆☆☆ Bloodtainted Greatsword",
                     "☆☆☆ Ferrous Shadow",
                     "☆☆☆ Skyrider Sword",
                     "☆☆☆ Harbinger of Dawn",
                     "☆☆☆ Cool Steel"]
        summon = []
        a = random.randint(1, 1000)
        if pity[str(user.id)]['rateUpPity'] == 90:
            if pity[str(user.id)]['fiveGuarantee']:
                summon.append(random.choice(rateUpFiveStar))
                pity[str(user.id)]['rateUpPity'] = 0
                pity[str(user.id)]['fiveGuarantee'] = False
            else:
                h = random.randint(1, 2)
                if h == 1:
                    summon.append(random.choice(FiveSChar))
                    pity[str(user.id)]['rateUpPity'] = 0
                    pity[str(user.id)]['fiveGuarantee'] = True
                else:
                    summon.append(random.choice(rateUpFiveStar))
                    pity[str(user.id)]['rateUpPity'] = 0
                    pity[str(user.id)]['fiveGuarantee'] = False
        else:
            if a <= 6:
                if pity[str(user.id)]['fiveGuarantee']:
                    summon.append(random.choice(rateUpFiveStar))
                    pity[str(user.id)]['fiveGuarantee'] = False
                    pity[str(user.id)]['rateUpPity'] = 0
                else:
                    k = random.randint(1, 2)
                    if k == 1:
                        summon.append(random.choice(FiveSChar))
                        pity[str(user.id)]['rateUpPity'] = 0
                        pity[str(user.id)]['fiveGuarantee'] = True
                    else:
                        summon.append(random.choice(rateUpFiveStar))
                        pity[str(user.id)]['rateUpPity'] = 0
                        pity[str(user.id)]['fiveGuarantee'] = False
            else:
                if pity[str(user.id)]['fourGuarantee']:
                    summon.append(random.choice(rateUpFourStar))
                    pity[str(user.id)]['fourGuarantee'] = False
                else:
                    b = random.randint(1, 2)
                    if b == 1:
                        summon.append(random.choice(FourSWep))
                    else:
                        summon.append(random.choice(otherFourStar))
                    pity[str(user.id)]['fourGuarantee'] = True
        for i in range(9):
            d = random.randint(1, 1000)
            if pity[str(user.id)]['rateUpPity'] < 75:
                if d <= 6:
                    if pity[str(user.id)]['fiveGuarantee']:
                        summon.append(random.choice(rateUpFiveStar))
                        pity[str(user.id)]['fiveGuarantee'] = False
                        pity[str(user.id)]['rateUpPity'] = 0
                    else:
                        l = random.randint(1, 2)
                        if l == 1:
                            summon.append(random.choice(FiveSChar))
                            pity[str(user.id)]['rateUpPity'] = 0
                            pity[str(user.id)]['fiveGuarantee'] = True
                        else:
                            summon.append(random.choice(rateUpFiveStar))
                            pity[str(user.id)]['rateUpPity'] = 0
                            pity[str(user.id)]['fiveGuarantee'] = False
                if 6 < d <= 57:
                    if pity[str(user.id)]['fourGuarantee']:
                        summon.append(random.choice(rateUpFourStar))
                        pity[str(user.id)]['fourGuarantee'] = False
                    else:
                        e = random.randint(1, 2)
                        if e == 1:
                            summon.append(random.choice(FourSWep))
                        else:
                            summon.append(random.choice(otherFourStar))
                        pity[str(user.id)]['fourGuarantee'] = True
                else:
                    summon.append(random.choice(ThreeSWep))
            elif 75 <= pity[str(user.id)]['rateUpPity'] <= 89:
                if d <= 200:
                    if pity[str(user.id)]['fiveGuarantee']:
                        summon.append(random.choice(rateUpFiveStar))
                        pity[str(user.id)]['fiveGuarantee'] = False
                        pity[str(user.id)]['rateUpPity'] = 0
                    else:
                        l = random.randint(1, 2)
                        if l == 1:
                            summon.append(random.choice(FiveSChar))
                            pity[str(user.id)]['rateUpPity'] = 0
                            pity[str(user.id)]['fiveGuarantee'] = True
                        else:
                            summon.append(random.choice(rateUpFiveStar))
                            pity[str(user.id)]['rateUpPity'] = 0
                            pity[str(user.id)]['fiveGuarantee'] = False
                if 200 < d <= 257:
                    if pity[str(user.id)]['fourGuarantee']:
                        summon.append(random.choice(rateUpFourStar))
                        pity[str(user.id)]['fourGuarantee'] = False
                    else:
                        e = random.randint(1, 2)
                        if e == 1:
                            summon.append(random.choice(FourSWep))
                        else:
                            summon.append(random.choice(otherFourStar))
                        pity[str(user.id)]['fourGuarantee'] = True
                else:
                    summon.append(random.choice(ThreeSWep))
        summon.sort()
        summon.reverse()
        summonList = "\n".join(summon)
        g = summon.pop(0)
        if "☆☆☆☆☆" in g:
            self.color = 0xeeff00
        else:
            self.color = 0xaf4dff
        pity[str(user.id)]['allTimeWishes'] += 10
        embed = discord.Embed(color=self.color, timestamp=datetime.utcnow())
        embed.add_field(name="Your Wish",
                        value=f"{summonList}\n\nRateup Pity = {pity[str(user.id)]['rateUpPity']}",
                        inline=False)
        embed.set_footer(
            text="Ganyu go brr",
            icon_url=f"{self.client.user.avatar_url}")
        pity[str(user.id)]['rateUpPity'] += 10
        with open('wishPity.json', 'w') as f:
            json.dump(pity, f, indent=4)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Wish(client))


