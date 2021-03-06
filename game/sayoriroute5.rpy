label sayoriroute5:
    scene black
    with fade
    s "..."
    s "..."
    s "..."
    s "...{i}That's where you'll find...me..."

    call sayoriroute51
    call sayoriroute52
    call credit_sequence
    "Thank you for playing DDLCtVN Sayori Route!"
return

label sayoriroute51:
#{Interlude between h-scene and scene 8 includes a sequence of Sayori in the dark of MC's bedroom crying, then leaving}
#{Scene starts in the morning}
    
    scene bg bedroom
    with fade
    
    play music t12
    "I open my eyes after an eventful night, and eight well-earned hours of sleep."
    "I don't see Sayori next to me, so I assume she's in the bathroom and will walk back in at any moment, meaning I should probably just wait for her..."
    "...unfortunately, my bodily functions have other plans."
    "I suddenly have to use the bathroom like a wild dog."
    "I stand up, then power walk to the bathroom at the end of the hall, which in this scenario is quite a harrowing journey."
    scene black
    with wipeleft_scene
    "I knock on the door to get Sayori's attention."
    mc "Sayori I hope you're brushing your teeth because I'm coming in and I need to use the toilet!"
    "I open the door, then take myself to the glorious porcelain structure."
    "I perform my activities, and breathe a deep sigh of relief after a pretty agonizing 45 seconds."
    "My mind is so focused on the relief, that it takes me a few moments to realize..."
    mc "Oh, Sayori isn't in here."
    "I don't know why I said that out loud. Perhaps to prove to the ghost that lives in the shower drain that I'm not crazy."
    "Regardless, I finish using the bathroom, then leave."
    scene bg bedroom
    with wipeleft_scene
    "I go back to my room to see if Sayori has returned from wherever she was while I was doing my business."
    "She hasn't."
    mc "Huh."
    mc "Sayori?"
    "I call her name out, expecting a response, but get none."
    mc "Sayoriii!"
    "I do the same, slightly louder, but receive the same silence."
    "I'm certainly confused, but I realize, she must've gone home to get something."
    "In that case, I expect she'll be back in the next 20 minutes."
    "I decide to adjourn to the kitchen to make us some breakfast for when Sayori comes back."
    scene bg kitchen
    with wipeleft_scene
    "Considering what she told me yesterday about not feeling like she does enough for me, I choose to not make anything too special."
    "Eggs and toast should be sufficient."
    "I'm thankful that my cooking skills have become at least passable over the last few years, otherwise I'd be in a lot of trouble."
    "As I finish making our food, I check the time."
    "I started cooking about ten minutes ago."
    "Hopefully Sayori comes back soon."
    "I consider calling her, but I feel like she doesn't want to be treated like a child all the time."
    "I decide to wait, while taking small bites of my food."
    "Eating by myself isn't an issue to me, but there's something that amplifies how depressing it can be when you're watching steam float off the plate on the other end of the table."
    "Regardless, I choose to wait for Sayori."
    "One minute...two minutes...three minutes..."
    "Four minutes...five minutes...six minutes..."
    "Seven minutes...eight minutes..."
    "Nine...minutes..."
    "Um, okay, something feels off now."
    "I still haven't heard from Sayori and she hasn't come back."
    "I think I should call her."
    "I decide to go stand outside and get some fresh air, which is certainly needed after last night."
    "Plus, maybe Sayori will be on her way back as I'm calling her."
    stop music fadeout 1.5
    scene bg residential_day
    with wipeleft_scene
    "On the porch, I call her phone."
    "It's ringing, but she doesn't pick up."
    "I listen more closely, then I hear something faint in the distance."
    "I keep trying to call her phone, but now I'm walking toward the sound I hear."
    "The closer I get to it, the more concerned I become."
    "Because the closer I get to the noise, the more recognizable it becomes."
    "And the closer I get to the noise, the more I realize where I'm headed."
    scene black
    with fade
    "Once I finally reach the noise..."
    scene bg house
    with fade
    "{i}I'm at Sayori's front door."
    "My heart drops, because I see Sayori's phone sitting on her porch..."
    "But no Sayori."
    "With no regard for the safety of my own phone, I drop it, then barge into Sayori's house."
    "I walk inside and start yelling her name."
    mc "Sayori!"
    mc "Sayori, are you here? Please tell me you're here!"
    scene bg sayori_bedroom
    with wipeleft_scene
    "I dash up to her bedroom and go inside."
    mc "Sayori?!"
    "She isn't here."
    mc "{i}Dammit!"
    "I look throughout the rest of her house."
    "No sign of Sayori anywhere."
    "I feel so helpless right now."
    "My girlfriend is missing and I have no way of finding her."
    "I have to do something..."
    "Anything..."
    scene bg house
    with wipeleft_scene
    play music t13
    "I have an idea, then I run back outside."
    "I spot where I dropped my phone on the concrete."
    "I pick it up and see that the screen is shattered."
    mc "Dammit, dammit, no, not now!"
    mc "Come on please still work..."
    "I turn it on and unlock it, and thankfully the touchscreen is still responsive."
    "As long as that's the case, I can deal with this phone issue much later."
    "Right now, I'm in desperate need of help, and I know just who to call."
    
    if distraction == 'Monika':
        mc "Pick up, pick up, pick up..."
        m "Hello?"
        mc "Monika!"
        m "Hey, [player], is everything--"
        mc "Monika, is Sayori with you?!"
        m "N-no, I'm sorry, she's not. You haven't seen her?"
        mc "Not since last night. When I woke up this morning she was gone, and she left her phone at home, and Monika I'm really scared--"
        m "Hey, hey, [player], please try to relax, okay? I'm sure she's fine."
        m "Listen, do you want me to help you find her?"
        mc "Yeah I'd really appreciate that."
        m "Okay, I'll be over there in a few minutes, just stay where you are."
        m "We're going to find her. Everything will be okay."
        mc "Th-thank you, Monika."

        scene black
        with fade
        
        "A few minutes later, Monika's in the neighborhood."
        "I wish she'd gotten here as fast as she did yesterday given the circumstances, but I choose to withhold my frustration."
        "She still got here remarkably fast."

        scene bg house
        with fade

        show monika 1bd at t11 zorder 2
        m "Hey, [player]."
        m "Tell me, where do you think Sayori could've gone to?"
        show monika 1bc at t11 zorder 2
        mc "I-I'm really not sure. If anywhere I thought she'd be at her house, or with you talking about the club."
        m 1bd "I'm sorry, I wish she was."
        m "Let's just survey the neighborhood and see if we can find her anywhere."
        m "Maybe we can ask some of your neighbors if they've seen her around."
        show monika 1bc at t11 zorder 2
        "I take a few breaths, and I try to suppress my crying."
        "After the talk Sayori and I had at the park yesterday, I struggle to think about where she could've gone or why she decided to leave."
        show monika 1bf at t11 zorder 2
        "Monika notices my struggle."
        m 1bb "We'll find her."
        show monika 1ba at t11 zorder 2
        "Monika puts her hand on my shoulder and I nod, determined to find Sayori."
        scene black
        with fade
        scene bg residential_day
        with fade
        "Like she suggested, we decide to walk around the entire neighborhood, and I even knock on a few doors of neighbors I'm decently familiar with."
        "Every one of them told me the same thing."
        "'{i}I haven't seen her.'"
        "My tongue grows numb over these several minutes from saying the words, \"Thanks, anyway.\""
        "Every time I get an answer I don't want, another image of Sayori crying pops into my head."
        "I can't just let her be all alone out there, wherever she is."
        "I can't let her be alone with her thoughts like I'm alone with mine right now."
        show monika 1bd at t11 zorder 2
        m "[player], I hope you know you aren't alone right now."
        show monika 1bc at t11 zorder 2
        "{i}Did she just read my mind?"
        m 1bd "If you've got something to tell me, I want you to."
        show monika 1ba at t11 zorder 2
        "Monika's being a lot more supportive than she's ever been before."
        "This change in her demeanor really makes me feel closer to her as a friend."
        "Up to this point, she's always just struck me as the president of the club, and someone who's in a league above me, but I'm starting to realize now..."
        "She's only human, like me. She's capable of being a friend."
        stop music fadeout 1.5
        "I'm grateful to her for that at this moment, so I owe her the whole truth."
        play music t9
        show monika 1bf
        mc "Monika, yesterday, on our picnic, Sayori started to feel really down on herself."
        mc "She thought that me doing all of that for her was proof that I'm better to her than she is to me, and it made her feel insecure."
        mc "All I could do was convince her otherwise, because when she has those kinds of thoughts, I feel responsible for making sure she doesn't have them anymore."
        mc "When she's not around, I feel like she's in a lot of danger."
        mc "She's trapped with her thoughts..."
        show monika 1bc at t11 zorder 2
        mc "With her....{i}rainclouds."
        mc "It's why I've constantly tried so hard to make her feel better, and I've been willing to do just about anything to get her mind off things."
        mc "Sayori can't be by herself in her condition."
        mc "I love her and when I started to date her, I vowed to protect her however I can."
        show monika 1bf at t11 zorder 2
        "I realize that tears are pouring down my cheek as I tell all of this to Monika."
        "I can't say I've let myself be vulnerable to anybody like this before."
        "But I know I can trust Monika to be supportive."
        m 1bg "[player]..."
        m 2bb "I don't think you realize how great of a person you are."
        m 2be "Sayori's lucky to have you."
        show monika 2ba at t11 zorder 2
        mc "*sniffle* Thank you, Monika."
        mc "I'm just at a loss for what to do now."
        mc "Without her phone on her, and without anyone seeing her, she might as well have fallen off the face of the earth."
        m 2bg "I know you don't want to, but I think it'd be best for you if you went home for a little while."
        m "Just try getting your mind off things, and I'll go look for her."
        m "I'll call you if anything comes up, okay?"
        show monika 2be at t11 zorder 2
        "I can't find it in myself to go home at a time like this, but I feel compelled to trust Monika's judgment."
        mc "O-okay, Monika. I'll talk to you soon."
        m 4bk "See you later, [player], I'll do my best."
        m "And hey, who knows, maybe Sayori will be at home now!"
        show monika 2bj at t11 zorder 2
        "I have my doubts about that, but I thank Monika for saying anything to keep me reassured."
    
    elif distraction == 'Yuri':
    #{ In the Yuri branch, Yuri has trouble finding the right things to say to MC and starts to feel bad.}
        "I take a deep breath and try to steady myself."
        "Yuri will know what to do."
        "I pick up the phone and dial her number with shaking hands."
        "The phone barely has time to ring before she picks up."
        mc "Hey Yuri." 
        y "Hey [player], what's the matter?"
        "I guess even Yuri can read my voice right now."
        mc "Sayori ran away."
        y "What do you mean?"
        mc "Well, when I woke up this morning she was gone, I checked my house and hers, and all I could find was her phone that she left on her front porch." 
        y "I-I...never imagined Sayori would do something like that."
        mc "I didn't either. She seemed to be working through her dep--problems, pretty well."
        y "Why did you call me, of all people?"
        mc "Well, you helped me out a lot with the picnic, and you're so reliable during meetings."
        y "O-oh, well, thank you, [player]. Do you want my help looking for her?"
        mc "If you wouldn't mind, that would help me a lot right now."
        y "I'll be there as quickly as I can."
        mc "Thank you so much."
        y "No problem, see you soon."
        "Yuri hangs up the phone."

        scene bg livingroom
        with wipeleft_scene

    
        "About ten anxious minutes go by before I hear the doorbell ring."
        "I open the door and greet Yuri, before stepping out onto the porch with her."

        scene bg residential_day
        with wipeleft_scene

        show yuri 1bf at t11 zorder 2
        y "So, you said you've checked your house and hers?"
        show yuri 1be at t11 zorder 2
        mc "Yeah, I searched both top to bottom. I can't think of any reason she would be hiding in her house or mine anyways."
        y 1bf "Well, I'll take your word for it. Where else do you think she could have gone?"
        show yuri 1be at t11 zorder 2
        mc "I can't think of many places she would have gone. Maybe somewhere around town?"
        y 1bf "I've noticed her around the coffee shop I go to sometimes, maybe she could be around there?"
        show yuri 1be at t11 zorder 2
        mc "Yeah, we've been there, I think."
        y 1bb "Okay, let's go."

        scene black
        with fade

        "We take the familiar path up to the city, and even with Yuri around it feels lonely."

        scene bg cafe
        with fade

        show yuri 1bf at t11 zorder 2
        y "Is this the place?"
        show yuri 1be at t11 zorder 2
        "We stand in front of the coffee shop."
        mc "Yeah, me and Sayori have come here a few times."

        scene bg cafe_in
        with wipeleft_scene
        stop music fadeout 1.5

        "Stepping inside, the store is fairly empty, with only a few people sitting around the small tables."
        "We look around and Yuri even checks the bathroom, but Sayori is nowhere to be found."
        show yuri 1bf at t11 zorder 2
        y "I don't think she's here."
        show yuri 1be at t11 zorder 2
        "My breath catches a little with disappointment, and the worry on Yuri's face grows."
        show yuri 1bt at t11 zorder 2
        mc "H-have any other ideas?"
        "Yuri notices my voice shaking."
        y 1bb "I'm sure we'll find her soon. It might be a long shot, but there's this bookstore I go to sometimes, and I've taken her there with me once. Maybe she went there for some reason?"
        mc "Yeah..."
        scene black
        with fade
        "I trail off as we walk back outside."
        "We walk through the busy streets for a while before eventually ending up at the bookstore."
        
        scene bg bookstore
        with fade

        show yuri 1bb at t11 zorder 2
        y "Well, this is the place."
        show yuri 1ba at t11 zorder 2
        mc "After you..."
        "Yuri gives me a faint but worried smile and start looking inside, with me following her."
        y 1bb "I'll check this side, you check from the other."
        show yuri 1ba at t11 zorder 2
        mc "Okay, sounds good."
        show yuri 1ba at thide
        hide yuri
        "We check the store, the narrow aisles making covering a lot of ground difficult."
        "Eventually we meet up at the front of the store again."
        show yuri 1be at t11 zorder 2
        mc "Did you find anything?"
        "I ask, already knowing the answer."
        show yuri 1bt at t11 zorder 2
        "Yuri frowns."
        y 2bf "No, nothing. Did you?"
        show yuri 2be at t11 zorder 2
        mc "No, I didn't find anything either."
        y 2bf "I think we should head back, it's starting to get late."
        show yuri 2be at t11 zorder 2
        mc "What?! We can't stop looking now, what if she got lost?"
        y 2bt "I'm not sure she could have gotten lost..."
        show yuri 2bw at t11 zorder 2
        stop music fadeout 1.5
        mc "Well, what if she--"
        "I notice how much Yuri is starting to worry."
        play music t9
        y 2bv "I-I'm sorry...that I wasn't of much help today."
        show yuri 2bw at t11 zorder 2
        mc "No, you helped me a lot. It would have taken me forever to look through the entire bookstore alone."
        y 3bq "Still, I've just been useless all day. I only sped up some stuff a little."
        y "You should have asked Monika or Natsuki for help, I'm sure they would have thought of something better."
        show yuri 3be at t11 zorder 2
        mc "At least you thought of something, all I did was worry."
        y 3bv "I've been useless all day, [player]."
        show yuri 3bw at t11 zorder 2
        mc "Don't say that, I--"
        "I sigh, defeatedly."
        "It's hard to listen to Yuri so down on herself."
        "Partly because she's my friend and I don't like hearing her say these things, and partly because I feel like I'm talking to Sayori again."
        "But...I'm not."
        "She's still not here."
        "{i}Why would she do this to me after everything we've been through?"
        mc "Why do you think Sayori would do something like this?"
        y 2bf "It's possible she thought she was still a burden to you."
        show yuri 2be at t11 zorder 2
        mc "Yuri, I've been with her for months now! If she had those problems we would have worked through them together, she's past that."
        y 2bf "All I'm saying is that these things can take a lot of time to work through, I know what it's like."
        show yuri 2be at t11 zorder 2
        mc "Sorry, but you and Sayori aren't the same person! Plus, I've been helping her through it this whole time. She's better than that."
        y 1bv "Y-you're right. I'm sorry."
        y "I really haven't been any help after all."
        show yuri 1bw at t11 zorder 2
        "I sigh."
        mc "No, I'm sorry. I shouldn't have blown up on you like that."
        mc "You've been a big help to me just by being here."
        y 2bu "I'm...relieved to hear you say that." 
        show yuri 2be at t11 zorder 2
        mc "I think we should get going now. It's getting dark, like you said."
        y 1bf "Right."
        show yuri 2bw at t11 zorder 2
        scene black
        with fade
        "We walk back to my house together and stop at my front door."
        scene bg residential_day
        with fade
        show yuri 1be at t11 zorder 2
        mc "Thanks so much for helping me look for her."
        y 1bf "Don't worry about it, this is very important to me too."
        y 1bb "And thank you for consoling me earlier."
        show yuri 1ba at t11 zorder 2
        mc "Yeah, I can say the same to you."
        show yuri 1bc at t11 zorder 2
        "We both laugh weakly."
        y 1bb "Well, I should get going right now. I have some things to do at home as well."
        show yuri 1ba at t11 zorder 2
        mc "Sure, I'll see you tomorrow."
        y 1bh "Hopefully Sayori will be back by then."
        show yuri 1be at t11 zorder 2
        mc "I really hope so."
        show yuri 1be at thide
        hide yuri
        "As I watch Yuri turn the corner, I unlock my front door and step inside."
        scene bg livingroom
        with wipeleft_scene
        "I sigh and flop down on the couch."

