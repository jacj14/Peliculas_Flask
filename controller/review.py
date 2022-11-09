from application import app
from model.repository import ReviewRepository
from model.entity import Review

repository = ReviewRepository()

@app.route("/api/review", methods = ['POST'])
def create_review():
    return repository.insert()

@app.route("/api/review/<id>", methods = ['GET'])
def listReviewId():
    return repository.findById()

@app.route("/api/review/<code>", methods = ['GET'])
def listReviewCode():
    return repository.findByMovieCode()

@app.route("/api/review/<id>", methods = ['PUT'])
def updateReview():
    repository.update()
    
@app.route("/api/review/<id>", methods = ['DELETE'])
def deleteReview():
    repository.delete()
    