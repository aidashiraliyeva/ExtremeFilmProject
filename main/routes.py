from app import app
from app.models import *
from app import db
from flask import Flask, render_template, redirect,request,url_for
import os






@app.route('/')
def index():
    return "salam kele"

