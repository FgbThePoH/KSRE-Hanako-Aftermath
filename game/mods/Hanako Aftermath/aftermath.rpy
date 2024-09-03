label aftermath_start:
    stop sound
    stop music

    scene black
    play sound sfx_alarmclock volume 0.15 fadein 5.0 loop

    "{cps=3}mmh...   {/cps}{w=5.0}{cps=9}five more minutes...{/cps}"

    play sound sfx_hollowclick volume 0.05

    mystery "{size=-15}H... ..p."

    mystery "{size=-15}Hi.."

    play sound sfx_rustling volume 0.1

    mystery "{size=-10}Hi.. c.. ..p."

    "..."

    play sound sfx_rustling volume 0.2

    "mmh..."

    mystery "{size=-5}Hisao!"

    play sound sfx_rustling volume 0.3

    mystery "Come on wake up."

    scene bg school_dormhisao
    with openeye
    
    show hanako basic_worry_close at offscreenleft
    with charachange

    "A familiar ceiling."

    show hanako basic_worry_close at closeleft
    with charamovefast

    "And a familiar face."

    play music music_daily fadein 1.0 volume 0.5

    ha "Hisao come on, wake up, we will be late."

    hi "Yeah yeah, I'm awake."

    "I say, as I try to muster up strength to sit on the bed."

    "Maybe studying all night was a bad idea."

    show hanako basic_smile_close at center
    with charamovefast

    "Hanako smiles and leaves the room when she confirms that I woke up."

    hide hanako
    with charaexit
    play sound sfx_doorclose volume 0.5

    "My bed is calling my name to come back but I get up, not taking the beds tempting offer."

    "Still half asleep, my body switches into auto-mode, getting me into my uniform."

    "After opening the windows to let some fresh air in, I decide to wash my face to fully wake up before Hanako returns, I don't want her to worry about me today."

    scene bg school_dormbathroom
    with locationskip

    "As soon as I enter the bathroom another familiar face comes running to me, one I would have rather not seen today."

    show kenji neutral_close at center
    with charaenter

    play music music_kenji fadein 0.5

    ke "Hisao! Sleep well?"

    "Leaving me no personal space as usual, No suprises there I stopped expecting that from him a long time ago."

    "I make my way to the faucet for that ice cold wake up call."

    hi "Not at all, We-"

    "The cold water turns my brain on just in time to stop the words from leaving my mouth."

    hi "{b}I{/b} studied all night {b}alone{/b}."

    show kenji neutral at center
    with charadistant

    ke "Yeah I heard dude, noises didn't stop coming from your room last night."

    show kenji tsun
    with charachange

    ke "I thought you finally snapped after hearing that much head banging."

    show kenji happy
    with charachange 

    ke "Good to see you're still in one piece."

    hi "Wha- Why would I? Ah nevermind."

    "I can't do this right now, I have to get out of here quick."

    hi "Hey Kenji, are you taking todays exam?"

    show kenji tsun
    with charachange

    ke "Ugh! Really dude? That's what you want to talk about right now?"

    ke "Our class takes exams at a later date. Now I have to study too {i}thanks{/i} for reminding me."

    ke "I'm out of here."

    "I'm one step ahead."

    hide kenji
    with charaexit

    "I open the door and look outside, I see Hanako coming back with some food on her hands."

    play sound sfx_doorslam volume 2

    "I close the door as fast as humanly possible."

    show kenji tsun_close at center
    with characlose

    ke "What's up dude? Saw someone out there or something?"

    "Being stuck with Kenji for long is one thing but Kenji seeing Hanako here would be a fate worse than death."

    "Not just for me but for Hanako as well."

    ke "You have a weird look on your face. Are you ok?"

    hi "Yeah, I'm ok nothing, nothing is going on."

    show kenji happy_close
    with charachange

    ke "Great, let me pass then."

    hi "No can do."

    show kenji tsun_close
    with charachange

    ke "What. Why?"

    hi "{cps=5}I-uh..{/cps} I just remembered you don't have and money for snacks and stuff to study right?"

    hi "I couldn't bare to see you get struck with another 7 years of bad luck again."

    show kenji happy_close
    with charachange

    ke "Man you worry about the weirdest stuff."

    ke "Don't worry about it, I got some change from shopping yesterday."

    show kenji neutral_close
    with charachange

    ke "But if you want to support the defensive mesures against our cause I won't stop you."

    "I know I shouldn't but... I don't have any other options."

    hi "Oh? and what would those be I'm really down to listen right now, {b}right here{/b}."

    show kenji happy_close
    with charachange

    ke "Right now? Sure let me get my presentation sheets from my room."

    "Who has presentation sheets ready for that at hand."

    hi "No need just explain it to me here."

    play sound sfx_doorclose volume 0.1

    "That was my rooms door closing, Hanako must have made it in."

    show kenji tsun_close
    with charachange

    ke "I can't just do a presentation without my sheets, It would ruin my reputation."

    ke "It will take just under two hours Hisao, you will be like a newborn with all the truth laid upon you."

    ke "Naked and afraid."

    "Get me out of here."

    hi "Two hours is too long I have an exam remember? How about I visit you afternoon?"

    show kenji happy_close
    with charachange

    ke "Oh that's right. You go do your thing I'll see you after school."

    hi "Sure... I'll see you after school..."

    ke "See ya!"

    hi "Same."

    stop music fadeout 1.0

    scene bg school_dormhisao
    with locationskip

    play music music_daily fadein 3.0
    play sound sfx_doorclose

    "This will bite me in the back later but we are safe now."

    ""

    ""

    ""
