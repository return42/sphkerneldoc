.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/devinet.c

.. _`__ip_dev_find`:

\__ip_dev_find
==============

.. c:function:: struct net_device *__ip_dev_find(struct net *net, __be32 addr, bool devref)

    find the first device with a given source address.

    :param struct net \*net:
        the net namespace

    :param __be32 addr:
        the source address

    :param bool devref:
        if true, take a reference on the found device

.. _`__ip_dev_find.description`:

Description
-----------

If a caller uses devref=false, it should be protected by RCU, or RTNL

.. This file was automatic generated / don't edit.

