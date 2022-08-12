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

var txt = document.getElementById('creative-text');

function changeColour(){
const max = 255;
let a = Math.floor(Math.random() * max);
let b = Math.floor(Math.random() * max);
let c = Math.floor(Math.random() * max);
txt.style.color = `rgb(${a},${b},${c})`;
};

setInterval(changeColour, 1000);