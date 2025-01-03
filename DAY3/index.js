// Function to calculate age based on date of birth
function calculateAge(dob) {
  const birthDate = new Date(dob);
  const today = new Date();
  let age = today.getFullYear() - birthDate.getFullYear();
  const monthDifference = today.getMonth() - birthDate.getMonth();

  // Adjust age if the birth date hasn't occurred yet this year
  if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }

  return age;
}

// Function to display age on the page
function displayAge() {
  const dobInput = document.getElementById('dob').value;
  const age = calculateAge(dobInput);
  const ageDisplay = document.getElementById('ageDisplay');
  ageDisplay.textContent = `Your age is: ${age}`;
}

// Adding event listener to the button
document.getElementById('calculateButton').addEventListener('click', displayAge);