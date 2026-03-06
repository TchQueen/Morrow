define sounds = ['audio/A1.ogg']
define bgmm = ['audio/MORROWTHEME.mp3']

init python:
   def type_sound(event, interact = True, **kwargs):
      if not interact:
         return

      if event == "show": #if text's being written by character, spam typing sounds until the text ends
         renpy.sound.play(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))

      elif event == "slow_done" or event == "end":
         renpy.sound.stop()



define p = Character("'...'", callback=type_sound)
define r = Character("???", callback=type_sound)
define c = Character("[namae]", callback=type_sound)
define m = Character("Morrow", callback=type_sound)


label start:
   play music "MORROWTHEME.mp3" volume 0.2
   scene main background
   with fade

   show player normal
   with dissolve
   p "I just moved to a new farm last night and immediately fell asleep."


   show player smile at right
   with moveinright
   p "Wow!"
   p "What green hills!"
   show player normal at right

   show morrow poker at left
   with moveinleft
   r "..."

   show player smile at right
   p "Hello!"
   p "I just got in last night. Do you live here too?"
   show player normal at right

   show morrow normal at left
   r "Hello"
   r "Yes, I do live here."
   r "What's your name?"
   show morrow poker at left

   $ namae = renpy.input("Name, Please!")

   $ namae = namae.strip()

   if namae == "":
    $ namae = "Sam"

   show morrow normal at left
   r "I see."
   r "I suppose that's an okay name for a horse. My name is Morrow."
   show morrow poker at left

   show player thinking at right
   c "(I guess a cat would be proud. Best not to take offense.)"

   show player smile at right
   c "Nice to meet you, Morrow!"
   show player normal at right

   show morrow normal at left
   m "I suppose you want a tour of the place now"

   show player smile at right
   c "A tour! How exciting!"
   show player normal at right

   show morrow sniffy at left
   m "It's not much of a tour, anyway."
   m "There's just these stables, the chickens live on the other side."
   m "The fields are also quite nice. You can see them from here."
   show morrow poker at left

   "Bark! Bark!! Bark!!!"
   show morrow surprised at left

   show player thinking at right
   c "(There's a dog here too? Why didn't Morrow mention?)"
   show player normal at right

   m "I have to go now!"
   hide morrow surprised
   with fade

   show player thinking at right
   c "(He was a little weird just now.)"
   c "(Should I follow him?)"

   show player normal at walk
   c "(He went down here...)"
   c "(He's in the final stall. I think I should be able to see what's happening if I look over a little.)"
   hide player normal

   scene barn bg

   c "(Are they sharing a meal?)"
   c "That must be the dog from before!"

   show puck surprise1 at left
   r "?!?!?!"

   show player thinking at right
   c "(What awful scars on that dog's face!)"
   hide puck surprise
   hide player thinking

   show morrow angry at left
   m "What are you doing here?!?"

   show player awkward at right
   c "I'm sorry for startling you!"
   c "I didn't mean to say that out loud."
   m "Get out!"
   c "Sorry!"
   hide morrow angry with dissolve
   hide player awkward with dissolve

   scene main background
   show player sad at right
   with dissolve
   c "I really messed up today."

   show morrow sad at left
   with moveinleft
   m "Hey..."
   show morrow remorse at left

   c "I'm really sorry about earlier..."
   c "I shouldn't have followed you."

   show morrow sad at left
   m "It's fine."
   m "I shouldn't have lost my temper like that."
   show morrow remorse at left

   show player thinking at right
   c "(He looks tired.)"

   show player serious at right
   c "Are you okay?"
   show player sernom at right

   show morrow sad at left
   m "Would you like to hear a story?"
   show morrow remorse at left

   show player thinking at right
   c "(Oh dear)"
   show player serious at right
   c "I'm guessing it's about that dog from earlier?"
   show player sernom at right

   show morrow normal at left
   m "You're not as dumb as I thought."
   m "His name is Puck."
   show morrow poker at left

   show player serious at right
   c "He's got such awful-looking scars on his head."
   show player sernom at right
   
   show morrow normal at left
   m "Would you like to know how it happened?"
   
   menu:
      "Yes or No?"
      "Yes":
         show player serious at right
         c "I'd be happy to listen."
         show player sernom at right

      "No":
         show player serious at right
         c "You don't have to tell me if you don't want to."
         show player sernom at right
         show morrow sniffy at left
         m "Why would I tell you if I didn't want to?"
         show morrow poker at left
         show player thinking at right
         c "(Still as prickly as ever)"
         show player sernom at right
         show morrow sad at left
         m "I'm sorry. I want to tell you for whatever reason."
         m "Will you listen?"
         show morrow remorse at left
         show player serious at right
         c "Then, yes. I'd be happy to listen."
         show player sernom at right
         jump contd

