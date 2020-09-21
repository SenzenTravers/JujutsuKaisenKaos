import random
class Character:
    def __init__(self, name, nature):
        self.name = name
        self.nature = nature
    def myname(self):
        nom = f"{self.name}"
        return nom

class Room:
    def __init__(self, name, contenance = []):
        self.name = name
        self.contenance = []

    def movein(self, Character):
        if len(self.contenance) < 2:
                self.contenance.append(Character)
                print(f"Yay, {Character.name} moved in!")
    def moveout(self, Character):
        self.contenance.remove(Character)
        print(f"{Character.name} moved out!")
        
    def roommate(self, Character):
        if Character in self.contenance:
            if self.contenance[0] == Character:
                return self.contenance[1].name
            else:
                return self.contenance[0].name

    def interact(self):
        if len(self.contenance) == 0:
            return "  "
        elif len(self.contenance) == 1:
            soc_lonely1 = f"{self.contenance[0].name} is singing \"All by myself.\" By themselves. Alone."
            soc_lonely2 = f"{self.contenance[0].name} is having some healthy \"me\" time involving hot chocolate, nail care and a movie."
            soc_lonely3 = f"{self.contenance[0].name} is feeling like they're missing out on something."
            soc_lonely4 = f"{self.contenance[0].name} is reading old Gege Akutami's poems and mocking them. A fair revenge."
            soc_lonely5 = f"Meanwhile, {self.contenance[0].name} was all alone."
            soc_lonely6 = f"{self.contenance[0].name} is having some fun on their own. Whether it involves violent deaths or not, no one can say."
            soc_lon_suku = f"{self.contenance[0].name} is alone... Just kidding. He has a permanent pet-body owner to keep him company."
            soc_lon_yuji = f"{self.contenance[0].name} is alone... Just kidding. He has a permanent pet-mind parasite to keep him company."
            if (self.contenance[0] == itadori_yuji) or (self.contenance[0] == sukuna):
                lonelysuyu = [soc_lon_suku, soc_lon_yuji, soc_lonely1, soc_lonely2, soc_lonely3, soc_lonely4, soc_lonely5, soc_lonely6]
                return random.choice(lonelysuyu)
            else:
                lonely = [soc_lonely1, soc_lonely2, soc_lonely3, soc_lonely4, soc_lonely5, soc_lonely6]
                return random.choice(lonely)
        elif len(self.contenance) == 2:
            zero = self.contenance[0].name
            one = self.contenance[1].name
####################### ALLIES LINES #############################################
            alliemaid = f"{zero} took {one} to a maid café. They ate pancakes and took kawaii selfies. {one} may never recover."
            alliemaid2 = f"{one} took {zero} to a maid café. They ate anime-themed menus and took kawaii selfies. {zero} still hasn't come down from the sugar rush."
            alliemission = f"{zero} and {one} went on a mission together! It was a lovely bonding experience funded on solidarity through joint violence."
            alliemission2 = f"{one} and {zero} hunted foes together. {zero} got {one} a head trophy as a proof of good will and/or friendship and/or a flirting attempt. {one} is feverishly googling n\"sublte langauge cues HOW TO KONW FLIRRT???\" at the moment."
            alliesick1 = f"{one} got sick! {zero} cared for them until they got better, then they had sex and {zero} caught {one}'s cold. It was a valuable lesson about the power of hurt/comfort and quarantine."
            alliesick2 = f"{zero} got sick! {one} dumped their ass at the hospital. Then they became sex friends, but only after {zero} was cured. {one} is serious about health matters."
            alliedrunk = f"{zero} and {one} got very, very drunk. They might have slept together. Nobody knows for sure except Gojo, who got sealed before he could tell. {one} whimpers a little whenever they think about it."
            allieharajuku = f"{one} and {zero} visited Harajuku. {one} won a tentacle monster plushie at the pachinko."
            alliebully = f"{zero} bullied {one}."
            alliebitch = f"{zero} and {one} bitched about Gojo Satoru together."
            allieprof = f"{zero} and {one} are in a virtuous, healthy professional relationship."
            alliefriend = f"{zero} and {one} built a beautiful friendship. They are now friends since middle school."
            alliebracelet = f"{one}, possibly not in their right mind, offered friendship bracelet to {zero}, who might never recover for reasons either positive or negative."
            alliezoo = f"{zero} and {one} went to the zoo. {one} scared the bears, probably not on purpose."
            allietraining = f"{zero} and {one} fought for training purpose."
            allietraining2 = f"{zero} and {one} fought for hurting purpose."
            alliekill = f"{zero} killed {one}. Well."
            alliepic = f"For reasons nebulous for men and curses alike, {one} is currently in possession of naked {zero} pics. They are feeling an unexpected amount of distress from this fact."
            allies = [alliemaid, alliemaid2, alliemission, alliemission2, alliesick1, alliesick2, alliedrunk, allieharajuku, alliebully, alliebitch, allieprof,
                      alliefriend, alliebracelet, alliezoo, allietraining, allietraining2, alliekill, alliepic]
