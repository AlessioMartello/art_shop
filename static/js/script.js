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
