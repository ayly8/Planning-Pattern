function display_sug() {
    //get user input and store into variables
    var x = document.getElementById("x").value;
    var y = document.getElementById("y").value;
    var z = document.getElementById("z").value;

    // send POST request to /generate_plan endpoint with the data from input fields
    fetch('/generate_plan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({x: x, y: y, z: z})
    })
    .then(response => response.json())
    .then(data => {
        // updates website with suggested result from chatgpt api
        document.getElementById("suggestion_result").innerText = data.suggestion;
    });
}