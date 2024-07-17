
$(document).ready(function () {
    $('#prediction-form').on('submit', function (e) {
        e.preventDefault();

        var data = {
            Weight: $('#weight').val(),
            Length1: $('#length1').val(),
            Length2: $('#length2').val(),
            Length3: $('#length3').val(),
            Height: $('#height').val(),
            Width: $('#width').val()
        };

        $.ajax({
            type: 'POST',
            url: '/predict',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {
                $('#result').html('Predicted Species: ' + response.predicted_species);
            },
            error: function (error) {
                console.log(error);
                $('#result').html('An error occurred.');
            }
        });
    });
});
