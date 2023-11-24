# MinehutFileDownloader
A python script to download all of the files on your minehut server, regardless of if the server is paid.

**Tutorial**
* Step 1: boot the minehut server. Minehut will not let you do anything at all until you boot the server.
* Step 2: Join the server with a minecraft account. The server will automatically close unless there's a player inside, and if the server closes the downloader will begin to download invalid content.
* Step 3: To find the auth token, you'll need to go to open your developer console on the minehut configure server page. Then, click on the Network tab and wait for a request to happen. Once a request happens, click on it, go to the headers tab, and copy the value of the header called 'Authorization.' When the script asks for auth token, right click and paste that into the console. Include the word Bearer.
* Step 4: To get the server id, go back to the request and copy the random string of characters that's inside of the request url. Right click and paste that into the console when asked.\n
