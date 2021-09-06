# visuaudio
### A fun GUI application to visualize audio spectrum

```visuaudio.py``` uses the ```pyqtgraph``` and ```pyaudio``` libraries to view the audio spectrum of input sound.

## Running the application:
1) Clone repository
2) ```$ pip install -r requirements.txt```<br>
3) ```$ python visuaudio.py```
<br>

## Visuaudio default bar graph display
<p align="center">
<img src=https://i.imgur.com/pIpCaUQ.png alt="Audio Spectrum GUI"
    width=800>
</p>
                                                                                               
## Color Change

#### You can change color of graph by playing with the following commands:
* ↑,→,←: R,G,B += 10
* F1 ~ F9: White ~ Pink
<br>

## Notes:

* Ensure you have a working input sound source (e.g. a working input mic).
* Run the application on your native terminal (i.e. not iTerm2, etc.).
* Python 2 is not supported. It is advised to run this application using Python>=3.6.
                                                                                          
<b>MacOS</b>

* You will have to grant Terminal permission to use the input sound source.
             
<b>Windows</b>

* Go link: <a href=https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio>Click here!</a>
* You should download:

        PyAudio-0.2.11-cp{your python version}-cp{your python version}m-win_amd64.whl

* Installation:

        $ pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
        
<b>Ubuntu Linux</b>

* Currently unknown. It is likely possible to execute the app in Linux, but it is yet untested.
                                                                                           
