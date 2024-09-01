import streamlit as st
import pandas as pd
from io import StringIO
import requests

# Titre de l'application
st.title("Application avec Page de Connexion")

# Utilisateurs autorisés (exemple simple)
AUTHORIZED_USERS = {
    'admin': 'admin123',
    'user1': 'password1',
    'user2': 'password2'
}

# Fonction pour la vérification des identifiants
def check_credentials(username, password):
    return AUTHORIZED_USERS.get(username) == password

# Fonction pour obtenir l'adresse IP de l'utilisateur
def get_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        response.raise_for_status()
        return response.json()["ip"]
    except requests.RequestException:
        return None

# Variable d'état pour garder l'utilisateur connecté et stocker l'adresse IP
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user_ip' not in st.session_state:
    st.session_state.user_ip = get_ip()

# Affichage de la page de connexion si l'utilisateur n'est pas connecté
if not st.session_state.logged_in:
    st.subheader("Veuillez vous connecter pour accéder à l'application")

    # Formulaire de connexion
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    login_button = st.button("Se connecter")

    if login_button:
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Connexion réussie !")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
else:
    # Affichage de l'application principale après la connexion réussie
    st.subheader("Bienvenue dans l'application !")

    # Données intégrées directement dans le script
    data = """
    wayaye972,88.123.49.57
GosthNoAspect,176.140.21.165
L'arnck4801,109.13.162.56
zkewi 200iQ,90.89.111.57
Bosspendragon,91.166.170.69
zangetsu59110,81.66.12.219
buffetMicrobe53,93.27.167.218
MatthewH947,82.22.179.72
JK20019618,90.194.25.58
ProBossKizzy,2.28.25.34
Somerballss,77.103.83.229
joshy 20062016,82.46.135.228
ZFR MATEO#5229,90.1.147.20
CsXs3zq,93.10.173.6
CSL Nahaa,70.49.120.116
QCQCQC420,217.15.224.152
BlackWolf1494,198.16.226.26
Le pilote 64,80.9.29.215
tuc sniper4098,109.23.177.161
ptit gros,91.175.154.2
Lazar20Srb,176.136.68.174
Talkados563,86.216.145.62
Ethanv37912422,92.2.151.97
Mini skoobz,176.139.79.252
Idan allwood I,82.3.73.52
PSG BASTIEN,90.42.242.64
naruto99248,86.252.218.33
Benladeny1237,2.3.180.151
TAAO HERETIC,90.221.158.225
fxlipe420,87.176.56.41
YX YIIYZ XY,88.173.0.179
Il 3k ll,90.91.181.103
XgamerRenard,37.66.52.103
GG Marseille,89.94.130.10
PierreLuc09,209.169.143.60
qngt,90.3.186.196
velistu5446,90.108.177.140
wugo5046,90.110.108.57
eziobkil3569,83.205.243.82
jtebangbang,88.125.213.37
pechotacons,91.174.30.19
ragond,74.127.200.137
resnalyia,86.237.12.217
Matox925297,90.58.47.168
berettagang,82.64.151.181
MAXIBOOM59,85.168.188.99
kenzofj,77.148.121.31
Farm329jd,81.251.59.105
Eldrago891,109.215.202.203
Sl0anTdc,90.49.96.93
latefaun4661687,90.18.8.62
NYUN1A,128.78.27.168
SUMMER DRIFT674,78.122.31.117
Tr3iK0,176.132.169.59
C2B enzo,91.172.217.224
EL PAQUITO,91.165.225.171
SN NeKiZo,45.44.224.186
pécholamoula,88.173.140.166
MR Lebron J,88.174.24.128
PapaShark19,207.47.227.32
Evann74,88.181.139.100
Raye1302,88.120.208.62
Amperial AzaRiA,86.195.142.100
FreemodeGuys,91.171.172.26
kystashu,37.68.73.245
SOLOGNAC2864,91.175.76.13
tRIPzHayley,31.49.156.143
Formersky,94.12.198.114
Alvinpro2455,83.254.0.77
Dougs99,92.20.182.174
Fazelm7470,176.250.11.153
Xdcr3am6443,2.219.72.43
JBOX Robin,86.130.185.50
IngrownAnimal8,212.159.81.217
rubisrodrigo,212.194.181.21
HamiltronZz4880,91.168.33.64
SQUALE 360,82.142.18.226
SatinHydra46135,2.220.171.116
Marko3206,91.44.24.30
vosash,88.171.100.198
raph421927,88.174.148.67
GDOG5050,77.98.123.95
MassRossi46,188.5.193.173
qBlendiii,185.56.65.172
MTB GUY#6567,24.200.32.126
Bilixez28435,74.15.119.220
racturnia,70.80.29.166
Gxsaaq,90.45.30.15
MarineNv5712,176.155.107.38
juju 638847,88.177.25.193
titant man5523,86.250.86.6
Nathyx28,176.135.110.49
HOV destiny,77.202.107.94
Driss Omarri,94.109.234.54
TrophicTitan163,88.219.211.42
DJ D1rty dan,176.188.249.160
GTAlysia,46.69.206.168
RABIDhunter070,81.152.29.78
N4T4N4EL4889,86.214.185.131
InsanityMC3113,86.178.217.138
PLUNGERPIGGY,86.17.186.184
LyrikApfel875,2.243.151.88
Crapule60,169.155.250.161
Verizucker11,62.225.232.59
Croqmitaine,90.15.211.213
darklolo31,92.135.35.203
Enimatek94,78.193.158.73
KEKEjunior4876,194.183.208.119
Xerminyia,91.175.7.249
ZEY2064,109.223.24.84
piounette,92.128.49.113
Anacondas3599,88.126.206.71
XXlFluxylXX,91.163.65.78
smokeweed055023,173.178.9.131
Jeremymacd2,207.96.206.236
Driiixiiia,88.125.113.11
Mafiastentig,91.166.150.135
dannerfuser23,86.242.203.33
FrelonM,91.171.60.62
xX NORAK Xx,81.254.7.28
V R4Z3R V,88.127.74.53
SaClaque2,86.214.85.61
n2zh,92.157.53.108
Nidbart,90.0.49.85
XIVAMITSU2673,123.50.102.65
Emxkos,90.101.114.38
Parrain MGNO,90.55.15.105
XghostFuturX,213.44.39.104
Neonayaon,82.33.139.230
AshtonK1259,82.29.157.178
Black pro4276,86.176.161.73
lllbakhawlll,91.171.234.123
WIll624685,31.39.67.22
IIIII2229,90.114.218.218
Xl UPYOU lX,90.5.188.71
JimGamer189013,88.174.216.71
Ghost Midas7887,90.125.120.165
xuvizia,86.63.246.132
G5B miche55,92.138.55.8
Ezio Verttera,37.65.38.97
DressOne7832734,81.64.5.170
BossSteeve,89.89.62.57
CMDT NET0,31.32.177.50
Glory Hxy,86.204.114.216
lnsturnia,91.166.30.143
BOUFFERMAROUE,88.166.137.169
theovrn2,176.131.211.117
XdonooX,86.198.135.123
iiDraaKenii,37.65.22.92
Shadox5365,5.51.95.128
Fox5016,31.35.236.211
MARCO44270,86.214.146.85
l qTvrn l,90.22.46.64
ntxvmt76,90.70.169.10
il tpas Il,86.234.85.158
emixP33p,90.214.172.191
Louphanna,86.223.214.97
Malone9816,90.58.160.97
Trixilla7843,89.88.175.134
Lalan game9960,92.144.48.60
Tristan12009,77.202.28.122
ScorpionLZ7792,93.12.71.40
Rkg59,91.164.210.77
KingDodgepot,86.131.231.66
Papi8700,176.177.45.118
Grenat77,86.220.11.146
sweetyx9801,88.179.210.161
Julienbg1789,90.12.32.23
Gamereo12,88.177.86.183
Ryze9448,213.245.199.193
Faco186092,109.9.238.40
E9o8,91.174.100.152
w q x w q a,62.34.32.234
X VIP EvAn X,90.2.65.90
evixnia,90.3.149.94
LeSuperLoup,88.160.216.67
c8ramba3,95.168.10.72
paradisemeet,109.220.39.33
xwkf,86.63.246.202
QUXUZY,176.152.83.219
Vintaxi,81.49.86.135
Tenshotaki,91.168.70.99
LePierrot1805,89.3.8.236
Seteilui Z,176.174.126.120
magmax2582,92.188.175.17
s33vt,88.177.45.163
Cube5633,86.205.142.134
Flyk theo,87.89.191.177
Tank KV23971,86.236.79.56
SCRAPI SC1,185.109.173.130
cameron20105707,78.116.108.135
I Axya I,96.21.105.159
Jemal Partou,176.169.76.251
l Senor Juan,213.213.246.6
ABC QWeYRa,86.214.97.103
moha8160,88.168.113.207
I Juanito,35 89.81.57.94
aleex09Gamers,81.220.211.134
Ninja Melon8806,89.86.233.186
JuanMenandez,91.173.227.74
SoundBerry84973,86.147.10.4
Ahevu,88.120.149.138
E4o4Gamer88,90.7.39.197
BrianOconner768,92.158.160.102
PsYcHoThe2636,176.146.29.85
TsaBorz3502,176.146.29.85
XDserox,86.246.134.66
Ayd fan5555,92.40.190.39
Nutsy2010,90.200.46.157
ruellecachera,90.0.250.75
InheritorHD1,86.133.85.17
OH BLABLABLA,193.250.132.213
Polak3305,86.243.108.51
Buscape57,83.115.77.126
GrainedMirror17,176.183.239.33
XDonooX,86.198.135.123
Gouzie fr,81.53.116.135
d1 gmb,94.173.11.169
Dianelov98,92.17.58.207
DoMingoozoo67,86.243.210.64
DoMingoozoo67,86.243.210.64
MSTACKZZ8647,165.120.18.232
ki11ercreeperz,2.121.210.164
FordZMustang,83.233.97.21
JuicyTrout41704,81.141.151.111
Py0ojiT8418,92.26.147.197
Lol1296,90.195.165.26
OrXa84,193.248.143.163
Jack5827,92.26.207.140
grumpyCNT2361,92.15.50.238
ITz Twist3d Koi,86.233.249.247
xDYNAM1CxX4193,31.36.98.90
Oiuy1826,88.166.100.111
Powa 2334,176.182.173.130
Jiftq,88.126.206.44
MysT AzuR,37.65.177.38
II KXOB II,31.37.133.92
SilentTheHill,176.165.193.70
Faze Exotic9345,86.195.142.100
SeamedSeeker60,206.172.147.196
Quentinio137072,90.30.105.164
Le GAMER2253,82.65.117.206
Lama5846708,176.133.231.98
Cannular,82.66.196.20
megadozzzz,176.168.96.208
cobra mann5475,88.137.182.245
vantilation,88.137.182.245
MisterPlouk,91.205.43.147
Xyrieal,91.205.43.147
Pain7071,89.157.11.30
Loreso4632,93.5.246.11
G4B OKAY,109.27.160.16
Natsu 1017396,83.195.22.54
overmax300,91.172.137.208
TEI AONIME,90.23.3.244
Bryanbg71700,81.65.135.130
Gregoryr1783,176.133.219.162
zouzoulafleche,88.175.82.203
RZRdrago,109.210.136.76
vNxtexia IL,83.198.69.224
CZ aaron,86.209.12.6
ludoa27,88.166.74.37
F7 Fasen,176.136.43.138
Bigjess76,173.177.24.27
Moe Szyslak6978,89.88.153.186
xspectre666x,88.178.234.99
Classic Slea,81.251.73.9
Motard du 16313,92.128.37.123
Pavla12447,91.173.12.31
Kenza4533,88.173.237.200
Ronoa Zora4973,88.162.198.141
EntreeMur842176,92.157.65.135
Azvex Karma,88.161.13.199
Azvex Skeazy,62.34.123.23
Mathis 1325,176.155.126.107
Pot2Fluff,176.155.126.107
Blue lock3786,81.220.62.115
RedK1llerSK,31.10.174.222
Inzctif,92.148.61.68
DAY on 144HZ,91.167.0.151
Elf alyssia,92.148.61.68
JLlucas2583,91.169.57.161
BaD Boy 48184,90.29.27.137
I Noxlake I,89.87.205.221
I NoxIval I,88.142.209.32
LIL GAMBINO1502,176.179.40.235
DUCKI7556,92.140.30.216
Nk TouToun,86.211.9.206
Melinagta14,90.34.40.31
juju0102,176.163.99.75
Hyzsko,82.66.196.20
Lu20Ma09,77.196.231.144
Gwoerzltschii,5.44.120.36
Arsacolyte,93.7.197.139
DauntedJungle53,86.246.67.11
IWaRe Ryukl,37.66.47.119
Loveur2kefta,88.180.154.200
MisterBrise,31.32.177.50
CosinusTarte468,88.169.188.72
RCA WESKYZ,87.88.196.243
xXzerkikxX,88.167.230.8
GuudAim4You,91.171.49.80
XIIIXER,92.171.184.198
MisterBrise,31.32.177.50
Bastien66666,90.62.255.224
Yalqy 449,88.167.124.18
wassim34,89.84.181.189
EZR NiTox,88.177.33.133
OPss Nexus,88.163.84.179
Hevik3,91.160.94.238
Lestunter2157,88.125.113.11
Hunfire8513,90.22.244.33
Lokibul,86.241.86.4
MotorKarma29174,87.177.191.84
Anonymedu771291,31.39.162.170
Herbi6089,91.164.116.232
Magnum017237,86.192.23.171
Yann154467,91.169.28.194
US vYpeNokk,90.78.85.81
SneaxX7326,2.12.210.27
Rembook214,90.49.203.207
Cxcogameur,31.32.224.159
Yanisv16,88.127.160.142
kiwistar88,86.250.115.173
AMBRO00000,31.32.133.221
ruellecachera,90.0.250.75
vexaxy,31.37.241.153
esclxvage,92.158.82.104
super forssy,81.108.237.31
SkynsFreez,37.65.17.185
L'oncle Benz,109.223.163.235
YORKYFAMILY2871,91.160.157.30
PSR NaYzox,93.11.199.152
Terminator8758,89.84.24.206
MkTripleShoot,176.174.165.80
Warix fr5988,90.89.248.77
Drakus zorba,109.208.227.164
Yanouss9,109.222.25.120
Maxim3724,88.169.52.1
Mnu16,176.187.234.11
K4zu9816,88.180.158.199
N0gul x,88.172.108.161
Lepro344224,176.134.225.176
SolvedVeil1149,70.31.252.188
Leboug8519,86.217.108.70
RIDDICK9746452,165.169.229.89
Kerann25,92.130.183.151
ToxicVxpe6692,92.184.107.83
Deadly Fury,81.49.138.54
Le boss2368,176.165.20.13
FrostyYard94251,92.170.188.120
Jedu37,176.169.161.31
Ghost702092,90.120.78.24
NerroUWU6886,109.223.12.237
MATHEO083545,92.88.12.22
KsK XalWer,37.65.9.163
Zirox LD,37.65.46.27
CLY Mayeu,83.115.178.27
WQ16 XD3ED,81.251.86.72
WQ16 ADRI,176.160.169.214
Kly7574,176.151.135.201
I REZNYA I,92.184.110.16
Tatara667,90.78.83.92
Charlesgamers88,45.44.230.86
Galoux31,212.195.90.103
TsaBorz3502,176.148.209.101
Zoulow6392,90.66.94.68
gsc 135,84.101.242.219
Likoz1349,84.101.242.219
Theomo98,37.65.36.230
IEl Wualo x,87.88.142.21
Zoulow6392,90.66.94.68
Maytheg10,109.30.225.202
SERR DAV 77,176.171.217.80
E9o8,86.201.63.139
kDz Ghost,82.121.38.38
ShOot amau,176.132.115.222
Clan22222,77.201.38.18
DistantChunk421,37.66.62.177
ALLAH5312,86.140.175.198
isaftnr,91.12.88.90
Majo9403,84.182.250.161
UpwardSpiral1,176.249.192.206
JojolstLost1482,89.245.22.34
Harry4108,86.29.217.215
Youtubeur2479,88.165.224.160
Russia1062,88.170.116.91
RNL RORO,90.93.93.5
Darklight8345,91.170.26.169
MouSskoff,88.120.214.227
Kyle12342657,82.34.25.97
JimmoidJimmy,86.140.204.140
CheliABC123,78.149.231.32
ILSPIDERSIL,69.157.139.160
sTeeL x FrozEN,88.166.40.93
AMPKiller1819,2.4.97.138
serpent6943,88.170.249.236
Iz N3r0x Iz,90.79.72.165
Sosa x94,37.66.176.105
Sheeeeshez,78.113.7.163
Muushu6080,91.172.201.131
TTV PANDA4983,100.43.122.135
FigueMer4040313,70.53.209.162
JLshanks3177,91.163.201.38
Rubicara666,176.133.151.105
Le pro kenzi,37.66.176.105
vHxsw,176.187.41.180
Avitlair,86.228.14.39
ApexPunkill9899,89.89.161.161
TournadeauQC,24.37.42.162
Quentinio137072,90.30.105.164
YOUNG PIG 9728,142.183.237.76
Brokwchi,91.168.209.5
opiaces,88.184.137.239
BIG JEFF KILLER,38.128.228.61
Solopunk9658,77.130.173.34
Xxphanex52,88.163.127.40
Djib014,109.221.194.22
Le sapin66,207.236.112.112
niixo1007,86.192.203.4
Xotiic9593,166.48.221.25
Unrealzedr0x,184.161.224.66
Lol gty8862,212.195.178.60
Elite Kayzer,86.206.46.227
Unrealzedr0x,212.195.178.60
Rayandz787713,88.178.217.218
Super Patate 3,192.81.241.225
BossGangstaN,81.249.203.186
Taaikoo,92.142.221.59
DARKEN3645,37.65.118.248
VampyThrone1780,46.235.183.36
Kxn7t,213.245.123.24
Toti9322,76.69.196.86
Thayoox,94.239.181.251
AYOUB 779 YT,88.123.183.176
FOoLeK OsTyLe,88.177.145.134
Fretz682946,88.123.211.163
Mr Vertulia,109.140.177.170
piloose,2.9.177.247
Loup381915,157.208.9.162
Buscape57,83.115.77.126
nathan20152,170.249.33.136
DADAX59,104.200.81.174or86.223.246.129
ALEX2000XQc,142.126.24.88
GzYagami,88.183.241.153
Modz 7340,81.11.203.190
TxT Tony2292,96.23.229.223
Jeteezsegpa,62.35.49.229
No AIR x On RPG,91.174.71.22
bztm0rts,82.142.8.66
math5699,91.175.184.143
Ruben9716,90.65.97.43
II Tounss II,195.36.176.9
Xmickael84,90.73.94.197
Papi du 94,88.160.111.190
Goldentag8558,162.244.45.198
Twitch Caneton,91.170.147.163ChuteRagout2372
zMazato,88.162.247.146
Tchoupi6445,88.172.99.158
Raneyonn,88.172.99.158
TONTON OXI,88.164.240.6
Justiineee19,176.136.78.100
Salford773458,92.11.167.229
Harry74690,81.100.10.97
Grich8944,91.32.147.12
Uppedhen4,84.68.214.139
OllietheGreener,86.5.227.1
BurnleyBoy07,151.225.177.104
Grich8944,91.32.147.12
Cod174058,86.188.17.209
FaNaTiKZ3uS,176.152.244.177
CobraJulio74141,86.72.189.69
Cvbnhj,86.18.249.146
Foxy138709,86.139.149.176
GingrDangr,81.111.180.75
BlakeL18,51.194.94.157
ChuteRagout2372,90.220.74.117
darksyd00,91.172.16.173
Luca6777,176.158.217.138
Energydidou,88.176.29.131
DiCaprio925,92.138.45.18
IICryptoII581,31.36.230.229:1025
Cnx70ytb,88.178.109.89
LMMqr,92.159.188.12
Aaron94946826,88.164.240.6
IISV3II,2.11.172.185
Turtals2006,86.179.139.36
Corycarr92,78.148.38.171
Safz1203,94.195.168.197
HickoryArgent55,88.183.168.233
JadAyoKha007,88.160.191.62
CobraNinja67,90.19.166.83
Louloupnc,109.221.90.247
Sionalwun,94.4.51.187
silentsmoker1,90.198.175.24
Crowl3y19,94.8.71.199
Abel8633,81.183.88.96
FirexD3vil,86.238.62.214
Defaultkilla147,86.6.81.94
Zk762943,62.35.8.215
Mariusfnatic,91.169.87.56
Melolya,89.81.199.134
C2515,176.133.117.251
Bima972,2.3.50.75
Maxmathis44,88.160.206.179:24316
WilyDAVID,184.145.192.123
purplepoulet,212.195.178.60
Elite Kayzer,86.206.46.227
MuralLeader3271,37.68.99.127
mattou88,81.65.71.208:1412
MZ9 Mitsou,90.9.207.100
Hunfire8513,90.22.244.3381.65.71.208
Lucenzo245,37.67.25.208:24340
Docteur fox7812,91.174.202.140:46098
Fcswat mayvi,86.205.17.218
T1CameleonT1,176.148.49.106
Nezox6054,31.34.24.50
ManouskaFury,176.174.83.185
ZURG AKUMA,176.147.204.198
Gh0st flo28,90.107.12.127
Lamar3180,78.193.189.44
Nonogtapro78,90.25.126.32
Steph du 6,90.25.126.32
Batiste59B,90.29.155.1
ken flash1621,31.37.166.128
El Cazador3683,89.159.238.240
BlacK jus5337,209.142.87.232
Hendez01,2.223.61.196
Faonzazou2008,184.145.171.37
VrDr7447,142.183.237.132
CDN ClanDo6373,88.173.242.60
sousballon92,77.198.112.42
vL Alchimiia xX,78.252.137.133
LPB Hxpyy,135.19.234.114
Dark lord3598,217.39.56.227
fouinefouine501,88.160.126.132
yoyo87657275,74.59.159.9
Gw fuze4,86.235.244.24
Pro2719,37.66.55.68
Aopl5590,88.174.236.217
Guest King3800,109.220.206.13
XxGtahllnxX,2.10.16.11
Nisixx0908,92.158.158.104
PGX pm,176.183.227.163
tanguy596935,90.39.77.48
Kxnzy lv,96.21.34.23
BLS Teejay,90.62.44.153
X GoRiLle X,92.159.118.159
Droxz racing,91.86.104.178
Kitombo1939,90.29.52.217
W Ascohz,92.158.124.16
Sacha price,90.116.96.98
Makce6728,82.216.184.52
JongleurZero638,188.188.9.161
BRYAN 737626,88.173.17.36
Mongraal2804,37.66.149.66
saga7228,109.223.140.240
ludoa27,88.166.74.37
xXNounoursXx10,92.188.121.72
LEEEEEE REENARD,79.80.82.134
Diable573818,31.38.222.184
Lynaxo 095722,37.65.113.41
Mini mrlust9338,70.24.237.252
Will624685,31.39.67.22
Mexsysy2458,88.125.160.159:20758
SAW LOCKARIUS 2,86.195.58.81
Piyla3763,213.119.183.124
PouPou94z,91.161.213.14
Solo Kqyde,88.176.53.170
TiMercedes,184.146.234.17
XxKAIZER33xX,37.66.38.51:50734
x Maddock x,82.68.83.142
JGarner2000,51.241.172.168
LeGitanDu456588,176.147.166.54
l'empereur7,176.147.168.230
Le tombere,83.196.47.225
Unknown AJH,78.149.174.176
Pupuce507789,90.22.16.153
InfinitiMarc,45.149.183.252
ZzRipoker,88.171.18.41
legoax,90.0.98.108
M8Panther3342,88.181.132.209
italianoDTRR,88.122.165.131
Nyvle345,176.137.241.113
chemsou166168,105.100.117.73
x ezurixia x,109.27.114.107
couscous24,86.234.169.178
DukyOnsumin,88.127.94.234
Ara Away,88.127.94.234
Didi61190,90.22.66.147
The king594292,82.65.201.113
XxSangoohanxX,81.49.13.104
Richi2564,81.245.70.176
Nymixo2239,176.190.184.63
Gladiator48150,90.113.88.42
L3Noe,81.220.211.156
ClamantBird403,212.132.226.222
AS 3 ZER,86.214.19.121
VirtuoZ Tats Jr,89.80.220.77
OH BLABLABLA,90.50.90.103
MuralCoronet899,89.2.150.44
Victor4428220,86.227.28.172
xeqny,176.133.13.153
Xx2FAST4UxX2079,57.134.0.40
hero weed 2001,107.159.242.31
Le Rakoon,70.51.32.251
Mialakhalifier,70.48.125.220
Phoenixbio2490,45.47.200.77
DaggerTooth5073,71.70.203.225
Lizz7561,83.81.26.163
Oioiuk2019,86.133.2.203
XxMcGregorxX851,176.139.69.69
ICSmrb57,188.7.187.153
    """

    # Conversion des données intégrées en DataFrame
    data_io = StringIO(data)
    df = pd.read_csv(data_io, delimiter=',', header=None, names=['Nom d\'Utilisateur', 'Adresse IP'])

    # Vérifier si l'utilisateur connecté et son IP existent dans les données
    matched_user = df[(df['Nom d\'Utilisateur'] == st.session_state.username) & 
                      (df['Adresse IP'] == st.session_state.user_ip)]

    # Afficher un message seulement si une correspondance est trouvée
    if not matched_user.empty:
        st.success(f"Utilisateur {st.session_state.username} avec IP {st.session_state.user_ip} trouvé dans les données.")

    # Afficher les données sous forme de tableau
    st.write("Données importées:")
    st.dataframe(df)

    # Champ de texte pour le filtre de l'utilisateur
    filter_input = st.text_input("Recherchez par Nom d'utilisateur ou Adresse IP:")

    if filter_input:
        # Filtrer les données par nom d'utilisateur ou adresse IP
        filtered_df = df[df['Nom d\'Utilisateur'].str.contains(filter_input, case=False, na=False) | 
                         df['Adresse IP'].str.contains(filter_input, case=False, na=False)]
        st.write(f"Résultats pour '{filter_input}':")
        st.dataframe(filtered_df)