#################### ENEMIES LINES
            enebitch = f"{zero} and {one} bitched about Gojo Satoru together."
            enebully = f"{zero} bullied {one}."
            enebully2 = f"{one} bullied {zero} but {zero} got bored and left midway."
            enenose = f"{zero} bit {one}'s nose. Not 100% jujutsu-approved but certainly efficient."
            enegerman = f"{one} managed to German supplex {zero}, one of the tricks covered in what is called \"the Itadori Yuji's Ancestral Cursed Technique.\""
            enekill = f"{one} killed {zero}. I mean... yeah."
            enekick = f"{zero} killed {one}. They might have also kicked the body while they were at it."
            enefight = f"To the utter surprise of no one ever, {one} and {zero} fought."
            enewin = f"{one} and {zero} fought. {one} won. Yay! (?)"
            enemoral = f"{zero} and {one} fought. {one} lost but claims moral victory."
            eneaccident = f"{one} killed {zero} by sheer accident. They are currently trying their hardest to pretend it was on purpose."
            enekiss = f"{one} and {zero} did the \"kissing on accident because of a very well-timed fall\" thing. The most distressing thing about it is the fear of turning into shojo protagonists."
            eneslept = f"{zero} and {one} slept together. The world needs (?) more info about the incident."
            eneelope = f"{one} and {zero} eloped. They are now living happily as goats herders in Malaysia."
            enemarry = f"{one} and {zero} got married. There was a logic to it. There were reasons, convincing ones. It's just that nobody know what they are."
            enemies = [enebitch, enebully, enebully, enebully2, enenose,  enegerman, enekill, enekick, enefight, enewin, enemoral, eneaccident, enekiss,
                       eneslept, eneelope, enemarry]

##################################### GOJO
###ENEMY
            gojosurprise = f"Gojo killed {Room.roommate(self, gojo)}, to the surprise of no one."
            gojocry = f"Gojo bullied {Room.roommate(self, gojo)}. He definitely made them cry."
            gojoremains = f"To this day, {Room.roommate(self, gojo)}'s remains haven't been found."
            gojobully = f"Gojo bullied AND killed {Room.roommate(self, gojo)}."
            gojobadcop = f"Gojo played bad cop with {Room.roommate(self, gojo)}. Nobody played good cop."
            gojopat = f"Gojo patted {Room.roommate(self, gojo)}'s head. Then he killed them."
            gojocatch = f"Gojo played catch with {Room.roommate(self, gojo)} and caught every bit!"
            gojohelp = f"Gojo helped {Room.roommate(self, gojo)} become one with nature thanks to a healthy application of violence."
            gojosex = f"Gojo slept with {Room.roommate(self, gojo)}... Wait, what?"
            gojobully = f"Gojo bullied/fought {Room.roommate(self, gojo)}. Bullying and fighting are pretty much the same thing for him."
            gojocrush = f"Gojo crushed {Room.roommate(self, gojo)} and made it into a teaching moment."
            gojomilk = f"Gojo crushed {Room.roommate(self, gojo)} and bought himself a milkshake with their money."
            gojoelope = f"Gojo eloped with {Room.roommate(self, gojo)}, to the surprise of many -- {Room.roommate(self, gojo)} included."
            gojoenemy = [gojosurprise, gojocry, gojoremains, gojobully, gojobadcop, gojopat, gojocatch, gojohelp, gojosex, gojobully, gojocrush, gojomilk,
                         gojoelope, enekiss, eneaccident, alliebracelet, alliepic, alliezoo, alliemaid, alliemaid2, alliemission, alliesick2, allieharajuku,
                         allieprof, alliefriend,]            

