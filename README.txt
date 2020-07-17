python manage.py runserver


ingyu-django.disqus.com

var disqus_config = function () {
    this.page.url = '{{ disqus_url }}';  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = {{ disqus_id }}'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};

(function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://ingyu-django.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
})();


git clone git@github.com:ryan-hwang-00/ch99.git