#{ In the Monika branch, Monika helps to reassure MC that Sayori will be okay. }
#{ I'd say about two pages are needed here to match the Monika branch. Have MC and Yuri search for Sayori around town instead of the neighborhood, like around the library and cafe }

    elif distraction == 'Natsuki':
#{ Natsuki feels scared about Sayori, and MC ends up having to comfort her instead }
#{ They look for her around school }

        "Like yesterday, I call up Natsuki."
        "She answers pretty quickly."
        n "Hello?"
        mc "Natsuki, do you know where Sayori is?!"
        n "N-no, I don't. S-Sayori's missing?"
        mc "Yes, and I have no idea what to do. She left her phone on her porch, I have no way of finding her."
        n "Where have you tried looking?"
        mc "Not a lot of places yet...just around our houses."
        n "Maybe she just wanted to be by herself somewhere."
        n "Y-yeah, I'm sure that's it."
        mc "Natsuki, are you okay?"
        n "Huh?"
        n "Oh, yeah, I'm fine."
        n "Um, so listen, I know you probably want my help looking for her, so what do you say we meet at school?"
        mc "W-why at school?"
        n "Well, first of all because it's right in the middle of where both live."
        n "And second, well..."
        n "I'll tell you when we get there."
        "Without a warning, Natsuki hangs up the phone, leaving me no choice but to follow her instructions and meet her at school."

        scene bg school
        with wipeleft_scene

        stop music fadeout 1.5
        "About ten minutes later I've walked the familiar walk from my neighborhood to our school, and inside see Natsuki standing by some lockers."
        show natsuki 1bk at t11 zorder 2
        n "H-hey, I'm glad you came."
        mc "I should be saying that to you."
        mc "Thank you for helping me out."
        mc "I just can't imagine where Sayori might've gone to."
        mc "After today I owe you big time."
        n 1bb "D-don't say things like that, [player], Sayori's my friend too."
        n "I want her to be okay, I don't owe you anything."
        show natsuki 1bg at t11 zorder 2
        mc "If you insist."
        mc "S-so, uh, I guess let's start looking."
        n 1bk "Y-yeah."

        show natsuki at thide
        hide natsuki

        scene bg corridor
        with wipeleft_scene
        "Natsuki and I walk around the first floor of the school and don't find much."
        "We come across some students who have obligations to attend to over the weekends, like designing banners for school events and whatnot."
        "We also come across teachers who have meetings or the like among each other."
        "We keep asking around if anyone has seen Sayori."
        "I'll admit, a lot of the students are wearing street clothes, and I didn't recognize many of them because of that."
        "If Sayori was here, I'd imagine some people would also have the same trouble, if not for her big red bow."
        "Thinking about Sayori's bow makes me smile momentarily, but then I break down a little bit."
        "I stop walking and prop myself up against the wall."
        show natsuki 1bc at t11 zorder 2
        n "Hey are you okay?"
        mc "..."
        n 1bb "[player], come on."
        show natsuki 1bg at t11 zorder 2
        mc "I...I can't..."
        n 1bb "[player], c-come on, don't be a dummy."
        n "Look, we haven't even checked the clubroom yet."
        n "If she's at school, I'd bet a million bucks that's where she is."
        show natsuki 1bg at t11 zorder 2
        "All I can do is nod, and let Natsuki take the lead."

        show natsuki at thide
        hide natsuki

        "We walk up a flight of stairs and walk down the hallway that I've become very well-acquainted with this year."
        "Seeing the pep in Natsuki's step as she leads us toward the clubroom gives me some confidence."
        "She's doing everything she can to make me feel better, and feel confident that we'll find Sayori here."
        "She did such a good job, that for a moment there, I was certain that we'd find Sayori in the Literature Club room when we opened the door."

        scene bg club_day
        with wipeleft_scene

        "Natsuki reaches the door to the clubroom and swings it open."
        show natsuki 4bb at t11 zorder 2
        n "Sayori! You in here?"
        "No response."
        "Just like that, I lose all my faith and I'm back to square one."
        n 4bm "She's...not here."
        n "B-but that's okay, I'm sure she's somewhere."
        mc "Natsuki..."
        n "We still have the cafeteria to check."
        n "Maybe she's looking for something to eat."
        mc "Natsuki--!"
        n "W-well I guess if she was at your house she wouldn't have to come all this way for some food."
        n "But it doesn't hurt to look!"
        mc "Natsuki!"
        show natsuki 1bp at t11 zorder 2
        "Natsuki stops dead in her tracks."
        "I've never raised my voice like that to her, and it seems like she squirms at the sound."
        show natsuki 1bi at t11 zorder 2
        mc "I'm...I'm sorry for yelling, but..."
        mc "I don't think she's at school."
        mc "We've checked pretty much everywhere."
        n "Um..."
        n 3bu "N-not everywhere!"
        show natsuki at thide
        hide natsuki
        scene bg corridor
        with wipeleft_scene
        "Next thing I know, Natsuki's walking out the door, then wordlessly begins leading me somewhere else."
        "We approach a staircase and climb it, then see a door out to the roof."
        "{i}Does Natsuki really think Sayori would be up here?"

        scene bg schoolroof
        with wipeleft_scene
        play music t13
        "Natsuki opens the door out to the roof and starts looking around, and only after she's already walked across the entire surface is when I humor her and walk out there myself."
        show natsuki 1bb at t11 zorder 2
        n "Sayori!"
        n 1be "Sayoriiii!"
        mc "Natsuki, she isn't here."
        show natsuki 1bf at t11 zorder 2
        mc "What makes you so sure she would've come up here anyway?"
        n 1bg "..."
        n 12bc "It's...because..."
        n "This is where Sayori and I became friends."
        show natsuki 12bd at t11 zorder 2
        stop music fadeout 1.5
        mc "W-wait, really?"
        show natsuki 12bb at t11 zorder 2
        "Natsuki nods."
        play music t9
        n 12bc "This place is special to me. It's where the best friendship I've ever had started."
        n "Before I joined the club, I'd come up here to read manga, then one day, out of nowhere, Sayori showed up."
        n "I had actually recognized her from a time we met at the vending machines."
        n "She was actually really excited to see me for some reason, and we talked for a little while."
        n "That's when she convinced me to join the Literature Club."
        show natsuki 12bb at t11 zorder 2
        mc "I...I never knew that part."
        "Now that I think about it, Sayori did say she'd tell me that story later."
        n 4bx "Th-that's why I thought she'd be at school, and why I thought she'd be up here."
        n 4bm "I guess I just think more of that moment than she does."
        n "For her, it was probably one of a bunch of happy moments she has every single week."
        n "For me...it was life-changing."
        show natsuki 4bg at t11 zorder 2
        "This is crazy to hear."
        "I knew Natsuki and Sayori were close, but I didn't think Sayori meant that much to Natsuki."
        mc "Natsuki, I think you're wrong about something."
        mc "I guarantee you that moment was as important to Sayori as it was to you."
        mc "Believe it or not, happy memories like that are few and far between for her."
        mc "If this is where she became best friends with someone so near and dear to her, then..."
        mc "I think you had the right idea in mind."
        mc "I just really wish she was up here."
        n 1bm "[player]..."
        show natsuki 1bg at t11 zorder 2
        mc "Yeah, Natsuki?"
        n 1bm "I'm scared."
        n "I don't want Sayori to be missing."
        n "I want to find her more than anything."
        show natsuki 42bf at t11 zorder 2
        "Natsuki starts crying, and reluctantly I walk up to her and give her a hug."
        show natsuki at thide
        hide natsuki
        "I start sniffling back, and a single tear pours down my cheek."
        mc "I wanna find her too."
        mc "I can't let her be alone."
        "After Natsuki and I accept defeat at the school, we both decide to go home."
        "It stings to have not gotten anywhere, but at a time like this, where both Natsuki and I are in distress, it's best for us to take a break."

