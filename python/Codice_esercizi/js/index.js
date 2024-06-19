function paint(color) {
    const circle = document.getElementById('circleID');
    circle.style = `background-color:${color}`;
  }

function paint_random() {
  const circle = document.getElementById('circleID');
  color = "#" + ((1 << 24) * Math.random() | 0).toString(16).padStart(6, "0")
  circle.style = `background-color:${color}`;
}

