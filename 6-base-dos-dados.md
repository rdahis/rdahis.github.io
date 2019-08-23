---
layout: default
permalink: /base-dos-dados/
---

<html>
<head>
<title>Google Sheets API Quickstart</title>
<meta charset="utf-8" />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<style>
body {
font-family: "Lato", sans-serif;
}

.sidenav {
height: 100%;
width: 0;
position: fixed;
z-index: 1;
top: 0;
left: 0;
background-color: #111;
overflow-x: hidden;
transition: 0.5s;
padding-top: 60px;
}

.sidenav a {
padding: 8px 8px 8px 32px;
text-decoration: none;
font-size: 25px;
color: #818181;
display: block;
transition: 0.3s;
}

.sidenav a:hover {
color: #f1f1f1;
}

.sidenav .closebtn {
position: absolute;
top: 0;
right: 25px;
font-size: 36px;
margin-left: 50px;
}

@media screen and (max-height: 450px) {
.sidenav {padding-top: 15px;}
.sidenav a {font-size: 18px;}
}
</style>
</head>
<body>
<!--<p>Google Sheets API Quickstart</p>-->

<!--Add buttons to initiate auth sequence and sign out-->
<button id="authorize_button" style="display: none;">Authorize</button>
<button id="signout_button" style="display: none;">Sign Out</button>

<pre id="content" style="white-space: pre-wrap;"></pre>

<script type="text/javascript">
// Client ID and API key from the Developer Console
var CLIENT_ID = '1008856217608-dmln7iptbpi1skiijo4aq7phuomu0evr.apps.googleusercontent.com';
var API_KEY = 'AIzaSyBwh2eGEed4OY90fo_wlfI188reHQ54NH4';

// Array of API discovery doc URLs for APIs used by the quickstart
var DISCOVERY_DOCS = ["https://sheets.googleapis.com/$discovery/rest?version=v4"];

// Authorization scopes required by the API; multiple scopes can be
// included, separated by spaces.
var SCOPES = "https://www.googleapis.com/auth/spreadsheets.readonly";

var authorizeButton = document.getElementById('authorize_button');
var signoutButton = document.getElementById('signout_button');

/**
*  On load, called to load the auth2 library and API client library.
*/
function handleClientLoad() {
gapi.load('client:auth2', initClient);
}

/**
*  Initializes the API client library and sets up sign-in state
*  listeners.
*/
function initClient() {
gapi.client.init({
apiKey: API_KEY,
clientId: CLIENT_ID,
discoveryDocs: DISCOVERY_DOCS,
scope: SCOPES
}).then(function () {
// Listen for sign-in state changes.
gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);

// Handle the initial sign-in state.
updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
authorizeButton.onclick = handleAuthClick;
signoutButton.onclick = handleSignoutClick;
}, function(error) {
appendPre(JSON.stringify(error, null, 2));
});
}

/**
*  Called when the signed in status changes, to update the UI
*  appropriately. After a sign-in, the API is called.
*/
function updateSigninStatus(isSignedIn) {
if (isSignedIn) {
authorizeButton.style.display = 'none';
signoutButton.style.display = 'block';
listMajors();
} else {
authorizeButton.style.display = 'block';
signoutButton.style.display = 'none';
}
}

/**
*  Sign in the user upon button click.
*/
function handleAuthClick(event) {
gapi.auth2.getAuthInstance().signIn();
}

/**
*  Sign out the user upon button click.
*/
function handleSignoutClick(event) {
gapi.auth2.getAuthInstance().signOut();
}

/**
* Append a pre element to the body containing the given message
* as its text node. Used to display the results of the API call.
*
* @param {string} message Text to be placed in pre element.
*/
function appendPre(message) {
var pre = document.getElementById('content');
var textContent = document.createTextNode(message + '\n');
pre.appendChild(textContent);
}

var valores = [];

/**
* Print the names and majors of students in a sample spreadsheet:
* https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
*/
function listMajors() {
gapi.client.sheets.spreadsheets.values.get({
spreadsheetId: '1ZRL7s4SQrtFO5T-q2l1jpPupO8DPLu3ZKg0SWMftMXc',
range: 'database',
}).then(function(response) {
for (var i = 1; i < response.result.values.length; i++)
$("#mySidenav").append('<a href="#" onclick="Secoes('+i+');">'+response.result.values[i][0]+'</a>');

valores = response.result.values;
}, function(response) {
appendPre('Error: ' + response.result.error.message);
});
}

function Secoes(i)
{
var secoes = $("#secoes");

secoes.empty();
for (var j = 1; j < valores[0].length; j++)
if (valores[i][j] != "")
{
secoes.append('<h2>'+valores[0][j]+'</h2>');
secoes.append(j != 12 ? '<p>'+valores[i][j]+'</p>' : '<a href='+valores[i][j]+'>'+valores[i][j]+'</a><br/>');
secoes.append('<br/>');
}
}

</script>
<div id="mySidenav" class="sidenav">
<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
</div>

<span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; bases de dados</span>
<div style="text-align:center;" id="secoes"></div>

<script>
function openNav() {
document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
document.getElementById("mySidenav").style.width = "0";
}
</script>
<script async defer src="https://apis.google.com/js/api.js"
onload="this.onload=function(){};handleClientLoad()"
onreadystatechange="if (this.readyState === 'complete') this.onload()">
</script>
</body>
</html>
