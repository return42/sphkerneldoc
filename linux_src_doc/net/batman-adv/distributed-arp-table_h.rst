.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/distributed-arp-table.h

.. _`batadv_dat_init_orig_node_addr`:

batadv_dat_init_orig_node_addr
==============================

.. c:function:: void batadv_dat_init_orig_node_addr(struct batadv_orig_node *orig_node)

    assign a DAT address to the orig_node

    :param struct batadv_orig_node \*orig_node:
        the node to assign the DAT address to

.. _`batadv_dat_init_own_addr`:

batadv_dat_init_own_addr
========================

.. c:function:: void batadv_dat_init_own_addr(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if)

    assign a DAT address to the node itself

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*primary_if:
        a pointer to the primary interface

.. _`batadv_dat_inc_counter`:

batadv_dat_inc_counter
======================

.. c:function:: void batadv_dat_inc_counter(struct batadv_priv *bat_priv, u8 subtype)

    increment the correct DAT packet counter

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param u8 subtype:
        the 4addr subtype of the packet to be counted

.. _`batadv_dat_inc_counter.description`:

Description
-----------

Updates the ethtool statistics for the received packet if it is a DAT subtype

.. This file was automatic generated / don't edit.

