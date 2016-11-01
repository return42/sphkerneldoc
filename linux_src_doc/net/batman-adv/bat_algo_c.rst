.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bat_algo.c

.. _`batadv_algo_init`:

batadv_algo_init
================

.. c:function:: void batadv_algo_init( void)

    Initialize batman-adv algorithm management data structures

    :param  void:
        no arguments

.. _`batadv_algo_dump_entry`:

batadv_algo_dump_entry
======================

.. c:function:: int batadv_algo_dump_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_algo_ops *bat_algo_ops)

    fill in information about one supported routing algorithm

    :param struct sk_buff \*msg:
        netlink message to be sent back

    :param u32 portid:
        Port to reply to

    :param u32 seq:
        Sequence number of message

    :param struct batadv_algo_ops \*bat_algo_ops:
        Algorithm to be dumped

.. _`batadv_algo_dump_entry.return`:

Return
------

Error number, or 0 on success

.. _`batadv_algo_dump`:

batadv_algo_dump
================

.. c:function:: int batadv_algo_dump(struct sk_buff *msg, struct netlink_callback *cb)

    fill in information about supported routing algorithms

    :param struct sk_buff \*msg:
        netlink message to be sent back

    :param struct netlink_callback \*cb:
        Parameters to the netlink request

.. _`batadv_algo_dump.return`:

Return
------

Length of reply message.

.. This file was automatic generated / don't edit.

