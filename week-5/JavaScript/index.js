let age = 0
let msg = ""
console.log("Javascript console testing")
document.getElementById("confirm button").click = check_age;{
    age = document.getElementById("age").innerText.valueOf()
    if(age <= 18) {
        msg = "Access Denied"
        //Access Denied
        document.getElementById("get_in").innerHTML = msg
    } else{
        msg = "Access Granted"
        document.getElementById("get_in").innerHTML = msg
    }
}