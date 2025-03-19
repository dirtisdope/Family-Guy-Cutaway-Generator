import random
m = input("Press enter to generate cutaway: ")
if m == "":
    people = [
        "Tom Cruise ",
        "Lizzo ",
        "Ronald McDonald ",
        "The Chicken ",
        "Stewie ",
        "Brian ",
        "Quagmire ",
        "Bill Gates ",
        "Jack Black ",
        "Vanilla Ice ",
        "Kanye West ",
        "Bill Cosby ",
        "Will Smith ",
        "Bruce Willis ",
        "Chris Hemsworth ",
        "Ariana Grande ",
        "Dwayne 'The Rock' Johnson ",
        "Ellen DeGeneres ",
        "Oprah Winfrey ",
        "Morgan Freeman ",
        "Ryan Reynolds ",
        "Keanu Reeves ",
        "Emma Watson ",
        "Meryl Streep ",
        "Selena Gomez ",
        "Justin Bieber ",
        "Zac Efron ",
        "Jennifer Lawrence ",
        "Samuel L. Jackson ",
        "Will Ferrell ",
        "Chris Pratt ",
        "Jim Carrey ",
        "Sharon Stone ",
        "Michael B. Jordan ",
        "Rihanna ",
        "Beyoncé ",
        "Johnny Depp ",
        "Taylor Swift ",
        "Emma Stone ",
        "Dwayne 'The Rock' Johnson "
    ]
    
    sentences = [
        "Remember the time I went to, ",
        "...Like the time I, ",
        "Like a, ",
        "Remember the time I saw, ",
        "Hey Chris, remember the time we, ",
        "Like when I, ",
        "You know what happened when I, ",
        "Oh man, I remember when I, "
    ]
    
    places = [
        "Disneyland ",
        "The Forest ",
        "The Barber Shop ",
        "The Golf Course ",
        "The Museum of Loaded Pistols and Spring Loaded Boxing Gloves ",
        "Prison ",
        "The M&M Factory ",
        "Cleveland's House ",
        "A haunted house ",
        "The Moon ",
        "A trampoline park ",
        "The Sahara Desert ",
        "The North Pole ",
        "A sushi restaurant ",
        "A drive-thru ",
        "A rollercoaster ",
        "An abandoned mall ",
        "The Super Bowl halftime show ",
        "A theme park for aliens ",
        "The Grand Canyon ",
        "A beach in Hawaii ",
        "A secret government base ",
        "A luxury yacht ",
        "A dance club in Paris ",
        "The Eiffel Tower ",
        "An underground cave system ",
        "A wrestling ring ",
        "A tropical island ",
        "A zombie apocalypse survival camp ",
        "A comic book convention ",
        "A high-speed racetrack ",
        "A karaoke bar ",
        "A remote cabin in the mountains ",
        "A spaceship ",
        "A magic castle ",
        "A ninja dojo ",
        "A hidden speakeasy ",
        "A haunted library ",
        "A wildlife safari "
    ]
    
    actions = [
        "Ran from a herd of stampeding chickens",
        "Formed a rock band with a bear",
        "Wrestled an alligator in a hot tub",
        "Drove a car made of Jell-O",
        "Stole the Declaration of Independence for a selfie",
        "Got stuck in a vending machine",
        "Dressed up as a giant hot dog for a parade",
        "Tried to outsmart a talking dog",
        "Had a dance-off with a robot",
        "Competed in a potato sack race against a squirrel",
        "Flew a kite made of spaghetti",
        "Taught a llama to salsa dance",
        "Ran a lemonade stand with an evil genius",
        "Built a time machine out of a toaster",
        "Fought a giant squid with a pool noodle",
        "Got into a slap fight with a mime",
        "Tamed a wild shopping cart",
        "Exploded a piñata full of glitter",
        "Competed in a hot dog eating contest against a velociraptor",
        "Started a rock-paper-scissors tournament with aliens",
        "Had a karaoke contest with a raccoon",
        "Hitchhiked across the galaxy with a cyborg",
        "Became the official referee of a superhero fight",
        "Built a giant sandcastle on top of a volcano",
        "Had a potato gun war with a group of squirrels",
        "Fought off an army of angry garden gnomes",
        "Ran a marathon while being chased by a giant T-rex",
        "Had a dance-off against an army of robots",
        "Taught a kangaroo to breakdance",
        "Survived a gladiator battle against a cheetah",
        "Rode a roller coaster made out of noodles",
        "Tried to outsmart a vending machine with a psychic octopus",
        "Escaped a haunted amusement park on a go-kart",
        "Joined a circus and became the world's tallest clown",
        "Raced a spaceship against a herd of cows",
        "Had a ninja fight with a group of penguins"
    ]
    
    things = [
        "Sloth",
        "Platypus",
        "Penguin",
        "Cheetah",
        "Hummingbird",
        "Llama",
        "Mantis",
        "Dolphin",
        "Frog",
        "Octopus",
        "Giraffe",
        "Koala",
        "Panda",
        "Tarantula",
        "Meerkat",
        "Toucan",
        "Zebra",
        "Sparrow",
        "Armadillo",
        "Wombat",
        "Crocodile",
        "Dragonfly",
        "Chameleon",
        "Puffin",
        "Elephant",
        "Kangaroo",
        "Tiger",
        "Rhinoceros",
        "Gorilla",
        "Polar Bear",
        "Peacock",
        "Seahorse",
        "Jellyfish",
        "Sea Otter",
        "Pufferfish",
        "Snake",
        "Monkey",
        "Shark",
        "Butterfly",
        "Bat",
        "Starfish",
        "Slug",
        "Raven",
        "Bat",
        "Axolotl",
        "Caterpillar",
        "Narwhal"
    ]
    
    P = random.choice(people)
    S = random.choice(sentences)
    PL = random.choice(places)
    A = random.choice(actions)
    T = random.choice(things)
    
    if S == "Remember the time I went to, ":
        print(S + PL + "with " + P)
    
    if S == "Remember the time I saw, ":
        opt = [S + P + "at " + PL, S + P + A + " at " + PL]
        print(random.choice(opt))
        
    if S == "Hey Chris, remember the time we, ":
        print(S + A + " at the " + PL)
    
    if S == "...Like the time I, ":
        print(S + A + " with " + P)
    
    if S == "Like a, ":
        print(S + T + ", " + A)
    
    if S == "Like when I, ":
        print(S + A + " with " + P + "at " + PL)
    
    if S == "You know what happened when I, ":
        print(S + A + " with " + P)
    
    if S == "Oh man, I remember when I, ":
        print(S + A + " with a " + T + " at " + PL)
