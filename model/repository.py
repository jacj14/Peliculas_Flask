from model.entity import Movie, Review
from model.db import execute, commit

class MovieRepository:
      
      def insert(movie: Movie) -> None:
            sql = f"""
                  INSERT INTO Movies (code, name, iamge_url, year)
                  VALUES ('{movie.code}', '{movie.name}', '{movie.image_url}', {movie.year});
                  """
            cursor = execute(sql)
            cursor.close()
            commit()
      
      def findByCode(code: str) -> Movie:
            sql = f"""
                  SELECT code, name, email, image_url, year
                  FROM Movies
                  WHERE code = {code};
                  """
            cursor = execute(sql)
            result = cursor.fetchone()
            cursor.close()
            
            return Movie(
                  code = result[0],
                  nombre = result[1],
                  image_url = result[2],
                  year = result[3]
            )
      
      def findAll () -> list:
            sql = """
                  SELECT code, name, email, image_url, year
                  FROM Movies
                  ORDER BY name;
                  """
            cursor = execute(sql)
            result = cursor.fetchall()
            cursor.close()
            
            response = list()
            
            for data in result:
                  response.append(Movie(
                        code = data[0],
                        nombre = data[1],
                        image_url = data[2],
                        year = data[3]
                  ))
            
            return response

class ReviewRepository:
      
      def insert(review: Review) -> None:
            pass
      
      def findById(id: int) -> list:
            pass
      
      def findAll () -> list:
            pass
      
      def update(review: Review) -> None:
            pass
      
      def delete(id: int) -> None:
            pass