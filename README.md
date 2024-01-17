<h1 aling=center>TheHive Remastred</h1>

<div align="center"  >

<img src="./iconfiles/logo.png" style="border-radius:50%" height="auto" width="auto"/>
</div>

<p>Advanced professional osint toolkit with TheHive Remastred</p><br>




- TheHive Remastred:
    - Advanced and easy graphical interface
    - Local authentication to prevent files from being scrambled
    - Open soruce & Free
    - Extensive features
        - Face recognition ( coming soon )
        - Face detection (Now Active)
        - Face verification ( Now Active )
        - Voice verification ( Now Active)
        - Clone voice detections ( coming soon )
        - Iban parser ( Now Active)
        - Video frame extractor ( Now Active)
        - Phone number parser ( Now Active )
        - Google dork generator ( coming soon )
        - Hash identify ( coming soon )
        - External module support ( coming soon )

        - Region based tools
            - Tc Verificator ( math algorithm ) ( Now Active ) 
            - Tc Calculator ( math algorithm ) ( Now Active )


<br>

<h1> Installation and Startup </h1>
<br>

## Direct Installing ( No python venv )

<br>

```shell
# Clone the repo
git clone https://github.com/MehmetYukselSekeroglu/TheHive.git

# Join TheHive directory
cd TheHive

# Install requirements
python -m pip install -r requirements.txt

# Start Application 
python main.py

```

<br>

## Installing with python venv

<br>


```shell
# Clone the repo
git clone https://github.com/MehmetYukselSekeroglu/TheHive.git

# Join TheHive directory
cd TheHive

# Generate new virtaul env
python -m venv .venv

# Activate venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # Linux and MacOS

# Install requirements for venv
python -m pip install -r requirements.txt

# Start Application 
python main.py

# To exit the virtual environment ( All Platforms )
deactivate

```




<br>
<h1>Images from the interface</h1>

<br>

## Welcome Screen

<br>

<img src="./img/welcomeScreen.png">
<br>
<p>A simple welcome screen welcomes you. At the top, there is the latest status of the system and TheHive, and at the bottom, there is brief information about the vehicle and producer contact information. In general, most operations are performed through the menu bar.</p>

<br>


## Voice Verification

<br>

<img src="./img/voiceVerification.png">

<br>

<p>Thanks to Resemblyzer-based voice verification, you can understand whether 2 voice samples belong to the same person or to others. Thanks to Resemblyzer, the parts of the voice for analysis are detected and the similarity ratio is calculated using cosine similarity. Generally, rates of 75% and above belong to the same person, but do not forget that the model may be wrong.</p>
<br>

## Face Verification

<br>

### Result given by faces belonging to the same person
<img src="./img/FaceVerification.png">


### The results on different people's faces
<img src="./img/FaceVerificationFarkliKisiler.png" />
<br>

<p>There is a high rate of difference between the detection of different and the same people. InsightFace's buffalo_l model is used to detect facial points, then the cosine similarity formula is used via numpy to calculate the similarity, which is why it does not give 100% in different pictures of the same people.
<br>

## Face Detection

<br>


<img src="./img/FaceDetection.png">

<p>All analysis results are printed in the other tab to get full details about the insightFace based face detection system detections for the detection system and trials before the face verification system</p>

<br>


## Video Frame Extractor

<br>
<img src="./img/video2frame.png">

<br>
<p>In order to examine the videos more easily and in detail, the opencv-based video frame parsing feature separates the videos into frames, giving the entire status to the screen without the application freezing, thanks to its multi-threading feature</p>
<br>


## Iban Parser

<br>
<img src="./img/ibanParserGUI.png">
<br>
<p>IBAN, which is frequently used in payment transactions, contains certain information. You can access certain open source information by analyzing them. This module does this automatically. Currently, there is full support only for IBANs belonging to Turkey. It is possible that it may provide incomplete information for other IBANs.</p>
<br>


## Sound Converter 

<br>

<img src="./img/soundConverter.png">

<br>
<p>Although it is not necessary in this tool, I wanted to add the audio converter that I wrote during the learning phase :)</p>

<br>


# Credit[s]

<p>
Logo Designer <a hred="https://github.com/omersayak">Ömer Şayak</a>

</p>