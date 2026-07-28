function validateForm(){

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;


    if(name == ""){
        alert("Name is required");
        return false;
    }


    if(email == ""){
        alert("Email is required");
        return false;
    }


    if(phone.length != 10){
        alert("Enter valid phone number");
        return false;
    }


    return true;

}


// Search Employee

function searchEmployee(){

    let input = document.getElementById("search").value.toLowerCase();

    let rows = document.querySelectorAll("#employeeTable tr");


    rows.forEach(row => {

        let text = row.innerText.toLowerCase();

        if(text.includes(input)){
            row.style.display="";
        }
        else{
            row.style.display="none";
        }

    });

}