######## GOJO ALLIES
            gojobullyfr = f"Gojo bullied {Room.roommate(self, gojo)}."
            gojoaffbully = f"Gojo affectionately bullied {Room.roommate(self, gojo)}."
            gojokind = f"Gojo was kind to {Room.roommate(self, gojo)}, but in an obnoxious way."
            gojonerves = f"Gojo got onto {Room.roommate(self, gojo)}'s nerves. He might have done it on purpose."
            gojonerves2 = f"Gojo got onto {Room.roommate(self, gojo)}'s nerves. He might have been oblivious about it."
            gojoslept = f"Gojo slept with {Room.roommate(self, gojo)}."
            gojodrunkd = f"Gojo got incredibly drunk with {Room.roommate(self, gojo)} and they slept together. Regrets might be had."
            gojofreloped = f"Gojo eloped with {Room.roommate(self, gojo)}, to the surprise of many -- {Room.roommate(self, gojo)} included."
            gojogreat = f"Gojo and {Room.roommate(self, gojo)} bonded while playing Monopoly! They became great friends. What an heartwarming news! Something awful is probably going to occur soon to balance it out."
            gojomyth = f"{Room.roommate(self, gojo)} hasn't seen Gojo once since they became roommates. They are beginning to suspect that Gojo is a myth."
            gojomurder = f"Gojo killed {Room.roommate(self, gojo)}. Well."
            gojoally = [gojobullyfr, gojoaffbully, gojokind, gojonerves, gojonerves2, gojoslept, gojodrunkd, gojofreloped, gojogreat, gojomyth, gojomurder]

## GOJO GETO
            gojonost = "Gojo and Geto reminisced about their school days. It was sad. They were sad. Everybody was sad."
            goge = "Gojo killed Geto. He'd have gotten drunk afterward but he doesn't drink, so he drank lemonade and bullied his colleagues instead."
            gogebubble = "Gojo and Geto gave up on fighting for the day and went to try out tapioca bubble tea. They hated it."
            gogekill = "Gojo killed Geto. I mean... well... yeah."
            gogemoral = "Gojo and Geto fought. Geto lost but claims moral victory."
            gogekiss = f"Gojo and Geto did the \"kissing on accident because of a very well-timed fall\" thing. They're mostly distressed about the fact it's such a shojo cliché."
            gogeslept = "Gojo and Geto slept together. The world definitely needs more info about the incident."
            gogeelope = "Gojo and Geto eloped. They are now living peacefully as a two-man mafia in Brazil."
            gogemarry = "Gojo and Geto got married. There was a logic to it. There were reasons, convincing ones. It's just that nobody know what they are."
            gojoget = [gojosurprise, gojosex, gojoelope, gojonost, gojomurder, goge, gogebubble, gogekill, gogemoral, gogekiss, gogeslept, gogeelope, gogemarry]

################### SUKUYUJI
            suyudrama = "In a fit of (justified) pettiness, Yuji watched two whole seasons of the worst korean soap opera known to man just to hear Sukuna scream."
            suyuheight = "Sukuna was mocking Yuji’s height when Yuji reminded him that it was his height, too. Sukuna has been sulking ever since."
            suyuarm = "Sukuna and Yuji were so bored that they tried to play arm wrestling with each other and got seriously hurt."
            suyuohno = "\"If you think about it, aren' you touching Sukuna every time you touch your own body?\" Nobara asked Yuji one day of boredom.\n Yuji and Sukuna's sex life never recovered."
