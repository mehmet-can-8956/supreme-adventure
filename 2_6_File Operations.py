with open("poem.txt","w") as p:
    p.write("when i look into your eyes\n")
    p.write("i see the deep blue sea color\n")
    p.write("when i hold your hand\n")
    p.write("i feel like i touch clouds in the sky\n\n")
    
with open("poem.txt","a") as p:
    p.write("when i smell your hairs\n")
    p.write("i feel like i am in a flower garden\n")
    p.write("when i say i love you\n")
    p.write("you say wake up you talk in your sleep\n")
    
with open("poem.txt","r") as p:
    poem=p.read()
print(poem)