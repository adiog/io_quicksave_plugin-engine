// This file is a part of quicksave project.
// Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

#ifndef QUICKSAVE_PLUGINENGINE_H
#define QUICKSAVE_PLUGINENGINE_H

#include <PythonBeanAPI.h>
#include <bean/RichItemBean.h>

class PluginEngine
{
public:
    static RichItemBean process(ItemBean itemBean)
    {
        return PythonBeanAPI::call<ItemBean, RichItemBean>("process", itemBean);
    }
};

#endif //QUICKSAVE_PLUGINENGINE_H_H
