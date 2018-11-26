.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/distributed-arp-table.h

.. _`batadv_dat_init_orig_node_addr`:

batadv_dat_init_orig_node_addr
==============================

.. c:function:: void batadv_dat_init_orig_node_addr(struct batadv_orig_node *orig_node)

    assign a DAT address to the orig_node

    :param orig_node:
        the node to assign the DAT address to
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_dat_init_own_addr`:

batadv_dat_init_own_addr
========================

.. c:function:: void batadv_dat_init_own_addr(struct batadv_priv *bat_priv, struct batadv_hard_iface *primary_if)

    assign a DAT address to the node itself

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param primary_if:
        a pointer to the primary interface
    :type primary_if: struct batadv_hard_iface \*

.. _`batadv_dat_inc_counter`:

batadv_dat_inc_counter
======================

.. c:function:: void batadv_dat_inc_counter(struct batadv_priv *bat_priv, u8 subtype)

    increment the correct DAT packet counter

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param subtype:
        the 4addr subtype of the packet to be counted
    :type subtype: u8

.. _`batadv_dat_inc_counter.description`:

Description
-----------

Updates the ethtool statistics for the received packet if it is a DAT subtype

.. This file was automatic generated / don't edit.

