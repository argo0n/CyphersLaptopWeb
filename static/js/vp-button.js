const button = document.getElementById("vp-button");
button.style.position = "absolute";
button.addEventListener("touchstart", moveButton);
button.addEventListener("mouseover", moveButton);

var count = 0;
var counter = document.getElementById('minty');

function moveButton(event) {
    event.target.style.top = Math.floor(Math.random() * (window.innerHeight-20)) + "px";
    event.target.style.left = Math.floor(Math.random() * (window.innerWidth-20)) + "px";
    count += 1;
    counter.innerHTML = `You tried getting free VP ${count} times `;
}

