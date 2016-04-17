.. -*- coding: utf-8; mode: rst -*-

========
l3mdev.h
========


.. _`l3mdev_ops`:

struct l3mdev_ops
=================

.. c:type:: l3mdev_ops

    l3mdev operations


.. _`l3mdev_ops.definition`:

Definition
----------

.. code-block:: c

  struct l3mdev_ops {
    u32 (* l3mdev_fib_table) (const struct net_device *dev);
    struct rtable *	(* l3mdev_get_rtable) (const struct net_device *dev,const struct flowi4 *fl4);
    int (* l3mdev_get_saddr) (struct net_device *dev,struct flowi4 *fl4);
    struct dst_entry * (* l3mdev_get_rt6_dst) (const struct net_device *dev,const struct flowi6 *fl6);
  };


.. _`l3mdev_ops.members`:

Members
-------

:``l3mdev_fib_table``:
    Get FIB table id to use for lookups

:``l3mdev_get_rtable``:
    Get cached IPv4 rtable (dst_entry) for device

:``l3mdev_get_saddr``:
    Get source address for a flow

:``l3mdev_get_rt6_dst``:
    Get cached IPv6 rt6_info (dst_entry) for device