#{PATHS RECONVERGE HERE}
    stop music fadeout 1.5
    if distraction == "Natsuki" or distraction == "Monika" :
        scene bg livingroom
        with wipeleft_scene
        "I arrive at home once again, feeling as defeated as any one person can feel."
    "I keep asking myself if there's something I could've done differently."
    "The thought of driving Sayori away stings more than any wasp or scorpion ever could."
    scene bg bedroom
    with wipeleft_scene
    "I lie on my bed, breaking down more and more each passing second."
    "I groan, moan, and bloan, which is not even a word yet I do it anyway."
    "My nose is red, and tears continue to pour down my cheeks."
    mc "Sayori..."
    mc "Sayori...!"
    mc "Dammit, Sayori, where are youuu?!"
    "I must look pathetic right now, but if a bus full of judgmental eighth graders passed through my bedroom right now, I wouldn't care."
    "There's nothing in the world that can take me lower than I am right now."
    "A half hour passes at home, and I don't hear from anyone."
    "The more silence that persists inside my bedroom outside of my involuntary noises, the more hope I lose."
    "What could I have done differently to keep Sayori around?"
    "Was I not supportive enough of her?"
    "Is it possible I was {i}too{/i} supportive of her?"
    "Whatever the case may be, these thoughts continue to haunt me."
    "It seems as though I'm finally experiencing what Sayori refers to as a raincloud."
    "I open my busted phone and go over to my photos."
    "I look at the pictures Sayori and I have taken over the last number of months and years."
    "The innocent look of ignorance inhabits my face in every single one, while on Sayori's face, I can detect the pain in her eyes."
    "I can't believe I never knew about her depression before recently."
    "I should have been more attentive."
    "I should have helped her sooner."
    "But now I can't help but feel like it's my fault she's missing."
    "I drop my phone on my bed beside me, then slam my head against my pillow multiple times."
    mc "Dammit, dammit, dammit!"
    "I'm a miserable creature."
    "I stop hurting myself only to hear my ears ringing..."
    "Then when that ringing stops, I hear...a different ringing."
    "It's my phone!"
    "I pick it up, hoping it's a friend with good news."
    "I look at my screen and see nothing but a phone number with a local area code."
    mc "You gotta be kidding me."
    "Any other day I'd hang it up completely, but at this point, I'll answer anything."
    "I answer the call."
    mc "H-hello, [player] speaking."
    "..."
    "I hear nothing for a moment, and prepare to hang up, that is until, out of the corner of my ear I hear..."
    s "[player]?"
    "Oh my god."
    mc "Sayori?! Sayori, is that you?!"
    s "Y-yeah, it's me, [player]."
    mc "Sayori, where did you go? Why did you leave? What's going on?!"
    "Sayori's voice is gentle, completely opposite of mine."
    s "[player], do you remember when we were little, and we used to go to that pond?"
    "My memories are a tad hazy at this moment, especially, but I manage to reclaim a memory from once upon a time."
    "Then another, then another, then another until the entire anthology of Sayori and myself is as plain as day."
    mc "I think so, Sayori."
    s "Hehe...come find me."
    "The call ends."
    "I sit there motionless, feeling so many things at once."
    "I know Sayori likes to play games, but at a time like this..."
    "Still, I know where she is, and I know how to find her again, and that's more than I was able to say just five minutes ago."
    scene bg livingroom
    with wipeleft_scene
    "I leave my room with all my necessary belongings, then prepare to make the trek back to a place from my childhood."
    "I take a deep breath, and I exit my house."
    scene bg residential_day
    with wipeleft_scene
    play music t12
    "In a sheer moment my mind recalibrates itself to how it was when I was eleven years old."
    "I take a turn out of my street, then walk a block down."
    "I take a right at the big sakura tree (it's not in season, but I still very distinctly remember the tree itself)."
    "Then I walk down the rocky path that leads to the pond."
    scene bg pond
    with wipeleft_scene
    "It's a walk Sayori and I took about a hundred times when we were kids."
    "It's no small source of memories for me."
    "And to think I never even thought to look for her at this pond..."
    "{i}Have we really grown up that much?"
    "As I approach the water on the horizon, I look directly forward."
    "In the distance, I see..."
    "Sayori."
    "The love of my life."
    "The girl I thought I lost today."
    "I see her, still wearing her pajamas from last night."
    "I take a closer look at her and notice that she's completely barefoot."
    "I wonder if she was sleepwalking last night."
    "She's never had that issue in the past."
    "Besides, if she was sleepwalking, would she have gone out of her way to leave her phone on her porch?"
    "I put these thoughts aside as I get closer to her, then I stand to her right and see her face."
    "She's drowning in her own sweat, or tears, or both."
    "Her bare feet are colored dirt brown and concrete black from walking around all day with no shoes, not to mention her hair is a total mess."
    "{i}What the hell did you put yourself through today, Sayori?"
    "I have to imagine the look of terror I have on my face is alarming."
    "Sayori finally turns her head up toward me."
    "She puts on a smile, then tilts her head."
    show sayori pjd at t11 zorder 2
    s "Congrats."
    s "You win."
    show sayori pjk at t11 zorder 2

return

