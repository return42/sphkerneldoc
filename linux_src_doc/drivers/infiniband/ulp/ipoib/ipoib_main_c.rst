.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/ipoib/ipoib_main.c

.. _`ipoib_get_master_net_dev`:

ipoib_get_master_net_dev
========================

.. c:function:: struct net_device *ipoib_get_master_net_dev(struct net_device *dev)

    :param dev:
        base IPoIB net_device
    :type dev: struct net_device \*

.. _`ipoib_get_master_net_dev.description`:

Description
-----------

Returns the master net_device with a reference held, or the same net_device
if no master exists.

.. _`ipoib_get_net_dev_match_addr`:

ipoib_get_net_dev_match_addr
============================

.. c:function:: struct net_device *ipoib_get_net_dev_match_addr(const struct sockaddr *addr, struct net_device *dev)

    the given net_device.

    :param addr:
        IP address to look for.
    :type addr: const struct sockaddr \*

    :param dev:
        base IPoIB net_device
    :type dev: struct net_device \*

.. _`ipoib_get_net_dev_match_addr.description`:

Description
-----------

If found, returns the net_device with a reference held. Otherwise return
NULL.

.. This file was automatic generated / don't edit.

