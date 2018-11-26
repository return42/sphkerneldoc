.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/bridge/br_forward.c

.. _`br_forward`:

br_forward
==========

.. c:function:: void br_forward(const struct net_bridge_port *to, struct sk_buff *skb, bool local_rcv, bool local_orig)

    forward a packet to a specific port

    :param to:
        destination port
    :type to: const struct net_bridge_port \*

    :param skb:
        packet being forwarded
    :type skb: struct sk_buff \*

    :param local_rcv:
        packet will be received locally after forwarding
    :type local_rcv: bool

    :param local_orig:
        packet is locally originated
    :type local_orig: bool

.. _`br_forward.description`:

Description
-----------

Should be called with rcu_read_lock.

.. This file was automatic generated / don't edit.

