function display_sug() {
   var x = document.getElementById("x").value;
    var y = document.getElementById("y").value;
    var z = document.getElementById("z").value;

    fetch('/get_suggestion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'x=' + encodeURIComponent(x) + '&y=' + encodeURIComponent(y) + '&z=' + encodeURIComponent(z)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("suggestion_result").innerText = data.suggestion;
    });
}