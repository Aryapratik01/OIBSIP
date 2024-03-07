let display = document.getElementById('display');
let currentInput = '';

function appendCharacter(char) {
  currentInput += char;
  updateDisplay();
}

function clearDisplay() {
  currentInput = '';
  updateDisplay();
}

function calculate() {
  try {
    currentInput = eval(currentInput).toString();
    updateDisplay();
  } catch (error) {
    currentInput = 'Error';
    updateDisplay();
  }
}

function updateDisplay() {
  display.textContent = currentInput;
}
