.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/can/skb.h

.. _`can_skb_priv`:

struct can_skb_priv
===================

.. c:type:: struct can_skb_priv

    private additional data inside CAN sk_buffs

.. _`can_skb_priv.definition`:

Definition
----------

.. code-block:: c

    struct can_skb_priv {
        int ifindex;
        int skbcnt;
        struct can_frame cf;
    }

.. _`can_skb_priv.members`:

Members
-------

ifindex
    ifindex of the first interface the CAN frame appeared on

skbcnt
    atomic counter to have an unique id together with skb pointer

cf
    align to the following CAN frame at skb->data

.. This file was automatic generated / don't edit.

