# Parse the new cropped ASCII art and measure its dimensions
raw_ascii = """
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
          ddddddddddddddddddddddddddddddddddddddddr/----/Zdddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddc1--------11-1rddZrrcJddddddddddddddddddddddddd          
          ddddddddddddddddddddddddddddddddZZJc1-<-<1---11111----1---1-1cdddddddddddddddddddddd          
          ddddddddddddddddddddddddddddddJJJc/1----<<<<-<--<---1-------1-/rZddddddddddddddddddd          
          dddddddddddddddddddddddddddZcr/111-1---<<----------------------1rZZddddddddddddddddd          
          dddddddddddddddddddddddddZZ/111-11----<-1/ccJccrr//1-------------1cddddddddddddddddd          
          ddddddddddddddddddddddddd/11-11111/1-1rJZZZdddddZddZZZJc/-<<<<<<---1Zddddddddddddddd          
          dddddddddddddddddddddddr----1/1111/1/cJZdddddddddddddddZZJc1<<<<<<--1cdddddddddddddd          
          dddddddddddddddddddddJ----1111/11///cJZZddddddddddddddddZZJJr-<<<<<--1rddddddddddddd          
          dddddddddddddddddddd/---111111111/1rJZZddddddddddddddddZZZZJJc/-<<<---1rdddddddddddd          
          ddddddddddddddddddd1--111111111111rJZZddddddddddddddddddZZZZJJJr-<-<--1/cddddddddddd          
          dddddddddddddddddZ---11111111--11/JZZddddddddddddddddddZZZZZZJJc/<---1-1/Zdddddddddd          
          ddddddddddddddddJ----11-1111----/JZddddddddddddddddddddddZZZZJJcr-<---11/cdddddddddd          
          dddddddddddddddJ-----1-111-----1/rccrrr/rrJJZZddddddZZZZdZZZZZJJr1<----11cZddddddddd          
          ddddddddddddddc-----1--1--------1111-----11//cZZZZZZcrr//1//rrrcr1<-1--1/rZddddddddd          
          dddddddddddddr-------1-----<--/rcJJJJcr///rrrJZZdZJr/111-------111<-1---1rZddddddddd          
          ddddddddddddr-------1----<-1-////cr111////rrcJZddZJr/1111/rcccr/11<--<--//Jddddddddd          
          dddddddddddcr-----------<--1//11-/r---rr//JJJJZddZJr//--1--1r////1<-----11Jddddddddd          
          dddddddddddJ1---------<--1/rrccJccrrrcrcJJZZZZZdddZJccrr1-/r1-1///-<<---1/Zddddddddd          
          dddddddddddc11-------<<-1/cJZZZZZZZZZZZZZZZJJZZdddZJccJJrr/rrrrrr/-<<---1/Jddddddddd          
          dddddddddddc11------<<-1rJZZdddddddddZdZZZZZZZZZddZZJJJJZZZJJJJJcr-<-<<-1Zdddddddddd          
          dddddddddddZ/-------<<1rJZZZZdddddZdZdddZZJJZZZddddZJcJZZZZZZZZZJc1<<-<--ddddddddddd          
          dddddddddddc--<----<--1cZZZddZdddddddddZZJZZZJZZZZZZJJJZZZZZZZZZJJ1<<<-<1ddddddddddd          
          ddddddddddZ/-<-<---<<-/cJZZZdddddddddZZZZJc/--rcrrrrrrcZZZZZZZZJJJ1<<-<--ddddddddddd          
          ddddddddddc/1-<-----<-/cJZZZZZZddddddddZZZcrrrr//11/1rJZZZZZZZZZJc-<<--1-1dddddddddd          
          ddddddddddcJ/1--<<<-<-/JJZZZZZZdZdZZdddZZZJr///1//111cJJZZZZZJJJJr<<----1-rZZddddddd          
          ddddddd/Zrr1---<-<<<<</JJZZZZZZZZZZZJcccrccccJccrrr////rJZJZJJJJc----<-1-1rZdddddddd          
          dddddddddJr1----1-<<<</JJZZZZZZZZZJcr//rc///rrrrrr///rrcrccJJJccr<//--c//cr/JJZZdddd          
          dddddddddddddddZr-<<<<rJJZZZZZZZZJcccJJJJJZZZJJJJJcr1-1//rcJJcc1-1--JJdddJrcJJddddd          
          ddddddddddddZddZr<<<<<<-rJJJJJJZJJZZZZZZZZJJcccccJJJJJJJJJJJJcc/<<-/Zddddddddddddddd          
          ddddddddddddccr/-<<<<<<-rrcJJJJJJJJZZZZZZZJJccrrrrrcccJJJJccccr<-/1JZddddddddddddddd          
          ddddddddddddZc--<<<--<<-ccrrcJJJJJJZZZZZZZZZdZZZZZJJJJJccccrr/<<<----1-cZJdddddddddd          
          dddddddddddddcr<--1---<<cJcr/rrccJJJZZZZZdZZZZZZZZZZZJJJcrr/-<<<<<<--rccrddddddddddd          
          dddddddddddddJ/-</r--<<-cJJJcr///rr/rrcJccJJJJJJJJJJcccr/11<<-<<<<--rcZdZddddddddddd          
          dddddddddddddZJ-<-<<<-<-rJJJJccr/-1-11/rrrcccrrJcrrr//11-/-<<<-----//Zdddddddddddddd          
          dddddddddddddddZc-------/cJJJJJcrr/-----1111/1/1/111---1r/<<<<<<<--/Jddddddddddddddd          
          ddddddddddddZJ1----------1cJJJJJccrr/1--------<-<-<--1/rr/<<<<<---/Jdddddddddddddddd          
          dddddddddZ-<<--------------cJJJJJccrrr///111-111111//rrrr1<<<<<<-----<-1cddddddddddd          
          dddddZJr--<-----------------rcJJJJcccrrr///////////rrcrr/-<<<<<-----1--<-----1rJZddd          
          Zc1111---<-<-----------------/ccJJJcccrrrr//////rrccrrr//-<<<<<--<<<<---<<<--------1          
          --1------<--------------------1rccJccccrrrrrrrrrrrccrr//1--<<----<<<<<<----<--------          
          ----------<------------------<--rcccccccrrrrrrrccccrr////1-<-<--<<<<<<<<---<--------          
          ------------------------<<<<<<<<-rcccccccccccccccccrrrrr/-<---<<<<<<<<<<<-----------          
          ------<----<---------<<<<<<<<<<<-<-cJJJJJJJJJJJJJJcccJcc-<<--<<<<<<<<<<<<<----------
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