######################### SUKUMEGUMI
            sumecoffee = f"To the utter surprise of no one ever, {one} and {zero} fought. The wager was that they'd have a date if Sukuna won. The issue was obvious, but Megumi did get free coffee out of it."
            sumesaved = "Megumi was fighting a difficult opponent when Sukuna swooped in, defeated the guy and princess carried Megumi to safety despite Megumi's legs working perfectly fine."
            sumerevenge = "Yuji was fighting a difficult opponent when Megumi swooped in, helped him defeat the guy and insisted until Yuji let him princess carry him to safety just to make a point to Sukuna. Sadly, he couldn't carry Yuji more than two meters before his arms gave out."
            sumebully = "Sukuna keeps staring at Megumi just to bully him. It works quite well."
            sumebully2 = "Megumi keeps ignoring Sukuna just to bully him. It works quite well."
            sumeuraume = "Megumi was going to sleep when he heard a noise under his bed. He checked and met Uraume's unblinking gaze.\n Megumi didn't sleep that night."
            sume = [sumecoffee, sumesaved, sumerevenge, sumebully, sumebully2, enebitch, alliepic, enenose, enefight, eneaccident, enekiss, eneslept, enemarry, sumeuraume]
########################### VARIOUS CHARACTER LINES
## SUKUNA
            sukubully = f"Sukuna killed {Room.roommate(self, sukuna)}, to the surprise of no one."
            sukucry = f"Sukuna bullied {Room.roommate(self, sukuna)}. He definitely made them cry."
            sukuremains = f"To this day, {Room.roommate(self, sukuna)}'s remains haven't been found."
            sukubully2 = f"Sukuna bullied AND killed {Room.roommate(self, sukuna)}."
            sukubadcop = f"Sukuna patted {Room.roommate(self, sukuna)}'s head comfortingly. Then he killed them."
            sukucatch = f"Sukuna played catch with {Room.roommate(self, sukuna)} and caught every bit!"
            sukunature = f"Sukuna helped {Room.roommate(self, sukuna)} become one with nature thanks to a healthy application of violence."
            sukusleep = f"Sukuna slept with {Room.roommate(self, sukuna)} and didn't even kill them afterwards??"
            sukusleep2 = f"Sukuna slept with {Room.roommate(self, sukuna)} and didn't even kill them afterwards. Uraume did, though."
            sukuelope = f"Sukuna eloped with {Room.roommate(self, sukuna)}, to the surprise of many -- {Room.roommate(self, gojo)} included."
            sukudisappoint = f"Sukuna almost killed {Room.roommate(self, sukuna)} before Yuji managed to take ovr. He's currently whining about the unfairness of life and the lowliness of brats in a corner of Yuji's head."
            sukunareac = [sukubully, sukucry, sukuremains, sukubully2, sukubadcop, sukucatch, sukunature, sukusleep, sukusleep2, sukuelope, sukudisappoint]
## CHOSO
            chosoignore = f"{Room.roommate(self, choso)} talked for quite a long time before they realized that Choso was to busy thinking about his brother to listen."
            chosoyuji = f"When talking about his brothers, Choso spoke about \"Yuji, one of the youngest\". {Room.roommate(self, choso)} started googling \"Alzheimer death painting curse human hybrids\" but gave up when they realized what they'd just typed."
            chosostanding = f"Choso didn't fight with {Room.roommate(self, choso)}. He didn't play nice either: he just didn't care.\n{Room.roommate(self, choso)} might have prefered a fight, for their ego's sake."
            chosocompany = f"Choso isn't the most proactive ally, but {Room.roommate(self, choso)} like that they can talk about anything and everything with him. Granted, it's because he doesn't care, but still."
            chosoharlequin = f"Choso pinned {Room.roommate(self, choso)} against a wall and swept them in a passionate, feverish kiss. {Room.roommate(self, choso)} and the natural world's order may never recover."
            chosolight = f"{Room.roommate(self, choso)} thought that Choso was showing a facial expression, but it was just a trick of the light."
            chosoally = [chosoignore, chosostanding, chosocompany, chosoyuji, chosoharlequin, chosolight]
            chosoenemy = [chosoignore, chosostanding, chosoharlequin, chosolight]

