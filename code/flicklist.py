import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movies = ["The Big Lebowski", "Only Lovers Left Alive", "Interstellar", "The Wind Rises", "My Neighbor Totoro"]

        # TODO: randomly choose one of the movies, and return it

        randomSelection = random.randrange(len(movies))
        return movies[randomSelection]


        #return "The Big Lebowski"

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        movie2 = self.getRandomMovie()
        movie3 = self.getRandomMovie()
        movie4= self.getRandomMovie ()
        movie5= self.getRandomMovie()



        #movie = self.getRandomMovie()
        #tomorrowMovie = self.getRandomMovie()



        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<ul><li>" + movie + "</li></ul>"





        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tomorrowResponse = "<h1>Tomorrow's Movie </h1>"
        tomorrowMovie = self.getRandomMovie()
        self.response.write(response)
        self.response.write(tomorrowResponse)




        #self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
