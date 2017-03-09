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
        console.log(item);
        console.log(item.bean);
        console.log(item.bean.item);
        console.log(item.bean.item.url);
        img.src = 'http://fs.quicksave.io/' + item.bean.item.url + '/thumbnail.png';
        dom.appendChild(img);
        return dom;
    }

    static menu(item, dom)
    {
    }
}

pluginEngine.registerPlugin(WikipediaPlugin);
