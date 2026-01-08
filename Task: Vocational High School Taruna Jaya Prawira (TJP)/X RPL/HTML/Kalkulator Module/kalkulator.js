
    let display = document.getElementById('display');
    let currentInput = '0';
    let shouldResetDisplay = false;

    function updateDisplay() {
      display.textContent = currentInput;
    }

    function appendToDisplay(value) {
      if (shouldResetDisplay) {
        currentInput = '0';
        shouldResetDisplay = false;
      }
      
      if (currentInput === '0' && value !== '.') {
        currentInput = value;
      } else {
        currentInput += value;
      }
      updateDisplay();
    }

    function clearDisplay() {
      currentInput = '0';
      updateDisplay();
    }

    function deleteLast() {
      if (currentInput.length > 1) {
        currentInput = currentInput.slice(0, -1);
      } else {
        currentInput = '0';
      }
      updateDisplay();
    }

    function calculate() {
      try {
        // Ganti simbol × dan − dengan operator JavaScript
        let expression = currentInput
          .replace(/×/g, '*')
          .replace(/−/g, '-');
        
        // Gunakan Function constructor untuk evaluasi aman
        currentInput = String(new Function('return ' + expression)());
        
        // Batasi angka terlalu panjang
        if (currentInput.length > 12) {
          currentInput = Number(currentInput).toExponential(5);
        }
      } catch (e) {
        currentInput = 'Error';
      }
      
      updateDisplay();
      shouldResetDisplay = true;
    }

    // Support keyboard
    document.addEventListener('keydown', function(e) {
      if (e.key >= 0 && e.key <= 9) appendToDisplay(e.key);
      if (e.key === '.') appendToDisplay('.');
      if (e.key === '+') appendToDisplay('+');
      if (e.key === '-') appendToDisplay('−');
      if (e.key === '*') appendToDisplay('*');
      if (e.key === ':') { e.preventDefault(); appendToDisplay(':'); }
      if (e.key === 'Enter' || e.key === '=') calculate();
      if (e.key === 'Backspace') deleteLast();
      if (e.key === 'Escape') clearDisplay();
    });