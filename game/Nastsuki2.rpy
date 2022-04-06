label Natsuki2:
    $ n_rep = 0
    $ tens_pick = ""
    $ y_name = "Yuri"
    $ s_name = "Sayori"
    $ n_name = "Natsuki"
    $ m_name = "Monika"

#For definitions file: Natsuki asset references
#Mod assets: BGs
#Black background
#image bg black = "mod_assets/black.png"

#Player house
#image bg bedroom_dirty = "mod_assets/bedroom_dirty.png"
#image bg livingroom = "mod_assets/livingroom.png"
#image bg livingroom_night = "mod_assets/livingroom_night.png"
#image bg livingroom_sunset = "mod_assets/livingroom_sunset.png"

#School
#image bg school = "mod_assets/school.png"

#Road Shots
#image bg road = "mod_assets/road.png"
#image bg road_sunset = "mod_assets/road_sunset.png"
#image bg road_night = "mod_assets/road_night.png"

#Bookstore
#image bg central_hub = "mod_assets/central_hub.png"
#image bg bookstore = "mod_assets/bookstore.png"
#image bg bookstore_sunset = "mod_assets/bookstore_sunset.png"
#image bg corner = "mod_assets/corner.png"
#image bg bowling_alley = "mod_assets/bowling_alley.png"

#Restaurant
#image bg resturant_front = "mod_assets/resturant_front.png"
#image bg resturant = "mod_assets/resturant.png"

#Cafe
#image bg cafe = "mod_assets/cafe.png"
#image bg cafe_in = "mod_assets/cafe_in.png"

#Movie Theater
#image bg theater = "mod_assets/theater_out.png"
#image bg theater_in = "mod_assets/theater_in.png"

#Carnival
#image bg carnival = "mod_assets/carnival.png"

#Mod Assets: Music
#bird chirpings
#define audio.t12 = "<loop 0>mod_assets/12.mp3"

