//In this javascript we will connect to Ruva's website
//I will make a form to input a value
//We're going to cerate a function that prevents a Null message from being submitted

function validateForm() {
  //create a variable that allows the form to take on a value
  var x = document.forms["myForm"]["fname"].value
  if (x == ""){
    //if a null statement then return the following
    alert("Name must be filled out");
    return false;
  }
}
