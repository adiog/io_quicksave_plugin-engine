class YouTubePlugin
{
    static match(item)
    {
        return ((typeof(item.bean.source_url) != 'undefined') && (item.bean.source_url.indexOf('youtube.com') != -1));
    }

    static icon(item)
    {
        return IconButton('youtube');
    }

    static display(item)
    {
        let dom = document.createElement('div');
        return dom;
    }

    static menu(item, dom)
    {
        dom.appendChild(Right(IconButton('download', function(ev) {YouTubePlugin.download(item)})));
    }

    static download(item)
    {

    }
}

pluginEngine.registerPlugin(YouTubePlugin);
