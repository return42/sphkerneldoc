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

.. _`l3mdev_link_scope_lookup`:

l3mdev_link_scope_lookup
========================

.. c:function:: struct dst_entry *l3mdev_link_scope_lookup(struct net *net, struct flowi6 *fl6)

    IPv6 route lookup based on flow for link local and multicast addresses

    :param struct net \*net:
        network namespace for device index lookup

    :param struct flowi6 \*fl6:
        IPv6 flow struct for lookup

.. _`l3mdev_fib_rule_match`:

l3mdev_fib_rule_match
=====================

.. c:function:: int l3mdev_fib_rule_match(struct net *net, struct flowi *fl, struct fib_lookup_arg *arg)

    Determine if flowi references an L3 master device

    :param struct net \*net:
        network namespace for device index lookup

    :param struct flowi \*fl:
        flow struct

    :param struct fib_lookup_arg \*arg:
        *undescribed*

.. This file was automatic generated / don't edit.

