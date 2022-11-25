document.addEventListener("DOMContentLoaded", () => {
  const btnDev = document.getElementById('dev')

  btnDev.addEventListener('click', () => {
      const age = document.getElementById('age')
      const sex = document.getElementById('gender')
      const chestpaintype = document.getElementById('chestpaintype')
      const restingbp = document.getElementById('restingbp')
      const cholesterol = document.getElementById('cholesterol')
      const fastingbs = document.getElementById('fastingbs')
      const restingecg = document.getElementById('restingecg')
      const maxhr = document.getElementById('maxhr')
      const exerciseangina = document.getElementById('exerciseangina')
      const oldpeak = document.getElementById('oldpeak')
      const st_slope = document.getElementById('st_slope')
  
      age.value = 10
      sex.value = 'M'
      chestpaintype.value = 'TA'
      restingbp.value = 
      cholesterol.value = 33
      fastingbs.value = 81
      restingecg.value = 'LVH'
      maxhr.value = 60
      exerciseangina.value = 'N'
      oldpeak.value = 11
      st_slope.value = 'Down'
  });

  const alertResult = document.getElementById('alert-result') 
  const alertMessage = document.getElementById('alert-message') 
  const alertDescription = document.getElementById('alert-description') 
  
  const alertStyle = {
    'Positive': 'alert-danger',
    'Negative': 'alert-primary',
    'Invalid': 'alert-warning'
  }

  const alertSymbol = {
    'Positive': '<i class="bi bi-heartbreak-fill me-3"></i>',
    'Negative': '<i class="bi bi-heart-fill me-3"></i>',
    'Invalid': '<i class="bi bi-exclamation-triangle me-3"></i>'
  }

  const alertHelperMessage = {
    'Positive': '<small>Be careful! Heart failure is detected.</small>',
    'Negative': '<small>No heart failure detected.</small>',
    'Invalid': '<small>Input data is not valid. Can\'t be processed by system.</small>',
  }

  const predictionResult = alertMessage.innerHTML

  console.log(predictionResult);
  if(predictionResult != '') {
    alertResult.classList.add(alertStyle[predictionResult])
    alertResult.insertAdjacentHTML('afterbegin', alertSymbol[predictionResult])
    alertDescription.insertAdjacentHTML('beforeend', alertHelperMessage[predictionResult])
    
    if(predictionResult == 'Positive' || predictionResult == 'Negative')
      alertMessage.parentElement.insertAdjacentHTML('afterbegin', 'Result: ')
    
    alertResult.classList.remove('d-none')
  }

})