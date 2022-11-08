class Movie:
      def __init__(self, code, name, image_url = None, year = None):
            self.code = code
            self.name = name
            self.image_url = image_url
            self.year = year
            
class Review:
      def __init__(self, name, email, description, raiting, movie_code, id = None):
            self.name = name
            self.email = email
            self.description = description
            self.raiting = raiting
            self.code = movie_code