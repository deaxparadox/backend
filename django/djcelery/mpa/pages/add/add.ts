
console.log("Welcome to Add.");




let headers = new Headers();
headers.append("Accept", "application/json");
// headers.append("Content-Type", "'application/x-www-form-urlencoded; charset=UTF-8'");
// headers.append('Access-Control-Allow-Origin', '*');
// headers.append('Access-Control-Request-Methods', 'POST, GET');
// headers.append('Access-Control-Request-Headers', 'Content-Type, Accept');
// headers.append("Cross-Origin-Resource-Policy", "cors")
// // headers.append('Content-Type', 'application/json')


// 
//      COMMON ADD VIEW
// 

const commonAddView = {
    task_status: async function task_status(task_id: string): Promise<any> {
        const response = await fetch(
            `http://localhost:8000/da/add/?id=${task_id}`,
            {
                method: "GET",
                mode: "cors",
                headers: headers,
            }
        )
        return await response.json()
    },
    get_task_id: async function get_task_id(x: number, y: number): Promise<string> {
        const response = await fetch(
            "http://localhost:8000/da/add/?x=100&y=100",
            {
                method: "GET",
                mode: "cors",
                headers: headers,
            }
        )

        const text = await response.text()
        const json = JSON.parse(text)
        return json.id
    },
}

async function commonAddViewMain() {
    let addBoxButton = document.querySelector("#add-box-button") as HTMLButtonElement;
    addBoxButton.onclick = async function (e) {
        let a = document.querySelector("#add-box-a") as HTMLInputElement;
        let b = document.querySelector("#add-box-b") as HTMLInputElement;




        let task_id = await commonAddView.get_task_id(100, 200);
        console.log(task_id)

        let status: string | null = null;
        let loop: boolean = true;
        let message: any | null = null;
        while (loop) {
            message = await commonAddView.task_status(task_id);
            console.log(message)
            if (message.result === 200) {
                console.log(message);
                loop = false
            }
        }
    }
}






// 
//      POST ADD VIEW
// 


let form = new FormData();
form.append("x", "100")
form.append("y", "100")


const postAddView = {
    task_status: async function task_status(task_id: string): Promise<any> {
        const response = await fetch(
            `http://localhost:8000/da/post-add/${task_id}/`,
            {
                method: "GET",
                mode: "cors",
                headers: headers,
            }
        )
        return await response.json()
    },
    get_task_id: async function get_task_id(x: number, y: number): Promise<string> {
        const response = await fetch(
            "http://localhost:8000/da/post-add/",
            {
                method: "POST",
                body: form,
                mode: "cors",
                headers: headers,
            }
        )

        const text = await response.text()
        const json = JSON.parse(text)
        return json.id
    },
}

async function postAddViewMain() {
    let addBoxButton = document.querySelector("#add-box-button") as HTMLButtonElement;
    addBoxButton.onclick = async function (e) {
        let a = document.querySelector("#add-box-a") as HTMLInputElement;
        let b = document.querySelector("#add-box-b") as HTMLInputElement;




        let task_id = await postAddView.get_task_id(100, 200);
        console.log(task_id)

        let status: string | null = null;
        let loop: boolean = true;
        let message: any | null = null;
        while (loop) {
            message = await postAddView.task_status(task_id);
            console.log(message)
            if (message.result === 200) {
                console.log(message);
                loop = false
            }
        }
    }
}

postAddViewMain();



