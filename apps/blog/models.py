from django.db.models import * 
from django.contrib.auth.models import User

# Create your models here.

class Tag(Model):
	name = CharField(max_length=100)
	def __unicode__(self):
		return self.name
class Post(Model):
	postedOn = DateTimeField(auto_now_add=True)
	title = CharField(max_length=100)
	gist = TextField()
	tags = ManyToManyField(Tag, blank=True, related_name='tag')
	image = CharField(max_length=100)
	backgroundImage = CharField(max_length=100, blank=True)
	gallery = CharField(max_length=100, blank=True)
	userUpVotes = ManyToManyField(User, blank=True, related_name="postLikes")
	url = CharField(max_length=100, unique=True)
	def __unicode__(self):
		return self.title
	def get_tags(self):
		return ", ".join([e.name for e in self.tags.all()])
class Paragraph(Model):
	post = ForeignKey(Post)
	text = TextField(blank=True)
	image = CharField(max_length=100, blank=True)
	Code = TextField(blank=True)
class Comment(Model):
	post = ForeignKey(Post)
	comment = TextField()
	time = DateTimeField(auto_now_add=True, null=True)
	userUpVotes = ManyToManyField(User, blank=True, related_name='commentLikes')
	def __unicode__(self):
		return comment
class Reply(Model):
	comment = ForeignKey(Comment)
	reply = TextField()
	time = DateTimeField(auto_now_add=True, null=True)
	userUpVotes = ManyToManyField(User, blank=True, related_name='replyLikes')
	def __unicode__(self):
		return self.reply