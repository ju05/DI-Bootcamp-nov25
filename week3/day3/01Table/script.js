function insertRow() {
  const table = document.getElementById('sampleTable');

  const newRow = table.insertRow(-1);

  const cell1 = newRow.insertCell(0);
  const cell2 = newRow.insertCell(1);

  // below is optional
  const size = table.rows.length;

  cell1.textContent = `Row${size} cell1`;
  cell2.textContent = `Row${size} cell2`;
}
