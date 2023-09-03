

console.log("Welcome to Add.");


let headers_api = new Headers();
headers_api.append("Accept", "application/json");
// headers.append("Content-Type", "application/json");
// headers.append('Access-Control-Allow-Origin', '*');
// headers.append("Cross-Origin-Resource-Policy", "no-cors")
// headers.append('Content-Type', 'application/json')


const post_request = async function (): Promise<string> {
    const f = await fetch(
        "http://localhost:8000/da/add/api/",
        {
            body: JSON.stringify(
                {
                    x: 100, 
                    y: 100,
                }
            ),
            method: "POST",
            mode: "cors",
            headers: headers_api,
        }
    )

    const json = await f.json();
    console.log(json)
    return json.id
}

const get_task_status = async function(): Promise<void> {
    const id = await post_request();

    const f = await fetch(
        `http://localhost:8000/da/add/api/?id=${id}`,
        {
            method: "GET",
            mode: "cors",
            headers: headers_api,
        }
    )

    const json = await f.json();
    console.log(json)
}

get_task_status()