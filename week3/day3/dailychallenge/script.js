const form = document.getElementById('libform');

// Other ways to do the same thing:
// const form = document.querySelector('#libform')
// const form = document.forms[0];
// const form = document.getElementsByTagName('form')[0];
// const form = document.body.firstElementChild.nextElementSibling

form.addEventListener('submit', function (e) {
  // always prevent default
  e.preventDefault();

  // get the pieces
  const noun = document.getElementById('noun').value;
  const adj = document.getElementById('adjective').value;
  const person = document.getElementById('person').value;
  const verb = document.getElementById('verb').value;
  const place = document.getElementById('place').value;

  // make a story
  const story = `One day, ${person} found a very ${adj} ${noun}.  They decided to ${verb} with it all the way to ${place}.`;

  const storyDiv = document.getElementById('story');
  storyDiv.textContent = story;
});
