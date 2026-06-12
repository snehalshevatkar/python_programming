function validateForm(){
    let title = document.getElementById("title").value.trim();
    let price = document.getElementById("price").value;

    if(title == ""){
        alert("Title required");
        return false;
    }

    if(isNaN(price) || price==""){
        alert("Price must be number");
        return false;
    }

    return true;
}