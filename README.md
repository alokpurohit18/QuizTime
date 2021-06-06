# KBC - The Game
A graphical quiz game for the Windows platform based on the famous reality show.


![](Images%20and%20Icons/kbc.png)


How to install and play the game - 

1.Install MySQL (database software) using the procedure as described in link - https://www.youtube.com/watch?v=GIRcpjg-3Eg .

2.While insatlling MySQL, set the password for your user 'root' as 'Alok1823!'.

3.Now open MySQL Workbench from the start menu and click on the plus sign to create a new connection. Enter the following details for the   new connection and click OK to create the connection - 

![](Images%20and%20Icons/connection.png)

4.Close Workbench now that the new connection is created.

5.Now go ahead and download this application repository as a zip folder.

6.Unzip to get the main application folder. 

7.Open Workbench again and double click the new connection to open it. Now from the menu bar on top selct 'Server'. From the dropdown select 'Data Import'.

8.Now select the option 'Import from self-contained file' and in click on the button to the extreme right to browse to the location of the unzipped application folder. Open this folder and then open the 'Database Design' folder. Select the file Database.sql and click OK. You can verify that the path selected in the text field is correct the path to the sql file.

![](Images%20and%20Icons/import.jpg)

9.Now click 'start import' at the bottom right of the screen. Once the import is complete, close Workbench.

10.Navigate to the application folder and open the 'GUI' folder in that. Now double click on the .exe file/appication to launch the game. Enjoy!!! 
