import re
import matplotlib.pyplot as plt
from email.parser import Parser

# Fonction pour analyser un email et détecter le phishing
def detect_phishing(email_text):
    # Expressions régulières pour détecter des liens suspects
    link_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    suspicious_link_pattern = r"(bit.ly|goo.gl|t.co)"  # Liens raccourcis
    suspicious_domains = ["example.com", "test.com"]  # Domaines suspects
    sender_pattern = r"[\w\.-]+@[\w\.-]+"  # Format d'email

    # Détection des liens
    links = re.findall(link_pattern, email_text)
    suspicious_links = [link for link in links if re.search(suspicious_link_pattern, link)]
    
    # Vérification des expéditeurs
    sender_match = re.findall(sender_pattern, email_text)
    if sender_match:
        sender = sender_match[0]
        suspicious_sender = any(domain in sender for domain in suspicious_domains)
    else:
        suspicious_sender = False

    # Retourner un résultat de détection de phishing
    return len(suspicious_links) > 0 or suspicious_sender

# Exemple d'emails à analyser
emails = [
    {"sender": "john.doe@bit.ly", "content": "Click here to win a prize: http://bit.ly/abcd1234"},
    {"sender": "susan.smith@example.com", "content": "Hello, please verify your account at http://test.com/login"},
    {"sender": "mark.jones@company.com", "content": "Important message from your bank."},
    {"sender": "phishing@unknown.com", "content": "Your account is locked. Click here to reset: http://t.co/reset"}
]

# Liste pour stocker les résultats de détection
detection_results = []

# Analyser chaque email
for email in emails:
    phishing_detected = detect_phishing(email["content"])
    detection_results.append({"email": email, "phishing_detected": phishing_detected})

# Générer un rapport
phishing_count = sum(result["phishing_detected"] for result in detection_results)
total_count = len(detection_results)
phishing_percentage = (phishing_count / total_count) * 100

print(f"Total d'emails analysés : {total_count}")
print(f"Emails suspectés de phishing : {phishing_count}")
print(f"Pourcentage d'emails suspectés de phishing : {phishing_percentage:.2f}%")

# Visualiser les résultats
labels = ['Phishing', 'Non Phishing']
sizes = [phishing_count, total_count - phishing_count]
colors = ['red', 'green']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Statistiques de détection de Phishing')
plt.axis('equal')  # Pour un graphique circulaire
plt.show()
