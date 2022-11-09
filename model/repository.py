from model.entity import Movie, Review
from model.db import execute, commit

class MovieRepository:
      
      def insert(movie: Movie) -> None:
            sql = f"""
                  INSERT INTO Movies (code, name, image_url, year)
                  VALUES ('{movie.code}', '{movie.name}', '{movie.image_url}', {movie.year});
                  """
            cursor = execute(sql)
            cursor.close()
            commit()
      
      def findByCode(code: str) -> Movie:
            sql = f"""
                  SELECT code, name, image_url, year
                  FROM Movies
                  WHERE code = '{code}';
                  """
            cursor = execute(sql)
            result = cursor.fetchone()
            cursor.close()
            
            return Movie(
                  code = result[0],
                  name = result[1],
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
            sql = f"""
                  INSERT INTO Review (name, email, description, raiting, code)
                  VALUES ('{review.name}', '{review.email}', '{review.description}', {review.raiting}, '{review.code}');
                  """
            cursor = execute(sql)
            cursor.close()
            commit()
            
      
      def findById(id: int) -> Review:
            sql = f"""
                  SELECT id, name, email, description, raiting, code
                  FROM Review
                  WHERE id = {id};
                  """
            cursor = execute(sql)
            result = cursor.fetchone()
            cursor.close()
            
            return Review(
                  id = result[0],
                  name = result[1],
                  email = result[2],
                  description = result[3],
                  raiting = result[4],
                  code = result[5]
            )
      
      def findByMovieCode (code: str) -> list:
            sql = f"""
                  SELECT id, name, email, description, raiting, code
                  FROM Review
                  WHERE code = '{code}';
                  """
            cursor = execute(sql)
            result = cursor.fetchall()
            cursor.close()
            
            response = list()
            
            for data in result:
                  response.append(Review(
                        id = data[0],
                        name = data[1],
                        email = data[2],
                        description = data[3],
                        raiting = data[4],
                        code = data[5]
            ))
            
            return response
      
      def update(review: Review) -> None:
            sql = f"""
                  UPDATE Review
                  SET name = '{review.name}',
                      email = '{review.email}',
                      description = '{review.description}',
                      raiting = '{review.raiting}',
                      code = '{review.code}'
                  WHERE id = {review.id};
                  """
            cursor = execute(sql)
            cursor.close()
            commit()
      
      def delete(id: int) -> None:
            sql = f"""
                  DELETE
                  FROM Review
                  WHERE id = {id};
                  """
            cursor = execute(sql)
            cursor.close()
            commit()