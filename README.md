<center><a href="http://www.youtube.com/watch?feature=player_embedded&v=wozGawDTALM
" target="_blank"><img src="http://img.youtube.com/vi/wozGawDTALM/0.jpg" 
alt="Problem loading image" width="560" height="315" border="10" /></a>
<p>Click the above image to see a YouTube demo.</p></center>

What is this?
-----------
  This is a relatively simple project to exhibit the extent of my experience 
  with data processing and visualisation.


Installation
------------
  Perform a simple "git clone" request from the URL
  https://github.com/gianlucatruda/titanic.git
  and all the relevant files will be downloaded.

  Please also ensure the Python 3.4 is installed,
  along with the following libraries:

  * Matplotlib
  * Requests
  * Flask

  If they aren't installed, you can install them through 'pip3'
  by opening your terminal and typing
    ```sudo pip3 install {name of library}```
  to install. 

  If 'pip3' is not installed, install it by typing
    ```sudo apt-get install python3-pip```

Usage Instructions
-----------------------------

  In terminal, navigate to the project directory.
  This directory should contain 'titanic.py'.

  Type
    ```python3 titanic.py```
  to run the script.

  Once it responds, a Flask server has been established
  on your local machine.

  Navigate to http://localhost:8080/
  to begin engaging with the software.

  When you are finished, press CTRL+C in terminal
  to quit the script.

    NOTE: If you are viewing the pages multiple times, it
    might be necessary to do a 'hard refresh' to ensure
    that the new data is loaded into the browser
    instead of cached data. 


How does it work?
-----------
  It consists of a single Python 3.4 script, which is responsible for
  the vast majority of the functionality. This is complemented with
  html files (and associated assets, scripts, etc.) to enhance the
  aesthetic experience.

  The script works in 3 stages:

  	1. Starts a Flask server on http://localhost:8080
  		and serves up a landing page with more info.

  	2. Waits for the user to request the data set,
  		at which point the Requests library is 
  		used to pull the JSON data from 
  		https://titanic.businessoptics.biz/survival .
  		A predefined class 'Passenger' is
  		instantiated for each parameter set (processed from
  		the JSON data).

  	3. Once the data has successfully been downloaded and
  		processed, Matplotlib is utilised to generate detailed 
  		graphics to illustrate the embarked/surviving data
  		across Sex, Age, and (cabin) Class. 
  		These graphics are rendered as .png files and 
  		then served up through Flask to the browser.

  Contacts
  --------

  o Gianluca Truda — trdgia001@myuct.ac.za


