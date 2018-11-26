.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/devinet.c

.. _`__ip_dev_find`:

\__ip_dev_find
==============

.. c:function:: struct net_device *__ip_dev_find(struct net *net, __be32 addr, bool devref)

    find the first device with a given source address.

    :param net:
        the net namespace
    :type net: struct net \*

    :param addr:
        the source address
    :type addr: __be32

    :param devref:
        if true, take a reference on the found device
    :type devref: bool

.. _`__ip_dev_find.description`:

Description
-----------

If a caller uses devref=false, it should be protected by RCU, or RTNL

.. This file was automatic generated / don't edit.

