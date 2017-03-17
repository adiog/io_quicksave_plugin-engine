class WolframPlugin
{
    static match(item)
    {
        return ((typeof(item.itemBean.freetext) != 'undefined') && (item.itemBean.freetext.indexOf('$') != -1));
    }

    static icon(item)
    {
        return IconButton('superscript');
    }

    static display(item)
    {
        let dom = div();
        return dom;
    }

    static menu(item, dom)
    {
        dom.appendChild(Left(IconButton('certificate', function(ev) {
            console.log('wolf');
            WolframPlugin.download(item);
        })));
    }

    static appid()
    {
        return '7YKHRU-L74LQHJLVE'
    }

    static download(item)
    {
        let url = 'https://www.wolframalpha.com/input/?appid=' + WolframPlugin.appid() + '&i=' + item.itemBean.freetext.replace(/\$/g, '');
        console.log(url);
        document.location.href = url;
    }
}

pluginEngine.registerPlugin(WolframPlugin);
