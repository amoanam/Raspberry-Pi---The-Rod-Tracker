/**
 * Updates the current color, distance and motor status calling teh corresponding methods
 */
function updateStatus() {
  // Update current color based on Open CV
  //updateCurrentColorOpenCV()
  
  // Update motor status
  //...
  
  // Update current distance
  //updateDistance()

  // Update current color based on Sensor
  //updateCurrentColorDistance()

  
}

/**
 * Update the current color based on OpenCV
 */
 async function updateCurrentColorOpenCV() {
  try {
    // Request color from server
    const requestResult = await requestColorFromOpenCV()
    // Get the HTML element where the status is displayed
    const green_open_cv = document.getElementById('green_open_cv')
    green_open_cv.innerHTML = requestResult.data[0]
    const purple_open_cv = document.getElementById('purple_open_cv')
    purple_open_cv.innerHTML = requestResult.data[1]
    const yellow_open_cv = document.getElementById('yellow_open_cv')
    yellow_open_cv.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    updateStatus('Error getting the color based on OpenCV')
  }
}

/**
 * Function to request the server to update the current color based on OpenCV
 */
 function requestColorFromOpenCV () {
  try {
    // Make request to server
    return axios.get('/get_color_from_opencv')
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Function to request the server to start the motor
 */
 function requestStartMotor () {
  
  try{
    console.log('Motor Started')
    return axios.get('/start_motor')

  }catch(e){
    console.log('Error Starting Motor', e)
    updateStatus('Error Starting Motor')

  }

}


/**
 * Function to request the server to stop the motor
 */
function requestStopMotor () {
  
  try{
    console.log('Motor Stopped')
    return axios.get('/stop_motor')

  }catch(e){
    console.log('Error Stoping Motor', e)
    updateStatus('Error Stoping Motor')

  }
}

/**
 * Function to request the server to move the motor to next color zone
 */
 function movetonext(){
  try{
    console.log('moving to next color zone')
    return axios.get('/move_to_next')

  }catch(e){
    console.log('Error while moving to next color zone', e)
    updateStatus('Error while moving to next color zone')

  }

}

/**
 * Update the status of the motor
 * @param {String} status 
 */
 async function updateMotorStatus() {
  // Get the HTML element where the status is displayed
  let m_status = await axios.get('/motor_status')
  let motor_sts = document.getElementById("motor_status")
  console.log("Motor Status---",m_status)
  motor_sts.innerText = m_status.data.status
  console.log('Updating Motor Status')
}


/**
 * Update the current color based on distance sensor
 */
 async function updateDistance() {
  // Get the HTML element where the status is displayed
  try{
    console.log("entering in try")
    const requestdistance = requestDistance()
    console.log("Distane",requestdistance)
 
  }catch (e) {
    console.log('Error getting the Distance', e)
    updateStatus('Error getting the Distance')
}
 }

/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor
 */
async function requestDistance () {
  //...
  try {
    // Make request to server
    let result = await axios.get('/get_distance')
    let distance = document.getElementById("distance")
    console.log("Distance",result.data.distance)
    distance.innerText = result.data.distance
  } catch (e) {
    console.log('Error getting the distance', e)
    updateStatus('Error getting the distance')
  }
}


/**
 * Update the current color based on distance sensor
 */
 async function updateCurrentColorDistance() {
  // Get the HTML element where the status is displayed
  // ...
  try {
    // Request color from server
    const Result = await requestColorFromDistance()
    // Get the HTML element where the status is displayed
    const green_sensor = document.getElementById('green_sensor')
    green_sensor.innerHTML = Result.data[0]
    const purple_sensor = document.getElementById('purple_sensor')
    purple_sensor.innerHTML = Result.data[1]
    const yellow_sensor = document.getElementById('yellow_sensor')
    yellow_sensor.innerHTML = Result.data[2]
  } catch (e) {
    console.log('Error getting the color from sensor', e)
    updateStatus('Error getting the color from sensor')
  }
}


/**
 * Function to request the server to get the color based
 * on distance only
 */
function requestColorFromDistance () {
  try {
    // Make request to server
    return axios.get('/get_color_from_distance')
  } catch (e) {
    console.log('Error getting Color from distance', e)
    updateStatus('Error getting Color from distance')
  }
  //...
}
 