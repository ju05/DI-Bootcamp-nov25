// In a JS file, write a JavaScript function to get the values of First and Last name of the following form
function getvalue(event) {
  event.preventDefault();

  const myForm = document.getElementById('form1');

  const firstName = myForm.elements['fname'].value;
  const lastName = myForm.elements['lname'].value;

  alert(`${firstName} ${lastName} submitted the form!`);
}
