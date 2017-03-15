class GitPlugin
{
    static match(item)
    {
        return ((typeof(item.itemBean.source_url) != 'undefined') && (item.itemBean.source_url.indexOf('github.com') != -1));
    }

    static icon(item)
    {
        return IconButton('github');
    }

    static display(item)
    {
        return $$$(div(), 'git -c http.sslVerify=false clone https://cdn.quicksave.io/' + String(item.itemBean.item_id) + '/git/.git repo');
    }

    static menu(item, dom)
    {
        dom.appendChild(Right(IconButton('download', function(ev) {GitPlugin.download(item)})));
    }

    static download(item)
    {
        document.location.href = 'https://cdn.quicksave.io/' + item.itemBean.item_id + '/git.tar';
    }
}

pluginEngine.registerPlugin(GitPlugin);
