const API_BASE_URL = 'http://127.0.0.1:8000';

document.getElementById('houseForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const houseAge = document.getElementById('houseAge').value;
    // Get values of other input fields here

    const houseFeatures = {
        'MedInc': /* Add value here */,
        'HouseAge': parseFloat(houseAge),
        'AveRooms': /* Add value here */,
        'AveBedrms': /* Add value here */,
        'Population': /* Add value here */,
        'AveOccup': /* Add value here */,
        'Latitude': /* Add value here */,
        'Longitude': /* Add value here */
    };

    const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(houseFeatures)
    });

    const result = await response.json();

    if (result.predicted_price) {
        document.getElementById('predictionResult').innerHTML = `Predicted House Price: ${result.predicted_price}`;
    } else {
        document.getElementById('predictionResult').innerHTML = `Error: ${result.error}`;
    }
});
