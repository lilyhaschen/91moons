import os
import discord
from discord import app_commands

MOONS = [
    {
        "name": "Moon 1 — The Whisper of the Forgotten Seed",
        "vision": (
            "You wake up in a room made of dry leaves and veils of mist. "
            "A winged hare hands you a magic seed and calls you Guardian of the Cycle. "
            "Évarya only exists as long as you believe in it."
        ),
        "mission": (
            "Name your seed. Plant it in a symbolic place—real or imaginary. "
            "Wish for it to grow."
        ),
        "fragment": ""
    },
    {
        "name": "Moon 2 — The Heart That Beats Beneath the Earth",
        "vision": (
            "Beneath the soil where Enrya was planted, something pulses. The roots touch a Living Stone, "
            "echoing an ancient sanctuary. A vision appears: a spiral altar surrounded by laughing spirits and an echoing lament."
        ),
        "mission": (
            "Pick up an old object and imagine it is a Living Stone. Listen to its lament and respond with a simple promise."
        ),
        "fragment": (
            "When the seed touches the stone and memory awakens, the lost Kingdom shudders in its sleep. "
            "Each restored link is a star rekindled in the sky of Évarya."
        )
    },
    {
        "name": "Moon 3 — The Song of the Golden Doe",
        "vision": (
            "You hear a sad song in your dreams. You find a golden doe trapped in invisible threads. "
            "She asks for help to be freed."
        ),
        "mission": (
            "Untangle some threads or string, imagining you are freeing the Doe. See her run free and leave golden flowers behind."
        ),
        "fragment": (
            "To free innocence is to weave the first embroidery of hope. The forest remembers those who listen to its whispers."
        )
    },
    {
        "name": "Moon 4 — The Mirror at the Bottom of the Well",
        "vision": (
            "You find an old well with a mirror of pure water, showing a forgotten version of yourself. "
            "The well once belonged to the seer Sylvindra."
        ),
        "mission": (
            "Look into a mirror and imagine a version of you from another world. Write what she would tell you to give you strength."
        ),
        "fragment": (
            "The mirrors of time do not show what will be, but what is hidden. The reflection of courage is revealed to those who dare remember."
        )
    },
    {
        "name": "Moon 5 — The Whispers of the Broken Oak",
        "vision": (
            "You find a colossal broken oak, whispering forgotten names. It asks you to listen to what it remembers."
        ),
        "mission": (
            "Hold something wooden to your ear, listen, and write down a name that comes to mind. This will be a sacred name."
        ),
        "fragment": (
            "Even broken, oaks hold the words of time. In their fibers, echoes of who we were before being forgotten sleep."
        )
    },
    {
        "name": "Moon 6 — The Song of the Misty Mill",
        "vision": (
            "In a stone mill covered by singing mosses, a melody floats in the air. "
            "Forgotten dreams are ground into silver dust there."
        ),
        "mission": (
            "Listen to a soft song and let an old memory come to you. Write it as a grain of ground dream."
        ),
        "fragment": (
            "In the mist sings what was forgotten. In the dust sleeps what can still bloom."
        )
    },
    {
        "name": "Moon 7 — The Guardian of the Glass Nest",
        "vision": (
            "You find a nest made of crystal threads with a pulsing egg. A wind bird offers you the egg to protect."
        ),
        "mission": (
            "Hold something small as if it were a magic egg. Imagine what you are caring for inside and write about it."
        ),
        "fragment": (
            "Not every wing flies, not every nest is visible. But every warmth is a promise."
        )
    },
    {
        "name": "Moon 8 — The Three Foxes of the Submerged Bridge",
        "vision": (
            "Three foxes (white, red, golden) guard a submerged bridge. To cross, you must answer impossible questions."
        ),
        "mission": (
            "Write three questions about yourself that seem impossible now. Write a wish for each."
        ),
        "fragment": (
            "The bridge between who we are and who we will be is guarded by enigmas with soft fur."
        )
    },
    {
        "name": "Moon 9 — Arbeth’s Silent Hive",
        "vision": (
            "You find a hive in a clearing of sleeping flowers. The honey feeds imagination, not the body."
        ),
        "mission": (
            "Eat something sweet (or imagine it). Write a fragment of story as if it were magic honey."
        ),
        "fragment": (
            "The sweetest words are born from silences with the scent of flowers."
        )
    },
    {
        "name": "Moon 10 — The Staircase in the Mist",
        "vision": (
            "A stone staircase covered in mist leads to the unknown. They say those who climb with an open heart see their secret refuge."
        ),
        "mission": (
            "Climb an imaginary staircase. At the top, visualize a place just for you and describe it as a landscape of Cortvalen."
        ),
        "fragment": (
            "For some, paradise is far away. For others, it is just the next step."
        )
    },
    {
        "name": "Moon 11 — The Bonfire of Unspoken Words",
        "vision": (
            "A blue fire burns, consuming feelings and words left unsaid. A spirit offers a parchment."
        ),
        "mission": (
            "Write something you've never said. Then tear it up or hide it—give it to the Blue Fire."
        ),
        "fragment": (
            "Not everything needs to be said to the world. But everything needs to be heard by you."
        )
    },
    {
        "name": "Moon 12 — The Mirror of the Crystal Lake",
        "vision": (
            "Enrya finds a lake smooth as glass with a floating mirror. The mirror shows who you would be without fear."
        ),
        "mission": (
            "Before the mirror, imagine your reflection without chains. Describe who this version of you is."
        ),
        "fragment": (
            "Sometimes what seems most like magic is remembering that we are still whole inside."
        )
    },
    {
        "name": "Moon 13 — The Cave of Future Voices",
        "vision": (
            "A cave where the echo returns not what you say, but what you will say. Future voices whisper possibilities."
        ),
        "mission": (
            "Imagine yourself one year from now. She says a phrase to you. Write it as a prophecy, then write your answer."
        ),
        "fragment": (
            "It’s not time that separates us from the future. It’s the words we haven’t yet dared to say."
        )
    },
    {
        "name": "Moon 14 — The Guardian of the Forgotten Bridge",
        "vision": (
            "A moss-covered bridge links present and past. A stone guardian rises, asking questions about regrets."
        ),
        "mission": (
            "Sit in silence. Imagine the bridge and the guardian. Answer: What have you left behind and still carry? What regret do you fear? What would you take if you crossed today?"
        ),
        "fragment": (
            "Some bridges don’t lead far away—they lead inward."
        )
    },
    {
        "name": "Moon 15 — The Willow of Forgotten Sleep",
        "vision": (
            "An ancient willow cradles memories. Sleeping under its branches, you live a dream of what could have been. Its leaves shine silver."
        ),
        "mission": (
            "Rest in silence, as if under the willow. Answer: What life would you have without wounds? What part of you is asleep? What did you dream?"
        ),
        "fragment": (
            "There are pains we don’t want to forget. But there are wearinesses so old only a dream can heal. The Willow doesn’t erase—it cradles. And when you wake… maybe you’ll remember who you almost were. And maybe, finally, be."
        )
    },
    {
        "name": "Moon 16 — The Ruins of Olyandor",
        "vision": (
            "Enrya reaches ancient ruins, where each stone whispers memories not lived. In the center, a stone reliquary pulses with an invented memory."
        ),
        "mission": (
            "Imagine a memory you wish were real. Write it. Give it a date, place, temperature, scent."
        ),
        "fragment": (
            "They say those who live among ruins have learned to find beauty in what isn’t whole. But there are also those who rebuild castles with just a single memory."
        )
    },
    {
        "name": "Moon 17 — The Garden of Things That Didn’t Last",
        "vision": (
            "Enrya finds a garden where lost but beautiful memories grow. Everything here blooms, even things that ended."
        ),
        "mission": (
            "Think of something you lost. Write a short letter to it. Bury the letter in your imaginary garden and watch a flower bloom."
        ),
        "fragment": (
            "Not everything eternal needs to last. Some things are eternal simply because they were truly felt."
        )
    },
    {
        "name": "Moon 18 — The Market of Useless Things",
        "vision": (
            "Enrya finds a market of useless but precious objects: sighs, bits of rainbow, lost buttons. Everything there has value."
        ),
        "mission": (
            "Pick a useless but precious object to you. Describe its smell, sound, memory. Carry it with you."
        ),
        "fragment": (
            "Useless things are like shooting stars: they don’t change destiny, but light up the moment."
        )
    },
    {
        "name": "Moon 19 — The Tree of Unsent Letters",
        "vision": (
            "A solitary tree filled with hanging letters, written but never sent. Apologies, words of love, promises."
        ),
        "mission": (
            "Write a letter you never dared send. Keep or destroy it. It becomes a leaf of the tree."
        ),
        "fragment": (
            "Not all silence is cowardice. Sometimes it’s just a letter waiting for the right time to be born."
        )
    },
    {
        "name": "Moon 20 — The Mad Hatter of the Upside-Down Heart",
        "vision": (
            "A crooked morning, a yellow sky upside down. Jumping mushrooms and the Hatter awaits. He offers you a deck of words to choose from."
        ),
        "mission": (
            "Write at least 10 spontaneous words. Mix them up, pick 3 at random. Write a story, poem, or letter combining those 3 words. Read aloud."
        ),
        "fragment": (
            "Not everything messy is wrong. Sometimes, it’s just the soul trying to dance without a script."
        )
    },
    {
        "name": "Moon 21 — The Well of Small Promises",
        "vision": (
            "A silent, damp dawn. A well covered in moss and lilac flowers. At the bottom, small lights: gentle promises never charged, that endure."
        ),
        "mission": (
            "Write a gentle promise to yourself, fold the paper and keep or symbolically burn it. Feel the well’s ritual."
        ),
        "fragment": (
            "Small promises are light enough to become a song even if the wind takes them away."
        )
    },
    {
        "name": "Moon 22 — The Bridge of Forgotten Fears",
        "vision": (
            "In the mist, a thin bridge appears over a dark stream. To cross, Lily must recognize an old fear she still carries."
        ),
        "mission": (
            "Write (or imagine) a fear that no longer makes sense but still follows you. Imagine dropping it from the bridge before crossing."
        ),
        "fragment": (
            "Fears do not cross bridges alone. They are left by the wayside, like old shoes, when we finally allow ourselves to pass."
        )
    },
    {
        "name": "Moon 23 — The Chest of Lost Smiles",
        "vision": (
            "Inside the trunk of a hollow tree, Lily finds a chest full of golden lights: forgotten smiles from other times."
        ),
        "mission": (
            "Recall a happy childhood moment, close your eyes and feel it. Place that smile in an 'imaginary chest', ready to access on tough days."
        ),
        "fragment": (
            "Stored smiles shine in the dark. They don’t save the world, but they light up a long night."
        )
    },
    {
        "name": "Moon 24 — The Shadow Who Chose to Stay",
        "vision": (
            "In a clearing, your shadow separates from Lily and lives adventures without fear. Lily learns she can accept the parts of herself she doesn’t want to see."
        ),
        "mission": (
            "Draw your shadow or write about a part of you you've tried to hide. Talk to it, even if only in your mind."
        ),
        "fragment": (
            "Accepting the shadow is freeing the light it hides. The dark side just wants to dance with you."
        )
    },
    {
        "name": "Moon 25 — The Lake of Whispered Secrets",
        "vision": (
            "Lily finds a deep lake where whispers rise from the water. They tell forgotten secrets from her own heart."
        ),
        "mission": (
            "Sit in silence and write (or think) a secret of yours for the water. Let the lake 'keep' it tenderly."
        ),
        "fragment": (
            "The lake tells no one, but gives courage to those who dare trust."
        )
    },
    {
        "name": "Moon 26 — The Grove of Swapped Names",
        "vision": (
            "Among trees with swapped nameplates, Lily needs to recover something forgotten about her own story."
        ),
        "mission": (
            "Swap the name of something in your room or house, just for today. See the world from a new angle. Reflect on how names change meanings."
        ),
        "fragment": (
            "When we change the name, we change the path we walk. Cortvalen smiles with every new naming."
        )
    },
    {
        "name": "Moon 27 — The Feathers of the North Wind Bird",
        "vision": (
            "A blue bird passes by, leaving behind a light feather. They say if you keep a feather from the wind, you’ll never get lost in the woods of doubt."
        ),
        "mission": (
            "Take (or imagine) a feather. Blow a wish of courage onto it and keep it as a talisman, physical or mental."
        ),
        "fragment": (
            "The north wind always brings a song to those in no hurry to arrive."
        )
    },
    {
        "name": "Moon 28 — The Clock Without Hands",
        "vision": (
            "In the middle of the forest, a stopped clock marks the time of feelings. Time only moves when you feel."
        ),
        "mission": (
            "Draw a clock and, instead of numbers, write important emotions for you. Which emotion makes your time move?"
        ),
        "fragment": (
            "Clocks are only cruel to those who forget to feel."
        )
    },
    {
        "name": "Moon 29 — The Garden of Small Waitings",
        "vision": (
            "A garden where each flower grows in the time of those who wait. There is no rush in Cortvalen."
        ),
        "mission": (
            "Plant (or imagine planting) a seed. Give it an intention. Observe daily, noting what changed inside and out."
        ),
        "fragment": (
            "The secret of the garden is not to bloom fast, but never to give up growing."
        )
    },
    {
        "name": "Moon 30 — The Veil of Gentle Truths",
        "vision": (
            "Lily finds a veil of transparent fabric. Looking through it, everything seems less frightening."
        ),
        "mission": (
            "Take a thin cloth or imagine one. Look at something difficult through it, making it softer, even if just for today."
        ),
        "fragment": (
            "Sometimes we need a veil to see the world less harshly."
        )
    },
    {
        "name": "Moon 31 — The Fountain of New Questions",
        "vision": (
            "A fountain that, instead of answers, offers questions that open new paths."
        ),
        "mission": (
            "Write down five questions you've never asked yourself. Choose one to reflect on today. What matters is asking, not answering."
        ),
        "fragment": (
            "Questions are seeds for new trails in the forest of days."
        )
    },
    {
        "name": "Moon 32 — The Book of Blank Pages",
        "vision": (
            "Lily finds a magic book that only shows blank pages—the future unwritten."
        ),
        "mission": (
            "Draw or write the beginning of a story you'd like to live. It can be impossible—everything is possible in Cortvalen."
        ),
        "fragment": (
            "Every blank page is an open key to the unlikely."
        )
    },
    {
        "name": "Moon 33 — The Ring of Silent Promise",
        "vision": (
            "Between the roots of a tree, Lily finds a ring. They say whoever makes a silent promise to themselves there will be heard by the forest."
        ),
        "mission": (
            "Make a promise just for yourself. You don't need to say or write it—just feel it."
        ),
        "fragment": (
            "Promises not spoken aloud grow deeper roots."
        )
    },
    {
        "name": "Moon 34 — The Meeting with the Chattering Grondelho",
        "vision": (
            "A Grondelho, a magical creature from Cortvalen, appears and speaks in metaphors. Only those who listen with their hearts understand."
        ),
        "mission": (
            "Write a metaphor about how you feel today. Read it aloud and try to feel what it reveals."
        ),
        "fragment": (
            "Speaking in metaphors is teaching the forest the language of dreams."
        )
    },
    {
        "name": "Moon 35 — The Dew of Good Dreams",
        "vision": (
            "At dawn, each leaf carries a shining drop of dew. Whoever collects a drop can remember a good dream."
        ),
        "mission": (
            "Write a beautiful dream you've had, real or invented. Keep it as dew for hard days."
        ),
        "fragment": (
            "Dreams kept in drops do not evaporate in the heat of fear."
        )
    },
    {
        "name": "Moon 36 — The Cave of Gentle Echoes",
        "vision": (
            "A cave where every word spoken comes back as a gentle echo, bringing comfort to the speaker."
        ),
        "mission": (
            "Say a kind word to yourself. Imagine the cave repeating it to you even more beautifully."
        ),
        "fragment": (
            "Kind words always return bigger than when they left."
        )
    },
    {
        "name": "Moon 37 — The Crossing of Dancing Pencils",
        "vision": (
            "Pencils float in the air forming bridges of color. Each color represents an emotion, and only those who draw their own path can cross."
        ),
        "mission": (
            "Take pencils or pens and draw a colorful path on paper, representing feelings of the day."
        ),
        "fragment": (
            "Colorful paths are maps to places we don't yet know how to name."
        )
    },
    {
        "name": "Moon 38 — The Mystery of Singing Seeds",
        "vision": (
            "Seeds sing softly, bringing calm. Lily finds one and feels peace."
        ),
        "mission": (
            "Choose a soft song to listen to. While it plays, imagine a seed growing in your heart, spreading calm."
        ),
        "fragment": (
            "Seeds that sing bloom first in silence."
        )
    },
    {
        "name": "Moon 39 — The Banquet of Small Miracles",
        "vision": (
            "A table is set with magical food. Each dish celebrates a small achievement or overcoming."
        ),
        "mission": (
            "List three good things that happened this week, even the smallest. Celebrate like a banquet of gratitude."
        ),
        "fragment": (
            "Small miracles feed the heart for great journeys."
        )
    },
    {
        "name": "Moon 40 — The Well of Sunken Stars",
        "vision": (
            "At the bottom of a well, submerged stars shine. They say each star is a forgotten wish."
        ),
        "mission": (
            "Close your eyes, pick an old wish and throw a stone (or just imagine) into the well, as if returning light to a star."
        ),
        "fragment": (
            "Stars only go out if no one remembers they exist."
        )
    },
    {
        "name": "Moon 41 — The Portal of Open Dreams",
        "vision": (
            "Before Lily appears a shining portal. It only opens to those who accept to dream with open eyes."
        ),
        "mission": (
            "Write or draw a daydream. Imagine yourself crossing the portal into this new world."
        ),
        "fragment": (
            "Portals only appear to those who dare to cross what doesn’t exist (yet)."
        )
    },
    {
        "name": "Moon 42 — The Mirror of Cloudy Waters",
        "vision": (
            "Enrya faces a lake of cloudy waters. Whoever dares look at their reflection sees not what they are, but what they fear to be."
        ),
        "mission": (
            "Look into a mirror, even if foggy or dirty, and imagine which version of yourself it shows today. Write about this reflection and what it wants to tell you."
        ),
        "fragment": (
            "The lake shows what time hides. Sometimes, we just need to dive to see."
        )
    },
    {
        "name": "Moon 43 — The Circle of Hair in the Wind",
        "vision": (
            "In a clearing, fairies celebrate by dancing with their hair loose in the wind, celebrating the freedom of small rebellions."
        ),
        "mission": (
            "Let your hair down (or imagine). Dance freely for 1 minute, even if sitting. Feel the wind (real or imagined)."
        ),
        "fragment": (
            "Freedom is learned in the spinning of hair and laughter without fear."
        )
    },
    {
        "name": "Moon 44 — The Tracks of the Gentle Wolf",
        "vision": (
            "Lily follows wolf tracks that do not frighten: they lead to shelter, not danger. The wolf only howls to scare away loneliness."
        ),
        "mission": (
            "Draw a trail of tracks or take a short walk around the house, leaving a trail of something good (scent, color, note)."
        ),
        "fragment": (
            "The wolf cares for what others flee from. Every guardian was once lonely."
        )
    },
    {
        "name": "Moon 45 — The Bench of Living Longings",
        "vision": (
            "On a lonely park bench, memories sit beside those tired of longing."
        ),
        "mission": (
            "Sit and fondly remember someone or something you miss. Allow yourself to feel, without guilt. Write a letter to this longing."
        ),
        "fragment": (
            "Longings only weigh while we deny their embrace."
        )
    },
    {
        "name": "Moon 46 — The Lantern of Night Creatures",
        "vision": (
            "Magical animals appear, each carrying a tiny lantern. They light up the dark corners of the mind."
        ),
        "mission": (
            "Draw (or imagine) little lanterns lit in a dark place in your memory or your room. Feel the difference."
        ),
        "fragment": (
            "Every night creature is a small courage lit up."
        )
    },
    {
        "name": "Moon 47 — The Smile of the Forgotten Statue",
        "vision": (
            "An old statue, covered in moss, smiles only when someone believes in its joy."
        ),
        "mission": (
            "Smile at an old photo, object, or plant, believing it can smile back at you. Write down the feeling."
        ),
        "fragment": (
            "Smiles sprout even from stones, when watered with attention."
        )
    },
    {
        "name": "Moon 48 — The Labyrinth of Broken Words",
        "vision": (
            "Unspoken or misunderstood words pile up, forming a small labyrinth. Lily must find her way out without getting lost in her own thoughts."
        ),
        "mission": (
            "List words or phrases you never finished saying. Pick one to complete today, even if just on paper."
        ),
        "fragment": (
            "Labyrinths of words are drawn by those afraid to be heard, but longing to be found."
        )
    },
    {
        "name": "Moon 49 — The Bag of Small Achievements",
        "vision": (
            "A gnome offers a bag that fits all the pride from small victories."
        ),
        "mission": (
            "List three recent achievements, even if they seem silly. Keep them in mind or write on paper to check on bad days."
        ),
        "fragment": (
            "Small achievements weigh less than failure, but carry you further."
        )
    },
    {
        "name": "Moon 50 — The Rooster of Brave Mornings",
        "vision": (
            "A magical rooster crows not to wake you, but to remind you each morning is a new chance."
        ),
        "mission": (
            "When you wake up, say (or think) a phrase of courage to yourself before anything else."
        ),
        "fragment": (
            "Dawn is always an invitation, never an obligation."
        )
    },
    {
        "name": "Moon 51 — The Keys to Invisible Doors",
        "vision": (
            "On the path, Lily finds keys that don't open normal doors but allow her to imagine secret passages."
        ),
        "mission": (
            "Draw a different, invented key. Write or imagine what it would open in your inner world."
        ),
        "fragment": (
            "Invisible doors exist only for those who seek different keys."
        )
    },
    {
        "name": "Moon 52 — The Embrace of the South Wind",
        "vision": (
            "A warm wind hugs and consoles. They say this wind is made of all the hugs that were missing."
        ),
        "mission": (
            "Hug yourself for a few seconds, feeling warmth and comfort. If you want, imagine the wind as an old hug."
        ),
        "fragment": (
            "The south wind blows when the heart remembers the comfort of embrace."
        )
    },
    {
        "name": "Moon 53 — The Awakening of the Flower of Fear",
        "vision": (
            "At the heart of the woods, a blue flower only blooms when someone looks at their own fear without looking away."
        ),
        "mission": (
            "Write (or draw) the shape and color of your fear today. Observe it without judging. See if it changes."
        ),
        "fragment": (
            "Fear, seen up close, often reveals itself as a flower — not a monster."
        )
    },
    {
        "name": "Moon 54 — The Locket of Guarded Feelings",
        "vision": (
            "Lily finds a locket where she can store a feeling to access when needed."
        ),
        "mission": (
            "Choose a feeling (joy, gratitude, longing...) and imagine placing it inside a small object. Use it as a mental amulet."
        ),
        "fragment": (
            "Feelings kept can bloom even in the harshest winter."
        )
    },
    {
        "name": "Moon 55 — The Backyard of Childhoods",
        "vision": (
            "An enchanted backyard appears, where children play with past versions of themselves."
        ),
        "mission": (
            "Recall a childhood game or song and repeat it today, even if just for a moment."
        ),
        "fragment": (
            "Time plays hide and seek with those who dare to be children again."
        )
    },
    {
        "name": "Moon 56 — The Little Bench of Silent Conversations",
        "vision": (
            "A little bench waits for conversations with yourself, without hurry or pressure."
        ),
        "mission": (
            "Sit alone for 5 minutes, listening to whatever your mind or heart wants to say. Write or just listen."
        ),
        "fragment": (
            "Silence is also a conversation, if the listening is honest."
        )
    },
    {
        "name": "Moon 57 — The Riddle of Entwined Hands",
        "vision": (
            "Two magical hands appear in the forest. With each interlacing of fingers, a doubt disappears."
        ),
        "mission": (
            "Join your hands (or imagine it) and ask yourself for help in solving a problem or making a decision."
        ),
        "fragment": (
            "Sometimes answers appear only when we join hands with our own destiny."
        )
    },
    {
        "name": "Moon 58 — The Balloon of Suspended Wishes",
        "vision": (
            "Magical balloons rise into the sky, carrying wishes that haven’t become plans yet."
        ),
        "mission": (
            "Write a wish you haven’t yet had the courage to plan. Imagine it rising like a colorful balloon."
        ),
        "fragment": (
            "Wishes only weigh us down when forgotten. Set free, they decorate the sky of hope."
        )
    },
    {
        "name": "Moon 59 — The Wheel of Seasons",
        "vision": (
            "A giant wheel of seasons spins, showing that everything changes, always. Spring, summer, autumn, winter, restart."
        ),
        "mission": (
            "Draw or imagine a wheel divided into four parts, writing what changed in you in each season of last year."
        ),
        "fragment": (
            "The cycle of seasons is a reminder that nothing is permanent—not pain, not fear."
        )
    },
    {
        "name": "Moon 60 — The Poem of the Talking Animals",
        "vision": (
            "Forest animals speak in silly, wise poems."
        ),
        "mission": (
            "Write a short poem in the voice of a magical animal. It doesn’t have to rhyme, just have fun."
        ),
        "fragment": (
            "The poetry of animals is always simple, but carries ancient secrets."
        )
    },
    {
        "name": "Moon 61 — The Thread of Sweet Memory",
        "vision": (
            "A golden thread appears, connecting Lily to a sweet memory."
        ),
        "mission": (
            "Take a thread, ribbon, or lock of hair and connect it to a cherished object. Leave it there today as an anchor of joy."
        ),
        "fragment": (
            "Sweet memories do not sour with time. They only become more precious."
        )
    },
    {
        "name": "Moon 62 — The Charm of the Wet Handkerchief",
        "vision": (
            "Rain falls softly. Whoever takes a handkerchief and wets it in the rain can dry old tears."
        ),
        "mission": (
            "Wet a handkerchief (or cloth), press it to closed eyes and imagine your sorrows being washed away."
        ),
        "fragment": (
            "Rain consoles those who do not hurry to dry themselves."
        )
    },
    {
        "name": "Moon 63 — The Testimony of the Ancient Stone",
        "vision": (
            "In the middle of the path, a mossy stone tells stories only to those who sit in silence upon it."
        ),
        "mission": (
            "Sit on something solid and be silent for 2 minutes, listening to whatever thoughts arise. Then write what the 'stone' told you."
        ),
        "fragment": (
            "Every old stone is a book waiting to be read in silence."
        )
    },
    {
        "name": "Moon 64 — The Portal of Invented Words",
        "vision": (
            "A portal opens only with new, invented words."
        ),
        "mission": (
            "Create a magic word for a feeling or wish of yours. Write it and invent a meaning."
        ),
        "fragment": (
            "New words create portals that old pains cannot cross."
        )
    },
    {
        "name": "Moon 65 — The Moonlight of Simple Things",
        "vision": (
            "Golden moonlight reveals beauty in all that is simple: a cup, a pillow, a scent."
        ),
        "mission": (
            "Choose a simple object and pay attention to it for 5 minutes, feeling gratitude for its existence."
        ),
        "fragment": (
            "The most magical things are those that survive the eyes of time."
        )
    },
    {
        "name": "Moon 66 — The Seal of Unlikely Friendship",
        "vision": (
            "Enrya meets an unlikely creature (like a flying fish or a blue fox) and forges an unexpected friendship."
        ),
        "mission": (
            "Draw or imagine an unlikely friend to accompany you today. Note its name, appearance, voice, and a secret."
        ),
        "fragment": (
            "Every unlikely friendship is a password to secret doors of the heart."
        )
    },
    {
        "name": "Moon 67 — The Mortar of Protective Herbs",
        "vision": (
            "In the woods, a mortar grinds herbs that protect the soul and bring good dreams."
        ),
        "mission": (
            "Smell an herb or tea, savor its aroma for 1 minute. Imagine it protecting your sleep and home."
        ),
        "fragment": (
            "Scents are secret guardians of happy memories."
        )
    },
    {
        "name": "Moon 68 — The Song of the Shy Fairy",
        "vision": (
            "A shy fairy sings so softly that only attentive hearts can hear."
        ),
        "mission": (
            "Be absolutely silent and try to hear a new or distant sound. Imagine it’s the fairy singing just for you."
        ),
        "fragment": (
            "Silence is a stage for voices that fear has not yet taught to shout."
        )
    },
    {
        "name": "Moon 69 — The Necklace of Dew Drops",
        "vision": (
            "At dawn, Lily finds a necklace made of shining drops, each one a moment of calm lived."
        ),
        "mission": (
            "List small moments of calm you felt this week. Imagine them as drops on a necklace and wear it mentally during the day."
        ),
        "fragment": (
            "Calm can also be collected, like hidden jewels."
        )
    },
    {
        "name": "Moon 70 — The Tree of Found Gifts",
        "vision": (
            "A tree where small lost objects grow: buttons, pencils, ribbons, memories."
        ),
        "mission": (
            "Find a forgotten object in your house and invent a new story for it. Leave it in a place of honor today."
        ),
        "fragment": (
            "Found gifts are reminders that the universe makes surprises too."
        )
    },
    {
        "name": "Moon 71 — The Fabric of Shared Stories",
        "vision": (
            "Magical weavers entwine threads of stories. Each thread is a shared memory."
        ),
        "mission": (
            "Tell someone (or write for yourself) a special memory. Imagine it weaving into a great magical fabric."
        ),
        "fragment": (
            "Shared stories never disappear. They become roots of trees that never fall."
        )
    },
    {
        "name": "Moon 72 — The Hat of Disguised Optimism",
        "vision": (
            "A hat that makes everything seem a little better, without anyone noticing."
        ),
        "mission": (
            "Wear (or imagine) a different hat. See a problem with new eyes. What changes?"
        ),
        "fragment": (
            "Disguised optimism is the magic that turns routine into adventure."
        )
    },
    {
        "name": "Moon 73 — The Shoe of Repeated Courage",
        "vision": (
            "A magic shoe appears: each step taken, courage increases, even slowly."
        ),
        "mission": (
            "Take three brave steps today: say no, try something new, or just get out of bed even without will."
        ),
        "fragment": (
            "Courage is a muscle: it trains every day, even with small steps."
        )
    },
    {
        "name": "Moon 74 — The Glow of Kind Words",
        "vision": (
            "Kind words appear like fireflies around Lily, lighting dark paths."
        ),
        "mission": (
            "Say something kind to someone (or yourself). Write how you feel before and after."
        ),
        "fragment": (
            "Fireflies don’t light up the whole world, just the piece they need to."
        )
    },
    {
        "name": "Moon 75 — The Amulet for Rainy Days",
        "vision": (
            "On a rainy day, Lily receives an amulet that protects her from gray sadness."
        ),
        "mission": (
            "Create (or imagine) an amulet from something small. Keep it in your pocket and remember it when the day gets tough."
        ),
        "fragment": (
            "Rain is just the sky washing the forest’s soul."
        )
    },
    {
        "name": "Moon 76 — The Balcony of Nighttime Stories",
        "vision": (
            "An enchanted balcony appears to listen to secrets of the night. Soft voices, gentle light."
        ),
        "mission": (
            "Tell a short story before bed, real or invented. Record it as audio or write it down if you wish."
        ),
        "fragment": (
            "Night stories cover sleep with blankets of adventure."
        )
    },
    {
        "name": "Moon 77 — The Sound of the Stone Heart",
        "vision": (
            "In silence, Lily realizes that even stones have a rhythm: slow, but steady."
        ),
        "mission": (
            "Listen to your own pulse or feel your heartbeat. Imagine it echoing in the stones along the path."
        ),
        "fragment": (
            "Even stones learn to beat when someone teaches them to listen."
        )
    },
    {
        "name": "Moon 78 — The Bath for Tired Feet",
        "vision": (
            "A magical stream refreshes the feet of those who have walked too far. It brings lightness and rest."
        ),
        "mission": (
            "Put your feet in cool water or imagine it. Feel the relief and let your worries flow away with the current."
        ),
        "fragment": (
            "Rested feet walk farther, even if the destination is unclear."
        )
    },
    {
        "name": "Moon 79 — The Ring of Saved Laughter",
        "vision": (
            "A golden ring stores sincere laughter. Whoever wears it never forgets to laugh on hard days."
        ),
        "mission": (
            "Try to remember a good laugh. Keep it as a mental ring to wear on gray days."
        ),
        "fragment": (
            "Saved laughter opens doors where keys don’t fit."
        )
    },
    {
        "name": "Moon 80 — The Whisper of the Blue Thrush",
        "vision": (
            "A blue thrush sings only for those who need hope. Its song is heard even when there’s no one around."
        ),
        "mission": (
            "Listen to a bird song or a calm music. Imagine the thrush singing just for you."
        ),
        "fragment": (
            "Hope is the melody that doesn’t need an audience."
        )
    },
    {
        "name": "Moon 81 — The Rug of Little Adventures",
        "vision": (
            "A magic rug takes Lily to new places without leaving the spot."
        ),
        "mission": (
            "Sit on a rug or blanket. Close your eyes and imagine a small adventure: a forest, a party, a castle."
        ),
        "fragment": (
            "Every adventure begins with eyes closed and ends with an open heart."
        )
    },
    {
        "name": "Moon 82 — The Note for Bright Days",
        "vision": (
            "Lily finds a note with an inspiring phrase, left by someone who once believed in tomorrow."
        ),
        "mission": (
            "Write yourself an optimistic note, keep it to read on a sad day."
        ),
        "fragment": (
            "Bright days hide behind clouds waiting for your gaze."
        )
    },
    {
        "name": "Moon 83 — The Clock of Needed Pauses",
        "vision": (
            "A magic clock only works when someone truly rests."
        ),
        "mission": (
            "Plan a 10-minute break just for yourself. Do nothing but exist in that time."
        ),
        "fragment": (
            "Pauses are hands that bring us closer to who we are."
        )
    },
    {
        "name": "Moon 84 — The Book of Beautiful Words",
        "vision": (
            "A book contains only beautiful words that warm and lift the heart."
        ),
        "mission": (
            "Choose a word you find beautiful. Repeat it like a mantra today."
        ),
        "fragment": (
            "Beautiful words are portable fireplaces for tired souls."
        )
    },
    {
        "name": "Moon 85 — The Bell of New Beginnings",
        "vision": (
            "A wind bell rings every time someone decides to start again, no matter how small the decision."
        ),
        "mission": (
            "Do something new today: a different route, a new flavor, an inverted routine."
        ),
        "fragment": (
            "The sound of a new beginning is always lighter than the weight of an ending."
        )
    },
    {
        "name": "Moon 86 — The Well of Kept Images",
        "vision": (
            "A magic well reflects images of the past gently, without pain."
        ),
        "mission": (
            "Look at an old photo and write about a detail, without nostalgia—just observing with care."
        ),
        "fragment": (
            "Images only hurt when we forget to look at them with tenderness."
        )
    },
    {
        "name": "Moon 87 — The Cloak of Healing Words",
        "vision": (
            "A cloak made of words of healing covers Lily at dusk."
        ),
        "mission": (
            "Write or say healing phrases to yourself: 'I forgive myself,' 'I am enough,' 'I deserve peace.' Use them as an invisible cloak."
        ),
        "fragment": (
            "Healing is dressing yourself in patience."
        )
    },
    {
        "name": "Moon 88 — The Earring of Gentle Voices",
        "vision": (
            "A magic earring lets you hear compliments and sweet words carried by the wind."
        ),
        "mission": (
            "Write or imagine compliments for yourself, even if they seem exaggerated. Listen to them with your eyes closed."
        ),
        "fragment": (
            "Gentle voices need neither mouth nor address."
        )
    },
    {
        "name": "Moon 89 — The Fan of Calm Storms",
        "vision": (
            "A magic fan calms inner storms, bringing fresh air in anxious moments."
        ),
        "mission": (
            "With your hand or a fan, make wind on your own face and imagine worries blowing away."
        ),
        "fragment": (
            "Storms exist so we learn to open the windows of the soul."
        )
    },
    {
        "name": "Moon 90 — The Embroidery of Waiting Days",
        "vision": (
            "Long days become embroidery: each stitch is a wait, each color, a hope."
        ),
        "mission": (
            "Draw or embroider colorful lines on paper, fabric, or in your mind, symbolizing different waits in life."
        ),
        "fragment": (
            "Waiting is the art of sewing hope into time."
        )
    },
    {
        "name": "Moon 91 — The Portal of Crossing",
        "vision": (
            "The day arrives when Lily finds the Portal of Crossing: an arch of light between trees, where all that has been lived turns into wings."
        ),
        "mission": (
            "Thank yourself for the journey. Make a small farewell ritual: light a candle, write a journey summary, or just take a deep breath, ready for the new."
        ),
        "fragment": (
            "Crossing is not the end—it is the beginning of everything that can be, now with the strength of 91 moons in your heart."
        )
    }
]
TOKEN = os.environ.get("DISCORD_TOKEN")
user_moons = {}

class MoonsBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        @self.tree.command(name="moon", description="Reveal your next Cortvalen Moon story!")
        async def moon(interaction: discord.Interaction):
            user_id = str(interaction.user.id)
            moon_num = user_moons.get(user_id, 0)
            moon = MOONS[moon_num % len(MOONS)]  # wrap around after 91

            # Build the reply
            out = [
                f"**{moon['name']}**\n",
                f"**Vision:** {moon['vision']}\n",
                f"**Mission:** {moon['mission']}\n",
            ]
            if moon['fragment']:
                out.append(f"**Fragment of the Grimorio:** {moon['fragment']}")
            # Update for next call
            user_moons[user_id] = moon_num + 1

            await interaction.response.send_message("\n".join(out), ephemeral=True)

    async def on_ready(self):
        print(f"🌙 Moons Bot ready as {self.user}")
        try:
            synced = await self.tree.sync()
            print(f"Slash commands synced: {len(synced)}")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

if __name__ == "__main__":
    if not TOKEN:
        print("Please set your Discord bot token in the DISCORD_TOKEN environment variable.")
        exit(1)
    MoonsBot().run(TOKEN)
