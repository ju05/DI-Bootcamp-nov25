const container = document.getElementById('container');
const jsstyle = document.getElementById('jsstyle');

container.addEventListener('click', thingClick);

jsstyle.addEventListener('click', btnClick);
jsstyle.addEventListener('mouseenter', buttonEnter);

function thingClick(e) {
  const elem = e.target;
  alert(`the ${elem.id} was clicked!`);
}

function btnClick(e) {
  const elem = e.target;
  alert(`the ${elem.id} was clicked!`);
  e.stopPropagation();
}

function buttonEnter(e) {
  const elem = e.target;
  elem.style.backgroundColor = 'red';
}
