.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/addrconf.h

.. _`__in6_dev_get`:

\__in6_dev_get
==============

.. c:function:: struct inet6_dev *__in6_dev_get(const struct net_device *dev)

    get inet6_dev pointer from netdevice

    :param dev:
        network device
    :type dev: const struct net_device \*

.. _`__in6_dev_get.description`:

Description
-----------

Caller must hold rcu_read_lock or RTNL, because this function
does not take a reference on the inet6_dev.

.. _`__in6_dev_get_safely`:

\__in6_dev_get_safely
=====================

.. c:function:: struct inet6_dev *__in6_dev_get_safely(const struct net_device *dev)

    get inet6_dev pointer from netdevice

    :param dev:
        network device
    :type dev: const struct net_device \*

.. _`__in6_dev_get_safely.description`:

Description
-----------

This is a safer version of \__in6_dev_get

.. _`in6_dev_get`:

in6_dev_get
===========

.. c:function:: struct inet6_dev *in6_dev_get(const struct net_device *dev)

    get inet6_dev pointer from netdevice

    :param dev:
        network device
    :type dev: const struct net_device \*

.. _`in6_dev_get.description`:

Description
-----------

This version can be used in any context, and takes a reference
on the inet6_dev. Callers must use \ :c:func:`in6_dev_put`\  later to
release this reference.

.. This file was automatic generated / don't edit.

