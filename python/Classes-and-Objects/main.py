class Student():
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self. track = tracks
        self. score = float(score)
    
    def change_name(self, new_name):
        self.change_name = new_name
        print ("The new name is now ", new_name, "..")

    def change_age(self, new_age):
        self.change_age = new_age
        print ("The new age is now ", new_age, "..")

    def add_track(self, new_track):
        self.change_name = new_track
        print ("The new track is now ", new_track, "..")

    def get_score(self):
        self.get_score = self.score
        print ("And the score is ", self.score,"..")


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
