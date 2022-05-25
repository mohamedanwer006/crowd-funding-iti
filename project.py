import json
class Project:

    def __init__(self, owner: str, title: str, target: int, start: str, end: str, details: str):
        self.owner = owner
        self.title = title
        self.target = target
        self.start = start
        self.end = end
        self.details = details

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
    
    def __str__(self):
        return f"{self.title}\t{self.owner}\t{self.target}\t{self.start}\t{self.end}\t{self.details}"



