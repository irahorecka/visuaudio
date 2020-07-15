# visuaudio
### A fun GUI application to visualize audio spectrum

```visuaudio.py``` uses the ```pyqtgraph``` and ```pyaudio``` libraries to view the audio spectrum of input sound.
<hr>

<b>Running the application:</b>
1) Clone repository
2) ```$ pip install -r requirements.txt```<br>
3) ```$ python visuaudio.py```
<br>

## Type of Graph

### Bar Graph
<p align="center">
<img src=https://i.imgur.com/pIpCaUQ.png alt="Audio Spectrum GUI"
    width=800>
</p>

### Scatter Graph
<p align="center">
<img src=https://github.com/20-1-SKKU-OSS/2020-1-OSS-10/blob/master/img/scatter.png?raw=true"
    width=800>
</p>
                                                                                             
### Curve Graph
<p align="center">
<img src=https://github.com/20-1-SKKU-OSS/2020-1-OSS-10/blob/master/img/curve.png?raw=true"
    width=800>
</p>                                                                                           
                                                                                           
### Line Graph
<p align="center">
<img src=https://github.com/20-1-SKKU-OSS/2020-1-OSS-10/blob/master/img/LineGraph.PNG?raw=true"
    width=800>
</p>
<b>       
<br>
                                                                                               
## Color Change

#### You can change color of graph in running.
* ↑,→,←: R,G,B += 10
* F1 ~ F9: White ~ Pink
<br>

## Notes:

* Ensure you have a working input sound source.(ex. Mic)
* Run the application on your native terminal (i.e. not iTerm2, etc.)
* You should run on Python version > 3 
                                                                                          
<b>MacOS</b>

* You will have to grant Terminal permission to use the input sound source.
             
<b>Windows</b>

* Go link: <a href=https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio>Click here!</a>
* You should download:

        PyAudio-0.2.11-cp{your python version}-cp{your python version}m-win_amd64.whl

* Installation:

        $ pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
        
<b>Ubuntu Linux</b>

* Currently unknown.
                                                                                           
