const siteURL = "//127.0.0.1:8000";
const styleURL = siteURL + 'static/css/bookmarklet.css'
const minWidth = 250;
const minHeight = 250;

// load css 
let head = document.getElementsByTagName("head")[0];
let link = document.createElement("link");
link.rel = "stylesheet";
link.type = 'text/css';
link.href = styleUrl + "?r" + Math.floor(Math.random() * 9999999999999999);
head.appendChild(link);


// Load HTML
let body = document.getElementsByTagName('body')[0];
boxHTML = <div id="bookmarklet">
    <a herf="#" id="close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="images"></div>
</div>;
body.innerhtml += boxHTML;