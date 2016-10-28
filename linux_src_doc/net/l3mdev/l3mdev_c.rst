.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/l3mdev/l3mdev.c

.. _`l3mdev_master_ifindex_rcu`:

l3mdev_master_ifindex_rcu
=========================

.. c:function:: int l3mdev_master_ifindex_rcu(const struct net_device *dev)

    get index of L3 master device

    :param const struct net_device \*dev:
        targeted interface

.. _`l3mdev_fib_table_rcu`:

l3mdev_fib_table_rcu
====================

.. c:function:: u32 l3mdev_fib_table_rcu(const struct net_device *dev)

    get FIB table id associated with an L3 master interface

    :param const struct net_device \*dev:
        targeted interface

.. _`l3mdev_get_rt6_dst`:

l3mdev_get_rt6_dst
==================

.. c:function:: struct dst_entry *l3mdev_get_rt6_dst(struct net *net, const struct flowi6 *fl6)

    IPv6 route lookup based on flow. Returns cached route for L3 master device if relevant to flow

    :param struct net \*net:
        network namespace for device index lookup

    :param const struct flowi6 \*fl6:
        IPv6 flow struct for lookup

.. _`l3mdev_get_saddr`:

l3mdev_get_saddr
================

.. c:function:: int l3mdev_get_saddr(struct net *net, int ifindex, struct flowi4 *fl4)

    get source address for a flow based on an interface enslaved to an L3 master device

    :param struct net \*net:
        network namespace for device index lookup

    :param int ifindex:
        Interface index

    :param struct flowi4 \*fl4:
        IPv4 flow struct

.. This file was automatic generated / don't edit.

