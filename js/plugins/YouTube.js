class YouTubePlugin
{
    static match(ecmaItem)
    {
        return ((typeof(ecmaItem.metaBean.source_url) != 'undefined') && (ecmaItem.metaBean.source_url.indexOf('youtube.com') != -1));
    }

    static icon(ecmaItem)
    {
        return IconButton('youtube');
    }

    static display(ecmaItem)
    {
        let dom = document.createElement('iframe');
        dom.id = 'ytplayer';
        dom.type = 'text/html'
        dom.width = 640;
        dom.height = 360;
        dom.src = ecmaItem.item.meta.source_url;
        dom.frameborder = 0;
        return dom;
    }

    static menu(item, dom)
    {
        dom.appendChild(Left(IconButton('download', function(ev) {YouTubePlugin.download(item)})));
    }

    static download(ecmaItem)
    {
        document.location.href = env.HTTPS_CDN_QUICKSAVE_IO + '/' + ecmaItem.item.meta.meta_hash + '/youtube';
    }
}

pluginEngine.registerPlugin(YouTubePlugin);
