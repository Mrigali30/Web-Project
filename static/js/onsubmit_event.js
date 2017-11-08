<script type="text/javascript">
  function ValidationEvent() 
  {
// Storing Field Values In Variables
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    // Regular Expression For Email
    var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    // Conditions
    if (email != '' && password != '') 
    {
      if (email.match(emailReg)) {

        alert("All type of validation has done on OnSubmit event.");
        return true;
      } 
      else {
        alert("Invalid Email Address...!!!");
        return false;
      }
    } 
    else 
    {
    alert("All fields are required.....!");
    return false;
    }
  }
</script>