## DAGON
            dagonbloub = f"Dagon talked to {Room.roommate(self, dagon)} for a while. He told them important things – untold truths not to be forgotten – secrets only the sea could hold. Halas, since Dagon only speak in cute sea-ish noises, {Room.roommate(self, dagon)} didn't understand a single thing. Still, they feel somewhat enlightened."
            dagonbubble = f"Dagon played bubbles with {Room.roommate(self, dagon)}. It was very fun! Afterwards, they ate people."
            dagonbook = f"{Room.roommate(self, dagon)} caught Dagon watching deep sea documentary with singular intensity. {Room.roommate(self, dagon)} is trying not to think too hard about it."
            dagonally = [dagonbloub, dagonbubble, dagonbook]

## TOJI
            tojiflex = f"In a fit of hubris, {Room.roommate(self, fushiguro_toji)} asked Toji to flex as hard as he could. Toji obliged. The universe never recovered."
            tojipay = f"{Room.roommate(self, fushiguro_toji)} was about to be killed by Toji when they offered money against their life. Toji accepted for 400 yens and a sandwich."
            tojidestroy = f"{Room.roommate(self, fushiguro_toji)} was never heard from again."
            tojiied = f"{Room.roommate(self, fushiguro_toji)} got Toji'ed to death."
            tojisurvive = f"{Room.roommate(self, fushiguro_toji)} managed to survive Toji by offering him cute Megumi pics. They fled before he thought to ask why they had them."
            tojienemy = [tojiflex, tojipay, tojidestroy, tojiied, tojisurvive]
            tojiflee = "Megumi duelled Toji for parental acountability and somehow won, possibly because of a freak accident or something."
            tojifight = "Megumi tried his best to land a punch on Toji but failed. Toji found it very cute, though."
            tojipassive = "Megumi keeps staring hard at Toji. Toji keeps trying just as hard to pretend he doesn't notice."
            tojibaddad = [tojiflee, tojifight, tojipassive]

## MEGU
            megubother = f"Megumi was peacefully reading his book when {Room.roommate(self, fushiguro_megumi)} came to put some ADVENTURE in his boring life. They tried telling him he should feel lucky but so far, he remains unconvinced."
            megupet = f"{Room.roommate(self, fushiguro_megumi)} wouldn't stop bothering him until he accepted summoning his shikigami so {Room.roommate(self, fushiguro_megumi)} could pet them."
            meguread = f"{Room.roommate(self, fushiguro_megumi)} tried taking a peek at Megumi's latest read. Turns out it was an overly depressing nonfiction book about japanese urbanization. {Room.roommate(self, fushiguro_megumi)} is appalled."
            megually = [megubother, megupet, meguread]

## HANAMI
            hanatalk = f"With odd gentleness, Hanami spoke about the importance of mass human genocide to the planet's survival. {Room.roommate(self, hanami)} remains unconvinced but it was all put quite politely so that's something, at least?"
            hanaflower = f"Hanami offered {Room.roommate(self, hanami)} a flower. {Room.roommate(self, hanami)} is more touched than they let on."
            hanagarden = f"{Room.roommate(self, hanami)} woke up to a gorgeous bed of flowers all around their bed. To this day, they still don't know if it's a gift, a threat, or both." 
            hanaally = [hanaflower, hanagarden]
            hanaenemy = [hanatalk, hanagarden]
## INO SPOILED BY NANAMI
            inobb = "Nanami patted Ino's head! Ino is thinking about framing that balaclava as a keepsake."
            inospoil = [inobb]
## YUJI
            yujibibou = f"Today, once again, Itadori Yuji was a cinnamon roll. {Room.roommate(self, itadori_yuji)} fought off the unexpected urge to pat his head."
            yujitour = f"Itadori Yuji dragged {Room.roommate(self, itadori_yuji)} to a Tokyo tour. Somehow, he managed to get them both lost."
            yujicook = f"Itadori Yuji started cooking everyday for {Room.roommate(self, itadori_yuji)} and him. {Room.roommate(self, itadori_yuji)} quietly add this as one more reason to petition for his survival."
            yujihear = f"{Room.roommate(self, itadori_yuji)} heard Yuji trying to scold an enemy and just... patted his head and pinched his cheeks. The poor boy tries so very hard."
            yujiangry = f"{Room.roommate(self, itadori_yuji)} made Yuji so angry, he punched a wall. {Room.roommate(self, itadori_yuji)} would have gloated, except he realy broke the wall rather than his hand."
            yujibully = f"{Room.roommate(self, itadori_yuji)} bullied Yuji. Sukuna also bullied Yuji. It was a good bonding experience."
            yujiwrestle = f"{Room.roommate(self, itadori_yuji)} challenged Itadori Yuji to an arm wrestling match. They changed their mind half a second into the match, but it was already too late for their arm."
            yujially = [yujibibou, yujitour, yujicook, yujihear]
            yujienemy = [yujiangry, yujibully, yujiwrestle]
