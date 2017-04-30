// This file is a part of quicksave project.
// Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

#pragma once

#include <PythonBeanAPI.h>
#include <bean/ItemBean.h>
#include <bean/InternalCreateRequestBean.h>

class PluginEngine
{
public:
    static ItemBean process(InternalCreateRequestBean bean)
    {
        return PythonBeanAPI::call<InternalCreateRequestBean, ItemBean>("process", bean);
    }
};