label sayoriroute52:
    "There's a lot of things going through my head right now, namely in regards to my first action here."
    "I don't know whether to scold Sayori, or celebrate finding her."
    "Something tells me that Sayori herself doesn't even know what she expects or deserves here."
    "My brain goes into overdrive. Truth be told, I'm very overstimulated right now."
    "All I can really do is..."
    mc "Sayori!"
    show sayori at thide
    hide sayori
    "I throw myself onto Sayori and start sobbing. I squeeze her in a tight embrace, possibly tighter than any human should hug another human."
    "I can't tell how Sayori is feeling now, but I realize she isn't hugging me back."
    mc "S-Sayori..."
    mc "I was so scared..."
    "Sayori's arms are still limp at her side."
    "I've never seen her look so...drained."
    s "[player]..."
    mc "Yeah, Sayori?"
    stop music fadeout 1.5
    s "...would you please let go of me?"
    "I feel like an arrow has gone through my heart hearing this."
    "I do as she asks, but I feel like I've reached a new level of worthlessness."
    show sayori pjk at t11 zorder 2
    mc "Sayori...what's going on with you?"
    "She doesn't answer me right away."
    "I continue to look her in the eye to encourage me to tell me."
    mc "Sayori, I spent all day looking for you."
    if distraction == 'Monika':
        mc "I asked Monika to help me look for you around the neighborhood."
    elif distraction == 'Yuri':
        mc "I asked for Yuri's help to look for you around town."
    elif distraction == 'Natsuki':
        mc "Natsuki and I tried looking for you around school. She was so worried."

    mc "I'm just having such a hard time trying to understand why you did this, Sayori..."
    mc "Ever since you told me about your depression, I've done all I could to help you feel better."
    show sayori pjv at t11 zorder 2
    mc "I told you once upon a time that I would make this go away, and I've worked so hard to do exactly that."
    mc "I just feel so..."
    "Don't say it."
    "Hear her out."
    "Don't bring your own feelings into this."
    "Learn from the past."
    mc "Sayori, will you please explain why you did this?"
    s pju "..."
    s pjv "...I feel like I'm at the end of my rope, [player]."
    play music t10
    s pjk "You've let me drag you down for too long."
    s "Compared to what you've done to make me happy, I've done nothing."
    s "I'm more worthless than the dirt on my feet right now."
    mc "Don't say that, Sayori!"
    s pjw "But it's {i}true{/i}, [player]!"
    s "How can I ignore something so true?!"
    s pjv "I used to be so proud of myself for being able to put a smile on all my friends' faces, but lately all I've done is make things worse!"
    s "Making other people happy is the only thing that gave me a purpose."
    s "It's the only thing that I was any good at."
    s pjk "But now even you've proven that I was never any good at that to begin with."
    s "That picnic you made for me..."
    s "It proved that all I do is burden people."
    s "I've tried so hard to convince myself it's not true, but..."
    s pjh "The more time I spend with you, the more I realize how pointless my existence is."
    s "All I do is think about ways to make people happier."
    s pjh "I think about ways to help Monika's role as club president easier, but all I'm capable of is getting on her bad side."
    s pjh "I think about how I can help Yuri feel more comfortable around each of us, but all that happens is she closes herself off even more."
    s pjh "I think about ways to make the Literature Club feel like a home away from home for Natsuki, but she just keeps getting angrier and angrier at everyone all the time."
    s "It's all just been a giant mess because of me."
    s "And to top everything off, you go out of your way to plan such amazing days for me. Why?"
    s "What have I done for you lately?"
    s pjk "I'm no good at anything."
    s "I'm no good to anyone."
    "..."
    mc "No, Sayori..."
    mc "I'm the one who's no good to anyone."
    mc "I've done everything I can to stop you from having these thoughts and you're still having them."
    mc "What does that say about me?"
    mc "The picnic, the games we've played, the endless hours we've spent with each other have all been for you, because I love you until the day I die."
    mc "But it's still not enough to get rid of those damned rainclouds."
    s pjh "[player]...you have nothing to be ashamed of."
    s pjt "There's nobody and nothing that can make the rainclouds go away."
    s "They're here to stay."
    s pjv "So if you'd rather spend the rest of your life with a clear conscience and without someone like me weighing you down, then..."
    s pjk "I think you should go now, and leave me."
    "{i}What is she saying all of a sudden?"
    mc "Sayori, are you... breaking up with me?"
    s pjf "..."
    s pjh "That's a strong phrase to use."
    s "I'd rather say that you're now...relieved of me."
    s "I'm not your responsibility anymore, [player]."
    s pjw "Now go, before I keep ruining your life!"
    show sayori pjv at t11 zorder 2
    mc "Sayori--"
    s pjw "I SAID GO!"
    mc "Sayori!"
    s pjp "Get out of my head, get out of my head, get out of my head..."
    mc "SAYORI!"
    s pju "--!"
    mc "We can't end things like this."
    mc "We're supposed to have a happy ending."
    s pjk "I...can't..."
    "..."
    "My whole world is sitting in front of me."
    "Sayori's my whole life."
    "What are you meant to do when everything you've been responsible for saving is just ready to give up?"
    "It would be as if the earth itself stopped spinning."
    "My whole life is flashing before my eyes as I see Sayori ready to throw us away."
    "As it flashes by...I catch a glimpse of the two of us as children, sitting in front of this very pond..."
    
    scene white
    with fade
    scene bg pond_flashback
    with fade

    #{flashback to Sayori and MC as kids}
    s "Hey, [player], you remember that movie we watched last year, with the farm girl and the lion and the scarecrow?"
    s "What was that movie called? {i}The Lizard of Moss{/i}?"
    mc "That's {i}Wizard of Oz{/i}, Sayori. Everybody knows that."
    s "Hehehe~, right, that's what it was called."
    s "What was your favorite part of that whole movie?"
    mc "Honestly, I didn't really like it all that much. I thought it was kinda boring and cheesy."
    s "Whaaa?!"
    s "Come on, [player], why are you so jaded?"
    mc "How do you know what that word means, dummy?"
    s "Hehehe, because! I have to look up all the words I can use to describe you when you're being a jerk!"
    s "I can't just use \"meanie\" all the time, it loses its effects."
    mc "Ahaha, you're so silly, Sayori."
    s "Ehehe~! So please, [player], can you tell me your favorite part?"
    mc "Well, I guess the part when they find out that the wizard was just some dude behind a curtain made me laugh."
    s "Hehe~! I liked that part too."
    mc "Well, I guess I gotta ask now."
    mc "What was your favorite part of it?"
    s "...Um, well..."
    s "It's kind of embarrassing."
    mc "I won't laugh, I promise."
    s "Okay..."
    s "I think my favorite part was that song the girl sang super early in the movie."
    s "I wish I knew the words to it."
    mc "We can look it up when we get home."
    s "Okay!"
    s "And then do you think we could maybe..."
    s "Sing it together?"
    stop music fadeout 1.5
    mc "Heheh...never in a million years, Sayori."

    scene white
    with fade
    scene bg pond
    with fade

    #{back to present day}
    show sayori pjk at t11 zorder 2
    "..."
    "The truth is, even though I didn't like the movie a whole lot, I remember the song really well."
    "To this day, I remember the words."
    "In fact, there are times where I feel like I'm always hearing that song while I sleep at night."
    "I told Sayori I'd never sing it with her in a million years."
    "Well, given everything that we've been through since that day, and everything we've been through these last few months..."
    "It's already felt like a million years have passed."

    play music otr
    mc "{i}...somewhere...over the rainbow...{/i}"
    mc "{i}Way up high...{/i}"
    show sayori pju at t11 zorder 2
    mc "{i}There's a land that I heard of...{/i}"
    show sayori pjv
    mc "{i}Once in a lullabye...{/i}"
    show sayori pju at t11 zorder 2

    "..."

    $s_name = "Both"
  
    s pje "{i}Somewhere...over the rainbow...{/i}"
    s "{i}Skies are blue...{/i}"
    s pjt "{i}And the dreams that you dare to dream...{/i}"
    s "{i}Really do come true...{/i}"

    s pjr "{i}Someday I'll wish upon a star and wake up where the clouds are far behind me...{/i}"
    s "{i}Where troubles melt like lemon drops, away above the chimney tops...{/i}"
    s pjs "{i}That's where you'll find me...{/i}"

    $s_name = "Sayori"

    s pjq "..."
    s pjt "You...said...you'd never sing that song with me."
    s "I...didn't even think you'd remember it..."
    show sayori pjt at t11 zorder 2
    mc "Sayori, of course I remember it."
    s pjl "Because it's a really popular movie song?"
    show sayori pjt at t11 zorder 2
    mc "No...because that song reminds me of you..."
    mc "That song is a memory for me."
    mc "A memory of the two of us that I've held dear to me forever."
    mc "Sayori, you've been in my life since the very beginning, and I don't want {i}this{/i} to be our bitter end."
    show sayori pjk at t11 zorder 2
    mc "I need you in my life, Sayori."
    mc "I don't care that you think you're holding me down, because I'll always deny it."
    mc "I wouldn't be able to live with myself if I abandoned you."
    show sayori pjf at t11 zorder 2
    mc "That's why I'll always be there for you, and I want you there for me."
    mc "Even if it's for a million years."
    s pje "[player]..."
    show sayori at thide
    hide sayori
    "Sayori leaps onto me."
    "She knows now that she's always been important to me, and she always will be."
    s "I'm sorry I tried pushing you away, [player]."
    s "The rainclouds, they just won't stop shouting at me."
    mc "Then..."
    mc "I guess I'll just have to shout louder."
    mc "AHHHHHHHHH!!!!!!"
    s "Ehehehe~! [player]!"
    s "You're so silly!"
    mc "I LOVE YOU SAYORIIIIII!!"
    $ allCapsPlayer = player.upper()
    s "I LOVE YOU TOOOOO, [allCapsPlayer]!!"
    s "Ahahahaha~!"
    mc "*ahem* Ow, my throat."
    mc "Yeah, not doing that again."
    s "M-maybe I can make it feel better."
    mc "Are you gonna massage my trachea?"
    s "Ewwwwww!"
    s "No! I was just trying to say..."
    s "I wanna kiss you."
    mc "Hehe, yeah, I know."
    "I pull Sayori in, and we kiss."
    "The sense of affection that was missing just a few minutes ago, it's all come rushing back."
    "It's true what they say, as cheesy as it is."
    "{i}You don't know what you've got until it's gone."
    mc "Sayori, do you remember the last time we were here together?"
    mc "We were like fifteen or something, right?"
    s "Oh yeah! We were taking walks by ourselves and then ran into each other here."
    mc "That's right! I guess neither of us could resist coming to see this place."
    s "It's always been special to me."
    mc "I wonder why we haven't visited here in so long."
    s "I always thought you or anyone else would make fun of me if I'd asked."
    s "I think it was special to me, but to anyone else it'd be kinda childish."
    mc "You always could've asked."
    s "Yeah...but, we're here now. That's something to be happy about."
    "I smile warmly."
    mc "Yeah."
    "I hold Sayori's hand then walk over to the edge of the pond with her."
    show sayori pjx at t11 zorder 2
    s "Hey, [player]?"
    show sayori pja at t11 zorder 2
    mc "Yeah?"
    s pjx "That time we were here when we were fifteen, do you remember when you dared me to go swimming in the pond even though I didn't have a swimsuit?"
    show sayori pja at t11 zorder 2
    mc "W-what? That isn't what happened! You're the one who dared me!"
    s pjr "I'm pretty sure it was the other way around. I called you a pervert because I thought you just wanted me to get my clothes wet!"
    show sayori pjq at t11 zorder 2
    mc "N-no way! I didn't!"
    mc "..."
    mc "Wait, did I?"
    mc "No, I'm almost certain you dared me."
    s pjr "Hehehe~, well whoever dared who doesn't really matter."
    s pjx "What I'm wondering is..."
    s pjwink "Do you wanna go skinny dipping?"
    show sayori pja at t11 zorder 2
    "..."
    "I think I'm lightheaded."
    mc "B-but Sayori, people might see us!"
    mc "Children live in this neighborhood!"
    s pjq "Come on, [player], it'd be so much fun!"
    s "What have you got to lose?"
    show sayori pja at t11 zorder 2
    mc "Well, money by virtue of a fine if we're caught, to start."
    s pjj "Don't be such a fuddy duddy, [player]."
    s "This will be a story you'll be able to tell people forever!"
    show sayori pji at t11 zorder 2
    mc "..."
    mc "Okay, to make you happy..."
    mc "Let's do it."
    show sayori pjr at h11 zorder 2
    s "Hehehehe~!"
    show sayori at thide
    hide sayori
    "Sayori very hastily removes her clothes and leaves me almost speechless."
    show sayori undr at h11 zorder 2
    "I've seen her naked body a bunch of times by this point but there's just something so..."
    "{i}Magical{/i} about it this time."
    "The sunlight shines off her skin giving her the radiance of an angel."
    "Her smile is so bright it would make Nikola Tesla blush."
    "Her breasts look like something out of a Renaissance painting."
    "To be perfectly honest, I'm not even lost in lust at the moment."
    "I'm simply dumbfounded by the beauty that stands in front of me."
    show sayori at thide
    hide sayori
    "I go up to Sayori, lift her chin up toward me, and give her a long kiss."
    show sayori undx at t11 zorder 2
    s "Ehehehe...what was that for?"
    show sayori unda at t11 zorder 2
    mc "To thank you for being you."
    show sayori undq at t11 zorder 2
    "Sayori smiles and hugs me, pressing her nearly bare body against the entirety of my person."
    show sayori at thide
    hide sayori
    "I clear my throat."
    "If I wasn't lusting over her before, I certainly am now."
    "I finally take my clothes off as well, and she blushes seeing me."
    show sayori undy at t11 zorder 2
    "I wonder if she's having the same thoughts about my nude body cast in front of the sunset that I was having for her."
    s unds "Hehehehe~, your butt is flat."
    "Guess not."
    "I laugh, then offer to take Sayori's hand."
    show sayori unds at h11 zorder 2
    s "Nope!"
    show sayori at thide
    hide sayori
    scene sayori_pond
    with fade
    "Sayori goes to my side and shoves me into the water."
    "My teeth immediately start chattering, and Sayori laughs at the squeal I let out."
    mc "H-h-hey! You did that to me when we were y-y-younger too!"
    s "You know what they say, old habits die hard! Ehehehe~!"
    "I stand up from the water, dripping from my neck down to my waist. I reach forward and grab Sayori's hands and begin to pull her in toward me."
    s "Ahahahaha! Noooo!"
    mc "Hey, you're the one who wanted this! Now c'mere!"
    "Sayori continues to laugh uncontrollably as she hits the water and stands in front of me."
    s "J-j-j-j-j-j-jeez, it is r-r-r-r-really c-c-c-c-cold."
    mc "What did I tell you? Ahahaha!"
    "Sayori tries to giggle but her body rejects her request and only produces a small squeak."
    "Finally she gets used to the temperature of the water and she and I begin to have a lot of fun."
    "We start splashing each other, then make our way further into the pond and start swimming normally."
    scene black
    with fade
    "This goes on for about twenty minutes before we decide we'll need to leave the water and dry off while the sun is still out."
    "We leave the water and lie next to each other on the grass hoping to dry off as much as possible."
    scene bg pond_night
    with fade
    "I have my arm around her shoulder and she's snuggling into it."
    "I feel particularly macho as she has her hands on my unremarkable chest."
    "The moon starts to make its presence known as its light shines down on the two emotionally and hormonally compromised teenagers."
    "I look at Sayori and smile. Despite the fact that she felt so hurt today, I'm confident I've done a good job at helping her feel good, valuable, and loved."
    "It feels like this is going to mark a new chapter in our relationship."
    mc "It's a new day, Sayori."
    s "Yeah..."
    s "It is."
    stop music fadeout 2.0
    mc "We should go home and get changed."
    mc "And you should call [distraction] to let her know you're safe. I'm sure she's worried sick about you."
    s "I will."
    scene bg residential_night
    with fade
    "Sayori and I start walking. Our clothes are pretty damp as we weren't able to completely dry off but it can't be helped."
    "As I reach my front door the exhaustion of the day hits me harder than a truck hitting a cute schoolgirl at the beginning of an isekai series."
    show sayori pjwink at t11 zorder 2
    s "Hey, [player], I'm going to go take a shower, and then I have a special surprise for you~"
    show sayori pjy at t11 zorder 2
    mc "O-oh, g-great."
    "There's just too much sexual energy emanating from the two of us right now, I don't know why I even act surprised."
    "Sayori walks inside and goes to shower."
    show sayori at thide
    hide sayori
    "I was going to suggest that she shower at her own place so that neither of us would have to wait, but she already took off by the time I was going to speak up."
    "No big deal, maybe I could just shower at her place instead."
    "Besides, I'll probably have to go over there and grab some fresh clothes for her anyway."
    "She's been wearing soiled pajamas since last night."
    scene bg house_night
    with fade
    mc "Yeah this'll be alright with her I'm sure."
    scene bg sayori_bedroom_night
    with fade
    "I enter Sayori's house and walk up to her bedroom."
    "Man, it really has been a while since I've been here, today's panic search notwithstanding."
    "It's probably been a while since either of us have been here, in fact."
    "Sayori's stuffed cow and bird both greet me with their blank stares as I walk into the room."
    mc "You know, bird, out in the open, I never really liked you."
    "..."
    mc "Speechless again, huh? Coward."
    "I chuckle to myself at my dumb joke, then walk over to Sayori's closet and open it."
    "I try to remember where she puts each type of clothing, but as far as I can tell, everything's as disorganized as ever."
    mc "No wonder I used to clean her room up for her. It really is distracting."
    "Since it's such a free for all in there I don't make much of an effort to find matching pieces of clothing."
    "I just need to grab a shirt, some shorts, and some underwear."
    mc "Do I need to bring a bra?"
    mc "...{i}Nah."
    "I've retrieved a pair of shorts and panties from this mess, but for some reason finding a shirt is proving harder than I expected."
    "At this point I'm just grasping at fabric."
    "And then I feel something else...something kind of...tough? And...frayed?"
    "My curiosity gets the best of me, so I open my hand up to get a better grip on whatever it is I'm feeling, then pull it."
    "It feels really heavy and dense."
    "I put the clothes I had in my right hand down on the floor and grab the object with that hand."
    "Finally after pulling for a few moments, the object begins to see the light of day."
    "I don't fully register what it is until it's on the floor in front of me."
    "..."
    play music tdt
    "What the hell...?"
    "{i}What the hell??"
    "Is this a nightmare?"
    "It has to be."
    "Sayori wouldn't have this."
    "What sits in on the floor in front of me is a thick brown rope tied into a noose."
    "This can't be real. My eyes are deceiving me."
    "I refuse to believe what it is I'm looking at."
    "I try to understand the series of events that might've led to Sayori having something like this in her bedroom, but my imagination fails me."
    "All I can do is tear up in massive confusion and fear."
    mc "Sayori..."
    "I barely produce her name before my voice gives out."
    "I decide to grab the noose again to make sure I'm not just hallucinating."
    "The sense of it on my fingertips forces me to flinch and release short breaths."
    "It's real."
    "{i}It's very real."

    if SayoriVar < 5 :
        call sayoribadending
    else :
        call sayorigoodending
