const btn = document.getElementById('jsstyle');

btn.addEventListener('mouseover', handleMouseOver);
btn.addEventListener('click', handleClick);
btn.addEventListener('mouseout', handleMouseOut);

const btn2 = document.getElementById('jsstyle2');

btn2.addEventListener('mouseover', handleMouseOver);
btn2.addEventListener('click', handleClick);
btn2.addEventListener('mouseout', handleMouseOut);

function handleMouseOver(e) {
  const myBtn = e.target;
  myBtn.style.backgroundColor = 'blue';
}

function handleClick(e) {
  const myBtn = e.target;
  myBtn.style.borderRadius = '60px';
  myBtn.style.backgroundColor = 'purple';
}

function handleMouseOut(e) {
  const myBtn = e.target;
  myBtn.style.backgroundColor = 'lightgrey';
  myBtn.style.borderRadius = '0px';
}