## NOBARA
            nobshopping = f"Nobara dragged {Room.roommate(self, kugisaki_nobara)} for a shopping session. It's been one day, but their friends and family are still confident."
            nobnice = f"Today, Nobara was lovely and sweet toward {Room.roommate(self, kugisaki_nobara)}. It rattled them so much they took her to a check-up."
            nobjudge = f"Nobara and {Room.roommate(self, kugisaki_nobara)} spent a chill day doing people-watching and people-judging. It wasn't a competition but Nobara won anyway." 
            nobpretty = f"Nobara and {Room.roommate(self, kugisaki_nobara)} fought. Nobara would like to point out that she looked very fashionable and stylish while they did so."
            nobbully = f"Nobara trashtalked {Room.roommate(self, kugisaki_nobara)} into a fight, and nobody expected any less from her."
            noboffense = f"{Room.roommate(self, kugisaki_nobara)} immensely offended Nobara by calling her \"not that unsufferable when you get to know her.\n"
            nobally = [nobshopping, nobnice, nobjudge]
            nobenemy = [nobpretty, nobbully, noboffense]

## MAHITO
            mahfriend = f"Mahito spoiled {Room.roommate(self, mahito)} with gift made from transfigured humans. {Room.roommate(self, mahito)}... appreciated it?"
            mahfrbully = f"Mahito bullied {Room.roommate(self, mahito)}, but in an affectionate way."
            mahmonopoly = f"Mahito and {Room.roommate(self, mahito)} played an unholy amount of board games."
            mahenth = f"Mahito and {Room.roommate(self, mahito)} fought. Mahito showed his appreciation for his foe through mental torture, as you do."
            mahvex = f"Mahito fought with {Room.roommate(self, mahito)} and was rude enough to keep talking about Itadori Yuji while they did! At least, he was polite enough to offer excuses when {Room.roommate(self, mahito)} expressed their frustration.\nHe still didn't stop, though."
            mahnerv = f"Mahito got on {Room.roommate(self, mahito)}'s nerves, probably on purpose."
            mahnerv2 = f"Mahito got on {Room.roommate(self, mahito)}'s nerves without even trying."
            mahflirt = f"Mahito may have flirted {Room.roommate(self, mahito)}. Unless he was just being an innocent unnerving creep. Or both."
            mahsex = f"Mahito slept with {Room.roommate(self, mahito)}, which went as surprisingly as sex can go with a sociopathic shapeshifter. It may have felt... good? Room.roommate{(self, mahito)} is waiting to be able to form complete sentences again before they pass judgement on that one."
            mahally = [mahfriend, mahnerv, mahnerv2, mahfrbully, mahmonopoly, mahsex, mahflirt]
            mahenemy = [mahenth, mahnerv, mahnerv2, mahvex, mahflirt]
## MEIMEI
            meipraise = f"Mei Mei told {Room.roommate(self, meimei)} they were worth good money. Coming from her, it's technically great praise! {Room.roommate(self, meimei)} hesitates to ask how much exactly."
            meievening = f"Mei Mei and {Room.roommate(self, meimei)} spent a lovely evening out. It almost felt like a date, especially with Ui Ui glaring daggers at {Room.roommate(self, meimei)} for the whole evening."
            meimeaxe = f"As they fought, {Room.roommate(self, meimei)} requested the autorization to \"axe a question\" to Mei Mei. They died shortly afterward but it was worth it."
            meially = [meipraise, meievening]
            meienemy = [meimeaxe]

