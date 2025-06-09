def generate_scorecard(product):
    return {
        'name': product['name'],
        'price': product['price'],
        'scores': {
            'satisfaction': {'score': 88, 'comment': 'Yüksek kullanıcı memnuniyeti'},
            'flaw': {'score': 12, 'comment': 'Minimum risk'},
            'aura': {'score': 85, 'comment': 'Şık ve kaliteli görünüm'},
            'expert': {'score': 90, 'comment': 'Bağımsız testlerde yüksek puan'}
        }
    }