#Scene 1 - Tension(1):
    scene black
    play music t12
    "It's morning."
    "Pale, impossibly bright sunlight filters into my room between the blinds and directly onto my shut eyes. Even so, it manages to wake me up."
    mc "Ngh..."
    scene bg bedroom_dawn
    with dissolve_scene_full
    "I open my eyes, wincing as the light fills my vision. After the intial pain fades, I try to sit up, but fail."
    "Looking to my left, I find Natsuki lying beside me. Her arms wrapped around my midriff and my arm is underneath her."
    "I have long since lost any feeling in the limb, but I barely notice as I watch Natsuki."
    "Her eyes are closed and her mouth is slightly parted as she breathes slowly and evenly."
    "She looks so peaceful. And, well... {w=0.25} cute of course."
    "..."
    "And naked."
    "I don't mean to gawk at her like this. It's just... {w=0.5} she looks so innocent and pure that I can't bring myself to look away."
    "I love her so much."
    "Another minute passes and then, Natsuki begins to stir and mumbles something incoherently."
    show natsuki dbla2 at t11 zorder 2
    n "Mmm... [player]?"
    "I hesitate."
    mc "Good morning, Natsuki."
    n "How long have you been awake?"
    mc "A couple of minutes, actually."
    show natsuki dblai
    "She sits up and looks at me with a somewhat annoyed expression. Whether because of me or just being woken up isn't clear."
    n dblah "Were you watching me sleep?"
    show natsuki dblai
    mc "I, uh... {w=0.25} Y-yes? Sorta?"
    n dblah "That's creepy, [player]."
    "I start to defend myself, but before I can even get a word out, she cuts me off."
    n dblal "I'm teasing. God, you're easy."
    show natsuki dblaj
    "I frown. It's too early for jokes."
    "Or much of anything else really."
    n dblak "What time is it?"
    mc "5:35 a.m."
    mc "Don't worry, we've got some time before school."
    n dblad "So breakfast then?"
    show natsuki dblaa
    mc "Sounds good to me. I'm not sure what I have, though."
    show natsuki dblaz
    "Natsuki grins at me as if I had just challenged her ability to make something delicious from scraps."
    n dblal "Trust me, you'll love whatever I whip up."
    n dblae "You'd better, anyways, or I won't make breakfast for you ever again."
    show natsuki dblag
    mc "Fair enough. But we should probably get dressed first, right?"
    n dblab "Well, duh."

    scene bg kitchen
    with wiperight
    stop music

    "Turns out I had more than I thought. Bread, eggs, cinnamon, butter, flour, and a few other things."
    "Natsuki really outdid herself."
    "I tried to help, of course. But since I'm not really much of a cook, all I really did was end up making a mess. Oh well, at least one of us will clean it up later"
    "Right now, I've got a massive plate with two huge slices of french toast, scrambled eggs, and hash browns on it. And right next to the plate, I have a large glass of fresh orange juice."
    "Natsuki has a nearly identical plate as well, on the other side of the table."
    "I don't think I've eaten this well since... well, ever really."
    show natsuki 4y at t11 zorder 2
    n 4y "Don't just stare at it. Eat it, dork."
    show natsuki 2j
    "Natsuki's words snap me back to the present and I meet her eyes. She hasn't eaten any of hers yet either."
    mc "Ah, sorry. It's just a lot more than what I was expecting, to be honest."
    show natsuki 2k
    mc "It smells and looks really good, though."
    show natsuki 1j 
    "Natsuki seems pleased by the praise."
    show natsuki at thide
    hide natsuki
    "I pick up the fork and cut off a small piece of toast. It's covered in maple syrup and oozing off the fork."
    "I shove the square in my mouth and chew."
    "..."
    "....."
    show natsuki 1n at t11
    "Natsuki is watching me closely as I chew, presumably looking for some sort of reaction, positive or negative."
    "I swallow and take a sip of orange juice."
    n 1m "Well?"
    mc "Well, what?"
    n 1n "Do you like it?"
    "I look down at my glass as if thinking hard about the question."
    mc "It's alright, {w=0.25} I guess."
    show natsuki 4o
    "Natsuki looks like she's going to punch me."
    "I grin."
    show natsuki 4c
    mc "I'm joking, Natsuki. I love it {i}almost{/i} as much as I love you. You're a really good cook."
    show natsuki 4s
    "Natsuki blushes and looks down at her plate."
    n 3t "I-idiot. I'm glad you like it so much."
    show natsuki at thide
    hide natsuki
    "Relative silence filled the room as we finish eating our meals. We decide not to talk about last night, which was probably for the best. It would just end up being awkward."
    "After we've eaten our fill and put the dishes in the sink to be washed later, Natsuki and I split up to finish our separate tasks before school."
    scene bg residential_day
    with wipeleft_scene
    "A few minute later, Natsuki and I are standing on the street corner outside my house, waiting for Sayori."
    "There's a slight nip in the air, so Natsuki is shaking beside me obviously not pleased with the weather."
    show natsuki 1b at t11 zorder 2
    n 4b "Why are we waiting for her exactly?"
    show natsuki 1f
    "Her tone was rather sharp, but her temper probably came from being forced to stand around in the cold rather than directed at Sayori herself."
    mc "Sayori and I always walk to school together."
    show natsuki 4g
    "Natsuki stares at me. I wilt under her gaze."
    mc "Well, usually, anyway. When she wakes up on time."
    mc "Besides, she still has a few minutes."
    n 4i "..."
    n 4h "You really do care about her, don't you?"
    "I pause. It was a simple question with a simple answer. But for some reason, I feel like this is some sort of test."
    "Of what, however, I have no clue."
    mc "Of course, I do. I mean, we've been friends since kindergarten at least."
    show natsuki 4s
    mc "Sure, she has her flaws. We all do. But she really turns any bad or boring day bright and cheerful just by being there."
    show natsuki 4u
    "Natsuki looks down at her feet, thinking about my words."
    show natsuki 2a
    "Finally she looks up and nods."
    n 2a "I see what you mean. She really has been the heart of the club, in her own way, even more so than Monika."
    "Silence once again fills the air while we wait, but it only lasts for a second."
    n 1k "What do you think my flaws are?"
    mc "I'm sorry?"
    show natsuki 1m
    n 4k "You said \'we all have flaws.\' What are mine?"
    "I hesitate. It seems I've accidentally set myself up for this."
    menu:
        "Should I be honest, or should I assure her that it doesn't matter?"
        
        "Be honest":
            #Scene 1a
            $ n_rep += 1
            n "Honesty is always the best policy, I think."
            mc "Well... um..."
            "Natsuki looks at me expectantly. I can see she's scared of what I might say."
            "I clear my throat and then speak."
            show natsuki 1n
            mc "Natsuki, you know I would only say this because I love and respect you."
            "{i}Not to mention the fact that you asked me for it{/i}."
            mc "But I guess you can come off as sort of...{w=0.5} abrasive at times."
            n 4m "Abrasive?"
            show natsuki 4n
            "She doesn't sound angry or particularly upset about it. Just a little... put down."
            "I feel a little bad, but she seems to want to know what I mean by that."
            mc "Just in how you deal with new people and experiences. I know you and I didn't exactly get along at first."
            n 4o "W-well! That was because...{w=0.25} b-because I..."
            show natsuki 42b
            "She breaks off and turns her gaze towards nothing in particular."
            show natsuki 42b
            "I step closer and put my hands on her shoulders in what I hope in a comforting way."
            mc "It's alright, I'm not saying that it's necessarily a bad thing."
            mc "Some people might disagree, but I never will."
            show natsuki 42a
            "Her eyes dart back to me warily."
            mc "Honestly, I like that side of you. It's what attracted me to you in the first place."
            n 42c "Not because you just thought I was cute?"
            "I smile and shake my head."
            mc "Okay, maybe I did think you were kind of cute, but that isn't the point."
            show natsuki 42a
            mc "I admire your tenacity and honesty."
            mc "You've never been afraid to say what you think or how you feel about those closest to you."
            show natsuki 4h
            mc "I wanted to be one of those people. One of the few you let your guard down around, even if I had to wade through waves of insults to get there."
            show natsuki 4m
            mc "What I'm trying to say is, I knew there had to be a good person behind that wall of solitude, and I proved that there is."
            show natsuki 4i
            mc "But it wouldn't hurt to let that side of you show more often."
            "I hold Natsuki at arm's length for a few moments as she considers my words."
            n 4b "No offense."
            n "But that sounds like a load of crap."
            show natsuki 1g
            "I suppress the urge to sigh and let my arms drop to my sides."
            "That was pointless."
        
        "Avoid the topic":
            #Scene 1b
            $ n_rep -= 1
            mc "Natsuki..."
            show natsuki 1c
            "She looks at me, clearly attentive to what I'm about to say."
            show natsuki 1a
            "I slide closer and put my arms around her petite frame. She blushes slightly but doesn't react otherwise."
            show natsuki 1c
            mc "It doesn't matter what I think or what anybody else thinks."
            mc "You know you best and I love everything about you. I wouldn't change a single thing if I could."
            show natsuki 1a
            "A small grin breaks across her face as she looks up at me."
            n 1l "You wouldn't even wish I was taller?"
            "Now it's my turn to smile."
            mc "Nope."
            n 1d "Why?"
            mc "Because you look cuter when you're tiny."
            show natsuki 1e
            "Instantaneously, she breaks away from me and whips around to deliver a swift punch to my shoulder."
            "There wasn't enough force behind it to leave a mark and it's obvious she meant it as a joke."
            show natsuki 1v at d11
            n "I'm {i}not{/i} cute!"
            show natsuki 1y
            "I grin more as I rub the sore spot on my shoulder."
            mc "I'm teasing, of course."
            mc "{w=0.25}But you are totally cute."
            show natsuki 4y
            "She huffs in mock annoyance and the subject is dropped altogether."

    "A few minutes pass and I glace at my watch. It's two minutes past the time we were supposed to leave already. Natsuki must be aware of the time too."
    n 1b "Look, [player], I don't think Sayori's coming any time soon."
    n 1d "So let's go before {i}we're{/i} late."
    "I want to argue, and know that I probably should, but I can't think of any good reason to wait longer, so I just nod and agree."
    show natsuki at thide
    hide natsuki
    "She turns away and starts walking down the street, so I jog to catch up to her." 
    "After a few moments, Natsuki remembers that she doesn't know her way around this part of town very well yet, so
    she lets me take the lead the rest of the way."
    "I tell her that she'll learn the route pretty quickly since there are very few turns and it's mostly straight for half a mile after that."

    scene bg school
    with wipeleft_scene
    "We arrive a few minutes before the bell rings, indicating the start of a new school day."
    "On the one hand, I dread the upcoming classes."
    "But on the other hand, at least there's the literature club after school."
    "I let the thought sink in. I actually look forward to the club meetings these days."
    "It's only been a few weeks, but I've noticed a massive turnaround in my view on the club."
    "I make a mental note to thank Natsuki for those cupcakes on my first day. I probably wouldn't have met her otherwise."
    "The thought saddens me, but also seems utterly foreign at the same time."
    "I can't imagine life without her now."
    "Is that what happens when you meet someone special?"
    show natsuki 4e at t11 zorder 2
    n "Hey, [player], are you spacing out again?"
    mc "Sort of. But it's not important. What's up?"
    show natsuki 4f
    "I can tell Natsuki is a little annoyed."
    n "I said \'I'm gonna go to class.\'"
    show natsuki 4h
    mc "Okay, but before you go-"
    show natsuki 4i
    "I beckon her, and she steps closer with an impatient expression."
    show natsuki 4b
    "I kiss her without warning."
    "I can sense her tensing for a moment before she relaxes and reciprocates the gesture."
    "It's not very long, nor is it particularly intense, but the passion and warmth is there."
    show natsuki 4d
    "It's only a moment later when Natsuki pulls herself away and I immediately find myself longing for the sensation once again."
    show natsuki at thide
    hide natsuki
    "Out of the corner of my eye and off in the distance, I notice a gaggle of classmates standing around and staring at us."
    "They're entirely female and, as I recall, among the more popular students."
    "But not the type of popular that Monika is."
    "I seem to remember Monika even mentioning them specifically. \"They're the sort of people I can't stand,\" she said, or something to that effect."
    "I decide not to mention anything to Natsuki to prevent ruining the moment."
    "If they want to judge and make snarky comments, that's their choice. It has nothing to do with me or Natsuki."
    show natsuki 1h at t11 zorder 2
    "Natsuki, on the other hand, is blushing furiously and struggling to keep any sense of indifference on her face."
    mc "You're cute when you're flustured."
    n 1r "S-shut up! I'm leaving now."
    show natsuki at thide
    hide natsuki
    "With that, she turns away and walks briskly into the school building and I'm left with a horde of faceless students on all sides."

    scene bg class_day
    with wipeleft_scene
    "Classes are over for the day."
    "Sayori wasn't in class today."
    "As worried as I am about it, I manage to push the thought into the back of my mind."
    "I instead focus on my..."
    "{i}My girlfriend{/i}."
    "It's still kind of strange to think of her like that."
    scene bg corridor
    "We talked in science class. Not about anything in particular. Just talked."
    "And later, during lunch, we ate together."
    "Even after all that, I still find myself craving her company. It's like when she's gone, I'm missing a part of myself."
    "It feels lonely."
    "That's another thing."
    "I wonder if I really had been lonely before and now I'm just starting to notice it."
    "There is a saying, \"Ignorance is bliss.\""
    "It's hard to say where I stand on that."
    "Was I happy before?"
    "I know I'm not unhappy now."
    "And I wasn't unhappy back then."
    "But I do fully recognize that I wasn't living the most... {w=0.25}exciting of lives."
    "The Literature Club, Natsuki, and all the girls around me have pulled me out of my comfort zone."
    "But how long could I have gone without knowing Natsuki or Yuri or Monika before I would've felt something different?"
    "Would I ever stop being unhappy?"
    "I shake the heavy thoughts from my head as I reach the clubroom door."
    "I wonder if I should wait for Natsuki before I go inside. I don't really want to bring a lot of attention to ourselves."
    "However, the decision is made for me when Natsuki approaches me from my right."
    show natsuki 4d at r11 zorder 2
    n "Hey~!"
    mc "Hey! How was your day?"
    n 1s "It was fine. I was thinking about you a lot, though. I wish we had more classes together."
    mc "Yeah, same here."
    mc "But we live together, so I guess we can't complain too much."
    mc "Maybe the distance at school isn't the worst thing in the world."
    show natsuki 1b
    mc "I wouldn't want to get sick of you so easily. Ehehe..."
    show natsuki 1v at d11
    "Natsuki slugs me in the arm."
    n 5n "Dummy."
    mc "So... this is our first club meeting since we became {i}official{/i} official."
    mc "Do you think the girls will notice something is different?"
    n 4j "Nothing's different, [player]."
    mc "Well... we did... do... {w=0.5}{i}that{/i}."
    show natsuki 1z
    "Natsuki snickers."
    n 3d "Do you think the other girls are like sharks when it comes to pheromones or something?"
    mc "Ehehe... I guess I'm just nervous about how I'll come off."
    n 1a "Don't be. We'll be fine."
    "Natsuki takes my hand, asserting that she wants the other girls to notice us."
    "I don't complain, and I open the clubroom door, walking inside with Natsuki."
    show natsuki at thide
    scene bg club_day
    with wipeleft_scene
    show yuri 1e at t11 zorder 2
    "We quickly notice Yuri sitting there, expectedly."
    show yuri 1k
    "What we don't expect, however, is the look she throws our way as we walk in and head for the closet."
    show yuri at thide
    hide yuri
    show natsuki 1a at t11 zorder 2
    mc "D-did you notice Yuri looked at us kinda dirty there?"
    n 2t "N-no, I didn't see that."
    "Someone's bad at lying."
    scene bg closet
    with wipeleft_scene
    show natsuki 1s at t11 zorder 2
    "Natsuki grabs a random manga carelessly, which is odd considering she's usually very careful about how her volumes are handled."
    "She nearly killed me over it when we first met."
    "She seems a little absent-minded."
    "As we sit down and open the book to read it, someone else walks into the room."
    show natsuki at thide
    hide natsuki
    scene bg club_day
    with wipeleft_scene
    show sayori 4r at t11 zorder 2
    s "Hi, everybody!"
    show sayori 4a at t21 zorder 2
    show yuri 1e at f22 zorder 2
    y "Hello, Sayori."
    show sayori 4b
    y 2h "Do you mind if we speak, privately? There's something I'd like to discuss with you."
    show yuri at t22
    "That sounds a little sketchy."
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    "I shrug it off and start to read some more, then try to get Natsuki's attention so she can turn the page, but when I look at her she's not even paying attention to the book."
    show natsuki 2u at t11 zorder 2
    mc "Natsuki?"
    n 2k "H-huh?!"
    mc "Are you okay?"
    n 2t "Y-yeah, I'm just fine."
    n 2l "Let's keep reading! I really like this volume."
    mc "... Uhm yeah. Me too."
    show natsuki at thide
    hide natsuki
    show monika 2l at t31 zorder 2
    show sayori 3l at t32 zorder 2
    show yuri 1g at t33 zorder 2
    "A moment later, Monika, tardy as always to her own club, enters the room, and is quickly beckoned by Yuri to join in on her and Sayori's conversation."
    "This congregation on the other side of the room is making me anxious. It's very suspicious that Yuri wanted to talk to everyone in the club except Natsuki and me."
    "I stand up to address this situation."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show natsuki 1o at t11 zorder 2
    n "[player], wait, don't--!"
    show natsuki at thide
    hide natsuki
    mc "Hey, uh, is there something going on here you'd rather we not be in the know about?"
    show monika 1o at t11 zorder 2
    m "..."
    show monika 1o at t21 zorder 2
    show yuri 3g at t22 zorder 2
    show yuri at f22
    y "..."
    show yuri at t22
    show monika 1o at t31 zorder 2
    show yuri 3g at t33 zorder 2
    show sayori 1k at t32 zorder 2
    show sayori at f32
    s "..."
    s 3l "Hey, [player]!"
    show sayori at t32
    "At least Sayori's cheeriness is still all-present."
    mc "Hi, Sayori. Do you care to fill me in on what's going on here?"
    show yuri 1w
    show sayori 1k
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show monika at f11
    m 3p "Uh, [player], let's talk outside for a minute, just one on one."
    show monika at thide
    hide monika
    "I look at Yuri, who's still yet to say a word to me, then look at Sayori, who's looking back and forth between myself, Natsuki sitting on the other end of the room."
    "As I walk out the door with Monika, I notice Sayori sit down and start rubbing an eraser up and down the desk."
    scene bg corridor
    with wipeleft_scene
    "Monika and I leave the room and close the door behind us, and she starts to speak up."
    show monika 1r at t11 zorder 2
    m "Listen, [player], I want to preface this by saying, I'm not taking anyone's side here."
    m 2g "If i'm being honest, I think Yuri is being a little bit too... reactive?"
    m 4d "But she's concered."
    show monika 4c
    mc "About...{w=0.25} what?"
    show monika 4r
    "Monika sighs."
    m 2r "She's concerned about how you're influencing Natsuki."
    show monika 2q
    mc "Excuse me?"
    mc "I'm gonna give that purple-haired shit a piece of my mi--{nw}"
    m 2g "Hey, hey, relax."
    show monika 2h
    "Monika grabs me by the arm to pull me back to my previous spot and calm me down."
    m 2d "Look, she's being very vague. But essentially, she's worried about the impact you and Natsuki's relationship will have on club affairs."
    m "I don't want you to think I'm trying to get between you and Natsuki, but I think it'd be best to take things a little more subtly while the club is in session."
    show monika 2c
    mc "Really? You're trying to supress our relationship just because Yuri is kind of uncomfortable?"
    m 1r "Its...{w=0.5} not just Yuri."
    show monika 2q
    mc "What are you...{w=0.25} oh..."
    "I think about the way Sayori looked a minute ago. I wonder if she's being affected by this too."
    m 1g "Look, I want you and Natsuki to be happy. But this club is important to me, and I don't want it to fall apart at the seams."
    show monika 1e
    mc "It sounds like you don't trust us."
    m 2i "I'd appreciate it if you didn't put words in my mouth, [player]."
    show monika 2h
    mc "S-sorry..."
    "Something about that shift of tone is her voice was very alarming and intimidating."
    m 4b "As club president..."
    m 4n "A-and as your friend..."
    m 2p "I just want what's best for everyone in the club."
    m 2d "And like I said... I'm not taking sides here. I'm looking at things objectively, not emotionally."
    show monika 2e
    "I absord what Monika says, and as long as she's speaking purely objectively, I guess I can't argue with her."
    "I'll do whatever she thinks is right, so that the club can stay intact."
    show monika at thide
    hide monika
    scene bg club_day
    with wipeleft_scene
    "Monika and I return to the room and catch sight of Yuri and Sayori now minding their own business, while Natsuki waits impatiently for my return."
    "I give Monika a nod of understanding, then walk over to Natsuki."
    show natsuki 4n at t11
    "I feel like Natsuki should know about what Monika and I just talked about, but I know how she can be and I don't want her to snap in the middle of the club meeting."
    "I want to heed Monika's advice, so maybe it'd be best to spend the time with someone else during the club meeting today."
    mc "Hey, Natsuki, listen..."
    mc "You and I spend a lot of time together, right?"
    n 2t "Pfft, yeah, duh."
    show natsuki 2s
    mc "Well, club is the one time we have where we can do something a little different."
    mc "Why don't we take advantage of that and each spend some time with someone else?"
    n 2m "Y-you don't want to read with me?"
    mc "No! That's not it!"
    show natsuki 2n
    mc "I'd love to read with you, but I think we should expand our horizons a little bit, you know?"
    mc "I don’t want us to forget that we have more people in our lives than just each other."
    show natsuki 2s
    mc "Everyone here really cares about each other so let's let them know we care about them."
    show natsuki 2t
    "Natsuki forces a smile at first, but soon it looks genuine."
    n 3l "Sure, I'd like to do that."
    n 4z "I wouldn't wanna get sick of you so easily. Ahaha~!"
    mc "Heh, you little jerk."
    "Natsuki smiles at me."
    n 3d "S-so who are you going to spend time with?"
    show natsuki 3a
    mc "Hmmm..."

    menu:
        "Who {i}am{/i} I going to spend time with?"

        #scene 1c
        "Sayori":
            $ tens_pick = "s"
            mc "I can spend time with Sayori today, I'm sure she misses me."
            n 3m "O-okay, I'll go hang out with Yuri then."
            show natsuki 1n
            "She seems hesitant, but before I can speak up and see if she wants to switch places, she stands up and walks toward Yuri."
            show natsuki at thide
            hide natsuki
            "Well, guess there's nothing left to do except kick it in with Sayori."
            "I stand up and walk over to the desk next to Sayori, then take a seat."
            show sayori 1k at t11 zorder 2
            mc "Hey, Sayori!"
            s 1r "Oh, hi [player]!"
            s 2a "How are you doing?"
            mc "Pretty good, how about you?"
            s 2k "I'm...{w=0.25}" 
            s 4l "... Good! R-really good!"
            mc "Glad to hear that."
            s 3c "What are you doing here? Aren't you supposed to be reading with Natsuki?"
            show sayori 3b
            mc "Nah, we decided to do something else. So i'm gonna spend my club time with you."
            s 4d "Aw, that's so sweet, [player]!"
            s 1y "I've missed you, to be honest."
            "Called it."
            mc "So have I."
            show sayori 1s
            "I smile at Sayori and she beams back at me."
            mc "So, what do you wanna do?"
            s 1a "Well, recently I've started getting into musicals."
            mc "Really? That's super cool."
            "The only musical I've ever seen Sayori watch before this point has been one we watched as kids together."
            "But it was a movie, not a live show."
            s 4q "Uh huh!"
            s 4a "And I think that musicals are a super cool form of literature!"
            mc "That's really cool, Sayori. So what do you wanna do today to celebrate that?"
            s 2x "I was gonna try looking for a script to a musical I like and read lines."
            s "I think acting would be fun! Do you wanna help me?"
            show sayori 2a
            mc "You want me to read lines with you?"
            s 4r "Yeah!"
            show sayori 4q
            "I've never acted before in my life, but this could be fun."
            mc "Sure thing! So what musical is it? Something silly like the one we watched as kids?"
            s 1l "N-no, actually, it's a little bit of a heavy one."
            mc "Oh?"
            s 1d "It's about a guy with social anxiety who tried to make the family of his recently departed classmate believe he was his best friend."
            s 3k "And he has to carry a lie for months on end to this family because he doesn't want to break their hearts, and also because he finally found people who accept him for who he is, which 
            he's wanted for his whole life."
            "..."
            "Holy crap."
            show sayori 1g
            mc "Sayori, that {i}is{/i} really heavy."
            mc "I wouldn't think you'd be into something like that."
            s 1a "Me either, but it was so awesome when I first watched it."
            s 2q "So, let me find the script and we can run lines together!"
            mc "Sounds great to me! This should be fun."
            show sayori 1a
            "Sayori finds a portion of this show's script to read lines from, and she and I assign roles."
            "I quickly realize that Sayori is actually a very good actress, at least compared to the driftwood-esque performance I'm giving."
            mc "Sayori, have you ever thought about trying out for school plays? I think you'd be really good at it!"
            s 5b "Y-you think so?"
            s 5a "I wouldn't wanna embarrass myelf, but if you really think I'm good at it then maybe I'll give it a shot."
            mc "I think you'll do awesome."
            s 2d "Thanks for the support, [player]. You're so great."
            mc "You're welcome, Sayori."
            show sayori at thide
            hide sayori
            "Soon after, the club meeting ends, and Monika dismisses the four of us."
            scene bg corridor
            with wipeleft_scene
            show natsuki 2j at t11 zorder 2
            "I meet Natsuki outside of the clubroom, then take her hand and swing our arms back and forth as we walk and talk."
            n 2i "So, how'd it go with Sayori?"
            show natsuki 2j
            mc "It was great! I learned Sayori's actually a very good actress."
            n 2l "Really? That's so cool."
            n 2q "I could never get on stage in front of people, I'd be so nervous."
            show natsuki 2s
            mc "Sayori said the same thing, but I'm encouraging her to put herself out there and audition for the school play."
            n 1j "You're really supportive. I'm glad to have someone like you behind me."
            mc "I'll always be happy to support you, Natsuki."
            mc "How'd it go with Yuri, by the way?"
            n 1t "Uh... it was okay, I guess. We had some tea together."
            n 3s "But... somehow she knew we were living together, which threw me off. Did you say anything?"
            mc "No, I didn't, but that's really strange."
            n 2q "She was also really quiet."
            mc "Yuri's always quiet."
            n 1u "Yeah but... I dunno, I might be overthinking. I hope I didn't do anything to offend her."
            mc "I'm sure you didn't, Natsuki."
            "... Is what I'm telling myself and her so I don't make her nervous..."
            show natsuki at thide
            hide natsuki

        #scene 1d
        "Yuri":
            $ tens_pick = "y"
            mc "I can talk to Yuri, I think that'd be best for both of us."
            n 3z "Okay, cool, so then I can go hang out with Sayori!"
            show natsuki at thide
            hide natsuki
            "Natsuki excitedly stands up and trots over to Sayori, and they sit together, chatting like old pals."
            "I actually wonder how close the two of them really are. I might have to ask about that at some point."
            "I figure I've wasted enough time, so I stand up and walk toward Yuri."
            show yuri 1g at t11 zorder 2
            "I clear my throat to grab her attention."
            mc "Good afternoon, Yuri."
            y 1h "... Good afternoon, [player]."
            mc "So... whatcha doin'?"
            y 1k "I'm reading, evidently."
            "She sure is. She has her book out in front of her and everything."
            show yuri 1g
            "Looks like reading to me."
            "Wait, why am I having this inner monologue?"
            mc "Uh, well, would you like to read with me? I'd like to hear more about the book you're enjoying."
            y 2k "To be honest I'm not enjoying it very much. It seems a little...{w=0.5} I don't know, unwelcomed, in a few places?"
            mc "Yeah, I hate stuff that feels unwelcomed."
            show yuri 1e
            "Yuri gives me a blank gaze."
            mc "..."
            mc "Am I bothering you?"
            y 1q "Uh..."
            y "I wouldn't necessarily say you're bothering me, but..."
            y 3u "I was hoping for some alone time."
            y 3w "B-but I’m sorry if I made you feel offended."
            "That was a weird personality shift, but I’ll let it go."
            y 1b "H-how about you and I share some tea?"
            mc "O-oh, sure, that sounds great!"
            y 1a "Very well. Would you like to accompany me to get some water?"
            mc "Yeah, totally."
            "Yuri stands up and marks her page, then reaches into her bag and grabs her pitcher, then the boiler."
            "She plugs it in and sets it on the desk, then beckons me to follow her out into the hallway."
            show yuri at thide
            hide yuri
            scene bg corridor
            with wipeleft_scene
            "Yuri and I walk down the hall in silence for a few moments until, surprisingly, she speaks up."
            show yuri 1b at t11 zorder 2
            y "So, how is your and Natsuki’s relationship progressing?"
            show yuri 1a
            "I can’t tell what she’s trying to convey with that question, but nonetheless I owe her an answer."
            mc "I-it’s been great. Excellent, as a matter of fact."
            mc "We’ve spent a lot of time together, and she nursed me back to health when I got sick recently."
            mc "I really enjoy her company."
            y 1b "I’ve heard that you’re living together as well."
            show yuri 1a
            "My heart drops slightly hearing this, as I wasn’t aware this was public info yet."
            mc "Y-yeah, th-things haven’t been the best for her at home, so I decided to take her in."
            y 1f "Doesn’t that seem a bit irresponsible this early in your lives, and in your relationship?"
            "... That really isn’t Yuri’s business."
            show yuri 1a 
            mc "Well, I wouldn’t say so. I think we both know what we’re getting into, so it’s okay."
            y "You say that now, but perhaps you won’t feel that way in a few weeks."
            y 3h "I’ll just say this... tread lightly."
            show yuri 3i
            mc "R-right... {w=0.25}thanks..."
            "{i}For the unsolicited advice, that is.{/i}"
            "Yuri and I find the water fountain, fill up the pitcher, then return to the clubroom and share some tea together."
            show yuri at thide
            hide yuri
            scene black
            with wipeleft_scene
            "It may have been the most uncomfortable cup of oolong I’ve ever drank, but it at least tasted good."
            scene bg club_day
            with wipeleft_scene
            "Soon after, the club meeting ends, and Monika dismisses the four of us."
            scene bg corridor
            with wipeleft_scene
            show natsuki 1a at t11 zorder 2
            "I meet Natsuki outside of the clubroom, then take her hand and swing our arms back and forth as we walk and talk."
            show natsuki 1b at f11 zorder 2
            n "So, how were things with Yuri?"
            show natsuki 1a at t11 zorder 2
            mc "Uh... {w=0.25}hard to say."
            show natsuki 2g at t11 zorder 2
            mc "She seemed nice to an extent, but she was also being a little cold."
            mc "I dunno, maybe I’m just not super used to talking to her. I feel like I haven’t gotten to know her as well as I could’ve since I joined the club."
            show natsuki 2d at f11 zorder 2
            n "Ehehe~! Yeah, Yuri’s a tough nut to crack, but don’t worry. I’m here to help you bash her open to get to the goodies inside."
            show natsuki 2a at t11 zorder 2
            mc "... Remind me to never let you near my zipper again."
            show natsuki 1l at d11 zorder 2
            "Natsuki slugs me in the shoulder."
            show natsuki 4j at t11 zorder 2
            mc "Oogh!"
            show natsuki 5z at f11 zorder 2
            n "Ahaha~! Dummy!"
            show natsuki at t11 zorder 2
            "She thinks it’s funny, but those punches hurt..."
            mc "What did you and Sayori do together?"
            show natsuki 3b at f11 zorder 2
            n "She talked to me about this musical she’s really into. It’s kinda dark and depressing."
            n 3c "Not really my style, but I’m glad she talked to me about it."
            n 3b "Then I told her about me and you and how things are going."
            n 5e "She seemed supportive, but when I brought you up, she...{w=0.5} didn’t really seem to wanna look at me all too much."
            show natsuki 5g at t11 zorder 2
            mc "Huh. Weird."
            mc "Maybe you dating her childhood best friend is kinda awkward to her, still."
            mc "I wouldn’t think too much about it."
            show natsuki 2d at f11 zorder 2
            n "Yeah, you’re right."
            show natsuki at thide
            hide natsuki
        
    scene bg house
    with wipeleft_scene
    "Walking for a bit longer, Natsuki and I finally arrive back home after what felt like the longest literature club meeting of our lives."
    scene black
    with fade