return


label sayoribadending:
    "After staring at the rope for what feels like days, I decide to call the one person who helped me keep a cool head as of late."
    mc "Hey Monika, sorry for calling you this late at night ."
    m "{i}No worries [player], what's up?"
    mc "Can you meet me at Sayori's place? There's something here I need your help with."
    m "{i}Yeah sure, just give me a couple minutes and I'll be right over."
    "Much quicker than expected, I hear the doorbell ring."
    scene black
    with fade
    "As I head over to answer it, I question if this was the right thing to do after all."
    "Eh, too late to turn back now."
    "I answer the door and greet Monika."
    scene bg house_night
    with fade

    show monika 2bc at t11 zorder 2
    mc "Good, you're here. Follow me."

    scene bg sayori_bedroom_night
    with wipeleft_scene

    show monika 2bh at t11 zorder 2
    "I lead her directly to Sayoris room and grab the noose off the floor."
    "She doesn't look surprised, only angry."
    mc "Why would she do this?"
    m 2bi "Well, only one way to find out, where is she right now?"
    show monika 2bh at t11 zorder 2
    mc "At my house, waiting for me to get her some clothes."
    m 2bi "Let's go."
    stop music fadeout 1.5
    show monika 2bh at t11 zorder 2

    scene black
    with fade
    "I run back to my house with Monika in tow."

    scene bg residential_night
    with wipeleft_scene
    #"Visions of Sayori hanging from the ceiling still taint my mind."
    "Nothing feels real anymore."
    "When was she planning on using this...?"
    "I can't even bring myself to even properly address the noose."
    "I practically break down my own front door."
    scene bg livingroom_night
    with wipeleft_scene
    "My emotions are too strong now to even really register the trail of flower petals leading up to my bedroom door."
    "I trample over her romantic gesture during my stampede to my room."
    "Nothing matters but making it to Sayori."
    "Nothing matters {i}but{/i} Sayori."
    "I storm upstairs and into my room."
    scene bg bedroom_night
    with wipeleft_scene
    show sayori unda at t11 zorder 2
    "Sayori's sitting on the bed patiently."
    "I instantly notice that she's got some special lingerie panties on."
    mc "So...that's what was in the bag, eh?"
    show monika 2bh at t21 zorder 2
    show sayori unde at t22 zorder 2
    "Sayoris face turns red as she notices Monika behind me and she covers herself with the blanket ."
    show sayori unde at thide
    hide sayori
    show sayori blae at t22 zorder 2
    mc "I... I would probably appreciate that, normally."
    mc "Right now, this just feels like a lie..."
    show monika 2bi at f21 zorder 3
    m "You could've asked for help, instead you decided to hide this and make things worse for you down the line."
    m "You couldn't even do the simple task of returning my jacket on time."
    m "[player] tries so hard to make you happy and {i}this{/i} is how you repay him?!?"
    show monika 2bh at t21 zorder 2
    show sayori blav at t22 zorder 2
    "I notice that Sayori is starting to tear up."
    mc "Hey, uhhh Monika?"
    show monika 2bi at f21 zorder 3
    m "All you do is try to make others happy, but for once in your life, did you ever stop and think that maybe what we want is for you to be open to us?!?"
    show monika 2bh at t21 zorder 2
    mc "I think you're taking this a bit far."
    show monika 2bi at f21 zorder 3
    m "Shut up, [player]. I'm talking to Sayori."
    show monika 2bh at t21 zorder 2
    show sayori blaj at f22 zorder 3
    s "Fine then."
    s "You want me to be open? I'll be open."
    play music t10
    s "No matter how hard I try, no matter who I talk to, it always ends the same way."
    s "So why bother?"
    s "All I do is destroy everyone else's feelings. So why even try to feign happiness?"
    s "[player], thanks for tonight, but I'm going home."
    show sayori blai at t22 zorder 2
    mc "Sayori wait."
    show sayori blav at f22 zorder 2
    s "No, it's obvious no one thinks I can do anything."
    s "Everything you said or did tonight was in pity wasn't it?"
    show sayori blav at thide
    hide sayori
    show monika 2bh at t11 zorder 2
    "Sayori runs off down the stairs with tears streaming down her cheeks."
    mc "Sayori come back!"
    m 2bi "Let her go, [player]. She's not worth it."
    show monika 2bh at t11 zorder 2
    "I disagree, but Monika stands in the doorway, stopping me from going after her."
    "While I'd never admit to it out loud, I doubt I can beat Monika in a fight."
    "But I still have to go after Sayori."
    show monika 2bh at t22 zorder 2
    "I try to get around her but she keeps moving to block any attempts I make at getting out."
    show monika 2bh at t21 zorder 2
    "After about a minute of scuffling like that, I start to get pissed off and push Monika to the side and leap down the stairs as I hear her fall to the ground."
    show monika 2bh at thide
    hide monika
    mc "Huh, maybe I'm stronger than I thought."
    scene bg livingroom_night
    with wipeleft_scene
    "As I reach the front door, I see that Sayori is nowhere to be found,"
    "She probably went home in the time it took me to get past Monika."
    mc "{i}Damn it!{/i}"
    scene bg residential_night
    with wipeleft_scene
    "I run across the street, too anxious to think straight."
    "Panting, I stop in front of Sayori's closed front door."
    scene bg house_night
    with wipeleft_scene
    "I pound on Sayori's door a few times before I hear her voice from the other side of the door."
    s "I CAN'T DO THIS ANYMORE, [allCapsPlayer]!"
    s "{i}EVERY SINGLE TIME{i} I START TO GET MY ACT TOGETHER, I MESS UP SOMEHOW AND RUIN EVERYTHING!"
    mc "Sayori, listen--"
    s "NO! I know what you're about to say, and I don't want to hear it."
    s "I'm just...tired."
    s "Leave. Now."
    mc "Sayori, if I leave now I'm not coming back."
    mc "If you don't want my support just tell me."
    mc "It will kill me to lose you, but I want you to be happy, and if that means that I have to make you cry a couple of times to get there I will."
    s "It's not that I don't want you with me, I just don't think it's worth it anymore."
    s "Please, I'm begging you, just go."
    mc "Fine then, I'll see you at school then, okay?"
    s "S-sure."
    stop music fadeout 1.5
    "I turn around and head back home, hoping that she'll be feeling better by tomorrow."
    scene bg residential_night
    with wipeleft_scene
    "Since it's getting late and I'm exhausted, I decide to skip the shower go to sleep for the night in my own filth."
    scene bg bedroom_night
    with wipeleft_scene
    "I get to my room and climb into bed, only to feel like someone's watching me and that I forgot something important."
    "I flip myself over, only to see a furious Monika looming over my bed."
    show monika 2bi at t11 zorder 2
    m "What the hell was that all about?!?"
    m "[player], do you realize what you did??"
    show monika 2bh at t11 zorder 2
    mc "'Do {i}I{/i} realize what {i}I{/i} did?'"
    mc "Yes, Monika, I did what I had to so I could go help my best friend."
    m 2bi "And were you not listening? There's a reason I was telling you she isn't worth this!"
    show monika 2bh at t11 zorder 2
    mc "That's not your decision to make. This isn't your house, either, so get out before I call the cops."
    show monika 2br at t11 zorder 2
    "She pauses."
    show monika 2br at thide
    hide monika
    "After a few moments, she leaves the room, and presumably my house entirely."
    "Annoyed, I turn back over to sleep."

    scene black
    with fade

    scene bg bedroom
    with fade

    "I wake up the next morning with the looming sensation that I'm gonna be in for a rough day."
    "After lazing around in bed for an hour, I finally decide to get up and get ready for school."
    
    scene bg kitchen
    with wipeleft_scene

    "As I eat my breakfast, I recall last night's events and start to get worried about Sayori."
    mc "I guess I'd better go check up on her."

    scene bg house
    with wipeleft_scene

    "I get into my uniform and head over to her house."
    "I knock on her door a couple times, but don't get an answer."
    "Just in case, I try opening the door, even though Sayori had it locked last night."
    "To my surprise, her front door is unlocked, so I decide to go inside and look for her."
    mc "Sayori! Wake up, we have school today!"
    mc "I'm leaving your breakfast on the kitchen counter for when you get ready!"
    "I get no answer other than the sound of her falling out of bed, so I assume she got the message and then I head off to school."
    
    scene bg class_day
    with wipeleft_scene

    "The day passes by uneventfully, save the few awkward hours where I share a class with Sayori."
    "One of which was math, and apparently that test we were supposed to be prepared for turned out to be today of all days."
    "And of course, I bombed it."
    "As if I needed another reason to loathe this day..."
    "As classes finally end, I dreafully head over to the clubroom."

    scene bg club_day
    with wipeleft_scene

    show monika 1h at t31 zorder 2
    show natsuki 1g at t32 zorder 2
    show yuri 1e at t33 zorder 2

    "As I enter, I'm greeted by Natsuki, Yuri, and Monika, the last of whom I avoid eye contact with."
    "Natsuki seizes the opportunity to walk up to me with an accusatory look on her face."
    show monika 1c at thide
    hide monika
    show yuri 1a at thide
    hide yuri

    show natsuki 1b at t11 zorder 2
    n "Sayori was acting weird today. What happened?"
    show natsuki 1g at t11 zorder 2
    mc "...what makes you think I'd know?"
    n 1b "You're her boyfriend. That's the kind of thing you should keep track of."
    show natsuki 1g at t11 zorder 2
    "I excuse Natsuki's flawed logic for a moment."
    mc "Look, I... I don't know if I'd consider myself her boyfriend anymore."
    n 1p "What??? What did you do to her, [player]?!?"
    "Natsuki freaks out on me."
    mc "Hey, why do you assume I did something to her?"
    mc "For all you know, she could have broken up with me!"
    n 1o "As if! I know Sayori, and she's far too much of a pushover to do something like that."
    "Are you defending her or insulting her?"
    n 1v "Tell me what happened! You better not have hurt her!"
    mc "I'm really not in the mood for this. Look, can you just leave me alone?"
    n 1o "...!"
    show natsuki 4g at t11 zorder 2
    "She doesn't seem happy to do it, but she turns and walks away from me."
    show natsuki 4g at thide
    hide natsuki
    "Yuri is the only one in the room who isn't looking at me with scorn."
    show monika 1h at t31 zorder 2
    show natsuki 1g at t32 zorder 2
    show yuri 1g at t33 zorder 2
    "She looks like she wants to say something but can't find the courage to say it."
    mc "Well then it looks like I'm no longer welcome here. Guess I'll take my leave."
    show natsuki 1p at f32 zorder 3
    n "Fine then, go! See if any of us care!"
    show natsuki 12d at t32 zorder 2
    "I leave the clubroom, making as little eye contact as possible with everyone."
    scene black
    with fade
    scene bg corridor
    with fade
    "Everything is crumbling right before my eyes."
    "My relationship, my friendships, the Literature Club, and I can't do a thing about it."
    "I have to go fix this however I can."
    "Sayori's behavior yesterday was alarming, but I think I can get through to her."
    "I just regret letting my emotions take over. I should've been stronger for her."
    "But it isn't too late. I still have time to fix this."
    "I love Sayori, as much as she says she doesn't want me to."
    "I have to be there for her, and I'll be damned if I don't at least try."
    "After leaving Literature Club early, I make my way back to my neighborhood with the assumption that Sayori is at her house."
    scene bg residential_day
    with wipeleft_scene

    "Strange, she's hardly spent any time at her house in the time that we've been dating. It feels like I'm starting again from square one."
    scene bg house
    with wipeleft_scene
    "I walk into Sayori's house and call out to her."
    scene bg sayori_hall
    with wipeleft_scene
    mc "Sayori! Are you home?"
    "I don't get any answer, as I expected, unfortunately."
    "I walk up the stairs and knock on her bedroom door at the end of the hall."
    mc "Sayori, it's me. I think we need to talk."
    "She doesn't say anything, but I hear her take a deep breath on the other side of the door."
    mc "Sayori, I'm sorry for how I behaved yesterday. And I'm sorry for the way Monika acted."
    s "..."
    s "Please go."
    play music t10
    mc "Sayori, please, I can't just let you close yourself off from everyone."
    mc "Natsuki is worried about you. Doesn't that matter to you?"
    mc "Me and Yuri are worried about you. And deep down I'm sure Monika is, too."
    mc "I want to help you, but you have to be the one to take that step."
    s "Who says I want to take that step?"
    s "I'd rather give up and stop trying. That way nobody needs to feel worried for me anymore."
    "This is so difficult, and I hate that it's that way."
    "From inside the room I can hear Sayori's stomach grumble. Loudly."
    mc "Sayori, did you eat anything today?"
    s "..."
    s "No."
    mc "Why don't we get you something to eat?"
    s "..."
    mc "I'll...take that as a yes."
    "I go downstairs and search Sayori's pantry for something to feed her."
    "I find a cup of instant noodles and prepare it, then return upstairs a few minutes later."
    mc "Sayori, I made you something. It's not much but you need to eat."
    s "..."
    s "Just leave it on the floor."
    mc "Do you promise me you're going to eat it?"
    s "..."
    mc "Sayori--"
    s "Yes, I promise. Now will you please leave me be?"
    "I sigh."
    mc "Okay. I'm going to check in on you later, though."
    mc "I...I love you, Sayori."
    s "..."
    "It was wishful thinking to think she'd reply to that."
    "The fact that we're at that point crushes me, but I can't afford to put my feelings over hers right now."
    scene bg livingroom
    with wipeleft_scene
    "I return home, then fall asleep several hours later."
    scene black
    with fade
    scene bg class_day
    with fade
    "The next day, I go to school and things are more or less the same. However, Sayori didn't show up to our first class. She eventually showed up, but after lunch."
    scene bg club_day
    with wipeleft_scene
    "Literature Club was cold and quiet, and nobody wanted to talk. It's obvious when Sayori isn't around that things are much more glum."
    show natsuki 4x at t11 zorder 2
    "Natsuki and I wordlessly exchange a look of disdain and concern as we both leave for the day."
    scene bg residential_day
    with wipeleft_scene
    "I return to my neighborhood to check up on Sayori once again."
    scene bg sayori_hall
    with wipeleft_scene
    "I walk up the stairs and approach her bedroom door, but I notice something."
    "The instant noodles are still on the ground where I left them, cold and completely uneaten."
    mc "Sayori!"
    mc "You told me you were going to eat this!"
    mc "Why would you lie to me?!"
    s "Because all I do is disappoint people. Haven't you figured it out?"
    mc "SAYORI. YOU'RE DOING THIS TO YOURSELF."
    s "THEN DO YOURSELF A FAVOR AND STOP CARING."
    mc "HOW CAN I DO THAT WHEN YOU'RE ACTING THIS WAY?!"
    s "[player], I've made up my mind. Leave. Stop checking up on me like I'm a rescue puppy."
    s "Just go away."
    mc "Sayori--"
    s "Will you just go already?"
    mc "Sayori--!"
    show sayori pjj at t11 zorder 2
    "The door swings open, and I nearly fall over in shock."
    "Sayori appears in front of me, then she looks at me with a look of anger I've never seen."
    s "Leave."
    s "And never..."
    s "{i}Ever come back!"
    show sayori pji at t11 zorder 2
    mc "..."
    mc "Sayori..."
    mc "What about...ending up over the rainbow?"
    s pjk "..."
    s "I had my chance to do that. And I blew it."
    s "There's no happy ending for me."
    s "And if you insist on constantly trying to fix me, then you're going to deprive yourself of your own happy ending."
    s pjv "So leave right now, and start over without me."
    s "I'm a hopeless case."
    "..."
    "I don't want to adhere to her demands whatsoever."
    "But the look in her eyes, the tone of her voice, the sheer hopelessness portrayed by her body language..."
    "It's like she's already a lost cause."
    "I don't think even the strongest person could fix this without a miracle."
    "Sayori..."
    scene black
    with fade
    "The girl I knew..."
    "The girl I {i}loved."
    "That Sayori is gone."
    "She's a shell of herself."
    "I failed her."
    "I walk out of Sayori's house, and accept defeat."
    "I couldn't protect her from herself."
    "I royally screwed up."
    "Maybe it was never meant to be."
    "There's no more 'over the rainbow' for Sayori."
    "Only rainclouds."
    pause(1)
    scene bg ending_b
    with fade
    pause(5)
    scene black
    with fade


