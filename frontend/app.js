async function analyze() {
    const q = document.getElementById('q').value;


    const res = await fetch(`http://localhost:8000/analyze?question=${q}`, {
      method: 'POST'
    });


    const data = await res.json();
    document.getElementById('out').innerText = JSON.stringify(data, null, 2);
}
