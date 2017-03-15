class WikipediaPlugin
{
    static match(item)
    {
        return item.hasTag('wiki');
    }

    static icon(item)
    {
        return IconButton('wikipedia');
    }

    static display(item)
    {
        let dom = document.createElement('div');
        let img = document.createElement('img');
        img.src = 'http://fs.quicksave.io/' + item.itemBean.url + '/thumbnail_crop.png';
        dom.appendChild(img);
        return dom;
    }

    static menu(item, dom)
    {
    }
}

pluginEngine.registerPlugin(WikipediaPlugin);
