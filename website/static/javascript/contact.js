// JavaScript to fade out the flash message after a certain duration
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var flashMessage = document.getElementById('flash-message');
        if (flashMessage) {
            flashMessage.style.opacity = '0';
            // Fade out duration (same as CSS transition duration)
            setTimeout(function() {
                flashMessage.style.display = 'none';
            }, 500);
        }
    // Duration after which the message fades out (in milliseconds)
    }, 2000); 
});