.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/tx_tso.c

.. _`tso_state`:

struct tso_state
================

.. c:type:: struct tso_state

    TSO state for an SKB

.. _`tso_state.definition`:

Definition
----------

.. code-block:: c

    struct tso_state {
        unsigned int out_len;
        unsigned int seqnum;
        u16 ipv4_id;
        unsigned int packet_space;
        dma_addr_t dma_addr;
        unsigned int in_len;
        unsigned int unmap_len;
        dma_addr_t unmap_addr;
        __be16 protocol;
        unsigned int ip_off;
        unsigned int tcp_off;
        unsigned int header_len;
        unsigned int ip_base_len;
        dma_addr_t header_dma_addr;
        unsigned int header_unmap_len;
    }

.. _`tso_state.members`:

Members
-------

out_len
    Remaining length in current segment

seqnum
    Current sequence number

ipv4_id
    Current IPv4 ID, host endian

packet_space
    Remaining space in current packet

dma_addr
    DMA address of current position

in_len
    Remaining length in current SKB fragment

unmap_len
    Length of SKB fragment

unmap_addr
    DMA address of SKB fragment

protocol
    Network protocol (after any VLAN header)

ip_off
    Offset of IP header

tcp_off
    Offset of TCP header

header_len
    Number of bytes of header

ip_base_len
    IPv4 tot_len or IPv6 payload_len, before TCP payload

header_dma_addr
    Header DMA address

header_unmap_len
    Header DMA mapped length

.. _`tso_state.description`:

Description
-----------

The state used during segmentation.  It is put into this data structure
just to make it easy to pass into inline functions.

.. _`efx_tx_queue_insert`:

efx_tx_queue_insert
===================

.. c:function:: void efx_tx_queue_insert(struct efx_tx_queue *tx_queue, dma_addr_t dma_addr, unsigned int len, struct efx_tx_buffer **final_buffer)

    push descriptors onto the TX queue

    :param struct efx_tx_queue \*tx_queue:
        Efx TX queue

    :param dma_addr_t dma_addr:
        DMA address of fragment

    :param unsigned int len:
        Length of fragment

    :param struct efx_tx_buffer \*\*final_buffer:
        The final buffer inserted into the queue

.. _`efx_tx_queue_insert.description`:

Description
-----------

Push descriptors onto the TX queue.

.. _`tso_fill_packet_with_fragment`:

tso_fill_packet_with_fragment
=============================

.. c:function:: void tso_fill_packet_with_fragment(struct efx_tx_queue *tx_queue, const struct sk_buff *skb, struct tso_state *st)

    form descriptors for the current fragment

    :param struct efx_tx_queue \*tx_queue:
        Efx TX queue

    :param const struct sk_buff \*skb:
        Socket buffer

    :param struct tso_state \*st:
        TSO state

.. _`tso_fill_packet_with_fragment.description`:

Description
-----------

Form descriptors for the current fragment, until we reach the end
of fragment or end-of-packet.

.. _`tso_start_new_packet`:

tso_start_new_packet
====================

.. c:function:: int tso_start_new_packet(struct efx_tx_queue *tx_queue, const struct sk_buff *skb, struct tso_state *st)

    generate a new header and prepare for the new packet

    :param struct efx_tx_queue \*tx_queue:
        Efx TX queue

    :param const struct sk_buff \*skb:
        Socket buffer

    :param struct tso_state \*st:
        TSO state

.. _`tso_start_new_packet.description`:

Description
-----------

Generate a new header and prepare for the new packet.  Return 0 on
success, or -%ENOMEM if failed to alloc header, or other negative error.

.. _`efx_enqueue_skb_tso`:

efx_enqueue_skb_tso
===================

.. c:function:: int efx_enqueue_skb_tso(struct efx_tx_queue *tx_queue, struct sk_buff *skb, bool *data_mapped)

    segment and transmit a TSO socket buffer

    :param struct efx_tx_queue \*tx_queue:
        Efx TX queue

    :param struct sk_buff \*skb:
        Socket buffer

    :param bool \*data_mapped:
        Did we map the data? Always set to true
        by this on success.

.. _`efx_enqueue_skb_tso.context`:

Context
-------

You must hold \ :c:func:`netif_tx_lock`\  to call this function.

.. _`efx_enqueue_skb_tso.description`:

Description
-----------

Add socket buffer \ ``skb``\  to \ ``tx_queue``\ , doing TSO or return != 0 if
\ ``skb``\  was not enqueued.  \ ``skb``\  is consumed unless return value is
\ ``EINVAL``\ .

.. This file was automatic generated / don't edit.

