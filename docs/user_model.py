class User:
    def __init__(self, user_id, name, skills):
        self.user_id = user_id
        self.name = name
        self.skills = skills

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)
