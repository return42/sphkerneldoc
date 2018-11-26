.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/dst.h

.. _`skb_dst_drop`:

skb_dst_drop
============

.. c:function:: void skb_dst_drop(struct sk_buff *skb)

    drops skb dst

    :param skb:
        buffer
    :type skb: struct sk_buff \*

.. _`skb_dst_drop.description`:

Description
-----------

Drops dst reference count if a reference was taken.

.. _`dst_hold_safe`:

dst_hold_safe
=============

.. c:function:: bool dst_hold_safe(struct dst_entry *dst)

    Take a reference on a dst if possible

    :param dst:
        pointer to dst entry
    :type dst: struct dst_entry \*

.. _`dst_hold_safe.description`:

Description
-----------

This helper returns false if it could not safely
take a reference on a dst.

.. _`skb_dst_force`:

skb_dst_force
=============

.. c:function:: void skb_dst_force(struct sk_buff *skb)

    makes sure skb dst is refcounted

    :param skb:
        buffer
    :type skb: struct sk_buff \*

.. _`skb_dst_force.description`:

Description
-----------

If dst is not yet refcounted and not destroyed, grab a ref on it.

.. _`__skb_tunnel_rx`:

\__skb_tunnel_rx
================

.. c:function:: void __skb_tunnel_rx(struct sk_buff *skb, struct net_device *dev, struct net *net)

    prepare skb for rx reinsert

    :param skb:
        buffer
    :type skb: struct sk_buff \*

    :param dev:
        tunnel device
    :type dev: struct net_device \*

    :param net:
        netns for packet i/o
    :type net: struct net \*

.. _`__skb_tunnel_rx.description`:

Description
-----------

After decapsulation, packet is going to re-enter (netif_rx()) our stack,
so make some cleanups. (no accounting done)

.. _`skb_tunnel_rx`:

skb_tunnel_rx
=============

.. c:function:: void skb_tunnel_rx(struct sk_buff *skb, struct net_device *dev, struct net *net)

    prepare skb for rx reinsert

    :param skb:
        buffer
    :type skb: struct sk_buff \*

    :param dev:
        tunnel device
    :type dev: struct net_device \*

    :param net:
        netns for packet i/o
    :type net: struct net \*

.. _`skb_tunnel_rx.description`:

Description
-----------

After decapsulation, packet is going to re-enter (netif_rx()) our stack,
so make some cleanups, and perform accounting.

.. _`skb_tunnel_rx.note`:

Note
----

this accounting is not SMP safe.

.. This file was automatic generated / don't edit.

