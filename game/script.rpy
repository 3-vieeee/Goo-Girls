define a = Character("Audrime", who_color="#EB464D", what_color="#EB464D", image="audrime")
define s = Character("Slessica", who_color="#0056BF", what_color="#0056BF", image="sless")
define f = Character("Father",who_color="#FFCC29", what_color="#FFCC29")
define n = Character(None,what_color="#EB464D")

image report = "/Full art/Report.png"
image holding_hands = "/Full art/Holdinghands.png"
image Confession = "/Full art/Confession.png"
image bg trampoline_park = "/Backgrounds/trampoline.jpg"
image Ending = "/Full art/Ending.png"
image audrime uniform straight smile = "/audrime/Audrime uniform/audrime_uniform_straight_smile.png"
image audrime uniform right smile = "/audrime/Audrime uniform/audrime_uniform_right_smile.png"
image sless uniform left smile = "/slessica/Slessica uniform/sless_uniform_left_smile.png"
image audrime normal right frown ="/audrime/Audrime normal clothing/audrime_normal_right_frown.png"
image title = "/Full art/Title.png"
image sless uniform straight smile ="/slessica/Slessica uniform/sless_uniform_straight_smile.png"
image bg room ="/Backgrounds/room.jpg"
image bg cafeteria = "/Backgrounds/cafeteria.jpg"
image bg school_hall = Solid("#6b6f7a")
image bg street      = Solid("#4a4e5c")
image bg hilltop     = Solid("#2b3350")
image audrime normal down closed = "/Audrime/Audrime normal clothing/audrime_normal_down_closed.png"
image father = "/Full art/Father.png"
transform image_resize:
    fit "contain"
    xysize (1920, 1080)
transform bg_resize:
    fit "fill"
    xysize (1920,1080)
transform flashback_tint:
    matrixcolor TintMatrix("#d9b98a") * SaturationMatrix(0.5)

transform flashback_blur:
    blur 4
transform city_blur:
    blur 0
    linear 2.0 blur 12

transform city_focus:
    blur 12
    linear 1.5 blur 0

label start:
    "{color=#EB464D}I really need to fix my grades{/color}"
    show report at image_resize, truecenter with Dissolve(1.0)
    "{color=#0056BF}Well, Red, remember, I'm here for you{/color}"
    
    "{color=#0056BF}Besides, it's never too late for you bounceback.{/color}"
    scene black with Dissolve(0.5)
    "{color=#EB464D}Easy for you to say.{/color}"
    show title at image_resize, truecenter with wiperight
    ""
    hide title
    "{color=#EB464D}I used to be good at school Like so, so good.{/color}"
    "{color=#EB464D}But ever since about a year ago I just couldn't keep up. SHS: The place had some inexplicable drowning quality.{/color}"
    "{color=#EB464D}I was like a match tossed into a glass of water."
    "{color=#FFCC29}...{/color}"
    "{color=#EB464D}I was truly put out. Not just school. My hobbies. My room. Fuck.{/color}"
    "{color=#FFCC29}...{/color}"
    "{color=#EB464D}I cant live...{/color}"
    "{color=#EB464D}...like this any longer{/color}"
    "Audrime!"(what_color="#FFCC29",what_bold=True) 
    scene room at bg_resize, truecenter with hpunch
    show audrime normal down closed at left with moveinbottom
    a "gah!"
    f "Falling asleep when you should be studying. Typical."
    show father at right with moveinright
    a "..."
    hide audrime normal down closed
    show audrime normal right frown at left
    f "What's this?"
    n """
    And he barges into my room, almost tripping over a pile of unread books piled by the door. I realize what he’s reaching for, and try to grab it, 
    
    but I’m too late.
    """
    f "Your report card.\n The one that was supposedly lost in the mail?!"
    n "He's spluttering with poorly masked anger."
    f "And you have the gall to bring your friend over to my house."
    n "He slams the report card down." with vpunch
    f "I didn’t know I was raising an ungrateful, lazy, failure of a daughter."
    n "He turns to leave, but hesitates at the doorway."
    f "Why can’t you be more like that friend of yours?" (what_italic=True)
    a "Dad... I..."
    hide father with moveoutright
    n "But he slams the door behind him." with hpunch
    a "Fuck..."
    scene black with Dissolve(0.5)
    call flashback_cafeteria
    call filler
    call swingset_scene
    return
#filler bc we didn't finish
label filler:
    scene black with Dissolve(1.0)
    "Over the next few days, Audrime, jealous of her success and eager to appease her father, distances her self from her friend. She avoids her in the halls, and when the end of day bell rings she walks straight home to study"
    "We didn't finish this part lol." 
    return
# flashback
label flashback_cafeteria:
    scene black with Dissolve(1.0)
    scene bg cafeteria at flashback_tint, bg_resize with Dissolve(1.5)

    show sless uniform straight smile at right, flashback_tint, with Dissolve(0.5)
    s "Hey, Red! I got us a good table!"

    n "I remember… I walked over to her… she had picked a nice table, clean, near the only stocked vending machine… I sat down across from her, like I always did."

    show audrime uniform straight smile at left, flashback_tint with moveinleft
    a "Oh my god, did you see…"

    n "We talked about our weekend plans… I don't remember what we said exactly. But somehow the conversation pivoted to our futures."

    hide sless uniform straight smile
    show sless uniform left smile at right, flashback_tint
    s "So, I've been thinking… We should study programming next year! We've got the grades, and, being members of our local Hackclub chapter, we've made so many fun projects."
    a "I've been thinking the same thing! We'll be top of our class. And then… we can go to UP Slimiman together… we could be roommates!"
    hide audrime uniform straight smile
    show audrime uniform right smile at left, flashback_tint
    s "Roommates? Like… live together? Sleep.."
    n "I remember her choking on and coughing out a piece of food."
    scene black with Dissolve(1.5)
    return
