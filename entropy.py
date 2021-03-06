import math

#https://stackoverflow.com/questions/990477/how-to-calculate-the-entropy-of-a-file
def retEnt(data):

    d = {}
    for n in data:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1

    retVal = 0.0
    for k, v in d.items():
        frq = float(v)/len(data)
        retVal -= frq * (math.log(frq) / math.log(2))

    return retVal

def isEnglish(words,quadDict):
        words2 = words
        words = words.replace(' ','')
        words = words.replace('!','')
        words = words.replace('.','')
        words = words.replace('?','')
        words = words.replace('-', '')
        words = words.replace("'", '')
        words = words.replace("\n", '')
        words = words.replace(",", '')
        words = words.replace('(', '')
        words = words.replace(')','')
        words = words.replace('/','')
        words = words.replace('[', '')
        words = words.replace(']','')
        wordScore = 0
        entScore = 0
        for quad in range(len(words)-3):
            wordQuad = words[quad:quad+4]
            if wordQuad in quadDict:
                wordScore+= (quadDict[wordQuad])
               
            else:
                wordScore += -11
        wordScore = wordScore/(len(words)-3)
        entScore = retEnt(words)
        if len(words2) > 300:
            words2 = words2[0:300]
        #print(f'word: {words2} | score: {wordScore} | entropy: {entScore}')
        if abs(abs(wordScore) - entScore) <= 1:
            return True
        else:
            return False
# with open(sys.argv[1], 'r') as file:
#     words = file.read()
# words = words.replace(' ','')

quadLines = open('quads.txt','r').readlines()
quadDict = {}

for i in quadLines:
    line = i.replace(' ','')
    line = line.replace('\n','')

    if  len(line)>0:
       
        line = line.split('-')
        quadDict[line[0]] = float(line[1])*-1
# count = 0
# for i in quadDict:
#     print(i)
#     if count >=15:
#         break
#     count +=1
sentences = ['Medical transcription, also known as MT, is an allied health profession dealing with the process of transcribing voice-recorded medical reports that are dictated by physicians, nurses and other healthcare practitioners. Medical reports can be voice files, notes taken during a lecture, or other spoken material. These are dictated over the phone or uploaded digitally via the Internet or through smart phone apps.'
, 'Hola! Yo empec?? aprendo Espa??ol hace dos mes en la escuela. Yo voy la universidad. Yo tratar estudioso Espa??ol tres hora todos los d??as para que yo saco mejor r??pido. ??Cosa alg??n yo debo hacer adem??s construir m?? vocabulario? Muchas veces yo estudioso la palabras solo para que yo construir m?? voabulario r??pido. Yo quiero empiezo leo el peri??dico Espa??ol la pr??xima semana. Por favor correcto alg??n la equivocaci??nes yo hisciste. Gracias! ',
, 'Le rouge est une couleur vive. C???est la couleur de nombreux fruits et l??gumes, comme les tomates, les fraises ou les cerises. Le jaune est la couleur des bananes, du ma??s ou des poussins par exemple. Le bleu est tr??s pr??sent dans la nature : c???est la couleur du ciel et de la mer. Le rouge, le jaune et le bleu sont les trois couleurs primaires.', 'jkohdkiuabikugblhlddaiulynbsukjgbhhhunkalkgjy bahulkbndcgkbjuywhouniladkgbyjiidainuhllwkhibugwdahuilnlndkibhuloaihlcjunjnkihbuyacdojahscinpullbhiudaoijnldkjhblncncwkjlhdkiubayyshduolkauyshbdkcuiiyahundhiluwhugiodunboywyuoilaoitbyuussdygubhcjkblskjbnladjknlsoauidiyuobbiuotybayuibgssdhgkjlhjknaccssjnihldshkljbboihbucbioyupioyubadioyubgdiguoywwhkbjlasbhkjdhbkjlaopwuidioubyasiotyuudyigbuashkbjludhkjblashkjblldjkghbvzbiyuhonosiboguyxxc ibugyyhblkucadgjhkvvbchuaokiokibwugyooduibhoagyjkchbuiodagybdiuohbcbaihbdusihboucibhduahbiuasghjkuhibadygbiouwwiudbohaigbcyuuuihbodwwcbihuogdihbuoaibwhgudhcbiuogksyjhukblashkbjdhkjlbawioudi7uauyidaukjlbskljdnhhahjlknssdhknjaiuhldiouwaygbkagkhnjsdkhjlnnauydoiny7usagygjkdyhnkljxkhngjlldkhnlankhludgukbjwwahnuioigbouysysdhunlbkkahnkjlwhnukldsuhkbllahkldwhknjllahunklsuhklbddahwjklbnbhjknlasbkhjlldhubnawhklhbkjlsgbdhubkahbkjlshdhbkjlbjknlxcnmbljkznmbl,xnlbcbhjklabhuwuibhdhubwhiuobqhkljbahljkbsjlkdohuiqiuobhbhugashbjknldjnklbfkhbjlbiugfhbukahbjlkdhgsjkshbkljybjgkdyublnadhbkjlwhkjblagjbksyuhbhgbkj'
,"""Qu?? piensas de espa??ol?
Pues...En realidad, no es mucho dif??cil, no es como mis amigos dicen; dicen que espa??ol es taaaaaaaan dif??cil, son (o est??n?) equivocado. Si sigue en las clases (que no ellos hacen), la aprendizaje no es un problema.

Solamente he estudiado espa??ol durante casi tres a??os ahora, y mira! Ya mi espa??ol es mas o menos! Puedo hablar un poco sin un diccionario, es bastante bien.

Pienso que voy a continuar estudiar espa??ol en la escuela secondaria tambien. Me pregunto qu?? bien mi espa??ol va a ser despu??s de tres m??s a??os de aprender este idioma. Tal vez/qu??zas (difference?) puedo hablar espa??ol con fluidez dentro de/en tres a??os? No s?? jajajajaaja.

Estoy escribiendo una carta a alguien/alguno no(?) ni existe, estoy muy raro... Pero no es importante porque estoy preparando para mi examen en espa??ol para jueves, y esa es m??s importante que mis pensamientos sobre me. Tengo que conseguir una A de mi nota, porque (lo/eso??) es mi semestre ??ltimo en la escuela primaria.
"""
,"In other problems, the objective is generating draws from a sequence of probability distributions satisfying a nonlinear evolution equation. These flows of probability distributions can always be interpreted as the distributions of the random states of a Markov process whose transition probabilities depend on the distributions of the current random states (see McKean???Vlasov processes, nonlinear filtering equation).[8][9] In other instances we are given a flow of probability distributions with an increasing level of sampling complexity (path spaces models with an increasing time horizon, Boltzmann???Gibbs measures associated with decreasing temperature parameters, and many others). These models can also be seen as the evolution of the law of the random states of a nonlinear Markov chain.[9][10] A natural way to simulate these sophisticated nonlinear Markov processes is to sample multiple copies of the process, replacin"]

print()
for i in sentences:
    i = i.upper()
    word = i
    if len(i) > 250:
        word = word[0:250]
    print(f'word: {word} | {isEnglish(i, quadDict)}')
    print()
    print()







#determine whether arb file contains english or gibb

