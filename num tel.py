# Liste améliorée des préfixes pour les opérateurs français
prefixes = {
    'Orange': ['06', '07'],  # Orange utilise les préfixes 06 et 07 pour les mobiles
    'SFR': ['06', '07'],
    'Bouygues Telecom': ['06', '07'],
    'Free Mobile': ['06', '07'],
    'La Poste Mobile': ['06', '07'],
    'NRJ Mobile': ['06', '07'],
    # Vous pouvez ajouter plus de préfixes ici
}

def get_operator(phone_number):
    # Nettoyer le numéro de téléphone en supprimant les espaces et tirets
    phone_number = phone_number.replace(" ", "").replace("-", "")
    
    # Vérifier si le numéro commence par un des préfixes
    for operator, prefix_list in prefixes.items():
        for prefix in prefix_list:
            if phone_number.startswith(prefix):
                return operator
    return "Opérateur inconnu"

# Demander à l'utilisateur d'entrer un numéro de téléphone
phone_number = input("Entrez un numéro de téléphone : ")

# Appeler la fonction pour déterminer l'opérateur
operator = get_operator(phone_number)

# Afficher l'opérateur trouvé
print(f"L'opérateur pour le numéro {phone_number} est : {operator}")

# Ajouter une pause pour que le programme n'éteigne pas la fenêtre immédiatement
input("Appuyez sur Entrée pour quitter...")
