
$(document).ready(function () {
    $('#reviewPredictionForm').submit(function (e) {
        e.preventDefault();

        let productTitle = $('#productTitle').val();
        let productReview = $('#productReview').val();

        // Make an API call to the Flask server
        fetch('api code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'productTitle': productTitle,
                'productReview': productReview,
            }),
        })
            .then(response => response.json())
            .then(data => {
                // Update the UI with the prediction result
                let predictedRating = data.predicted_rating.toFixed(2);
                $('#predictedRating').attr('data-star', predictedRating);
                $('#predictedRating').html(`<h3>${predictedRating} out of 5</h3>`);
                $('#predictionResult').show();
            })
            .catch(error => console.error('Error:', error));
    });
});
