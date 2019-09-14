var toc = document.getElementById('toc');
if (toc) {
    var headings = [].slice.call(document.getElementById('content').querySelectorAll('h1, h2, h3, h4, h5, h6'));
    var tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'];
    var indexes = Array(tags.length).fill(0);
    headings.forEach(function (heading, index) {
        var anchor = document.createElement('a');
        anchor.setAttribute('name', 'toc' + index);
        anchor.setAttribute('id', 'toc' + index);

        var link = document.createElement('a');
        link.setAttribute('href', '#toc' + index);
        link.textContent = heading.textContent;

        var div = document.createElement('div');
        var tagName = heading.tagName.toLowerCase()
        div.setAttribute('class', tagName);

        // Number TOC
        currentIndex = tags.indexOf(tagName)
        indexes[currentIndex]++;
        indexArray = indexes.slice(0, currentIndex +1)
        indexes = indexArray.concat(Array(tags.length - currentIndex).fill(0))
        
        link.textContent = `${indexArray.join('.')}. ${link.textContent}`;

        div.appendChild(link);
        toc.appendChild(div);
        heading.parentNode.insertBefore(anchor, heading);
    });
}