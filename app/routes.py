from app import app
from flask import render_template
artists = [
    {'name': 'Lauryn Hill',
    'img' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8BkZXMCvK4krctzMNKOevheGP6wTCCbZ3Kw&usqp=CAU',
    'Genre': 'Hip hop, neo soul'},
        
    {'name': 'Barrington Levy', 
    'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8bNIZ4WQ7KTA2RKuOs6_nuhdSaZAGdK-bNg&usqp=CAU',
    'Genre': 'Reggae'},
    
    {'name': 'Carlos Vives',
    'img' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYeH9dSMHq6cHzrYvvf5ZpMpH_FM_Siz6EJg&usqp=CAU',
    'Genre' : 'Vallenato, tropical latin'},
        
    {'name': 'Beres Hammond',
    'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJOCONJNobU-Zuf5fCdO-t43X4Vi_p6sga8w&usqp=CAU',
    'Genre' : 'Reggae'},

    {'name': 'Fall Out Boy',
    'img' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYcEYySW42QSjKYc3kASWFViLASzQ0JP7Eew&usqp=CAU',
    'Genre' : 'Pop rock, alternative rock'}]
        
@app.route('/')
def index():
    return render_template('index.html', names=artists)


@app.route('/contact')
def contact():
    return render_template('contact.html', names=artists)