import os,requests,json,random
from time import time

HEADER = """
>     ___________________________________     <                   
>>    |  _____ _____ _____ _____ ____   |    <<
>>>   | | __  |     | __  |   __|    \  |   <<<
>>>   | | __ -|  |  |    -|   __|  |  | |   <<<
>>    | |_____|_____|__|__|_____|____/  |    <<
>     |_________________________________|     <

an idea generator (scraper) by: 
*-> github: Florian7T
*-> discord: Florian#9999

"""

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def format_len(_s:str) -> str:
    a = len(_s)//64
    if a > 0:
        lst = 0
        sbstr = ""
        len_s = len(_s)
        for i in range(a):
            x = _s[lst+64:].find(' ')
            print(x,lst,_s[lst+64:])
            sbstr+=_s[lst:lst+64+x]+"\n"
            lst = x+64+lst
            if lst+64>len_s:
                sbstr+=_s[lst:]
                break
        return  sbstr
    return _s

def main():
    clear()
    print(HEADER)
    print("""1. random
2. what-to-code.com
3. sideproject-generator.com
4. joshuaraichur.com (easy)
5. appideagenerator.com (apps only)
x. exit
""")
    while True:
        opt = input('~> ')
        print()
        try: opt = int(opt)
        except ValueError:
            if opt == 'x':
                clear()
                exit(0)
            print(f'\'{opt}\' is not a valid option')
            continue
        s = True
        if opt == 1:
            print('this option is yet to be added')
        elif opt == 2: what_to_code()
        elif opt == 3: sideproject_gen()
        elif opt == 4: joshua_gen()
        elif opt == 5: app_idea_gen()
        else:
            print(f'\'{opt}\' is not a valid option')
            s = False
        if s: break
    main()

def what_to_code():
    clear()
    rq = requests.get(url='https://what-to-code.com/api/ideas/random')
    d = json.loads(rq.text)
    print("BORED - github.com/Florian7T\n")
    print('='*64)
    print(format_len(d['title'])+'\n')
    print('- '*32)
    print(f'likes: {d["likes"]} - id: {d["id"]}\n\nsrc: what-to-code.com')
    print('='*64)
    liked = False
    while True:
        o = input('[n]next [l]like [x]exit ~> ')
        if o == 'n':
            what_to_code()
            break
        elif o == 'l':
            lrq = requests.post(f'https://what-to-code.com/api/ideas/{d["id"]}/like')
            if lrq.status_code == 200 and not liked:
                print('succesfully likes the idea!')
                liked = True
            elif liked: print('you already left this idea a like!')
            else: print('failed to like the idea!')
        elif o == 'x':
            break

def sideproject_gen():
    clear()
    i=random.choice(range(0,l_sideproj))
    d=sideproj[i]
    print("BORED - github.com/Florian7T\n")
    print('='*64)
    print(format_len(d['title'])+'\n')
    print('- '*32)
    print(f'link: {d["link"]}\nidea: {i}/{l_sideproj}\n\nsrc: sideproject-generator.com')
    print('='*64)
    while True:
        o = input('[n]next [x]exit ~> ')
        if o == 'n':
            sideproject_gen()
            break
        elif o == 'x':
            break

def joshua_gen():
    clear()
    i=random.choice(range(0,l_joshua))
    d=joshua['ideas'][i]
    print("BORED - github.com/Florian7T\n")
    print('='*64)
    print(format_len(d['idea'].replace("<a href=\'",'').replace('</a>',')').replace('\'>',' ('))+(('\n'+format_len(d['description'])+'\n') if 'description' in d else '\n'))
    print('- '*32)
    print(f'type: {d["type"]} - idea: {i}/{l_joshua}\n\nsrc: joshuaraichur.com')
    print('='*64)
    while True:
        o = input('[n]next [x]exit ~> ')
        if o == 'n':
            joshua_gen()
            break
        elif o == 'x': break

def app_idea_gen():
    clear()
    rq = requests.get('https://appideagenerator.com/call.php')
    d=rq.text
    print("BORED - github.com/Florian7T\n")
    print('='*64)
    print(format_len(d.replace('\n',''))+'\n')
    print('- '*32)
    print(f'src: appideagenerator.com')
    print('='*64)
    while True:
        o = input('[n]next [x]exit ~> ')
        if o == 'n':
            app_idea_gen()
            break
        elif o == 'x': break
if __name__ == "__main__":
    brq = requests.get('https://www.sideproject-generator.com/projects.js')
    jrq = requests.get('http://joshuaraichur.com/ideagen/ideas.json')
    l_txt = len(brq.text)
    sideproj = json.loads(brq.text[15:l_txt-4]+brq.text[l_txt-3:]) # evil comma
    joshua = json.loads(jrq.text)
    l_sideproj = len(sideproj)
    l_joshua = len(joshua['ideas'])
    main()