return

label sayorigoodending:
    mc "Grnghgh..."
    mc "{i}DAMMIT. NO."
    "I've ended up on my knees, and I begin to strike the floor with my open palms in horrifying anguish."
    mc "{i}WHY?"
    mc "{i}WHY?!"
    mc "{i}WHYYYY!!!!"
    "Several moments of silence pass after my meltdown and I'm now sitting on the floor propped up by Sayori's bed."
    "I continue to stare at the noose and all it does is stare back at me, taunting me."
    "As I sit there..."
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate
    pause(0.05)
    hide sayori_grim_fate
    show white
    pause(0.1)
    hide white
    show bg sayori_bedroom_night
    "I think..."    
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate
    pause(0.05)
    hide sayori_grim_fate
    show white
    pause(0.1)
    hide white
    show bg sayori_bedroom_night
    "Of Sayori..."    
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate
    pause(0.05)
    hide sayori_grim_fate
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate
    pause(0.05)
    hide sayori_grim_fate
    show white
    pause(0.1)
    hide white
    show bg sayori_bedroom_night
    "Actually..."
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate
    pause(0.05)
    hide sayori_grim_fate
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate
    pause(0.05)
    hide sayori_grim_fate
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate
    pause(0.05)
    hide sayori_grim_fate
    show white
    pause(0.1)
    hide white
    show bg sayori_bedroom_night
    "Putting this to use."
    show white
    pause(0.1)
    hide white
    show sayori_grim_fate2
    pause(0.5)
    hide sayori_grim_fate2
    show white
    pause(0.1)
    hide white
    show bg sayori_bedroom_night
    mc "GET OUT OF MY HEAD!"
    "I can't stand this uncertainty anymore."
    "{i}I have to confront Sayori about this."
    "I cease the staring contest with the deadly rope and pick it up, being reacquainted with its weight."
    "I groan as I lift it up and wrap it in a circle and leave Sayori's bedroom."
    "I know her, and I know this isn't her."
    "I need to hear her explanation for this."
    "I run back to my house drowning in tears."
    scene black
    with fade
    "Visions of Sayori hanging from the ceiling still taint my mind."
    "Nothing feels real anymore."
    "When was she planning on using this...?"
    "I can't even bring myself to even properly address the noose."
    "I practically break down my own front door."
    scene bg livingroom_night
    with fade
    "My emotions are too strong now to even really register the trail of flower petals leading up to my bedroom door."
    "I trample over her romantic gesture during my stampede to my room."
    "Nothing matters but making it to Sayori."
    "Nothing matters {i}but{/i} Sayori."
    stop music fadeout 1.5
    "I storm upstairs and into my room."
    scene bg bedroom_night
    with wipeleft_scene
    show sayori undd at t11 zorder 2
    "Sayori's sitting on the bed patiently."
    "I instantly notice that she's got some special lingerie panties on."
    mc "So... that's what was in the bag, eh?"
    show sayori undq at t11 zorder 2
    "Sayori smiles and nods happily, but it fades as my expression contorts."
    show sayori undg at t11 zorder 2
    mc "I... I would probably appreciate that, normally."
    mc "Right now, this just feels like a lie..."
    mc "You made this great display about showing yourself in very little..."
    mc "All while hiding something massive."
    show sayori undn at t11 zorder 2
    "She tilts her head in confusion, which turns to shock as I reveal the rope."
    show sayori undm at t11 zorder 2
    "All color flushes from her face."
    show sayori undw at t11 zorder 2
    s undv "No..."
    s "How..."
    show sayori undu at t11 zorder 2
    mc "You better explain yourself {i}right now.{/i}"
    s undv "I..."
    show sayori undu at t11 zorder 2
    "I can tell she's trying her best not to bawl."
    "Her change in her usual tone must be a testament to how much gravity this has for her."
    "My lips start to quiver."
    "My jaws are clenched so tightly it feels like my teeth are about to shatter."
    s "..."
    s undv "I can't say I really even wanted to use that noose."
    play music t10
    "She looks off for a second to collect herself."
    "Tears are welling up in her eyes more than mine."
    "I start to loosen up, and I drop the noose."
    s undk "It's odd."
    s "The day I planned to die, was the day my life truly began."
    show sayori undk at thide
    hide sayori
    "Does she mean...?"
    show sayori blag at t11 zorder 2
    s blag "The night before the festival, something was wrong."
    s "I should have been happy. I was finally loved by the person who meant the most to me."
    s "But when I went back inside after we were finally a couple...something started to say things in the back of my head."
    s "Things that all had to do with my death."
    s blak "These voices that told me to die..."
    s blaw "I hated them!"
    s blah "I thought killing myself would get them to finally go away."
    s blak "To get them out of my head."
    s "Of course, I could have just lived with them for your sake."
    s blah "But I also worried that living with this would hurt you, so in my rush, I thought it could solve two problems."
    s blak "So, that night, I tied the noose and planned to wake up early to finally hang myself."
    s "I was too tired at night to go through with it."
    s "But I slept in."
    s "And then, you woke me up."
    s blak "I was given a reason to stay one more day... one more week... one more month."
    s "Eventually, I pretty much refused the fact that I tried to kill myself and left the noose in my closet, and it's been there all this time..."
    s blag "Until now."
    s blav "I'm so sorry, [player]."
    s "I should have told you sooner."
    s "I know this sounds pretty stupid now, but I didn't want to hurt you if you found out."
    show sayori blau at t11 zorder 2
    "I feel betrayed, in a sense. I told her she could talk to me about anything at all. So why would she hide this from me? "
    "I finally loosen all the way up, and embrace Sayori."
    show sayori blau at thide
    hide sayori
    mc "Sayori..."
    s "Shh."
    s "I'm sorry...really..."
    s "You're gonna ask for me to promise to never try again, aren't you..."
    s "I...I wanna do that..."
    s "I wanna do what will help you feel better..."
    "Sayori's utterly bawling. She can barely speak through the tears."
    s "But I can't."
    s "I wanna be better so bad."
    s "I wish the dark clouds would just blow away."
    s "It's just that...I can't do that...I can't make you feel better."
    s "I can't even make myself feel better...so what's the point of trying...?"
    mc "...but I promise to always be there to try my best...to chase those clouds away myself."
    mc "I refuse to let you succumb to the rain ever again."
    "Sayori starts to tremble in my arms."
    "I realize that I may have blown things a little out of proportion." 
    "After all, if she was going to use that noose, she had every opportunity to use it today."
    "Instead she chose to give me, and above all herself, a chance."
    mc "Now, how about we put off that treat you were about to give me, and we burn this rope so that we never have to lay eyes on it again?"
    s "Yeah, I think it's time to accept and move on from this awfulness."
    "We go to the backyard and get everything set up; oil, matches, paper, and some rocks to attempt to keep sparks from hitting the grass and burning down the house." 
    scene bg residential_night 
    with wipeleft_scene
    show sayori blad at t11 zorder 2
    mc "Will you do the honors, Sayori?"
    "Sayori looks at me with tears in her eyes and giggles."
    s blas "Why yes, [player] I'd love to."
    show sayori blaq at thide
    hide sayori
    "She pours a little oil over some paper and the rope, strikes a match, and lights the rope on fire."
    "As we watch this wretched thing burn, I finally feel like I won't have to worry about Sayori killing herself anymore."
    "And as the last of the rope turns to ash, I notice that this entire time..."
    "Sayori was actually smiling."
    stop music fadeout 1.5

    scene black 
    with fade
    #break

    "I'd never had a more physically, emotionally, mentally, and spiritually exhausting day in my life before yesterday happened."
    "A lot of events took place that I'd care to not relive, but the fact of the matter is, Sayori and I took steps toward putting her depression down for good."
    "The keyword there is 'steps.'"
    "I'd be foolish to think I can heal her myself, in the span of a few months, let alone one day."
    "Once Sayori is more comfortable, I'll talk to her about finally going to therapy and getting prescriptions in order to help mend her depression."
    
    scene bg bedroom
    with fade
    
    play music t12
    "It's about time I stop trying to act like a superhero, and simply act as a boyfriend, and only do everything {i}within{/i} my power to make Sayori's life easier."
    "I sit up from my bed and stand next to it, then tap Sayori on the shoulder."
    mc "Sayori."
    "She opens her eyes and groans."
    s "Hmmnn...what is it?"
    mc "It's Monday. We have school, remember?"
    s "Ungh, okay, fiiine."
    show sayori undq at h11 zorder 2
    play music t2
    "Sayori stands up quickly, then gives me a kiss on the cheek."
    s undr "If it wasn't for you, I'd never wake up on time."
    show sayori undq at t11 zorder 2
    mc "Hey, you've woken up before me a couple times."
    s undx "Exactly. You're the only reason I wake up."
    show sayori unda at t11 zorder 2
    mc "Hey, Sayori, if we keep working on getting you better, I promise you'll see you have a lot more to live for than just me."
    s undl "Eheh, you say that like you don't want me to care about you anymore."
    show sayori undq at t11 zorder 2
    mc "Don't take it that far. I just want you to find that perfect middle ground. Understand?"
    s undx "Mhmm, I do, [player]. Thank you."
    show sayori undx at thide
    hide sayori

    scene bg kitchen
    with wipeleft_scene
    "Sayori and I get geared up for school, and leave after a few bowls of cereal."
    "After yesterday, it's the only thing either of us have the energy to prepare for breakfast."

    scene bg residential_day
    with wipeleft_scene

    "We head off to school, and drudge through the same tired routine we've been going through for the past number of years."
    
    scene bg corridor
    with wipeleft_scene

    "However, after what we've had to go through as of late, some stability is more than welcome."
    "After classes end for the day, I go to meet Sayori down the hall from the Literature Club."
    show sayori 1x at t11 zorder 2
    s "Hey."
    show sayori 1a at t11 zorder 2
    mc "Hey, how was your day after that nightmare in the morning?"
    show sayori 1n at t11 zorder 2
    "Oh yeah, turns out that math test Sayori and I were stressing over was actually today."
    "We walked into the room to find our teacher writing the time limit on the board, and the rest of our classmates reviewing concepts with each other at the last second."
    "Sayori and I tried to keep our cool and act like we were prepared, but that wasn't the case. Both of us started dying inside."
    s 1l "Heh...it was fine. But all things considered I think I did okay on that test."
    show sayori 1a at t11 zorder 2
    mc "Y-yeah, s-so did I."
    show sayori 1q at t11 zorder 2
    "My lying skills seem to have gotten worse since last week."
    s 2n "Oh yeah, the weirdest thing happened to me today at lunch."
    s "I got all my food, then I got money of out my purse to pay, and then the lunch lady said..."
    s 2c "{i}\"Don't worry about it, hun. It's taken care of.\""
    mc "Wait, so you didn't have to pay for your lunch?"
    s 4r "Nope! I don't know why, but I was pretty happy."
    s "We must have a really sweet lunch lady! I can't believe I never knew!"
    show sayori 1q at t11 zorder 2
    mc "Yeah, that must be the case."
    "That's pretty peculiar, but I think Sayori's giving the lunch lady a little too much credit."
    stop music fadeout 1.5
    "Not to say she isn't a nice person, but I have a feeling there's some other reason for that."
    scene bg club_day
    with wipeleft_scene
    "In any case, I take Sayori's hand and we walk in through the door of the Literature Club to find it...empty?"
    show sayori 1b at t11 zorder 2
    mc "Uh...did Monika cancel club again?"
    s 1c "Huh, I don't think so. We didn't get a note or any texts."
    "The light is still off, so I decide to flip it on."
    "Then, the next moment..."
    show sayori 4p at h44 zorder 2
    show natsuki 1l at l43 zorder 2
    show yuri 1d at l42 zorder 2 
    show monika 1b at l41 zorder 2
    $ m_name = "Everyone"
    play music t3
    m "SURPRISE!"
    $ m_name = "Monika"
    s "Whoa!!"
    mc "What the--?!"
    show sayori 4g at t44 zorder 2
    show natsuki 1z at t43 zorder 2
    show yuri 1c at t42 zorder 2 
    show monika 1j at t41 zorder 2
    "The other girls jump out from behind desks and the closet and just about give us heart attacks."
    "I look around the room some more and see a big tray of cupcakes on the teacher's desk, and above it hangs a big cotton candy-colored banner reading in big block letters 'Welcome Back Sayori!'"
    "Is this...a party?"
    show monika 1b at f41 zorder 3
    m "Did we startle you two?"
    show monika 1a at t41 zorder 2
    show natsuki 1a at t43 zorder 2
    show yuri 1a at t42 zorder 2 
    mc "Uh...yeah, kind of!"
    show sayori 4c at f44 zorder 3
    s "W-what is all this, you guys?"
    show sayori 4b at t44 zorder 2
    show natsuki 1l at f43 zorder 3
    n "Well, when we heard that you found Sayori, we just had to celebrate!"
    show natsuki 1a at t43 zorder 2
    show monika 1b at f41 zorder 3
    m "I thought it was a little over the top, but we thought you deserved it."
    show monika 1a at t41 zorder 2
    show yuri 1b at f42 zorder 3 
    y "After all, you've done nothing but try to make us smile for a long time now."
    y "So think of this as a celebration of our friendships with you, Sayori."
    show yuri 1a at t42 zorder 2 
    show monika 1k at f41 zorder 3
    m "What Yuri said!"
    show monika 1b at f41 zorder 3
    m "Sayori, you're an amazing vice president, and more importantly someone I hold very dear to me."
    show monika 1a at t41 zorder 2
    show natsuki 1l at f43 zorder 3
    n "Same here, Sayori, but...you already know that. Ehehe~!"
    n "We just...thought we'd show you how much we really appreciate you."
    n "So I made these cupcakes!"
    show natsuki 1a at t43 zorder 2
    show yuri 1d at f42 zorder 3 
    y "And I designed this banner."
    show yuri 1c at t42 zorder 2 
    show monika 1b at f41 zorder 3
    m "And I..."
    show monika 1l at f41 zorder 3
    m "Told them to do those things."
    m "Ahaha~!"
    show monika 1b at f41 zorder 3
    m "Oh yeah, I also paid for your lunch today. Just a little pre-celebration treat from me~"
    m "But really, Sayori...thank you for being you."
    show monika 1a at t41 zorder 2
    show yuri 1b at f42 zorder 3 
    y "You're the most wonderful person we know."
    show yuri 1a at t42 zorder 2 
    show natsuki 1l at f43 zorder 3
    n "And we're all so lucky to call you our friend."
    show natsuki 1l at f43 zorder 3
    $m = "Everyone"
    show natsuki 1l at f43 zorder 2
    show yuri 1d at f42 zorder 2 
    show monika 1b at f41 zorder 2
    m "We love you, Sayori!"
    $m = "Monika"
    show natsuki 1z at t43 zorder 2
    show yuri 1c at t42 zorder 2 
    show monika 1j at t41 zorder 2
    "..."
    s 4p "You guys!!!"
    show natsuki 1z at thide
    show yuri 1c at thide
    show monika 1j at thide
    show sayori 4p at thide
    hide natsuki
    hide yuri
    hide monika
    hide sayori
    "The girls all group hug, and I feel so happy in my heart."
    "I didn't ever imagine the girls would do something like this for her, but I'm glad they did."
    "They're proving to Sayori what I've known all along."
    "That life just wouldn't be the same without our bundle of sunshine."
    show sayori 4c at t11 zorder 2
    s "Guys...I don't know what to say."
    s "I can't possibly repay you all back enough for this."
    show sayori 4b at t22 zorder 2
    show monika 1b at f21 zorder 3
    m "You don't need to do anything of the sort, Sayori."
    show sayori 4b at t33 zorder 2
    show monika 1a at t31 zorder 2
    show natsuki 1l at f32 zorder 3
    n "We wanted to do this."
    show sayori 4b at t44 zorder 2
    show monika 1a at t41 zorder 2
    show natsuki 1a at t43 zorder 2
    show yuri 1b at f42 zorder 3
    y "If anything, this isn't nearly enough to repay you for all that you've done."
    show yuri 1a at t42 zorder 2
    mc "They're right, Sayori. Even me, I could spend every minute of every day saying thank you, and it wouldn't be enough."
    mc "Now you know what I've been saying, right?"
    mc "The girls all value you as much as I do."
    mc "You've done an amazing job making us all endlessly happy."
    mc "You've spent all this time playing a sort of game, hiding your feelings from us in order to protect ours."
    mc "But Sayori, that's a game with no winners, and we've reached game over."
    mc "It's time for you to be your true self. You don't need to jump through hoops for us like you think you do."
    show sayori 4e at f44 zorder 3
    stop music fadeout 2.0
    s "[player]...thank you for saying that. It means the world to me."
    s "Monika, Natsuki, Yuri...you're all the most amazing friends a girl could want."
    show sayori 2k at f44 zorder 3
    s "Even if we've had our differences, you've all been true to me all this time."
    s "And...if there's one thing I can do to make it up to you guys, it's this..."
    s "I have to be true to myself, and to each of you."
    s "So...here's the real truth."
    show sayori 1c at f44 zorder 3
    play music t9
    s "I...have depression."
    show sayori 1b at t44 zorder 2
    show monika 1c at t41 zorder 2
    show natsuki 1p at t43 zorder 2
    show yuri 1m at t42 zorder 2
    "The other three girls have varying expressions."
    "Monika seems almost sad, but like she already kind of knew."
    "Yuri seems to be at peace, like she also already knew."
    "Natsuki looks to be the most surprised, and she could start to tear up at any moment."
    show sayori 1c at f44 zorder 3
    s "When I invited [player] to this club, I had all of you in mind."
    s "I wanted him to come and make all of you happy like he'd done for me all my life."
    s "I wanted nothing more than for all of my friends to be happy."
    show monika 1a at t41 zorder 2
    show natsuki 1m at t43 zorder 2
    show yuri 1a at t42 zorder 2
    show sayori 2k at f44 zorder 3
    s "I did that so much that I forgot how to be happy without expending all my energy on everyone else."
    s "Eventually the rainclouds started moving in so much that all I could do was get drained."
    s "The rainclouds kept having their way with me, and it even got to a point where..."
    s "Where I considered..."
    show sayori 2c at f44 zorder 3
    s "That's...not important."
    show monika 1j at t41 zorder 2
    show natsuki 1j at t43 zorder 2
    show yuri 1c at t42 zorder 2
    show sayori 4x at f44 zorder 3
    show monika 1j at thide zorder 2
    hide monika
    show natsuki 1j at thide zorder 2
    hide natsuki
    show yuri 1c at thide zorder 2
    hide yuri
    show sayori 4x at t11 zorder 3
    s "The point is, [player] helped me to see things differently."
    s "And thanks to him, the rainclouds finally parted."
    s 2l "I don't know for how long, but..."
    s 1r "Thanks to all of you, I think I've reached a point where I can finally..."
    s 1s "Find myself..."
    s 1q "Over the rainbow."
    window hide
    $ renpy.pause(2)
    scene bg ending_a
    with fade
    pause(5)
    scene black
    with fade

    return
