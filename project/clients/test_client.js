const submitTask = async () => {
    let f = await fetch("http://localhost:9000/maths/submit/", {
        method: "POST",
        body: JSON.stringify({a:1,b:2}),
    })
    console.log(f.status)
    return 
}

submitTask();