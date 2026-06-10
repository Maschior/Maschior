# Parse the user's ASCII art and measure its dimensions
raw_ascii = """
          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddddc1-----1rdddddddddddddddddddddddddddddddddddd          
          ddddddddddddddddddddddddddddddddddddZc1--------11-1rddJ/rrJddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddZZc/-<--1--11111/----1----11Jdddddddddddddddddddddd          
          ddddddddddddddddddddddddddddddZZJJr/---<<<-<--------1-<-----11rcdddddddddddddddddddd          
          ddddddddddddddddddddddddddddZJcr111-----<<<<<-<---------------1/JZdddddddddddddddddd          
          ddddddddddddddddddddddddddZJr/111--1---<--1111111--------------11cZddddddddddddddddd          
          dddddddddddddddddddddddddZc111-1111----1rJZZZZZJJccr/1------------/Zdddddddddddddddd          
          ddddddddddddddddddddddddJ11--11111/1-1cJZZZddddddddZZZZJr-<<<<<<---/Jddddddddddddddd          
          dddddddddddddddddddddddr1---11111//1/cJZdddddddddddddddZZJr1<<<<<<--1Jdddddddddddddd          
          dddddddddddddddddddddZ1---1111111///cJZZdddddddddddddddZZZJJ/-<<<<<--1Jddddddddddddd          
          ddddddddddddddddddddc1--11111111111rJJZdddddddddddddddddZZZJJr1<<<---1/Jdddddddddddd          
          dddddddddddddddddddc---11111111111/cJZddddddddddddddddZZZZZJJJc1<-<---1/Zddddddddddd          
          ddddddddddddddddddc---1111111-1111cJZZddddddddddddddddZdZZZZZJJr---<--1/cZdddddddddd          
          dddddddddddddddddc---111-1111--11rJZdddddddddddddddddddZZZZZJJJc/<---11//Zdddddddddd          
          ddddddddddddddddc----11-1111----/JZddddddddddddddddddddddZZZZJJcr-<---11/Jdddddddddd          
          dddddddddddddddJ1----1-111-----1/cccccrrrcJJZZddddddZZZZZdZZZZJcr-----11/cdddddddddd          
          ddddddddddddddZ-----1-1-1-------111------1//rJZZZZZZJccrr/rrccJcr1<----1/rZddddddddd          
          dddddddddddddZ1-------1----<--1rrccccr///////cJZZZJc/11------111/1<-1---1/Zddddddddd          
          ddddddddddddZ1-------1-------1/rcrrcrr/1//rrcJZddZJr//11/////111--<--<--//Zddddddddd          
          dddddddddddZc------------<-11/11/1----11/rrcJJZddZJ/1111/rrrrcrr/-<-----1/Zddddddddd          
          dddddddddddJr----------<--11///11rr111rrrcJJJZZddZJr/11----1//1//1-<<<--//Zddddddddd          
          dddddddddddJ1---------<--1/rrcJJcccrrrrcJJZZJZZdddZJccrr11/r1-1//1-<----//dddddddddd          
          dddddddddddc---------<--1/rJZZZZZZZZZZZZZZZZJZZddZZJccJcrrrrrrrrr/-<<---1cZddddddddd          
          dddddddddddc11-------<-1/cZZZdZddddZdZZZZZZZZZZdddZJJJJJZJJJJJJJc/-<<-<-/Jdddddddddd          
          dddddddddddJ/-------<<-/cZZZdZddddddddddZZZJZZZdddZZJJJJZZZZZZJJJr-<<-<-1Zdddddddddd          
          dddddddddddZ1-<----<<-1rJZZZdddddddZdZdZZZJZZZdddddZJJJZZZZZZZZZJc-<<<<-/ddddddddddd          
          ddddddddddd/1-<<---<<-1cZZZZdZddddddddZZZJZZJJJJZJJJcJJZZZZZZZZJJc-<<--</ddddddddddd          
          ddddddddddJr-<<----<<-/cJZZZddddddddZZZZZJc/11rrrrr///cZZZZZZZZZJc-<<---1Zdddddddddd          
          ddddddddddc/--<-----<-/cJZZZZZZdddddddddZZcrrr///11//rJZZZZZZZZJJc-<<----cdddddddddd          
          ddddddddddJc11--<<<-<-/JJZZZZZZdZdZdZddZZZJr///1//11/cJJZZZZZJJJJ/<-<--1-/cZdddddddd          
          ddddddJZZZJrr---<<<<--/JJZZZZZZZZZZZZJJcccrrrr///1/11/rJJZJJJZJJc1---<--11cZdddddddd          
          ddddddddrr/------<<<<</JZZZZZZZZZZJJcrrrccJccccJJJcrcrrrcJJJJJJcr-1/--1111rrJZdddddd          
          dddddddddddZc/111<<<<<-cJZZZZJZZZZJc/11///rrr//////11/r//rcJJJcc1-/1-/cZrcccccJJdddd          
          ddddddddddddddddJ-<<<<</JJZZZZZZZZJJJJZZZZJJJZJZZZJcc/1//rrJJccc<---rJdddZdZZJdddddd          
          ddddddddddddJddZr<<<<<<-rJJJJJJJZJZZZZZZZJJJccrrccJJJJJJJJJJccc1<--cZddddddddddddddd          
          ddddddddddddcr/1-<<<<<<-rrcJJJJJJJJZZZZZZZJccrrrrrrcccJJJJcccc/-1//cdddddddddddddddd          
          ddddddddddddZ/--<<<--<<-ccrccJJJJJJZZJZZZZZZZZZZJJJJJJJccccrr/<<<--1/r/cZZdddddddddd          
          dddddddddddddJ/--<----<-cccrrccccJJZZZZZZZZZdZZZZZZZZJJJccrr/<<<<<<<-/JZcZdddddddddd          
          dddddddddddddcr<-----<<-cJJcr//rccccJJJZJZJZJJZJZZZJJJJJr//-<<<<<<<1ccrcZddddddddddd          
          ddddddddddddZJr-</r-<<<-rJJJcrr/1////rccccJJJJJJJJcccrr/11-<<<<<<<-1cJZddddddddddddd          
          ddddddddddddZZJ1<-<<--<-rJJJJccr/1--11//rrrrcrrcrrr///1-1/-<<<--<-</rZdddddddddddddd          
          dddddddddddddddZr-------1cJJJJJcrr/-----111/111/1111---1r/<<<<<<---/Jddddddddddddddd          
          dddddddddddddZJ/---------/JJJJJJccr//1-<-------------1/rr/<<<<<--1JZdddddddddddddddd          
          ddddddddddc1<<------------1JJJJJJccrr///1---------11/rrrr1<<<<<<-----1rZdddddddddddd          
          ddddddddc1<<---------------1cJJJJccccrr/////1111////rrrr/1<<<<<-------<<--/cJZdddddd          
          dddZc111-<<-----------------1ccJJJccccrrr/////////rrcrr//-<<<<<-----1--<-<-----11rZd          
          r1-111---<<------------------1rcJJJcccrrrrr/////rrccrrr/1-<<<<---<<<<----<<---------          
          -11-------<-------------------1rccJccccrrrrrrrrrrccrrr//1--<<-<--<<<<<<---<---------          
          ----------<------------------<-1rcccccccrrrrrrrccccrr////1-<-<--<<<<<<<<---<--------          
          -------------------------<<<<<<--rcccccccccccccccccrrrrr/-<-<-<<<<<<<<<<<-----------          
          -----------<----------<<<<<<<<<<--rccJJccccccJJJJJcccccr1<---<<<<<<<<<<<<<----------          
          ------<-------------<<<<<<<<<<<<<<<1cJJJJJJJJJJJJJJJJJJ1-<<-<<<<<<<-----------------          
          ------------------<<<<<<<<<<<<<<<<<<--1JZZZZZZZZZZZZZJ1---<<-<<<<-------------------          
          -------<--------<<<<<<<<<<<<<--<<<<<<---1cZZZZdZZZZZJ/--<---<<<<--------------------          
          -------<-----<<<<<<<-------------<<<<<-----cZdZdZZZZ/-------------------------------          
          <--1----<--------------------------<<<-------rddddZ/--------<-----------------------          
          --<----------------------------------<<<<<<<---JZZr-------<-<-----------------------          
          ---<-1---<-----------------------------<<<<<<<<<1c----<<<<<-<-----------------------          
          ----<------------------------------------------<<---<<<<----------------------------          
          -----<-1--<---------------------------------------<<<<------------------------------          
          ------<-1---------------------------------------------------------------------------          
          ----------------------------------------------<-<-----------------------------------          
          -------<--------------------------------------<-------------------------------------          
          -----<--<-1-----------------------------------<-------------------------------------          
          ------<-<-------------------------------------<-------------------------------------          
          ------<<-------------------------------------<<-------------------------------------          
          <--<<--<<<------------------------------------<-------------------------------------          
          -<--<<-<<<------------------------------------<-------------------------------------          
          --<<<<<-<<------------------------------------<-------------------------------------          
          ---<<<<<<<------------------------------------<-------------------------------------          
          ----<<<<<<---<--------------------------------<-------------------------------------          
          --<-<-<<<<--<-<-------------------------------<-------------------------------------          
          <---<<<<<<<<-<<<------------------------------<<----------------------------------<<          
          <<<---<<<<<<<<<-<-<--<-------------------------<-----------------------------------<
"""

lines = [l for l in raw_ascii.split('\n') if l.strip()]
print(f"Number of non-blank lines: {len(lines)}")
max_len = 0
min_leading_spaces = 9999
for l in lines:
    max_len = max(max_len, len(l))
    spaces = len(l) - len(l.lstrip())
    if len(l.strip()) > 0:
        min_leading_spaces = min(min_leading_spaces, spaces)

print(f"Max length of raw lines: {max_len}")
print(f"Min leading spaces: {min_leading_spaces}")

stripped_lines = [l[min_leading_spaces:].rstrip() for l in lines]
new_max_len = max(len(l) for l in stripped_lines)
print(f"Max length after stripping {min_leading_spaces} spaces: {new_max_len}")
