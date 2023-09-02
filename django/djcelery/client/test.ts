

console.log("Welcome to Add.");


let headers = new Headers();
headers.append("Accept", "application/json");
headers.append("Content-Type", "application/json");
headers.append('Access-Control-Allow-Origin', '*');
headers.append("Cross-Origin-Resource-Policy", "no-cors")
headers.append('Content-Type', 'application/json')


async function task_status(task_id: string): Promise<any> {
    const response = await  fetch(
        `http://localhost:8000/da/add/?id=${task_id}`,
        {
            method: "GET",
            // body: form,
            mode: "no-cors",
            headers: headers,
        }
    )
    let message =  await response.json()

    return message
}

const get_task_id = async  function(x: number, y: number): Promise<string> {
    const response = await fetch(
        "http://localhost:8000/da/add/?x=100&y=100",
        {
            method: "GET",
            // body: form,
            mode: "no-cors",
            headers: headers,
        }
    )
    const text = await response.text()
    console.log(text)
    const json = JSON.parse(text)
    return json.id
}

const main = async () => {
    // let id: string = await get_task_id(100, 200);    
    // const timeout = setInterval(async () => {
    //     const message = await task_status(id);
    //     console.log(message)
        
    // }, 500)

    let task_id = await get_task_id(100,  200);
    console.log(task_id)

    let status: string|null = null;
    let loop: boolean = true;
    let message: any|null = null;
    while (loop) {
        message = await task_status(task_id);
        console.log(message)
        if (message.result === 200) {
            console.log(message);
            loop = false
        } 
    }

}

main();

