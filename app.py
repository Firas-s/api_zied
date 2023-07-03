from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuration de la connexion à la base de données MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="client"
)

# Route pour la vérification de l'utilisateur
@app.route('/check_user', methods=['POST'])
def check_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Exécution de la requête SQL pour vérifier si l'utilisateur existe dans la base de données
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Users WHERE name=%s AND email=%s", (name, email))
    row = cursor.fetchone()

    if row is None:
        return jsonify({'message': 'Utilisateur non trouvé'})
    else:
        return jsonify({'message': 'Utilisateur trouvé'})

if __name__ == '__main__':
    app.run(debug=True)
