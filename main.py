import twint 


#General search section
looker = input("What are you wanting to search for:")

#Tweets talking about vehicles
def vehicles():
    vehicles = input("What Ukraine War weapons tweets do you want: ")

    if vehicles == "tractors, tanks, tank support vehicles, IFV, infantry fighting vehicles, APC, armored personnel carrier, command vehicles, scout vehicle, recon vehicle, infantry mobility vehicles, recovery and engineering vehicles, utitility vehicle, transport vehicle,   ":
        vehicles()
    else:
        print ("Not an allowed search.")
      
#Man portable weaposn search section
def man_portable_weapons():
  man_portable_weapons = input("What do you want to search for:")

  if man_portable_weapons == "guns, rifles, bombs, nuke, nuclear device, pistol, knife, grenade":
    man_portable_weapons()
  else:
    print ("Not an allowed search")
    
#Location being discussed
def location():
    location = input("Where in Ukraine do you want the tweets to talk about ")

    if location == "Kyiv, Kharkiv, ":
        location()
    else:
        print ("Not an allowed search.")

#Country that the tweet was put out from
def origin():
    origin = input("Where do you want the Tweet to originate from ")

    if origin == "Ukraine, Russian, United States, Great Britain, United Kingdom, Belarus, Poland.":
        origin()
    else:
        print ("Not an allowed search.")

#Person that the Tweet is coming from

person = input("Who are you wanting this tweet to be from: ") 
  

#Limit the amount of tweet that come out
print ("There could be way too many tweets to read through so this last bit is to restrict the amount tweets that you get.") 
limit = input("How many tweets do you want returned: ")


c = twint.Config()
c.search = looker
c.search = vehicles
c.search = man_portable_weapons
c.search = location
c.Near = origin
c.Username = person
c.Limit = limit
