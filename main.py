print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("Welcome to the Island of Treasures!")
print("Your mission is to find the treasure.") 

direction= input("Would you like to go left or right?\n").lower()

if direction == "left":
  print("Oh no! You've ended up in the mighty dragons cave! Game over!")
elif direction=="right":
  swim_or_wait= input("You've arrived to a river. Would you like to swim across or wait for a boat to come?\n").lower()
  if swim_or_wait=="swim":
    print('''  {{{}}}}}}.
             {{{{{}}}}}}}.
            {{{{  {{{{{}}}}
           }}}}} _   _ {{{{{
           }}}}  m   m  }}}}}
          {{{{C    ^    {{{{{
         }}}}}}\  '='  /}}}}}}
        {{{{{{{{;.___.;{{{{{{{{
 _      }}}}}}}}})   (}}}}}}}}}}
|\\   {{{{{}{{{) :   :{{{{{{{{{{{.
\\\\(\}}}}/       `@`  {{{}}}}}}}}}}.
 \ ( /{{{/ .CWWWO.   .CWWW{{{{{{{. {{{
  `\ \{{/  CWWWWWO'v'CWWWWWO}}\}}}}  }}
   }\ \/  /'CWWWO'   'CWWW{{{{{\{{{{  {
  {{{\   /{{{{\         /}}}}}} \{{{}}
  }}}}\_/}}}}}}\       /{{{{{{{{ \{{{{{{
 {{{{{{{{{{{{{{{)     (}}}}}}}}}\ \}}}}}}
  }}}}}}}}}}} }/       \}{{{{{{{{\ \{{{{
 {{{{{{{{{{{{{/    c    \{{{{{{{{`\ '-.
  }}}} }}}}}.V.         .V.}}{{{  )/\\\\
  {{{  {{{{.CWWV.     .VWWO.{ }}}    `\\\
   }}  }}} CWWWWWWV.VWWWWWWO}} {{{     `"`
   {  {{   CWWWWWWWVWWWWWWWO{   }} 
        }} CWWWWWWWWWWWWWWWO}}  { 
        {  CWWWWWWWWWWWWWWWO {
           'CWWWWWWWWWWWWWO'
            'CWWWWWWWWWWWO'
             'CWWWWWWWWWO'
              'CWWWWWWWO'
               ;CWWWWWO.
               CWWWWWWWO
               CWWWWWWWO
               CWWWWWWWO
nikki/jpp      'CWWWWWO'
                'CWAWO'
                .CMAMO.
               .CMAAAMO.
             .CMAIMAMIAMO.
           .CMAAIMAAAMIAAMO.
         .CMMAAIIAAZAAIIAAMMO.
        .CMAAAIIAAZ.ZAAIIAAAMO.
        CMAAIIIAAZ...ZAAIIIAAMO
        CAAIIIIAZ.. ..ZAIIIIAAO
        'CAIIIAZ..   ..ZAIIIAO'
         'CIIIZ..     ..ZIIIO'
          'CIIZ...   ...ZIIO'
           'CIZZ... ...ZZIO'
            'CIZ..   ..ZIO'
             'V..     ..V'
              Y'       'Y
              '         '
    ''')
    
    print("Oh no! You have been attacked by a gorgeous but vicious mermaid. Game over!")
  elif swim_or_wait == "wait":
      door= input("Great! You have arrived to your final destination. Please choose a door to enter the treasure vault. Is it going to be the red, blue or yellow one? Careful! The wrong choice might end up in you being fed to the lions!🦁\n").lower()
      if door== "red":
        print("Oh God! You woke up the furious gladiator! Game over!")
      elif door=="yellow":
          print("So close! You fell through a trap door straight into a lion pit! Game over!")
      elif door=="blue":
            print("Yay! You have won! The treasure is yours!")
      

