.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/main.c

.. _`batadv_mesh_init`:

batadv_mesh_init
================

.. c:function:: int batadv_mesh_init(struct net_device *soft_iface)

    Initialize soft interface

    :param soft_iface:
        netdev struct of the soft interface
    :type soft_iface: struct net_device \*

.. _`batadv_mesh_init.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_mesh_free`:

batadv_mesh_free
================

.. c:function:: void batadv_mesh_free(struct net_device *soft_iface)

    Deinitialize soft interface

    :param soft_iface:
        netdev struct of the soft interface
    :type soft_iface: struct net_device \*

.. _`batadv_is_my_mac`:

batadv_is_my_mac
================

.. c:function:: bool batadv_is_my_mac(struct batadv_priv *bat_priv, const u8 *addr)

    check if the given mac address belongs to any of the real interfaces in the current mesh

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param addr:
        the address to check
    :type addr: const u8 \*

.. _`batadv_is_my_mac.return`:

Return
------

'true' if the mac address was found, false otherwise.

.. _`batadv_seq_print_text_primary_if_get`:

batadv_seq_print_text_primary_if_get
====================================

.. c:function:: struct batadv_hard_iface *batadv_seq_print_text_primary_if_get(struct seq_file *seq)

    called from debugfs table printing function that requires the primary interface

    :param seq:
        debugfs table seq_file struct
    :type seq: struct seq_file \*

.. _`batadv_seq_print_text_primary_if_get.return`:

Return
------

primary interface if found or NULL otherwise.

.. _`batadv_max_header_len`:

batadv_max_header_len
=====================

.. c:function:: int batadv_max_header_len( void)

    calculate maximum encapsulation overhead for a payload packet

    :param void:
        no arguments
    :type void: 

.. _`batadv_max_header_len.return`:

Return
------

the maximum encapsulation overhead in bytes.

.. _`batadv_skb_set_priority`:

batadv_skb_set_priority
=======================

.. c:function:: void batadv_skb_set_priority(struct sk_buff *skb, int offset)

    sets skb priority according to packet content

    :param skb:
        the packet to be sent
    :type skb: struct sk_buff \*

    :param offset:
        offset to the packet content
    :type offset: int

.. _`batadv_skb_set_priority.description`:

Description
-----------

This function sets a value between 256 and 263 (802.1d priority), which
can be interpreted by the cfg80211 or other drivers.

.. _`batadv_batman_skb_recv`:

batadv_batman_skb_recv
======================

.. c:function:: int batadv_batman_skb_recv(struct sk_buff *skb, struct net_device *dev, struct packet_type *ptype, struct net_device *orig_dev)

    Handle incoming message from an hard interface

    :param skb:
        the received packet
    :type skb: struct sk_buff \*

    :param dev:
        the net device that the packet was received on
    :type dev: struct net_device \*

    :param ptype:
        packet type of incoming packet (ETH_P_BATMAN)
    :type ptype: struct packet_type \*

    :param orig_dev:
        the original receive net device (e.g. bonded device)
    :type orig_dev: struct net_device \*

.. _`batadv_batman_skb_recv.return`:

Return
------

NET_RX_SUCCESS on success or NET_RX_DROP in case of failure

.. _`batadv_recv_handler_register`:

batadv_recv_handler_register
============================

.. c:function:: int batadv_recv_handler_register(u8 packet_type, int (*recv_handler)(struct sk_buff *, struct batadv_hard_iface *))

    Register handler for batman-adv packet type

    :param packet_type:
        batadv_packettype which should be handled
    :type packet_type: u8

    :param int (\*recv_handler)(struct sk_buff \*, struct batadv_hard_iface \*):
        receive handler for the packet type

.. _`batadv_recv_handler_register.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_recv_handler_unregister`:

batadv_recv_handler_unregister
==============================

.. c:function:: void batadv_recv_handler_unregister(u8 packet_type)

    Unregister handler for packet type

    :param packet_type:
        batadv_packettype which should no longer be handled
    :type packet_type: u8

.. _`batadv_skb_crc32`:

batadv_skb_crc32
================

.. c:function:: __be32 batadv_skb_crc32(struct sk_buff *skb, u8 *payload_ptr)

    calculate CRC32 of the whole packet and skip bytes in the header

    :param skb:
        skb pointing to fragmented socket buffers
    :type skb: struct sk_buff \*

    :param payload_ptr:
        Pointer to position inside the head buffer of the skb
        marking the start of the data to be CRC'ed
    :type payload_ptr: u8 \*

.. _`batadv_skb_crc32.description`:

Description
-----------

payload_ptr must always point to an address in the skb head buffer and not to
a fragment.

.. _`batadv_skb_crc32.return`:

Return
------

big endian crc32c of the checksummed data

.. _`batadv_get_vid`:

batadv_get_vid
==============

.. c:function:: unsigned short batadv_get_vid(struct sk_buff *skb, size_t header_len)

    extract the VLAN identifier from skb if any

    :param skb:
        the buffer containing the packet
    :type skb: struct sk_buff \*

    :param header_len:
        length of the batman header preceding the ethernet header
    :type header_len: size_t

.. _`batadv_get_vid.return`:

Return
------

VID with the BATADV_VLAN_HAS_TAG flag when the packet embedded in the
skb is vlan tagged. Otherwise BATADV_NO_FLAGS.

.. _`batadv_vlan_ap_isola_get`:

batadv_vlan_ap_isola_get
========================

.. c:function:: bool batadv_vlan_ap_isola_get(struct batadv_priv *bat_priv, unsigned short vid)

    return AP isolation status for the given vlan

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vid:
        the VLAN identifier for which the AP isolation attributed as to be
        looked up
    :type vid: unsigned short

.. _`batadv_vlan_ap_isola_get.return`:

Return
------

true if AP isolation is on for the VLAN idenfied by vid, false
otherwise

.. This file was automatic generated / don't edit.

