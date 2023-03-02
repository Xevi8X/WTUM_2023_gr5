# WTUM_2023_gr5

## Wstępny pomysł:

Celem projektu jest opracowanie aplikacji do wykrywania twarzy na zdjęciach i określanie emocji rozpoznanych osób.
Projekt zakłada rozwiązanie dwóch podproblemów tj. wykrycia twarzy na zdjęciach i późniejszą klasyfikację emocji odczytanych z wyekstrahowanych zdjęć.

### Planowane modele:
#### Wykrywanie twarzy:
Wykorzystanie kaskadowego klasyfikatora Haara. Wykorzystanie biblioteki OpenCV
Przydatne linki:
https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html
https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

#### Wykrywanie emocji:
Sklasyfikowanie wyodrębnionych obrazów twarzy jako jedną z podstawowych emocji (zależnie od użytego data-setu może to być np. Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral). Do realizacji wykorzystany zostanie model konwolucyjnej sieci neuronowej

### Datasety:
#### Wykrywanie twarzy:
https://www.kaggle.com/datasets/dataturks/face-detection-in-images

#### Emocje:
https://www.kaggle.com/datasets/msambare/fer2013

### Inne pomysły
<ul>
  <li>Klasyfikator: szachy, zwierzęta, symbole, NLP (?)</li>
  <li>GAN - generator obrazów i binarny klasyfikator (Picasso, Monet)</li>
  <li>Text-To-Image</li>
  <li>Układ sterowania AI</li>
</ul>
