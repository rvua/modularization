class Movie: 
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.box_office = data['box_office']
        self.director_id = data['director_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 