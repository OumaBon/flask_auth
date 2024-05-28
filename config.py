class Development:
	DEBUG=True
	SECRET_KEY="top_secret"
	SQLALCHEMY_DATABASE_URI = "sqlite:///development.sqlite"
	SQLALCHEMY_TRACK_MODIFICATIONS = True


