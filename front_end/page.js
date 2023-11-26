$(document).ready(function() {
    $('#productPredictionForm').submit(function(e) {
        e.preventDefault();
         //perform prediction logic here
        let productTitle = $('#productTitle').val();
        let productDescription = $('#productDescription').val();
        let productPrice = $('#productPrice').val();

         //temporarly prediction result
        let predictedRating = Math.floor(Math.random() * 5) + 1;

         //showing model result
        $('#resultContainer').html(`<h3>Predicted Rating: ${predictedRating}</h3>`);
        $('#predictionResult').show();
    });
});

