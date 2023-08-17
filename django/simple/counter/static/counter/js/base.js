console.log("This is the counter base script.")

const worker1 = new Worker("/static/counter/js/worker.js");

worker1.postMessage("This is to worker.")

const counter = function() {
    let display = document.getElementById("display");
    let increase = document.getElementById("increase");
    let decrease = document.getElementById("decrease");

    increase.onclick = async function() {
        display.innerText = Number(display.innerText) + 1;
        
    }

    

    decrease.onclick = async function() {
        display.innerText = Number(display.innerText) - 1;
    }
}
counter();