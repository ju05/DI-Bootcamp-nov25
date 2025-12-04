console.log('Starting ...');

const addArticle = (event) => {
  event.preventDefault();
  const data = new FormData(event.target);

  const objBody = {
    method: 'POST',
    body: JSON.stringify(Object.fromEntries(data)),
    headers: { 'Content-type': 'application/json; charset=UTF-8' }
  };

  console.log('Working ...');
  fetch('https://jsonplaceholder.typicode.com/posts', objBody)
    .then((response) => {
      console.log(response);
      if (response.ok === true) {
        return response.json();
      } else {
        throw new Error('Wrong post');
      }
    })
    .then((obj) => {
      console.log(obj);
    })
    .catch((error) => {
      console.log(error);
    });
  console.log('Work Done ...');
};

const formArticle = document.querySelector('form');
formArticle.addEventListener('submit', addArticle);
