
# Project: 0x11. Python - Network #1
**Concepts**  
- **Python**, **Scripting**, **Back-end**, **API**  

**Resources**  
- [HOWTO Fetch Internet Resources Using urllib Package](https://intranet.alxswe.com/rltoken/KoRrs5dVWsb-B82e-M1TQQ)
- [Quickstart with Requests package](https://intranet.alxswe.com/rltoken/OGcRGPr7TSWtzypDd0ZibQ)
- [Requests package](https://intranet.alxswe.com/rltoken/dUNaNQrV2bMSstILitQbXQ)
## Tasks
- 0-hbtn_status.py - a Python script that fetches https://alx-intranet.hbtn.io/status
- 1-hbtn_header.py - a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
- 2-post_email.py - a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
- 3-error_code.py - a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
- 4-hbtn_status.py - a Python script that fetches https://alx-intranet.hbtn.io/status
- 5-hbtn_header.py - a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
- 6-post_email.py - a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response
- 7-error_code.py - a Python script that takes in a URL, sends a request to the URL and displays the body of the response  
	- If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code  
	- You must use the packages requests and sys  
	- You are not allowed to import packages other than requests and sys  
	- You don’t need to check arguments passed to the script (number or type)
- 8-json_api.py - a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
- 10-my_github.py -  a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
