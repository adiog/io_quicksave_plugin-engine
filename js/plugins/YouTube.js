class YouTubePlugin
{
    static match(item)
    {
        return ((typeof(item.itemBean.source_url) != 'undefined') && (item.itemBean.source_url.indexOf('youtube.com') != -1));
    }

    static icon(item)
    {
        return IconButton('youtube');
    }

    static display(item)
    {
        let dom = document.createElement('iframe');
        dom.id = 'ytplayer';
        dom.type = 'text/html'
        dom.width = 640;
        dom.height = 360;
        dom.src = item.itemBean.source_url;
        dom.frameborder = 0;
        return dom;
    }

    static menu(item, dom)
    {
        dom.appendChild(Left(IconButton('download', function(ev) {YouTubePlugin.download(item)})));
    }

    static download(item)
    {
        document.location.href = 'https://cdn.quicksave.io/' + item.itemBean.item_id + '/youtube';
    }
}

pluginEngine.registerPlugin(YouTubePlugin);
