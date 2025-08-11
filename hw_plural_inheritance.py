from abc import ABC, abstractmethod


class Films:
    all_films = []

    def __init__(self,rating,name,year,studio,main_actor):
        self.rating = float(rating)
        self.name = name
        self.year = year
        self.studio = studio
        self.main_actor = main_actor

        Films.all_films.append(self)
    @staticmethod
    def average_rating():
        total_rating = 0
        for film in Films.all_films:
            total_rating += film.rating
        return total_rating/len(Films.all_films)

    def show_name(self):
        for name in Films.all_films:
            print(f"{name}")


Films.all_films.clear()

f1 = Films(8.5, "Inception", 2010, "Warner Bros", "Leonardo DiCaprio")
f2 = Films(9.1, "The Dark Knight", 2008, "Warner Bros", "Christian Bale")
f3 = Films(7.8, "Interstellar", 2014, "Paramount", "Matthew McConaughey")
for film in Films.all_films:
    print(film.rating, type(film.rating))

print(Films.average_rating())



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 2 HUMAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



class Legs(ABC):
    def __init__(self,fingers,nails,feet,knee,heel,skin_color):
        self.fingers = fingers
        self.nails = nails
        self.feet = feet
        self.knee = knee
        self.heel = heel
        self.skin_color = skin_color

    @abstractmethod
    def show_info(self):
        return

class Hands(ABC):
    def __init__(self,fingers,nails,palm,wrist,elbow,shoulder,skin_color):
        self.fingers = fingers
        self.nails = nails
        self.palm = palm
        self.wrist = wrist
        self.elbow = elbow
        self.shoulder = shoulder
        self.skin_color = skin_color

    @abstractmethod
    def show_info(self):
        return

class Head(ABC):
    def __init__(self,brain,eyes,hair,mouth,lips,nose,ears,teeth,tongue):
        self.brain = brain
        self.eyes = eyes
        self.hair = hair
        self.mouth = mouth
        self.lips = lips
        self.nose = nose
        self.ears = ears
        self.teeth = teeth
        self.tongue = tongue

    @abstractmethod
    def show_info(self):
        return

class Chest(ABC):
    def __init__(self,heart,lounges,nipples):
        self.heart = heart
        self.lounges = lounges
        self.nipples = nipples

    @abstractmethod
    def show_info(self):
        return

class Belly(ABC):
    def __init__(self,stomach,kidney,liver,):
        self.stomach = stomach
        self.kidney = kidney
        self.liver= liver

    @abstractmethod
    def show_info(self):
        return

class Skeleton(ABC):
    def __init__(self,skull,ribs,spine,jaw,num_bones):
        self.skull = skull
        self.ribs = ribs
        self.spine = spine
        self.jaw = jaw
        self.num_bones = num_bones

    @abstractmethod
    def show_info(self):
        return


class Human(Legs, Hands, Head, Chest, Belly, Skeleton):
    def __init__(self, **kwargs):
        Legs.__init__(self, kwargs['leg_fingers'], kwargs['leg_nails'], kwargs['feet'], kwargs['knee'], kwargs['heel'], kwargs['skin_color'])
        Hands.__init__(self, kwargs['hand_fingers'], kwargs['hand_nails'], kwargs['palm'], kwargs['wrist'], kwargs['elbow'], kwargs['shoulder'], kwargs['skin_color'])
        Head.__init__(self, kwargs['brain'], kwargs['eyes'], kwargs['hair'], kwargs['mouth'], kwargs['lips'], kwargs['nose'], kwargs['ears'], kwargs['teeth'], kwargs['tongue'])
        Chest.__init__(self, kwargs['heart'], kwargs['lungs'], kwargs['nipples'])
        Belly.__init__(self, kwargs['stomach'], kwargs['kidney'], kwargs['liver'])
        Skeleton.__init__(self, kwargs['skull'], kwargs['ribs'], kwargs['spine'], kwargs['jaw'], kwargs['num_bones'])

    def show_info(self):
        info = []
        info.append(f"🦵 Legs: {self.fingers} fingers, {self.feet} feet, knee: {self.knee}, heel: {self.heel}, skin color: {self.skin_color}")
        info.append(f"👐 Hands: {self.palm} palm(s), wrist: {self.wrist}, elbow: {self.elbow}, shoulder: {self.shoulder}, skin color: {self.skin_color}")
        info.append(f"🧠 Head: brain: {self.brain}, eyes: {self.eyes}, hair: {self.hair}, mouth: {self.mouth}, lips: {self.lips}, nose: {self.nose}, ears: {self.ears}, teeth: {self.teeth}, tongue: {self.tongue}")
        info.append(f"❤️ Chest: heart: {self.heart}, lungs: {self.lounges}, nipples: {self.nipples}")
        info.append(f"🍔 Belly: stomach: {self.stomach}, kidney: {self.kidney}, liver: {self.liver}")
        info.append(f"💀 Skeleton: skull: {self.skull}, ribs: {self.ribs}, spine: {self.spine}, jaw: {self.jaw}, bones: {self.num_bones}")
        return "\n".join(info)

