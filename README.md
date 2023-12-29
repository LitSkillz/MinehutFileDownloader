# MinehutFileDownloader
A python script to download all of the files on your minehut server, regardless of if the server is paid.

**Tutorial**
1. Boot the minehut server. Minehut will not let you do anything at all until you boot the server.
2. Join the server with a minecraft account. The server will automatically close unless there's a player inside, and if the server closes the downloader will begin to download invalid content. This minecraft account should stay in the server during this whole process; be absolutely sure that it does not get kicked for afk.
3. Next, you'll need your auth token, profile id and session id. Simply go to the server page, press f12, and wait until there's a GET request called all_data. Click on that get request, and navigate to the request headers. Save your profile id, session id and authorization to a text document. When copying the authorization token make sure to copy the word "Bearer."
4. To get the server id, go back to the request and copy the random string of characters that's inside of the request url. Save this to the text document to.
5. Now you're ready to go. Run the script and paste in the information from the document when asked. Make sure the minecraft account doesn't leave until the script stops.

If you want to do this again, make sure to get the latest session id. The other information shouldn't change.