label contd:
   show morrow sad at left
   m "As you've said, Puck has scars on his face."
   m "I was the one who did it."
   show morrow remorse at left
   show player sad at right
   c "(Oh no!)"
   show player sadnom at right
   show morrow sad at left
   m "When he first arrived, he was as energetic and playful as one would expect from a puppy."
   m "But it got on my nerves. He followed me around. Biting, digging my clean farm. I couldn’t stand it."
   show morrow remorse at left
   show player thinking at right
   c "(Did he lose his temper and hurt him just because of that?!)"
   show morrow sniffy at left
   m "You're thinking something off track there, aren't you?"
   show morrow remorse at left
   show player awkward at right
   c "Sorry."
   show player sadnom at right
   show morrow sad at left
   m "Anyway, I kept it all in, but I was still angry everyday."
   m "One day, I woke up to find that I was wet for some reason, and my body was wet. I couldn’t figure it out at first."
   m "When I opened my eyes, Puck was looking at me, like she expected a pat on the head. Tongue out and panting. Then I started to smell it. It was pee. Puck had peed on me while I slept."
   m "I lost it. I started yelling and snarling but then he started barking, running around, like he thought it was all a game to him."
   m "Then I lashed out. At first I had no claws out. But he yelped, and I felt a strange sense of satisfaction. Relief."
   m "I swiped and swiped and she yelped and cried and I didn’t stop. I guess at some point my claws came out."
   m "By the time I came back to my senses, the damage had been done. So now he is my responsibility. It was my fault."
   show morrow remorse at left
   show player sad at right
   c "And you've ben taking care of him ever since. I'm guessing that was your meal earlier. Do you give him half of all your meals?"
   show player sadnom at right
   show morrow sad at left
   m "He tells me not to, and he tries not to eat it. But he is a dog after all, he can't resist."
   m "How can I not? It was my fault."
   show morrow remorse at left

   menu:
      "What now?"
      "Get Angry":
         show player angnom at right
         c "(for some reason I get angry, at both Puck and Morrow.)"
         show player angry at right
         c "So? Are you going to keep carrying your guilt around like a medal?"
         show player angnom at right
         show morrow surprised at left
         m "What?"
         show player angry at right
         c "Look. I can't tell you it wasn't your fault. But I also don't think you should carry it around like this."
         show player angnom at right
         show morrow confused at left
         m "I don't understand."
         show morrow remorse at left
      "Get Sad":
         c "(I feel a surge of immense sadness wash over me at the whole situation.)"
         show player sad at right
         c "You've been here all this time making amends, haven't you?"
         c "And that's good. But I also don't think it's okay for you to wear your guilt like this. For you or for Puck."
         show morrow remorse at left
         show player sadnom at right
         show morrow very sad at left
         m "But he has to carry those scars for the rest of his life..."
         show morrow remorse at left
         show player sad at right
         c "I haven’t even talked to Puck, but I feel like he doesn’t resent you. Does he? You’ve been working hard, haven’t you?"
         show player sadnom at right
         show morrow very sad at left
         m "But-"
         show player sad at right
         c "Listen to me!"
         show morrow remorse at left
         jump coontd

label coontd:
   show player angry at right
   c "I can't tell you how to live."
   c "I don’t know anything besides what you’ve told me, and I don’t have any easy answers to give you. But maybe, just maybe you don’t have to carry the weight of it every second of every day."
   show player sadnom at right
   m "...."
   show player thinking at right
   c "(Oh no, he's not saying anything. I might've just crossed a line."
   show player sernom at right
   show morrow normal at left
   m "Thank you."
   hide morrow normal with dissolve
   show player surprised at right
   c "(Did he just brush me with his tail??)"
   hide player surprised with dissolve

   c "We never did talk about Puck anymore, and Morrow is still very attentive."
   c "But I like to think they are both doing better, and in the days that follow we can see them going on walks as the sun sinks behind the hills of the small farm."








   return













   






