class SourceCppPlugin
{
    static match(item)
    {
        return item.hasTag('cpp');
    }

    static icon(item)
    {
        return IconButton('code');
    }

    static display(item)
    {
        return $$$(pre({class: 'prettyprint linenums lang-cpp', style: 'text-align: left'}), item.bean.item.freetext);
    }

    static menu(item, dom)
    {
    }
}

pluginEngine.registerPlugin(SourceCppPlugin);
