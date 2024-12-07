const incrementCounter = () => {
  const number = document.getElementById("number").value;

  const xhr = new XMLHttpRequest();
  xhr.open("POST", `/`, true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        console.log("200");
      } else {
        console.log("Unexpected");
      }
    }
  };
  xhr.send(`number=${number}}`);
}