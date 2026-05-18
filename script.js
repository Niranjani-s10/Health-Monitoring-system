document.getElementById("registerForm")?.addEventListener("submit", function(e){

    let firstName = document.getElementById("firstName").value;
    let email = document.getElementById("email").value;

    if(firstName === "" || email === ""){
        alert("Please fill all fields");
        e.preventDefault();
    }

});
document.getElementById('registerForm').addEventListener('submit', async(e)=>{

    e.preventDefault();

    const data = {
        firstName: document.getElementById('firstName').value,
        email: document.getElementById('email').value
    };

    const response = await fetch('http://127.0.0.1:5000/register', {

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body: JSON.stringify(data)

    });

    const result = await response.json();

    alert(result.message);

});