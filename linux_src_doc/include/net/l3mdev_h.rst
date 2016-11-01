.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/l3mdev.h

.. _`l3mdev_ops`:

struct l3mdev_ops
=================

.. c:type:: struct l3mdev_ops

    l3mdev operations

.. _`l3mdev_ops.definition`:

Definition
----------

.. code-block:: c

    struct l3mdev_ops {
        u32 (*l3mdev_fib_table)(const struct net_device *dev);
        struct sk_buff * (*l3mdev_l3_rcv)(struct net_device *dev,struct sk_buff *skb, u16 proto);
        struct sk_buff * (*l3mdev_l3_out)(struct net_device *dev,struct sock *sk, struct sk_buff *skb,u16 proto);
        struct dst_entry * (*l3mdev_link_scope_lookup)(const struct net_device *dev,struct flowi6 *fl6);
    }

.. _`l3mdev_ops.members`:

Members
-------

l3mdev_fib_table
    Get FIB table id to use for lookups

l3mdev_l3_rcv
    Hook in L3 receive path

l3mdev_l3_out
    Hook in L3 output path

l3mdev_link_scope_lookup
    IPv6 lookup for linklocal and mcast destinations

.. This file was automatic generated / don't edit.

