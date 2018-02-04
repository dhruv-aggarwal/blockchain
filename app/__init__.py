from flask import Flask


app = Flask(__name__)
app.config.from_object('app.settings')
__import__('app.api.v1.blockchain')


__all__ = ['app']
