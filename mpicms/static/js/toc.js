var toc = document.getElementById('toc');
var headings = [].slice.call(document.getElementById('content').querySelectorAll('h2, h3, h4, h5, h6'));
headings.forEach(function (heading, index) {
    var anchor = document.createElement('a');
    anchor.setAttribute('name', 'toc' + index);
    anchor.setAttribute('id', 'toc' + index);

    var link = document.createElement('a');
    link.setAttribute('href', '#toc' + index);
    link.textContent = heading.textContent;

    var div = document.createElement('div');
    div.setAttribute('class', heading.tagName.toLowerCase());

    div.appendChild(link);
    toc.appendChild(div);
    heading.parentNode.insertBefore(anchor, heading);
});
