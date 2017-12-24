from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Theja Gadde", email="tejasrig@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

# Items for Action
category1 = Category(user_id=1, name="Action")

session.add(category1)
session.commit()

item1 = CategoryItem(user_id=1, name="Star Wars: The Last Jedi",
                     description="""Rey develops her newly discovered
                      abilities with the guidance of Luke Skywalker, who is
                      unsettled by the strength of her powers. Meanwhile,
                      the Resistance prepares to do battle with the
                      First Order.""",
                     category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1, name="Justice League",
                     description="""Fueled by his restored faith in humanity
                      and inspired by Superman's selfless act, Bruce Wayne
                      enlists the help of his newfound ally, Diana Prince,
                      to face an even greater enemy.""",
                     category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1,
                     name="Jumanji: Welcome to the Jungle",
                     description="""Four teenagers discover an old video game
                      console and are literally drawn into the game's jungle
                      setting, becoming the adult avatars they choose.""",
                     category=category1)

session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1,
                     name="Thor: Ragnarok",
                     description="""Imprisoned, the almighty Thor finds
                      himself in a lethal gladiatorial contest against the
                      Hulk, his former ally. Thor must fight for survival and
                      race against time to prevent the all-powerful Hela
                      from destroying his home and the Asgardian
                      civilization.""",
                     category=category1)

session.add(item4)
session.commit()

item5 = CategoryItem(user_id=1,
                     name="Dunkirk",
                     description="""Allied soldiers from Belgium, the
                      British Empire and France are surrounded by the German
                      Army, and evacuated during a fierce battle in
                      World War II.""",
                     category=category1)

session.add(item5)
session.commit()

item6 = CategoryItem(user_id=1,
                     name="Avengers: Infinity War",
                     description="""The Avengers and their allies must be
                      willing to sacrifice all in an attempt to defeat the
                      powerful Thanos before his blitz of devastation and
                      ruin puts an end to the universe.""",
                     category=category1)

session.add(item6)
session.commit()


# Items for Animation
category2 = Category(user_id=1, name="Animation")

session.add(category2)
session.commit()


item1 = CategoryItem(user_id=1,
                     name="Coco",
                     description="""Aspiring musician Miguel, confronted
                      with his family's ancestral ban on music, enters the
                      Land of the Dead to find his great-great-grandfather,
                      a legendary singer.""",
                     category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1,
                     name="Ferdinand",
                     description="""After Ferdinand, a bull with a big
                      heart, is mistaken for a dangerous beast, he is
                      captured and torn from his home. Determined to return
                      to his family, he rallies a misfit team on the
                      ultimate adventure.""",
                     category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1,
                     name="The Polar Express",
                     description="""On Christmas Eve, a young boy embarks
                      on a magical adventure to the North Pole on the Polar
                      Express, while learning about friendship, bravery,
                      and the spirit of Christmas.""",
                     category=category2)

session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1,
                     name="The Star",
                     description="""A small but brave donkey and his
                      animal friends become the unsung heroes of
                      the first Christmas.""",
                     category=category2)

session.add(item4)
session.commit()

item5 = CategoryItem(user_id=1,
                     name="Frozen",
                     description="""When the newly crowned Queen Elsa
                      accidentally uses her power to turn things into
                      ice to curse her home in infinite winter, her sister,
                      Anna, teams up with a mountain man, his playful reindeer,
                      and a snowman to change the weather condition.""",
                     category=category2)

session.add(item5)
session.commit()


# Items for The Biography
category3 = Category(user_id=1, name="Biography")

session.add(category3)
session.commit()


item1 = CategoryItem(user_id=1,
                     name="The Disaster Artist ",
                     description="""When Greg Sestero, an aspiring film
                      actor, meets the weird and mysterious Tommy Wiseau in
                      an acting class, they form a unique friendship and
                      travel to Hollywood to make their dreams come true.""",
                     category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1,
                     name="The Greatest Showman",
                     description="""Inspired by the imagination of P.T.
                      Barnum, The Greatest Showman is an original musical
                      that celebrates the birth of show business and tells
                      of a visionary who rose from nothing to create a
                      spectacle that became a worldwide sensation.""",
                     category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1,
                     name="Darkest Hour",
                     description="""During the early days of World War II,
                      the fate of Western Europe hangs on the newly-appointed
                      British Prime Minister Winston Churchill, who must
                      decide whether to negotiate with Hitler, or fight on
                      against incredible odds.""",
                     category=category3)

session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1,
                     name="Frida",
                     description="""A biography of artist Frida Kahlo,
                      who channeled the pain of a crippling injury and her
                      tempestuous marriage into her work.""",
                     category=category3)

session.add(item4)
session.commit()


# Items for Comedy
category4 = Category(user_id=1, name="Comedy ")

session.add(category4)
session.commit()


item1 = CategoryItem(user_id=1,
                     name="Kingsman: The Golden Circle",
                     description="""When their headquarters are destroyed
                      and the world is held hostage, the Kingsman's journey
                      leads them to the discovery of an allied spy organization
                      in the US. These two elite secret organizations must band
                      together to defeat a common enemy.""",
                     category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1,
                     name="Home Alone",
                     description="""An eight-year-old troublemaker must
                      protect his house from a pair of burglars when he is
                      accidentally left home alone by his family during
                      Christmas vacation.""",
                     category=category4)

session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1,
                     name="Lady Bird",
                     description="""In the early 2000s, an
                      artistically-inclined seventeen year-old comes of age in
                      Sacramento, California.""",
                     category=category4)

session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1,
                     name="Logan Lucky ",
                     description="""Two brothers attempt to pull off a
                      heist during a NASCAR race in North Carolina.""",
                     category=category4)

session.add(item4)
session.commit()


# Items for Sci-Fi
category5 = Category(user_id=1, name="Sci-Fi ")

session.add(category5)
session.commit()


item1 = CategoryItem(user_id=1,
                     name="Ready Player One ",
                     description="""When the creator of a virtual reality
                      world called the OASIS dies, he releases a video in
                      which he challenges all OASIS users to find his
                      Easter Egg, which will give the finder his fortune.
                      Wade Watts finds the first clue
                      and starts a race for the Egg.""",
                     category=category5)

session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1,
                     name="Annihilation",
                     description="""A biologist signs up for a dangerous, secret
                       expedition where the laws of nature don't apply.""",
                     category=category5)

session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1,
                     name="Bright",
                     description="""Set in a world where mystical creatures
                      live side by side with humans. A human cop is forced
                      to work with an Orc to find a weapon everyone is
                      prepared to kill for.""",
                     category=category5)

session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1,
                     name="X-Men: Dark Phoenix",
                     description="""Jean Grey begins to develop incredible
                       powers that corrupt and turn her into a Dark Phoenix.
                       Now the X-Men will have to decide if the life of a team
                       member is worth more than all the people living
                       in the world.""",
                     category=category5)

session.add(item4)
session.commit()

print "added items!"