## MIWA
            miwacute = "Today, as always, Miwa was adorable and perfect. Sorry, {Room.roommate(self, miwa)}, you can't compare."
            miwacurse = f"Miwa and {Room.roommate(self, miwa)} hacked curses to pieces and drank tapioca bubble tea. They had a great, wholesome time."
            miwatried = f"{Room.roommate(self, miwa)} pranked Miwa into thinking they were only mean because of a sad childhood."
            miwally = [miwacute, miwacurse]
            miwenemy = [miwatried]
            
## TODO
            todoffend = "{Room.roommate(self, todo)} and Todo fought, but Todo left midway for one of Takada's exclusive meet-up events. {Room.roommate(self, todo)}'s pride still hasn't recovered to this day."
            todomind = "Todo clapped and mindfucked his way to victory against {Room.roommate(self, todo)}. The defeat in itself would sting bad enough, but it's the fact that they lost a battle of mind against that guy that really makes {Room.roommate(self, todo)} scream in their pillow."          
            todenemy = [todoffend, todomind]
## URAUME
            urabar = "Uraume and {Room.roommate(self, uraume)} spent the evening at a bar. Uraume mostly complained drunkenly about Megumi."
            uralose = "Uraume and {Room.roommate(self, uraume)} fought. Uraume spent the whole fight disdainfully claiming that Sukuna would have done better, fuelling {Room.roommate(self, uraume)} to victory through sheer frustrated humiliation."
            urastalk = "Uraume spent a happy day trailing Sukuna everywhere he went!"
            urafrust = "Uraume spent a frustrating day trailing Sukuna and Megumi everywhere they went!"
            uraally = [urastalk, urafrust]
            uraenemy = [urabar, uralose]
            
##############" Gojo reactions
            if (self.contenance[0].nature != self.contenance[1].nature) and (gojo in self.contenance):
                return random.choice(gojoenemy)
            elif (self.contenance[0].nature == self.contenance[1].nature) and (gojo in self.contenance):
                return random.choice(gojoally)
########## Sukuna reactions
            elif (sukuna in self.contenance) and (itadori_yuji in self.contenance):
                sukunayuji = [suyuohno, suyuarm, suyuheight, suyudrama, enebully, enebully2, enemoral, eneaccident, enemarry, eneslept]
                return random.choice(sukunayuji)
            elif (sukuna in self.contenance) and (fushiguro_megumi in self.contenance):
                return random.choice(sume)
            elif (sukuna in self.contenance) and (self.contenance[0].nature == self.contenance[1].nature):
                return random.choice(allies)
            elif (sukuna in self.contenance) and (fushiguro_megumi not in self.contenance):
                return random.choice(sukunareac)

################# Getwo reactions
            elif (getwo in self.contenance):
                getworeac = allies+enemies
                return random.choice(getworeac)

################## Random
            elif (fushiguro_toji in self.contenance) and (fushiguro_megumi in self.contenance):
                family = allies + megually + tojibaddad
                return random.choice(family)

################## Allies reaction
            elif self.contenance[0].nature == self.contenance[1].nature:
                allytemp = allies
                if choso in self.contenance:
                    allytemp = allytemp + chosoally
                if dagon in self.contenance:
                    allytemp = allytemp + dagonally
                if fushiguro_megumi in self.contenance:
                    allytemp = allytemp + megually
                if hanami in self.contenance:
                    allytemp = allytemp + hanaally
                if (ino in self.contenance) and (nanami in self.contenance):
                    allytemp = allytemp + inospoil
                if itadori_yuji in self.contenance:
                    allytemp = allytemp + yujially
                if kugisaki_nobara in self.contenance:
                    allytemp = allytemp + nobally
                if mahito in self.contenance:
                    allytemp = allytemp + mahally
                if meimei in self.contenance:
                    allytemp = allytemp + meially
                if miwa in self.contenance:
                    allytemp = allytemp + miwally
                if uraume in self.contenance:
                    allytemp = allytemp + uraally
                return random.choice(allytemp)



            elif self.contenance[0].nature != self.contenance[1].nature:
                enemytemp = enemies
                if choso in self.contenance:
                    enemytemp = enemytemp + chosoenemy
                if fushiguro_toji in self.contenance:
                    enemytemp = enemytemp + tojienemy
                if hanami in self.contenance:
                    enemytemp = enemytemp + hanaenemy
                if itadori_yuji in self.contenance:
                    enemytemp = enemytemp + yujienemy
                if kugisaki_nobara in self.contenance:
                    enemytemp = enemytemp + nobenemy
                if mahito in self.contenance:
                    enemytemp = enemytemp + mahenemy
                if meimei in self.contenance:
                    enemytemp = enemytemp + meienemy
                if miwa in self.contenance:
                    enemytemp = enemytemp + miwenemy
                if todo in self.contenance:
                    enemytemp = enemytemp + todenemy
                if uraume in self.contenance:
                    enemytemp = enemytemp + uraenemy
    
                return random.choice(enemytemp)
        else:
            pass


