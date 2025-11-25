function showBanner() {
  const banner = document.getElementById('sales-banner');
  banner.style.display = 'block';

  let countdown = 10;

  function updateBanner() {
    banner.textContent = `Sale ends in ${countdown} seconds!!!!`;
    countdown--;

    if (countdown < 0) {
      clearInterval(countdownInterval);
    }
  }

  const countdownInterval = setInterval(updateBanner, 1000);
}

setTimeout(showBanner, 5000);
