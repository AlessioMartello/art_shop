function display(){
    let x = document.getElementById("Div1");
    let y = document.getElementById("Div2");
    let z = document.getElementById("DonateMonthly");
    let a = document.getElementById("DonateOnce");
    if (x.style.display === "block" && a.style.display == "block") {
        x.style.display = "none";
        a.style.display = "none";
        y.style.display = "block";
        z.style.display = "block";

    }
    else {x.style.display = "block";
            a.style.display = "block";
        y.style.display="none";
        z.style.display="none";
}
}

var app = document.getElementById('app');
var typewriter = new Typewriter(app, {
  loop: false,
  delay: 100,
});

typewriter
  .pauseFor(500)
  .typeString('Artlessi')
  .start();


function changeColour(){
var txt = document.getElementById('creative-text');
const max = 255;
let a = Math.floor(Math.random() * max);
let b = Math.floor(Math.random() * max);
let c = Math.floor(Math.random() * max);
txt.style.color = `rgb(${a},${b},${c})`;
};
if ( window.location.pathname === '/' ){
    //code for index page
setInterval(changeColour, 1000);
}

function openPopUp (link, title, medium) {
switch (medium)
{
case 'fb': window.open(`https://www.facebook.com/sharer/sharer.php?u=https://artlessi.co.uk/blogs/${link}/`, 'windownam' , 'width=950,height=650,scrollbars=yes'); return false;
case 'pinterest': window.open(`http://pinterest.com/pin/create/button/?url=https://www.artlessi.co.uk/blogs/${link}/&description=${title}`, 'windownam' , 'width=950,height=650,scrollbars=yes'); return false;
case 'twitter': window.open(`https://twitter.com/share?text=${title}&url=https://www.artlessi.co.uk/blogs/${link}/&hashtags=Artlessi,blog`, 'windownam' , 'width=950,height=650,scrollbars=yes'); return false;
case 'linkedin': window.open(`https://linkedin.com/shareArticle?url=https://www.artlessi.co.uk/blogs/${link}/&title=${title}&source=https://www.artlessi.co.uk/`, 'windownam' , 'width=950,height=650,scrollbars=yes'); return false;
case 'whatsappweb': window.open(`https://api.whatsapp.com/send?text=Check out this blog by Artlessi: https://artlessi.co.uk/blogs/${link}/`, 'windownam' , 'width=950,height=650,scrollbars=yes'); return false;
case 'whatsappmobile': window.open(`whatsapp://send?text=Check out this blog by Artlessi: https://artlessi.co.uk/blogs/${link}/`, 'windownam' , 'width=950,height=650,scrollbars=yes'); return false;
case 'reddit': window.open(`https://www.reddit.com/submit?url=https://www.artlessi.co.uk/blogs/${link}/&title=${title} by Artlessi`, 'windownam' , 'width=950,height=650,scrollbars=yes'); return false;
}}

var xhttp = new XMLHttpRequest();
