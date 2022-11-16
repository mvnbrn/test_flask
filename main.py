# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, render_template, request
from flask_socketio import SocketIO,emit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
    app.static_folder = 'static'

    socketio = SocketIO(app)


    @app.route('/')
    def home():
        return render_template('home.html')


    @app.route('/imsi/')
    def imsi():
        return render_template('imsi.html')

    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