data = {'leg_fingers': 10, 'leg_nails': 10, 'feet': 2, 'knee': 2, 'heel': 2, 'skin_color': 'light',
    'hand_fingers': 10, 'hand_nails': 10, 'palm': 2, 'wrist': 2, 'elbow': 2, 'shoulder': 2,
    'brain': 1, 'eyes': 2, 'hair': 'brown', 'mouth': 1, 'lips': 'red', 'nose': 1, 'ears': 2, 'teeth': 32, 'tongue': 1,
    'heart': 1, 'lungs': 2, 'nipples': 2,
    'stomach': 1, 'kidney': 2, 'liver': 1,
    'skull': 1, 'ribs': 24, 'spine': 1, 'jaw': 1, 'num_bones': 206}

person = Human(**data)
print(person.show_info())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 3 INSTRUMENTS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class Instrument(ABC):
    def __init__(self, size, name, tunable, loudness, material):
        self.size = size
        self.name = name
        self.tunable = tunable
        self.loudness = loudness
        self.material = material

    @abstractmethod
    def play(self):
        return

class StringInstrument(Instrument):
    def __init__(self, num_strings, keys, size, name, tunable, loudness, material):
        super().__init__(size, name, tunable, loudness, material)
        self.num_strings = num_strings
        self.keys = keys

    def show_info(self):
        return (f"{self.name} is a a string instrument\n"
                f"This many strings {self.num_strings} are inside\n"
                f"Number of keys is {self.keys}\n"
                f"Size {self.size}\n"
                f"Tunable {self.tunable}\n"
                f"Level of loudness {self.loudness}\n"
                f"Made of {self.material}")

    def play(self):
        return f"Trinnь"

class WindInstrument(Instrument):
    def __init__(self, name, size, tunable, loudness, material, num_valves, key_type):
        super().__init__(size, name, tunable, loudness, material)
        self.num_valves = num_valves
        self.key_type = key_type

    def show_info(self):
        return (f"{self.name} is a wind instrument.\n"
                f"Number of valves: {self.num_valves}\n"
                f"Key type: {self.key_type}\n"
                f"Size: {self.size}\n"
                f"Tunable: {self.tunable}\n"
                f"Loudness: {self.loudness}\n"
                f"Material: {self.material}")

    def play(self):
        return f"ФЮФ"

class PercussionInstrument(Instrument):
    def __init__(self, name, size, tunable, loudness, material, drum_type, sticks_required):
        super().__init__(size, name, tunable, loudness, material)
        self.drum_type = drum_type
        self.sticks_required = sticks_required

    def show_info(self):
        return (f"{self.name} is a percussion instrument.\n"
                f"Drum type: {self.drum_type}\n"
                f"Sticks required: {self.sticks_required}\n"
                f"Size: {self.size}\n"
                f"Tunable: {self.tunable}\n"
                f"Loudness: {self.loudness}\n"
                f"Material: {self.material}")

    def play(self):
        return f"Boom"

class Sax(WindInstrument):
    def __init__(self, sax_sound, name, size, tunable, loudness, material, num_valves, key_type):
        super().__init__(name, size, tunable, loudness, material, num_valves, key_type)
        self.sax_sound = sax_sound

    def play(self):
        base_play = super().play()
        return f"{base_play}\n🎷 Sax sound: {self.sax_sound}"

class Drum(PercussionInstrument):
    def __init__(self, name, size, tunable, loudness, material, drum_type, sticks_required, drum_sound):
        super().__init__(name, size, tunable, loudness, material, drum_type, sticks_required)
        self.drum_sound = drum_sound

    def play(self):
        base_play = super().play()
        return f"{base_play}\n🥁 Drum sound: {self.drum_sound}"

class GrandPiano(StringInstrument):
    def __init__(self, name, size, tunable, loudness, material, key_num, key_type, piano_sound):
        super().__init__(key_num, key_type, size, name, tunable, loudness, material)
        self.piano_sound = piano_sound

    def play(self):
        base_play = super().play()
        return f"{base_play}\n🎹 Piano sound: {self.piano_sound}"

class HybridInstrument(Sax, GrandPiano):
    def __init__(self, sax_sound, name, size, tunable, loudness, material, num_valves, key_num, key_type, piano_sound, hybrid_sound):
        Sax.__init__(self, sax_sound, name, size, tunable, loudness, material, num_valves, key_type)
        GrandPiano.__init__(self, name, size, tunable, loudness, material, key_num, key_type, piano_sound)
        self.hybrid_sound = hybrid_sound

    def play(self):
        sax_part = Sax.play(self)
        piano_part = GrandPiano.play(self)
        return f"🎶 This hybrid instrument combines Sax and Grand Piano {self.hybrid_sound}\n{sax_part}\n{piano_part}"

hybrid = HybridInstrument(sax_sound="Waaaah",name="SuperSaxoPiano",size="large",tunable=True, loudness="maximum",material="carbon fiber",num_valves=0,key_num=88,key_type="weighted",piano_sound="Tiiinnng", hybrid_sound="🔥 Fusion mode activated")

print(hybrid.play())