"""
Crypto Price Tracker
Suit en temps réel les prix des cryptomonnaies via l'API CoinGecko
"""

import requests
import time
import os


def get_crypto_prices():
    """Récupère et affiche les prix des cryptomonnaies"""
    ma_liste = ["bitcoin", "ethereum", "solana", "dogecoin", "monero", "ripple"]
    cryptos = ",".join(ma_liste)
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': cryptos,
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }
    
    try:
        # Nettoie la console (cls pour Windows, clear pour Mac/Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lève une exception si erreur HTTP
        data = response.json()
        
        print(f"--- Live Crypto Tracker (MAJ: {time.strftime('%H:%M:%S')}) ---")
        print("-" * 45)
        
        for coin, info in data.items():
            price = info['usd']
            change = info.get('usd_24h_change', 0)
            color = "\033[92m" if change > 0 else "\033[91m"
            reset = "\033[0m"
            print(f"{coin.capitalize():<12}: ${price:>12,.2f} ({color}{change:+.2f}%{reset})")
        
        print("-" * 45)
        print("Ctrl+C pour arrêter le monitoring.")
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
    except Exception as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    try:
        while True:
            get_crypto_prices()
            time.sleep(30)  # Attend 30 secondes
    except KeyboardInterrupt:
        print("\n\nArrêt du programme...")
        print("Merci d'avoir utilisé Crypto Tracker!")
