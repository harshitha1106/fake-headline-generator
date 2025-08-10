import random
subject=["nirmala sitharaman","virat kohli","cricket team is","indian people","a group of monkeys"]
actions=["declares war","cooking biriyani on scooter","doing yoga on a train roof","teaching cows to code python","giving free wifi to ants","running a dharna on zoom"]
places=["statue of unity","at red fort","in mumbai local train","at ganga ghat","inside parliment"]
while True:
    a=input("do you want to generate a funny headline?(yes or no):").strip().lower()
    if a=="yes":
        print(f"Breaking news:\n{random.choice(subject)} {random.choice(actions)} {random.choice(places)}")
    else:
        break
print("\n Thanks for using fake news Headline generator.have a nice day")