#End scene 1

#Scene 2 - A Momento:
    scene livingroom
    with dissolve_scene_full
    "At home, Natsuki and I are prepared to put the day behind us and look ahead to tomorrow."
    "Or more precisely, ahead to tonight, as at around 5:30, Natsuki decides that she wants to start making dinner."
    mc "What do we have? I haven’t shopped in a little while."
    show natsuki 5g at t11 zorder 2
    n "You don’t say?"
    "She says that sarcastically as she opens a very painfully empty cabinet, letting the wind flow out of it."
    mc "S-sorry."
    n 4z "Hehe~! I’m just picking on you. I’d be happy to start making grocery runs for us."
    n 3d "You know, just as long as you learn how to clean after yourself better."
    show natsuki 3a at t11
    "Naturally I think back to the tornado, also known as me, that blew through my kitchen this morning when I tried to make breakfast."
    mc "Alright, I get it, no need to pick on me so much."
    n 1k "Did I hurt your feelings?"
    show natsuki 1n at t11
    "She says that with sincere concern."
    mc "No! Don’t worry!"
    n 1q "O-okay, good. I just don’t wanna actually hurt your feelings."
    show natsuki 1s at t11
    "A tsundere who {i}doesn’t{/i} want to insult me? Which slice-of-life manga did I wake up in this morning?"
    show natsuki at thide
    hide natsuki
    "I let Natsuki take control of the kitchen for the time being while she magically conjures up a dinner using nothing but instant noodles and soy sauce."
    "I remember that I left the bedroom a bit of a mess this morning and I adjourn to it to fix it up."
    scene bg bedroom
    with wipeleft_scene
    "I walk in and see mementos of our little experience and immediately start to get hormonal." #Uh wtf??? You mean emotional?
    "However, I choose to push the feelings down so I can focus on my chores."
    "Still..."
    "It’s weird knowing I’m not a virgin anymore."
    "I still feel just about the same, and I feel like Natsuki must feel the same way, too."
    "It’s not something I ever particularly cared about, but it’s comforting knowing I finally got to experience one of life’s greatest wonders."
    "And sharing that moment with a girl like Natsuki is something I’ll always treasure."
    "Once and for all I stop thinking about having sex...heh, awesome...then I start to pick stuff up off the floor."
    "Natsuki’s clothes sit on the ground and I pick them up, then throw them in the hamper to be washed."
    "I look at the box of belongings Natsuki brought with her and realize that this outfit I just picked up is just one of very few she managed to fit into it."
    "I ought to sacrifice some of the money from my parents’ stipend to let Natsuki go shopping soon."
    "Not to mention she might need some self-maintenance products like razors, shampoo, and other...feminine things."
    "I’m sure she has a lot of stuff at home, but I think she and I can both agree that we don’t want to venture back to her old house."
    "Her father must be infuriated with her and I both. I don’t want to see what happens if I were to see him face to face."
    "I’m scared I’d punch the son of a bitch in his mouth."
    "I finish picking up our dirty clothes, then I frustratingly attempt to make the bed."
    "Once these tasks are completed and the room is more liveable, I decide to take a break. I leave my bedroom and reunite with Natsuki."
    scene bg kitchen
    with wipeleft_scene
    "She’s in the kitchen cutting vegetables and boiling some water on the stove."
    "I have to give her credit, she’s doing a whole lot with very little at the moment."
    mc "What are you working on?"
    show natsuki 1b at t11 zorder 2
    n "Trying to make some noodles with steamed veggies."
    n 2d "Your pantry is not doing me any favors, but I can work some magic. Just trust me."
    show natsuki 2a at t11
    mc "I do trust you, Nats. Where’d you learn to cook so well anyway?"
    n 2t "Uh... it was... {w=0.25}my mom who taught me!"
    show natsuki 2s
    mc "Your mom? You haven’t mentioned her before, have you?"
    n 2u "..."
    mc "What's she like?"
    n 1q "Hey, uh, I don’t really want a lot of distractions right now, so do you think you could, like..."
    show natsuki 1s
    mc "O-oh, s-sure, no problem. Sorry to disturb you."
    n 1h "It’s okay, [player]. You should be finishing your chore too, you know?"
    show natsuki 1g
    mc "Well pardon me for wanting a break! Ahaha."
    n 5w "We don’t take breaks in this house! We take action!"
    show natsuki 5g at t11
    mc "You don’t decide what we do in this house!"
    n 5y "Give it time. You’ll learn that I can be {i}veeery{/i} persuasive."
    mc "Heh, I’ll hold you to that."
    show natsuki at thide
    hide natsuki
    "I leave the kitchen then return to the bedroom prepared to return to my tasks."
    scene bg bedroom
    with wipeleft_scene
    "I walk up to the box Natsuki brought with her and sift through it for a few moments, mentally preparing places where her belongings can be safely stored."
    "As I’m looking through, I catch sight of something at the bottom."
    "I reach into it and it feels dense, with the texture of worn leather."
    "I wrap my fingers around it, then pull it out, careful not to inadvertently let anything above it spill out onto the floor."
    "Extracting the curious item, I see that it’s a large leather-bound book, which appears to be several decades old."
    "I open the front cover, and written in very well-preserved calligraphy, it reads, {i}The Shimizu Family Cookbook.{/i}"
    "Huh. I wonder what’s inside."
    "I very delicately flip through the pages of the book, as it seems any careless motion can tear one of these ancient pages."
    "It’s filled with dozens of noodle, rice, meat, and seafood dishes, as well as lots of desserts."
    "I notice that the handwriting has some variation, implying that this has been written in by multiple people."
    "Sometimes there are notes in the margins in different handwritings on the same recipe, with suggestions for ingredient substitutes or different portion sizes."
    "From what I can gather, this is a cookbook spanning several generations of women in Natsuki’s kin."
    "I even see one or two cupcake recipes that Natsuki herself seemed to write into this book."
    "This is incredible! I have to ask her more about this."
    scene bg kitchen
    with wipeleft_scene
    "Cookbook in hand, I power walk my way back to the kitchen to smell some noodles and vegetables being cooked to perfection."
    "I feel extra encouraged to try Natsuki’s home cooking now that I’ve been acquainted with this book."
    "Natsuki turns toward me and smiles."
    show natsuki 1a at t11 zorder 2
    n 2l "Dinner’s almost rea--{nw}"
    show natsuki 1v at d11
    n "HEY!"
    "She notices the book in my hand, then dashes toward me, and instinctively I pull it away and above her head so she can’t reach."
    "At that moment, Natsuki knees me in the stomach, forcing me to lower the book toward my chest, and she snatches it from me."
    mc "Natsuki!"
    mc "What the hell!"
    n 1p "Oh my god! [player] I’m so sorry!"
    n 1m "I didn’t mean to do that! Are you hurt?"
    show natsuki 1n
    "The wind is a bit knocked out of me, but I regain my composure and take a deep breath and settle myself."
    mc "I-I’m fine."
    "Natsuki grabs my hand apologetically, then sets the book down on the table beside us."
    n 1u "I’m sorry. I just...don’t like other people touching this."
    mc "I’m sorry... I happened to look through it a little bit."
    mc "My curiosity got the best of me."
    n "No, it’s... fine."
    mc "Is there something you’re trying to hide from me, Natsuki?"
    n 1q "N-n-no! It’s nothing."
    n 1s "It’s just an important family heirloom and I wouldn’t want anyone damaging it."
    show natsuki at thide
    hide natsuki
    "The implication with those words is that she doesn’t trust me, but it’s not important."
    "I’m more zeroed in on the hesitation she had when I asked if she was hiding something."
    "I can tell that, in fact, she is, and won’t spill it."
    "I’ll ask her about it after dinner and the table is prepared, because it seems to be something important."
    "After Natsuki and I set the table, I examine all the food she’d prepared for us."
    "Delightful rice, noodles with some nose hair-singing spices, and steamed vegetables."
    "She also managed to prepare some miso soup, which I’m about 90 percent certain I didn’t have the ingredients for."
    "She definitely did some wacky voodoo stuff while I wasn’t looking, but as long as we’re eating good, I won’t complain."
    "Once we divvy up the dishes, Natsuki and I sit and eat in a pronounced silence for several minutes."
    "I look at her, but she’s not making eye contact with me. She looks at the book beside her after every other bite she takes."
    "Natsuki finally does look up at me and sees my utensil-less right hand and empty mouth."
    show natsuki 1k at t11 zorder 2
    n "How come you aren’t eating?"
    show natsuki 1j at t11
    "I take a deep breath, trying to gather all the thoughts I need in order to say what I have to say as delicately as possible."
    "However, Natsuki seems extremely worried."
    n 1m "I... didn’t do a good enough job for you, did I?"
    show natsuki 1n at t11
    "Wait what?"
    n 1u "I’m sorry, I should’ve known you wanted meat with all of this."
    n 12e "I wish I could’ve prepared something else, I..."
    show natsuki 42f at t11
    "Natsuki begins to well up, and I’m close to panicking."
    "I know that Natsuki has had trouble with confidence in the past. She gets this hopeless look in her eye when she feels like she isn’t good enough."
    "I’ve seen it when she’s shared poems with me, and I was always happy to assure her that I think very highly of everything she does and sets out to do."
    "Right now will be no different."
    mc "No, no, Natsuki, I promise you it’s all great!"
    mc "I couldn’t ask you to do much more than this, you did an incredible job here."
    mc "I just..."
    show natsuki 42h at t11
    mc "Natsuki, I’m worried about you."
    mc "You seem really tense about this cookbook thing."
    mc "And... you got very distant when I brought up your mom earlier."
    mc "If there’s something you need to talk to me about, just know I’m right here, and I want to know what’s going on."
    "Natsuki maintains the concerned expression on her face, then speaks up."
    n 42i "I don’t want you to worry about me."
    n "I don’t want you seeing that side of me, [player]."
    n 42f "I don’t want to be abandoned again..."
    mc "Natsuki I will never abandon you."
    mc "I’m taking the responsibility, a-as your boyfriend, to listen to your problems and understand you on a deeper level."
    mc "Please help me out here."
    n 42h "..."
    n 42e "You’re so...special to me."
    n "You mean the world to me, [player]."
    n 12g "I’m so grateful to you, so I won’t keep this in anymore."
    show natsuki 3u at t11
    "Natsuki puts her left hand on the recipe book, and strokes her fingers across it, as if she’s trying to absorb its aura."
    n 3q "This book..."
    n "It belonged to my Mama."
    n "And her mama before her."
    n "It's been passed down and passed around for generations for a few decades now."
    n "My mom was the last person to own it before me."
    n "I just don’t like to talk about her, because it...hurts me, and I’m scared you’ll think I come with way too much baggage and you’ll leave me, which would hurt me even more."
    show natsuki 2n at t11
    mc "Natsuki, I’m your boyfriend. I vow to you that I’ll never leave you because you’ve been through hard stuff in the past."
    mc "I want you to tell me about your mom. As long as you’re comfortable with it."
    n 3u "..."
    n 3q "I wasn’t super comfortable with it before, but..."
    n 3m "You changed that really quickly."
    n 1m "So I'll go ahead and tell you."
    show natsuki 1u at t11
    "Natsuki takes a deep breath, as if she requires all the oxygen in this room for what she’s going to say next."
    n 1h "My mom was...the best lady I knew."
    n "And... {w=0.25}when she was with my dad..."
    n 1n "My dad was a good person."
    n 2q "And... their marriage wasn’t perfect, but... {w=0.25}they loved each other, and they loved me."
    n 2u "And I loved both of them so much."
    show natsuki 12d at t11
    "Natsuki clenches her eyes closed, trying to block off any tears from escaping."
    show natsuki 12g at t11
    mc "Natsuki, you don’t have to feign strength for me. I promise I won’t judge you for crying."
    show natsuki 12f at t11
    "As I say this, Natsuki starts to sob and take rapid breaths for several moments before regaining her composure."
    show natsuki 12d at t11
    "She sighs, then continues."
    n 1u "So... {w=0.25}when I was eight years old, my parents and I took a road trip together."
    n 1q "Everything was... going fine, but..."
    n "It was late at night, and my parents were both tired and cranky from being on the road."
    n 1u "One thing... {w=0.25}led to another, and eventually..."
    n 1q "We crashed."
    n 1u "My Mama..."
    n 42d "..."
    n 42e "She didn't make it."
    n "She died on impact."
    show natsuki 42f at t11
    mc "Natsuki..."
    show natsuki at thide
    hide natsuki
    scene black
    with fade
    "I stand up and walk over to her, letting the horrific tale she just told me enter my brain."
    "It’s hard to process, but I’m trying my hardest."
    "I give Natsuki a hug as she cries into my chest."
    mc "It's okay, Nats..."
    mc "You can stop there for tonight."
    mc "I don't want you to feel too hurt."
    mc "But I’ll be here to comfort you tonight, and every night for the foreseeable and unforeseeable future."
    n "[player]..."
    mc "Yeah?"
    n "I already told you... no nicknames."
    "Her sobs start to slowly fade into giggles, and I squeeze Natsuki tighter."
    mc "Don’t play with fire, or you’ll get burned."
    "Natsuki and I share a laugh as we continue to hug."
    mc "I hope you aren’t mad at me for prying so much."
    n "N-no... {w=0.25}you weren’t..."
    n "I’m glad I told you."
    n "You gave me the strength I needed to take this step with you."
    n "I feel like we can trust each other so much more now that I told you my secret."
    mc "Do you have more to tell me?"
    n "..."
    n "Yes. But not right now."
    scene bg kitchen
    with dissolve_scene_full
    "I return to my seat and finally begin eating Natsuki’s delicious food."
    "I’m in pure bliss with every bite, and I’m so lost in it that I don’t notice her leave the room."
    show natsuki 2u at t11 zorder 2
    n "I was just... putting the book in a safe spot."
    n 2s "Thank you again for being so understanding..."
    n 2d "And not pressing charges for me kicking you in the stomach."
    show natsuki 2a at t11
    mc "Ahaha, this amazing food is enough recompense for what you did."
    n 2z "Ehehehe~!"
    n 2l "You’re a dork."
    n 1j "And... {w=0.5}I love you."
    mc "I love you too, Natsuki."
    show natsuki at thide
    hide natsuki
    "I continue to eat, and so does Natsuki."
    "Whether she wants to admit it or not, she and I are each other’s family now."
    "And I treasure getting to have a family dinner with her."
    "Like I treasure every moment the two of us share."
    "Natsuki... I will hold onto you and never let go..."
    "She and I are going to continue to thrive in this home..."
    scene black
    with fade
    "In {i}our{/i} home."




    scene end
    with fade
    "Thank you for playing DDLCtVN Natsuki Route!"
    return
