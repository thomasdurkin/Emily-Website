window.onload = function() {
    let observerOptions = {
        rootMargin: '0px 0px 0px 0px', // Increase bottom margin to avoid overlapping with footer
        threshold: 0.3
    };
    
    function observerCallback(entries, observer) {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                let direction = entry.target.dataset.animationDirection;
                let animationClass = `animate-${direction}`;
                entry.target.classList.add('animate-up');
                observer.unobserve(entry.target);
            }
        });
    };
    
    let observer = new IntersectionObserver(observerCallback, observerOptions);
    
    let target = '.hidden';
    document.querySelectorAll(target).forEach((i) => {
        observer.observe(i);
    });
};