// This file is a part of quicksave project.
// Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

#ifndef QUICKSAVE_PLUGINENGINE_H
#define QUICKSAVE_PLUGINENGINE_H

#include <PythonBeanAPI.h>
#include <bean/ItemBean.h>

class PluginEngine
{
public:
    static ItemBean process(MetaBean metaBean)
    {
        return PythonBeanAPI::call<MetaBean, ItemBean>("process", metaBean);
    }

    static MessageBean donetask(MessageBean messageBean)
    {
        return PythonBeanAPI::call<MessageBean, MessageBean>("donetask", messageBean);
    }
};

#endif //QUICKSAVE_PLUGINENGINE_H_H
