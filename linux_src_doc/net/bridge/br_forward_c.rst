.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/bridge/br_forward.c

.. _`br_forward`:

br_forward
==========

.. c:function:: void br_forward(const struct net_bridge_port *to, struct sk_buff *skb, bool local_rcv, bool local_orig)

    forward a packet to a specific port

    :param const struct net_bridge_port \*to:
        destination port

    :param struct sk_buff \*skb:
        packet being forwarded

    :param bool local_rcv:
        packet will be received locally after forwarding

    :param bool local_orig:
        packet is locally originated

.. _`br_forward.description`:

Description
-----------

Should be called with rcu_read_lock.

.. This file was automatic generated / don't edit.

