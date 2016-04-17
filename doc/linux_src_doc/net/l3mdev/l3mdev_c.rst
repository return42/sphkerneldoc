.. -*- coding: utf-8; mode: rst -*-

========
l3mdev.c
========


.. _`l3mdev_master_ifindex_rcu`:

l3mdev_master_ifindex_rcu
=========================

.. c:function:: int l3mdev_master_ifindex_rcu (const struct net_device *dev)

    get index of L3 master device

    :param const struct net_device \*dev:
        targeted interface



.. _`l3mdev_fib_table_rcu`:

l3mdev_fib_table_rcu
====================

.. c:function:: u32 l3mdev_fib_table_rcu (const struct net_device *dev)

    get FIB table id associated with an L3 master interface

    :param const struct net_device \*dev:
        targeted interface

