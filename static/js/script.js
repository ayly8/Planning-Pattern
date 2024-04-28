function display_sug() {
    var x = document.getElementById("x").value;
    var y = document.getElementById("y").value;
    var z = document.getElementById("z").value;

    fetch('/generate_plan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({x: x, y: y, z: z})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("suggestion_result").innerText = data.suggested_plan;
    });
    // document.getElementById("suggestion_result").innerText = "test"
}

