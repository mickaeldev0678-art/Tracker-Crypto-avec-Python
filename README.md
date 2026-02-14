# 📈 Crypto Tracker

Un tracker de prix de cryptomonnaies en temps réel utilisant l'API CoinGecko.

## 🚀 Fonctionnalités

- Suivi en temps réel des prix de 6 cryptomonnaies majeures
- Affichage des variations sur 24h avec code couleur (vert = hausse, rouge = baisse)
- Mise à jour automatique toutes les 30 secondes
- Interface console simple et claire

## 📋 Prérequis

- Python 3.6 ou supérieur
- Module `requests`

## 🔧 Installation

1. Clone ce repository :
```bash
git clone https://github.com/mickaeldev0678-art/crypto-tracker.git
cd crypto-tracker
```

2. Installe les dépendances :
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

Lance le script :
```bash
python crypto_tracker.py
```

Le programme affichera les prix en continu. Pour l'arrêter, appuie sur `Ctrl+C`.

## 📊 Cryptomonnaies suivies

- Bitcoin (BTC)
- Ethereum (ETH)
- Solana (SOL)
- Dogecoin (DOGE)
- Monero (XMR)
- Ripple (XRP)

## 🎨 Exemple de sortie

```
--- Live Crypto Tracker (MAJ: 14:32:15) ---
---------------------------------------------
Bitcoin     :  $  96,234.50 (+2.34%)
Ethereum    :  $   3,456.78 (-1.23%)
Solana      :  $     123.45 (+5.67%)
...
---------------------------------------------
Ctrl+C pour arrêter le monitoring.
```

## 🛠️ Personnalisation

Pour modifier les cryptomonnaies suivies, édite la liste `ma_liste` dans le fichier `crypto_tracker.py` :

```python
ma_liste = ["bitcoin", "ethereum", "solana", "dogecoin", "monero", "ripple"]
```

Consulte la [liste des IDs CoinGecko](https://api.coingecko.com/api/v3/coins/list) pour ajouter d'autres cryptos.

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## 🙏 Remerciements

- [CoinGecko API](https://www.coingecko.com/en/api) pour les données de prix
