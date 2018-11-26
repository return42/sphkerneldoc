.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/net_failover.c

.. _`net_failover_create`:

net_failover_create
===================

.. c:function:: struct failover *net_failover_create(struct net_device *standby_dev)

    Create and register a failover instance

    :param standby_dev:
        *undescribed*
    :type standby_dev: struct net_device \*

.. _`net_failover_create.description`:

Description
-----------

Creates a failover netdev and registers a failover instance for a standby
netdev. Used by paravirtual drivers that use 3-netdev model.
The failover netdev acts as a master device and controls 2 slave devices -
the original standby netdev and a VF netdev with the same MAC gets
registered as primary netdev.

.. _`net_failover_create.return`:

Return
------

pointer to failover instance

.. _`net_failover_destroy`:

net_failover_destroy
====================

.. c:function:: void net_failover_destroy(struct failover *failover)

    Destroy a failover instance

    :param failover:
        pointer to failover instance
    :type failover: struct failover \*

.. _`net_failover_destroy.description`:

Description
-----------

Unregisters any slave netdevs associated with the failover instance by
calling \ :c:func:`failover_slave_unregister`\ .
unregisters the failover instance itself and finally frees the failover
netdev. Used by paravirtual drivers that use 3-netdev model.

.. This file was automatic generated / don't edit.

