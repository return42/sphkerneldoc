.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbevf/ipsec.c

.. _`ixgbevf_ipsec_set_pf_sa`:

ixgbevf_ipsec_set_pf_sa
=======================

.. c:function:: int ixgbevf_ipsec_set_pf_sa(struct ixgbevf_adapter *adapter, struct xfrm_state *xs)

    ask the PF to set up an SA

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

    :param xs:
        xfrm info to be sent to the PF
    :type xs: struct xfrm_state \*

.. _`ixgbevf_ipsec_set_pf_sa.return`:

Return
------

positive offload handle from the PF, or negative error code

.. _`ixgbevf_ipsec_del_pf_sa`:

ixgbevf_ipsec_del_pf_sa
=======================

.. c:function:: int ixgbevf_ipsec_del_pf_sa(struct ixgbevf_adapter *adapter, int pfsa)

    ask the PF to delete an SA

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

    :param pfsa:
        sa index returned from PF when created, -1 for all
    :type pfsa: int

.. _`ixgbevf_ipsec_del_pf_sa.return`:

Return
------

0 on success, or negative error code

.. _`ixgbevf_ipsec_restore`:

ixgbevf_ipsec_restore
=====================

.. c:function:: void ixgbevf_ipsec_restore(struct ixgbevf_adapter *adapter)

    restore the IPsec HW settings after a reset

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_ipsec_restore.description`:

Description
-----------

Reload the HW tables from the SW tables after they've been bashed
by a chip reset.  While we're here, make sure any stale VF data is
removed, since we go through reset when num_vfs changes.

.. _`ixgbevf_ipsec_find_empty_idx`:

ixgbevf_ipsec_find_empty_idx
============================

.. c:function:: int ixgbevf_ipsec_find_empty_idx(struct ixgbevf_ipsec *ipsec, bool rxtable)

    find the first unused security parameter index

    :param ipsec:
        pointer to IPsec struct
    :type ipsec: struct ixgbevf_ipsec \*

    :param rxtable:
        true if we need to look in the Rx table
    :type rxtable: bool

.. _`ixgbevf_ipsec_find_empty_idx.description`:

Description
-----------

Returns the first unused index in either the Rx or Tx SA table

.. _`ixgbevf_ipsec_find_rx_state`:

ixgbevf_ipsec_find_rx_state
===========================

.. c:function:: struct xfrm_state *ixgbevf_ipsec_find_rx_state(struct ixgbevf_ipsec *ipsec, __be32 *daddr, u8 proto, __be32 spi, bool ip4)

    find the state that matches

    :param ipsec:
        pointer to IPsec struct
    :type ipsec: struct ixgbevf_ipsec \*

    :param daddr:
        inbound address to match
    :type daddr: __be32 \*

    :param proto:
        protocol to match
    :type proto: u8

    :param spi:
        SPI to match
    :type spi: __be32

    :param ip4:
        true if using an IPv4 address
    :type ip4: bool

.. _`ixgbevf_ipsec_find_rx_state.description`:

Description
-----------

Returns a pointer to the matching SA state information

.. _`ixgbevf_ipsec_parse_proto_keys`:

ixgbevf_ipsec_parse_proto_keys
==============================

.. c:function:: int ixgbevf_ipsec_parse_proto_keys(struct xfrm_state *xs, u32 *mykey, u32 *mysalt)

    find the key and salt based on the protocol

    :param xs:
        pointer to xfrm_state struct
    :type xs: struct xfrm_state \*

    :param mykey:
        pointer to key array to populate
    :type mykey: u32 \*

    :param mysalt:
        pointer to salt value to populate
    :type mysalt: u32 \*

.. _`ixgbevf_ipsec_parse_proto_keys.description`:

Description
-----------

This copies the protocol keys and salt to our own data tables.  The
82599 family only supports the one algorithm.

.. _`ixgbevf_ipsec_add_sa`:

ixgbevf_ipsec_add_sa
====================

.. c:function:: int ixgbevf_ipsec_add_sa(struct xfrm_state *xs)

    program device with a security association

    :param xs:
        pointer to transformer state struct
    :type xs: struct xfrm_state \*

.. _`ixgbevf_ipsec_del_sa`:

ixgbevf_ipsec_del_sa
====================

.. c:function:: void ixgbevf_ipsec_del_sa(struct xfrm_state *xs)

    clear out this specific SA

    :param xs:
        pointer to transformer state struct
    :type xs: struct xfrm_state \*

.. _`ixgbevf_ipsec_offload_ok`:

ixgbevf_ipsec_offload_ok
========================

.. c:function:: bool ixgbevf_ipsec_offload_ok(struct sk_buff *skb, struct xfrm_state *xs)

    can this packet use the xfrm hw offload

    :param skb:
        current data packet
    :type skb: struct sk_buff \*

    :param xs:
        pointer to transformer state struct
    :type xs: struct xfrm_state \*

.. _`ixgbevf_ipsec_tx`:

ixgbevf_ipsec_tx
================

.. c:function:: int ixgbevf_ipsec_tx(struct ixgbevf_ring *tx_ring, struct ixgbevf_tx_buffer *first, struct ixgbevf_ipsec_tx_data *itd)

    setup Tx flags for IPsec offload

    :param tx_ring:
        outgoing context
    :type tx_ring: struct ixgbevf_ring \*

    :param first:
        current data packet
    :type first: struct ixgbevf_tx_buffer \*

    :param itd:
        ipsec Tx data for later use in building context descriptor
    :type itd: struct ixgbevf_ipsec_tx_data \*

.. _`ixgbevf_ipsec_rx`:

ixgbevf_ipsec_rx
================

.. c:function:: void ixgbevf_ipsec_rx(struct ixgbevf_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    decode IPsec bits from Rx descriptor

    :param rx_ring:
        receiving ring
    :type rx_ring: struct ixgbevf_ring \*

    :param rx_desc:
        receive data descriptor
    :type rx_desc: union ixgbe_adv_rx_desc \*

    :param skb:
        current data packet
    :type skb: struct sk_buff \*

.. _`ixgbevf_ipsec_rx.description`:

Description
-----------

Determine if there was an IPsec encapsulation noticed, and if so set up
the resulting status for later in the receive stack.

.. _`ixgbevf_init_ipsec_offload`:

ixgbevf_init_ipsec_offload
==========================

.. c:function:: void ixgbevf_init_ipsec_offload(struct ixgbevf_adapter *adapter)

    initialize registers for IPsec operation

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_stop_ipsec_offload`:

ixgbevf_stop_ipsec_offload
==========================

.. c:function:: void ixgbevf_stop_ipsec_offload(struct ixgbevf_adapter *adapter)

    tear down the IPsec offload

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. This file was automatic generated / don't edit.

