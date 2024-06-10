window.onload = function() {
    let observerOptions = {
        rootMargin: '0px 0px 0px 0px',
        threshold: 0.5
    };

    function observerCallback(entries, observer) {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                let direction = entry.target.dataset.animationDirection;
                let animationClass = `animate-${direction}`;
                entry.target.classList.add(animationClass);
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