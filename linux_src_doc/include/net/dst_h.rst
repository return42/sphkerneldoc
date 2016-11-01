.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/dst.h

.. _`skb_dst_drop`:

skb_dst_drop
============

.. c:function:: void skb_dst_drop(struct sk_buff *skb)

    drops skb dst

    :param struct sk_buff \*skb:
        buffer

.. _`skb_dst_drop.description`:

Description
-----------

Drops dst reference count if a reference was taken.

.. _`skb_dst_force`:

skb_dst_force
=============

.. c:function:: void skb_dst_force(struct sk_buff *skb)

    makes sure skb dst is refcounted

    :param struct sk_buff \*skb:
        buffer

.. _`skb_dst_force.description`:

Description
-----------

If dst is not yet refcounted, let's do it

.. _`dst_hold_safe`:

dst_hold_safe
=============

.. c:function:: bool dst_hold_safe(struct dst_entry *dst)

    Take a reference on a dst if possible

    :param struct dst_entry \*dst:
        pointer to dst entry

.. _`dst_hold_safe.description`:

Description
-----------

This helper returns false if it could not safely
take a reference on a dst.

.. _`skb_dst_force_safe`:

skb_dst_force_safe
==================

.. c:function:: void skb_dst_force_safe(struct sk_buff *skb)

    makes sure skb dst is refcounted

    :param struct sk_buff \*skb:
        buffer

.. _`skb_dst_force_safe.description`:

Description
-----------

If dst is not yet refcounted and not destroyed, grab a ref on it.

.. _`__skb_tunnel_rx`:

__skb_tunnel_rx
===============

.. c:function:: void __skb_tunnel_rx(struct sk_buff *skb, struct net_device *dev, struct net *net)

    prepare skb for rx reinsert

    :param struct sk_buff \*skb:
        buffer

    :param struct net_device \*dev:
        tunnel device

    :param struct net \*net:
        netns for packet i/o

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

    :param struct sk_buff \*skb:
        buffer

    :param struct net_device \*dev:
        tunnel device

    :param struct net \*net:
        *undescribed*

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

