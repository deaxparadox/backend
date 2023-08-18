console.log("This is accordion page.")

let active1: boolean = false
let button1 = document.querySelector("#button1") as HTMLButtonElement;
let hide1 = document.querySelector("#hide1") as HTMLUListElement;
button1.addEventListener("click", () => {
    if (!active1) {
        hide1.style.height = "100%";
        active1 = true;
    } else {
        hide1.style.height = "0";
        active1 = false
    }
})

// 


let active2: boolean = false
let button2 = document.querySelector("#button2") as HTMLButtonElement;
let hide2 = document.querySelector("#hide2") as HTMLUListElement;
button2.addEventListener("click", () => {
    if (!active2) {
        hide2.style.height = "100%";
        active2 = true;
    } else {
        hide2.style.height = "0";
        active2 = false
    }
})