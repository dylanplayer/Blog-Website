
from flask import render_template, redirect, request
from datetime import date
from app import app
from replit import db


def getPosts(tempNumberOfPosts):
	temp_posts = []
	for x in range(1,tempNumberOfPosts+1):
		temp_posts.append([db["post#"+str(x)+"title"], db["post#"+str(x)+"author"], db["post#"+str(x)+"content"], db["post#"+str(x)+"date"]])
	return temp_posts


def addNewPost(tempNumberOfPosts, title, author, content, postDate):
	db["post#"+str(tempNumberOfPosts)+"title"] = title
	db["post#"+str(tempNumberOfPosts)+"author"] = author
	db["post#"+str(tempNumberOfPosts)+"content"] = content
	db["post#"+str(tempNumberOfPosts)+"date"] = postDate


@app.route('/')
def index():
	return render_template("index.html", posts = getPosts(int(db["numberOfPosts"])))

@app.route('/new')
def new():
	return render_template("new.html")


@app.route('/create',methods = ['POST'])
def create():
	title = request.form['title']
	author = request.form['author']
	content = request.form['content']
	db["numberOfPosts"] = int(db["numberOfPosts"]) + 1
	addNewPost(int(db["numberOfPosts"]),title, author, content, date.today().strftime("%d/%m/%Y"))
	return redirect("/")


