import random
play = True
symboles = ['carreaux', 'coeurs', 'trefles', 'piques']
cartes = ['As','2','3','4','5','6','7','8','9','10','Valet','Dame','Roi']

next = 0
pot = 0
wallet_player = 5000
player_2_wallet = 5000
print('1 = jouer')
print('2 = commande')
option = int(input('choisissez votre mode '))

if option ==2 :

     print('2 = miser la valeur du pot')
     print('3 = se coucher')
     print('4 = tapis')
     print('Vous commencer avec 5 000 Jetons')
     play = input('jouer True/False ')


while wallet_player>0 :
     print('____________________________________________________________')
     print('NOUVELLE PARTIE')

     a = random.choice(cartes)
     b = random.choice(symboles)
     c = random.choice(cartes)
     d = random.choice(symboles)
     e=random.choice(cartes)
     e2 =random.choice(symboles)
     f=random.choice(cartes)
     f2 =random.choice(symboles)
     g=random.choice(cartes)
     g2 =random.choice(symboles)
     h=random.choice(cartes)
     h2 = random.choice(symboles)
     i=random.choice(cartes)
     i2 =random.choice(symboles)

     a3 = random.choice(cartes)
     b3 = random.choice(symboles)
     c3 = random.choice(cartes)
     d3 = random.choice(symboles)
     e3=random.choice(cartes)
     e23 =random.choice(symboles)
     f3=random.choice(cartes)
     f23 =random.choice(symboles)
     g3=random.choice(cartes)
     g23 =random.choice(symboles)
     h3=random.choice(cartes)
     h23 = random.choice(symboles)
     i3=random.choice(cartes)
     i23 =random.choice(symboles)

     end_player1 =[a==c,a==e,a==f,a==g,a==h,a==i,c==e,c==f,c==g,c==h,c==i,e==f,e==g,e==h
     ,e==i,f==g,f==h,f==i,g==h,g==i,h==i,a and c == e,a and c ==f,a and c ==g,a and c ==h,a and c ==i,a and e ==c
     ,a and e ==f,a and e ==g,a and e ==h,a and e ==i,a and f ==c,a and f ==e,a and f ==g,a and f ==h,a and f ==i,a and g ==c
     ,a and g ==e,a and g ==f,a and g ==h,a and g ==i,a and h ==c,a and h ==e,a and h ==f,a and h ==g
     ,a and h ==i,a and i ==c,a and i ==e,a and i ==f,a and i ==g,a and i ==h,a and c and e ==f,a and c and e ==g,a and c and e ==h
     ,a and c and e ==i,a and c and f ==e,a and c and f ==g,a and c and f ==h,a and c and f ==i
     ,a and c and g == e,a and c and g ==f,a and c and g ==h,a and c and g ==i,a and c and h ==e
     ,a and c and h ==f,a and c and h ==g,a and c and h ==i,a and c and i ==e,a and c and i ==f,a and c and i ==g
     ,a and c and i ==h]

     end_player2 =[a3==c3,a3==e3,a3==f3,a3==g3,a3==h3,a3==i3,c3==e3,c3==f3,c3==g3,c3==h3,c3==i3,e3==f3,e3==g3,e3==h3
     ,e3==i3,f3==g3,f3==h3,f3==i3,g3==h3,g3==i3,h3==i3,a3 and c3 == e3,a3 and c3 ==f3,a3 and c3 ==g3,a3 and c3 ==h3,a3 and c3 ==i3,a3 and e3 ==c3
     ,a3 and e3 ==f3,a3 and e3 ==g3,a3 and e3 ==h3,a3 and e3 ==i3,a3 and f3 ==c3,a3 and f3 ==e3,a3 and f3 ==g3,a3 and f3 ==h3,a3 and f3 ==i3,a3 and g3 ==c3
     ,a3 and g3 ==e3,a3 and g3 ==f3,a3 and g3 ==h3,a3 and g3 ==i3,a3 and h3 ==c3,a3 and h3 ==e3,a3 and h3 ==f3,a3 and h3 ==g3
     ,a3 and h3 ==i3,a3 and i3 ==c3,a3 and i3 ==e3,a3 and i3 ==f3,a3 and i3 ==g3,a3 and i3 ==h3,a3 and c3 and e3 ==f3,a3 and c3 and e3 ==g3,a3 and c3 and e3 ==h3
     ,a3 and c3 and e3 ==i3,a3 and c3 and f3 ==e3,a3 and c3 and f3 ==g3,a3 and c3 and f3 ==h3,a3 and c3 and f3 ==i3
     ,a3 and c3 and g3 == e3,a3 and c3 and g3 ==f3,a3 and c3 and g3 ==h3,a3 and c3 and g3 ==i3,a3 and c3 and h3 ==e3
     ,a3 and c3 and h3 ==f3,a3 and c3 and h3 ==g3,a3 and c3 and h3 ==i3,a3 and c3 and i3 ==e3,a3 and c3 and i3 ==f3,a3 and c3 and i3 ==g3
     ,a3 and c3 and i3 ==h3]

     final_1 = sum(end_player1)
     final_2 = sum(end_player2)


     if a==c or a==e or a==f or a==g or a==h or a==i 	:
	     a = random.choice(cartes)
     if c==e or c==f or c==g or c==h or c==i :
     	c=random.choice(cartes)
     if e==f or e==g or e==h or e==i :
     	e = random.choice(cartes)
     if f==g or f==h or f==i :
     	f = random.choice(cartes)
     if g==h or g==i :
     	g = random.choice(cartes)
     if h==i :
     	h = random.choice(cartes)

     pot += 50
     wallet_player -= 25
     player_2_wallet -= 25
     print('pot =',pot)
     print('porte monnaie =',wallet_player)
     print("Vos cartes sont", a,"de", b, 'et', c ,"de", d)

     print('milieu est ', e+e2, f+f2, g+g2)
     next = int(input('Que faire ?'))

     if next==2 :
         player_2_wallet -= pot
         wallet_player -= pot
         pot += pot
         print('pot =',pot, 'et porte monnaie =',wallet_player)

     if next==3 :
         play = input("jouer encore ?")


     if next==4 :
         pot += wallet_player
         pot += player_2_wallet
         wallet_player -= wallet_player
         player_2_wallet -= player_2_wallet
         print('pot =',pot, 'et porte monnaie =',wallet_player)
         print(e+e2, f+f2, g+g2, h+h2, i+i2)
         if final_1>final_2 :
             print("c'est gagné")
             wallet_player += pot
             pot = 0
             play = input("jouer encore ?")
         else :
            print('Perdu')
            player_2_wallet += pot
            pot = 0
            play = input("jouer encore ?")


     print("Vos cartes sont", a,"de", b, 'et', c ,"de", d)
     print(e+e2, f+f2, g+g2, h+h2)
     next = int(input('Que faire ?'))

     if next==2 :
         player_2_wallet -= pot
         wallet_player -= pot
         pot += pot
         print('pot =',pot, 'et porte monnaie =',wallet_player)

     if next==3 :
         play = input("jouer encore ?")
         if play==False :
             exit()

     if next==4 :
         pot += player_2_wallet
         pot += wallet_player
         wallet_player -= wallet_player
         player_2_wallet -= player_2_wallet
         print('pot =',pot, 'et porte monnaie =',wallet_player)
         print(e+e2, f+f2, g+g2, h+h2, i+i2)
         if final_1>final_2 :
             print("c'est gagné")
             wallet_player += pot
             pot = 0
             play = input("jouer encore ?")
         else :
             print('Perdu')
             player_2_wallet += pot
             pot = 0
             play = input("jouer encore ?")
             if play==False :
                 exit()


     print("Vos cartes sont", a,"de", b, 'et', c ,"de", d)
     print(e+e2, f+f2, g+g2, h+h2, i+i2)
     next = int(input('Que faire ?'))

     if next==2 :
         player_2_wallet -= pot
         wallet_player -= pot
         pot += pot
         print('pot =',pot, 'et porte monnaie =',wallet_player)
         if final_1>final_2 :
             print("c'est gagné")
             wallet_player += pot
             pot = 0
             play = input("jouer encore ?")
             if play==False :
                 exit()

         else :
             print('Perdu')
             player_2_wallet += pot
             pot = 0
             play = input("jouer encore ?")
             if play==False :
                 exit()



     if next==3 :
         play = input("jouer encore ?")
         if play==False :
             exit()

     if next==4 :
         pot += player_2_wallet
         pot += wallet_player
         wallet_player -= wallet_player
         player_2_wallet -= player_2_wallet
         print('pot =',pot, 'et porte monnaie =',wallet_player)
         print(e+e2, f+f2, g+g2, h+h2, i+i2)
         if final_1>final_2 :
              print("c'est gagné")
              wallet_player += pot
              pot = 0
              play = input("jouer encore ?")

         else :
             print("perdu")
             player_2_wallet += pot
             pot = 0
             play = input("jouer encore ?")
             if play==False :
                 exit()


