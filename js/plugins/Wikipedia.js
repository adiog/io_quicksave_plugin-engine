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
        return dom;
    }

    static menu(item, dom)
    {
        dom.appendChild(Right(IconButton('asterisk', function(ev) {item.delayAction.restart();})));
    }
}

pluginEngine.registerPlugin(MP4Plugin);
