// function darkMode() {
//     let element = document.body;
//     // let title = document.getElementById("title");
//     // let bulk = document.getElementById("bulk");
//     // let button1 = document.getElementById("button1");
//     element.classList.toggle("dark-mode");
//     // title.classList.toggle("dark-mode-h1");
//     // bulk.classList.toggle("dark-mode-h2");
//     // button1.classList.toggle("button1");
// }

function stateCheck() {
    // console.log(`Page loading ${state}!!`)
    let element = document.body;
    // let button = document.getElementsByTagName("button");
    // let title = document.getElementsByTagName("h1");
    let state = localStorage.getItem("state")
    if (state !== 'dark') {
        element.className = "light-mode";
        // title.className = "light-mode";
        // button.className = "light-mode";
        console.log(state)
    } else if (state === "dark") {
        element.className = "dark-mode";
        // title.className = "dark-mode";
        // button.className = "dark-mode";
        console.log(state)
    }
}

function darkMode() {
    let state = localStorage.getItem("state")
    let element = document.body;
    // let button = document.getElementsByTagName("button");
    // let title = document.getElementsByTagName("h1");
    if (state !== 'dark') {
        element.className = "dark-mode";
        // title.className = "dark-mode";
        // button.className = "dark-mode";
        localStorage.setItem("state", "dark")
        console.log(state)
    } else if (state === 'dark') {
        element.className = "light-mode";
        // title.className = "light-mode";
        // button.className = "light-mode";
        localStorage.setItem("state", "light")
        console.log(state)
    }
}