
function showAlert(){
    alert (Hola);
}
function validateForm(){
    let password = document.getElementById("password").value;
    console.log(password);
    if (!ifThereNumber(password)){
        alert("La Contraseña no tiene el formato  establecido")
        return false;
    }

    return true;

    
}

function containsNumber(data){
    var hasNumber = /\d/;
    return hasNumber.test(data);
}

function ifThereNumber(data){
    let numbers = [0,1,2,3,4,5,6,7,8,9];
    findNumber = false;
    for(let i=0; i<numbers.length; i++){
        for( j=0; j<data.length; j++){
            if (data[j] == numbers[i]){
                findNumber = true;
                break;
            }
        }
        if (findNumber){
            break;
        }
    }
    return findNumber;
}


