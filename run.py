#!/usr/bin/env python3
from app import create_app, db


if __name__=="__maain__":
	app=create_app()
	with app.app_context():
		db.create_all()
		app.run()
