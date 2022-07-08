import webbrowser
print("Do you have confusion in choosing today's food?\n "
      "Don't worry, I will help you.\n"
      "Let me clear up your confusion with a fun chat...!")
print("1.Bakery and Bread\n2.Oils, Sauces and Salad Dressings \n3.Snacks and Crackers\n4.Pasta and Rice")
c=int(input("Enter your choice:"))

if(c==1):
      print("List of Bakery and Bread iteam:")
      print("1.Muffins\n2.Cinnamon rolls\n3.Tortillas")
      s=int(input("Wants to know any recipe(1.Yes 2:No):"))
      if(s==1):
            a=int(input("Which Iteam(Enter the no):"))
            if(a==1):
                  webbrowser.open("https://www.youtube.com/watch?v=DOZXZxJenZE")
            elif(a==2):
                  webbrowser.open("https://www.youtube.com/watch?v=am6_6KGnhpc")
            elif(a==3):
                  webbrowser.open("https://www.youtube.com/watch?v=CVEK9HkNmmU")
elif(c==2):
      print("List of Sauces, Salad Dressings,and Condiments iteam:")
      print("1.Salad dressing spread\n2.Salt and pepper\n3.Maxican salad")
      s = int(input("Wants to know any recipe(1.Yes 2:No):"))
      if (s == 1):
            a = int(input("Which Iteam(Enter the no):"))
            if (a == 1):
                  webbrowser.open("https://www.youtube.com/watch?v=g8U3w0n5XOU")
            elif (a == 2):
                  webbrowser.open("https://www.youtube.com/watch?v=lHU74Dmrffc")
            elif (a == 3):
                  webbrowser.open("https://www.youtube.com/watch?v=6izvTfJxdZo")
elif(c==3):
      print("List of Snacks and Crackers iteam:")
      print("1.Crackers\n2.Chakri\n3.Bhakhrwadi")
      s = int(input("Wants to know any recipe(1.Yes 2:No):"))
      if (s == 1):
            a = int(input("Which Iteam(Enter the no):"))
            if (a == 1):
                  webbrowser.open("https://www.youtube.com/watch?v=uBH3mcA9aA8")
            elif (a == 2):
                  webbrowser.open("https://www.youtube.com/watch?v=bn0eoi0EfX8")
            elif (a == 3):
                  webbrowser.open("https://www.youtube.com/watch?v=hDGfbzXqJOc")
elif(c==4):
      print("List of Pasta and Rice iteam:")
      print("1.Orzo\n2.Mutton Biryani.\n3.Manicotti")
      s = int(input("Wants to know any recipe(1.Yes 2:No):"))
      if (s == 1):
            a = int(input("Which Iteam(Enter the no):"))
            if (a == 1):
                  webbrowser.open("https://www.youtube.com/watch?v=vhqGE78yrtc")
            elif (a == 2):
                  webbrowser.open("https://www.youtube.com/watch?v=0DE-2vniskw ")
            elif (a == 3):
                  webbrowser.open("https://www.youtube.com/watch?v=gE-JIr6UVtw")