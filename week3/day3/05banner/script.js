function showBanner() {
  const banner = document.getElementById('sales-banner');
  banner.style.display = 'block';
  setInterval(hideBanner, 5000);
}

function hideBanner() {
  const banner = document.getElementById('sales-banner');
  banner.style.display = 'none';
}

setTimeout(showBanner, 5000);
