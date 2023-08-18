console.log("This is index.ts")


const navbarOtherDisplay = function () {
    let active: boolean = false;
    let button = document.querySelector("#other-topics-button") as HTMLLinkElement;
    let box = document.querySelector("#other-topics") as HTMLUListElement

    button.onclick = () => {
        if (active) {
            box.style.transform = "scale(0, 0)";
            box.style.animationName = "HideOtherTopics"
            box.style.animationDuration = ".3s"
            box.style.width = "0px"
            active = false;

        } else {
            box.style.transform = "scale(1, 1)"
            box.style.animationName = "ShowOtherTopics"
            box.style.animationDuration = ".3s";
            box.style.width = "20%"
            active = true;
        }
    }

    box.onmouseleave = () => {
        box.style.transform = "scale(0, 0)";
        box.style.animationName = "HideOtherTopics"
        box.style.animationDuration = ".3s"
        box.style.width = "0px"
        active = false;
    }
}
navbarOtherDisplay();


const leftBox = function () {
    let active: boolean = false;
    let panel = document.querySelector("#left-box") as HTMLDivElement;
    let open = document.querySelector("#left-box-open") as HTMLButtonElement;
    let close = document.querySelector("#left-box-close") as HTMLButtonElement;

    open.onclick = () => {
        panel.style.width = '100%'
        active = true
    }

    close.onclick = () => {
        panel.style.width = "0%"
        active = false
    }
}
leftBox();