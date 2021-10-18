document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {
        fetch("http://api.exchangeratesapi.io/v1/latest?access_key=284b4a65480cae5859ffd12234443577")
        .then(response => response.json())
        .then(data => {
            const currency = document.querySelector('#currency').value.toUpperCase();
            const rate = data.rates[currency];
            if (rate !== undefined) {
                document.querySelector('#result').innerHTML = `1 EUR is equal to ${rate.toFixed(3)} ${currency}.`
            } 
            else {
                document.querySelector('#result').innerHTML = 'Invalid Currency.'
            }
            console.log(data);
        })
        .catch(error => {
            console.log('Error:', error);
        });
        return false;
    }
});