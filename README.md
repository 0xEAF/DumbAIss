# DumbAIss
Interface pour une fausse IA (de @PolluuxX), codée en 1h30 par moi - challenge de @NatCode171 !

## Démarrage

> Pour l'éxécuter afin de la tester, il est recommandé de télécharger une version "release".
> A noter qu'elles ne sont disponibles uniquement pour Linux x64 et Windows x64.
> Lien: https://github.com/0xEAF/DumbAIss/releases

1. Pour éxécuter la version **sans interface** (faite par @PolluuxX) graphique/version terminal: `python3 dumbaiss.py`, ou `py dumbaiss.py` sur Windows
2. Pour éxécuter la version **avec interface** (faite par moi) graphique/version terminal: `python3 app.py`, ou `py app.py` sur Windows

## Développement

L'application a été développée en HTML/CSS/JavaScript pour l'interface, et un serveur Python pour recevoir les requêtes et utiliser "l'IA".
Le serveur web est une application [WSGI](https://fr.wikipedia.org/wiki/Web_Server_Gateway_Interface) 
composée en [Flask](https://fr.wikipedia.org/wiki/Flask_(framework)), et éxécutée via [Bottle](https://fr.wikipedia.org/wiki/Bottle_(framework)).

L'interface est ensuite montrée à l'utilisateur avec [PyWebView](https://pywebview.flowrl.com/), 
un équivalent Python à [ElectronJS](https://fr.wikipedia.org/wiki/Electron_(framework)), qui est paramétré pour utiliser
par défaut les modules bas-niveau [Qt](https://fr.wikipedia.org/wiki/Qt) via [PySide6](https://wiki.qt.io/Qt_for_Python),
mais d'autres peuvent être utilisées, voir [cette page](https://pywebview.flowrl.com/guide/installation.html) 
et [celle-ci](https://pywebview.flowrl.com/guide/web_engine.html) pour plus d'informations.