# Blurred "kaleidoscope" city lights (needs Ren'Py 7.4+)

label swingset_scene:

    scene bg school_hall with Dissolve(1.0)
    #show slessica worried at right
    #show audrime tired at left

    s "Audrime, are you ok? You look like you're melting."

    n "I sigh."
    a "Sless, I'm fine. Look, I have to go… study."

    s "I'm sorry… it's just… Are you ok? Is this about your grades?"

    a "My grades are fine." with vpunch
    n "I blurt it out a little too loud and a little too fast."

    n "She sighs and looks up at me with those caring eyes."
    s "No. Look. We're going somewhere to talk."

    n "She grabs me by the wrist."

    #show slessica determined at center with move
    a "Where are you dragging me?"
    s "C'mon Red, don't you trust me? It's a surprise."

    scene bg street with Dissolve(1.0)

    n "In spite of all the things I've done these past few weeks, of how far away I've pushed her, she never stopped caring for me any less."
    n "I'm angry at that. Why is she so perfect?"
    n "But the anger fades as I look into her eyes. So brilliantly red, kind… they make me trust her completely."
    n "I'd follow her off a cliff."
    n "I give her a nod, and she starts dragging me again. People stare at us as we pass them on the street."

    scene bg hilltop with Dissolve(1.5)

    n "After a while, we reach a park near the edge of town. It's a hill, adorned with an easy looking trail. Something metallic glints at the top."
    n "Sless finally lets go of me."

    s "Follow me."

    n "When we reach the top of the hill, I see a pristine metal swing set. Not a millimetre of rust scars its surface."
    n "Sless skips towards it and motions for me to follow. We sit down on the swings."

    #show slessica wistful at right
    s "We used to come here all the time, when we were little. Remember Red?"
    n "Her crimson eyes leave mine to stare wistfully off into the city."

    n "I follow her gaze. The city lights are bright. If I squint I can almost see the people walking… walking home from work, walking to parties, walking with their friends… girlfriends…"

    # Let the eyes unfocus
    show bg hilltop at city_blur

    n "But if I let my eyes unfocus, all the lights blur together, like a stained glass window, no, a kaleidoscope."
    n "And the little people are drifting around like floaters in my eye. It's beautiful."

    show bg hilltop at city_focus

    n "Suddenly I realise I've done this before."

    a "Yeah… I have a really vivid memory of us competing to see who could go the highest on the swings. I can't remember who won…"
    n "I laugh."
    n "I remember though, how her hair would fly brilliantly behind her when she swung up. I remember her smile when she finally returned to the ground…"
    a "I remember looking out at the city afterwards."

    s "You won. But… you refused to accept the victory. You kept saying we tied."
    n "She chuckles."
    s "I miss being like that."
    n "She looks up at me with those crimson eyes."
    s "Red, why've you been pushing me away?"

    a "Sless… Sless, I'm so, so, so, sorry. God, my dad is right…"

    #show slessica gentle at center with move
    n "She reaches over and grabs my hand, as if to stop me from floating away."
    n "Her hands are nice and cool. I'm now horribly aware of how sweaty mine are. Fuck… I hope I don't have dirt in my nails…"

    s "Don't say that."
    n "She squeezes my hand reassuringly."
    show holding_hands at image_resize with Dissolve(1.0)

    n "And I'm pulled back to Earth again, just like years ago, after my dizzying ride on the swings."
    n "These past few months, I've been failing so much, I lost trust in myself. And these past few days, I've been taking it out on the best friend I've ever had. The only friend."

    a "God I'm sorry, Sless. Fuck. FUCK." with vpunch

    s "Red, snap out of it. You have to get out of your head!"
    n "She has tears in her eyes."
    s "Remember Red. I'm always by your side. Red…"

    #hide slessica
    #show slessica hug at center
    n "Hopping off her swing, she runs to me and takes me into a loving embrace."
    s "Red, Red, Red…"

    n "I hug her back, holding her close. Blinking is not enough to stop the deluge of tears that starts to flow from my eyes."
    n "We cry a week's worth of tears in a few minutes, holding each other softly."

    n "Suddenly, she pushes me away gently."

    #show slessica nervous at right
    s "Red, there's something I need to tell you…"
    n "She hesitates. It's as if she's carefully picking each word."

    s "You're worth more than your grades. You're worth more than what your dad says about you."
    n "She gulps."

    s "I…"
    n "She wipes away tears."
    s "I think you're the kindest, most amazing girl I know, and it's been really hard for me to see you struggling like this, and…"
    n "She gulps and shakes her head as if to swipe these words out of the air. Whatever she's going to say, she wants to say it right."
    n "But I think I know what she wants to say. My heart knows."

    s "I love everything about you… I've liked you for some years."
    n "She laughs nervously."
    s "Remember how I was trying to show you something a few days ago?"

    n "A pang of guilt shoots through me. I shouldn't have been so dismissive of her then."

    scene confession at bg_resize with Dissolve(1.0)

    s "I bought us tickets to the trampoline park you always wanted to go to. I wanted to take you there to ask you, um…"
    s "Audrime, Red, will you be my girlfriend?"

    n "A wave of emotions crashes over me. I've felt this way too. Being so distant and resentful, I'd somehow managed to suppress these emotions…"

    a "Yes."
    scene black
    "..."
    "..."
    "some weeks later"
    scene bg trampoline_park at bg_resize with Dissolve(1.5)
    show Ending
    "The End."
    return