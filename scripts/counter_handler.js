const incrementCounter = () => {
  const number = document.getElementById("number").value;

  const xhr = new XMLHttpRequest();
  xhr.open("POST", `/`, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);

        const span = document.getElementById('response_messages');
        span.textContent = response.message;
      } else {
        var response = JSON.parse(xhr.responseText);
        if(response.error) {
          const span = document.getElementById('response_messages');
          span.textContent = response.error;
        } else {
          alert("Um erro inesperado aconteceu");
        }
      }
    }
  };
  xhr.send(`{"number": ${number}}`);
}