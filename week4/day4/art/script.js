console.log('Starting ...');

const displayArtwork = (art) => {
  const { title, artist_title: artist } = art.data;
  const paragraph = document.querySelector('#info-art');
  paragraph.textContent = `The painting is named 
    ${title} by the artist ${artist}`;
};

const displayError = (error) => {
  const paragraph = document.querySelector('#info-art');
  paragraph.textContent = `We have a problem ${error}`;
};

const getArtwork = () => {
  console.log('Working ...');
  fetch('https://api.artic.edu/api/v1/artworks/9')
    .then((response) => {
      console.log(response);
      if (response.ok === true) {
        return response.json();
      } else {
        throw new Error('Wrong artwork');
      }
    })
    .then((obj) => {
      displayArtwork(obj);
    })
    .catch((error) => {
      displayError(error);
    });
  console.log('Work Done ...');
};

getArtwork();
