function values() {
    let btn = document.querySelector("#plot");
    btn.addEventListener("click", () => {
        let x = document.querySelector("#x");
        let y = document.querySelector("#y");
        console.log(x.value, y.value);

        let graph = document.querySelector("#graph-holder");

        fetch("http://localhost:8000/")
            // .then(res => {res.json()})
            .then(data => console.log(data))
        

        // <img id="graph" src="data:image/png;base64, {{ graph }}" alt="">
    })

    
}

values();