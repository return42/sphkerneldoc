.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/gateway_client.c

.. _`batadv_gw_node_release`:

batadv_gw_node_release
======================

.. c:function:: void batadv_gw_node_release(struct kref *ref)

    release gw_node from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the gw_node

.. _`batadv_gw_node_put`:

batadv_gw_node_put
==================

.. c:function:: void batadv_gw_node_put(struct batadv_gw_node *gw_node)

    decrement the gw_node refcounter and possibly release it

    :param struct batadv_gw_node \*gw_node:
        gateway node to free

.. _`batadv_gw_get_selected_gw_node`:

batadv_gw_get_selected_gw_node
==============================

.. c:function:: struct batadv_gw_node *batadv_gw_get_selected_gw_node(struct batadv_priv *bat_priv)

    Get currently selected gateway

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_get_selected_gw_node.return`:

Return
------

selected gateway (with increased refcnt), NULL on errors

.. _`batadv_gw_get_selected_orig`:

batadv_gw_get_selected_orig
===========================

.. c:function:: struct batadv_orig_node *batadv_gw_get_selected_orig(struct batadv_priv *bat_priv)

    Get originator of currently selected gateway

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_get_selected_orig.return`:

Return
------

orig_node of selected gateway (with increased refcnt), NULL on errors

.. _`batadv_gw_reselect`:

batadv_gw_reselect
==================

.. c:function:: void batadv_gw_reselect(struct batadv_priv *bat_priv)

    force a gateway reselection

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_reselect.description`:

Description
-----------

Set a flag to remind the GW component to perform a new gateway reselection.
However this function does not ensure that the current gateway is going to be
deselected. The reselection mechanism may elect the same gateway once again.

This means that invoking \ :c:func:`batadv_gw_reselect`\  does not guarantee a gateway
change and therefore a uevent is not necessarily expected.

.. _`batadv_gw_check_client_stop`:

batadv_gw_check_client_stop
===========================

.. c:function:: void batadv_gw_check_client_stop(struct batadv_priv *bat_priv)

    check if client mode has been switched off

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_check_client_stop.description`:

Description
-----------

This function assumes the caller has checked that the gw state \*is actually
changing\*. This function is not supposed to be called when there is no state
change.

.. _`batadv_gw_election`:

batadv_gw_election
==================

.. c:function:: void batadv_gw_election(struct batadv_priv *bat_priv)

    Elect the best gateway

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_check_election`:

batadv_gw_check_election
========================

.. c:function:: void batadv_gw_check_election(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    Elect orig node as best gateway when eligible

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig node which is to be checked

.. _`batadv_gw_node_add`:

batadv_gw_node_add
==================

.. c:function:: void batadv_gw_node_add(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_tvlv_gateway_data *gateway)

    add gateway node to list of available gateways

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        originator announcing gateway capabilities

    :param struct batadv_tvlv_gateway_data \*gateway:
        announced bandwidth information

.. _`batadv_gw_node_get`:

batadv_gw_node_get
==================

.. c:function:: struct batadv_gw_node *batadv_gw_node_get(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    retrieve gateway node from list of available gateways

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        originator announcing gateway capabilities

.. _`batadv_gw_node_get.return`:

Return
------

gateway node if found or NULL otherwise.

.. _`batadv_gw_node_update`:

batadv_gw_node_update
=====================

.. c:function:: void batadv_gw_node_update(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node, struct batadv_tvlv_gateway_data *gateway)

    update list of available gateways with changed bandwidth information

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        originator announcing gateway capabilities

    :param struct batadv_tvlv_gateway_data \*gateway:
        announced bandwidth information

.. _`batadv_gw_node_delete`:

batadv_gw_node_delete
=====================

.. c:function:: void batadv_gw_node_delete(struct batadv_priv *bat_priv, struct batadv_orig_node *orig_node)

    Remove orig_node from gateway list

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_orig_node \*orig_node:
        orig node which is currently in process of being removed

.. _`batadv_gw_node_free`:

batadv_gw_node_free
===================

.. c:function:: void batadv_gw_node_free(struct batadv_priv *bat_priv)

    Free gateway information from soft interface

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_gw_client_seq_print_text`:

batadv_gw_client_seq_print_text
===============================

.. c:function:: int batadv_gw_client_seq_print_text(struct seq_file *seq, void *offset)

    Print the gateway table in a seq file

    :param struct seq_file \*seq:
        seq file to print on

    :param void \*offset:
        not used

.. _`batadv_gw_client_seq_print_text.return`:

Return
------

always 0

.. _`batadv_gw_dump`:

batadv_gw_dump
==============

.. c:function:: int batadv_gw_dump(struct sk_buff *msg, struct netlink_callback *cb)

    Dump gateways into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param struct netlink_callback \*cb:
        Control block containing additional options

.. _`batadv_gw_dump.return`:

Return
------

Error code, or length of message

.. _`batadv_gw_dhcp_recipient_get`:

batadv_gw_dhcp_recipient_get
============================

.. c:function:: enum batadv_dhcp_recipient batadv_gw_dhcp_recipient_get(struct sk_buff *skb, unsigned int *header_len, u8 *chaddr)

    check if a packet is a DHCP message

    :param struct sk_buff \*skb:
        the packet to check

    :param unsigned int \*header_len:
        a pointer to the batman-adv header size

    :param u8 \*chaddr:
        buffer where the client address will be stored. Valid
        only if the function returns BATADV_DHCP_TO_CLIENT

.. _`batadv_gw_dhcp_recipient_get.description`:

Description
-----------

This function may re-allocate the data buffer of the skb passed as argument.

.. _`batadv_gw_dhcp_recipient_get.return`:

Return
------

- BATADV_DHCP_NO if the packet is not a dhcp message or if there was an error
while parsing it
- BATADV_DHCP_TO_SERVER if this is a message going to the DHCP server
- BATADV_DHCP_TO_CLIENT if this is a message going to a DHCP client

.. _`batadv_gw_out_of_range`:

batadv_gw_out_of_range
======================

.. c:function:: bool batadv_gw_out_of_range(struct batadv_priv *bat_priv, struct sk_buff *skb)

    check if the dhcp request destination is the best gateway

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the outgoing packet

.. _`batadv_gw_out_of_range.description`:

Description
-----------

Check if the skb is a DHCP request and if it is sent to the current best GW
server. Due to topology changes it may be the case that the GW server
previously selected is not the best one anymore.

This call might reallocate skb data.
Must be invoked only when the DHCP packet is going TO a DHCP SERVER.

.. _`batadv_gw_out_of_range.return`:

Return
------

true if the packet destination is unicast and it is not the best gw,
false otherwise.

.. This file was automatic generated / don't edit.

