txt2openlyrics
===========

Version 1.0.0

txt2openlyrics is a tool which you used to convert song lyrics from a text(.txt) file to OpenLyrics XML format.


For more details about openlyrics see:

  http://openlyrics.org


The input text file format required:
* The text file should have the details of the song title, author in comments at the top
* The song lyrics should follow the comments after a new line
* A sample txt file AmazingGrace.txt is placed in the directory


Prerequisites Required:
 * Python > 3.0
 * python library lxml:
      http://pypi.python.org/pypi/lxml

if you have not installed lxml, install using the below command:

  * pip install lxml


To use this conversion tool, follow the steps below:

 * Navigate to the project directory terminal in command prompt and type the below command:

 python main.py
