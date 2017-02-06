import webapp2
import cgi
import jinja2
import os
from google.appengine.ext import db

# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape=True)

#def blog_key:
    #return db.Key.from_path('blogs', name)

class BlogPost(db.Model):
    created = db.DateTimeProperty(auto_now_add = True)
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)

    #def render(self):
        #self.render_text = self.content.replace('\n', '<br>')
        #return render_str("post.html", p=self)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render (self, template, **kw):
        self.write(self.render_str(template, **kw))

class Main(Handler):
    """ Handles requests coming in to '/'
        e.g. www.carlysblog.com/
    """
    def render_main(self):
        self.render("frontpage.html")

    def get(self):
        self.render_main()

class Blog(Handler):
    """ Handles requests coming in to '/blog'
        e.g. www.carlysblog.com/blog
    """

    def render_blog(self, posts=""):
        posts = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC LIMIT 5")
        self.render("blog.html", posts=posts)

    def get(self):
        self.render_blog()

class NewPost(Handler):
    """ Handles requests coming in to '/newpost'
        e.g. www.carlysblog.com/newpost
    """
    def render_new_post_page(self, title="", content="", error=""):
        self.render("newpost.html", title=title, content=content, error=error)

    def get(self):
        self.render_new_post_page()

    def post(self):
        title = self.request.get("title")
        content = self.request.get("content")

        if title and content:
            # construct a post object for the new post
            post = BlogPost(title = title, content = content)
            post.put()

            # render the confirmation message
            t = jinja_env.get_template("add-confirmation.html")
            response = t.render(post = post)
            self.response.write(response)
        # if the user typed nothing at all, redirect and yell at them
        else:
            error = "Please add both a title and some content."
            self.render_new_post_page(title, content, error)

class ViewPostHandler(webapp2.RequestHandler):
    def get(self, id):
        post_id = BlogPost.get_by_id(int (id))
        self.response.write(post_id.title + "<br>" + post_id.content)


app = webapp2.WSGIApplication([
    ('/', Main),
    ('/blog', Blog),
    ('/newpost', NewPost),
    webapp2.Route('/blog/<id:\d+>', ViewPostHandler)
], debug=True)