########## CHARACTERS & ROOMS
choso = Character("Choso", "Curse")
dagon = Character("Dagon", "Curse")
fushiguro_toji = Character("Fushiguro Toji", "Zombie")
fushiguro_megumi = Character("Fushiguro Megumi", "Shaman")
geto = Character("Geto Suguru", "Curse user")
getwo = Character("Getwo Suguru", "?")
gojo = Character("Gojo Satoru", "Shaman")
hanami = Character("Hanami", "Curse")
ieri_shoko = Character("Ieri Shoko", "Shaman")
ino = Character("Ino Takuma", "Shaman")
inumaki = Character("Inumaki Toge", "Shaman")
itadori_yuji = Character("Itadori Yuji", "Shaman")
jogo = Character("Jogo", "Curse")
kugisaki_nobara = Character("Kugisaki Nobara", "Shaman")
mahito = Character("Mahito", "Curse")
mechamaru = Character("Mechamaru", "Shaman")
meimei = Character("Mei Mei", "Shaman")
miwa = Character("Miwa Kasumi", "Shaman")
nanami = Character("Nanami Kento", "Shaman")
okkotsu_yuta = Character("Okkotsu Yuta", "Shaman")
panda = Character("Panda", "Shaman")
sukuna = Character("Sukuna", "Unknown")
todo = Character("Todo Aoi", "Shaman")
uraume = Character("Uraume", "Unknown")
utahime_iori = Character("Utahime Iori", "Shaman")
yoshino_junpei = Character("Yoshino Junpei", "Shaman")
yu_haibara = Character("Yu Haibara", "Shaman")
zenin_mai = Character("Zenin Mai", "Shaman")
zenin_maki = Character("Zenin Maki", "Shaman")
ijichi_kiyotaka = Character("Ijichi Kiyotaka", "Shaman")


room1 = Room("A beautiful penthouse")
room2 = Room("An ugly penthouse ):")
room3 = Room("A cult-funded villa")
room4 = Room("An ex-temple")
room5 = Room("A decrepit flat")
room6 = Room("A flat in Shibuya")
room7 = Room("A house (haunted?)")
room8 = Room("A house (haunted!)")
room9 = Room("Dagon's cool beach resort")
room10 = Room("A Tokyo student's room")
room11 = Room("An ex-flat in Shibuya")
room12 = Room("A private shrine")
room13 = Room("A mountain ryokan")
room14 = Room("A rental in Okinawa")
room15 = Room("A house in Malaysia")

sdf = [choso, dagon, fushiguro_megumi, fushiguro_toji, geto, getwo, gojo, hanami, ijichi_kiyotaka, ino, inumaki, itadori_yuji, jogo, kugisaki_nobara, ieri_shoko, mahito, mechamaru, meimei, miwa, nanami, okkotsu_yuta, panda, sukuna, todo, uraume, utahime_iori, yoshino_junpei, yu_haibara, zenin_mai, zenin_maki]
persos = [choso, dagon, fushiguro_megumi, fushiguro_toji, geto, getwo, gojo, hanami, ijichi_kiyotaka, ino, inumaki, itadori_yuji, jogo, kugisaki_nobara, ieri_shoko, mahito, mechamaru, meimei, miwa, nanami, okkotsu_yuta, panda, sukuna, todo, uraume, utahime_iori, yoshino_junpei, yu_haibara, zenin_mai, zenin_maki]
rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12, room13, room14, room15]

