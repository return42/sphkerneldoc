.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_ipsec.c

.. _`ixgbe_ipsec_set_tx_sa`:

ixgbe_ipsec_set_tx_sa
=====================

.. c:function:: void ixgbe_ipsec_set_tx_sa(struct ixgbe_hw *hw, u16 idx, u32 key, u32 salt)

    set the Tx SA registers

    :param struct ixgbe_hw \*hw:
        hw specific details

    :param u16 idx:
        register index to write

    :param u32 key:
        key byte array

    :param u32 salt:
        salt bytes

.. _`ixgbe_ipsec_set_rx_item`:

ixgbe_ipsec_set_rx_item
=======================

.. c:function:: void ixgbe_ipsec_set_rx_item(struct ixgbe_hw *hw, u16 idx, enum ixgbe_ipsec_tbl_sel tbl)

    set an Rx table item

    :param struct ixgbe_hw \*hw:
        hw specific details

    :param u16 idx:
        register index to write

    :param enum ixgbe_ipsec_tbl_sel tbl:
        table selector

.. _`ixgbe_ipsec_set_rx_item.description`:

Description
-----------

Trigger the device to store into a particular Rx table the
data that has already been loaded into the input register

.. _`ixgbe_ipsec_set_rx_sa`:

ixgbe_ipsec_set_rx_sa
=====================

.. c:function:: void ixgbe_ipsec_set_rx_sa(struct ixgbe_hw *hw, u16 idx, __be32 spi, u32 key, u32 salt, u32 mode, u32 ip_idx)

    set up the register bits to save SA info

    :param struct ixgbe_hw \*hw:
        hw specific details

    :param u16 idx:
        register index to write

    :param __be32 spi:
        security parameter index

    :param u32 key:
        key byte array

    :param u32 salt:
        salt bytes

    :param u32 mode:
        rx decrypt control bits

    :param u32 ip_idx:
        index into IP table for related IP address

.. _`ixgbe_ipsec_set_rx_ip`:

ixgbe_ipsec_set_rx_ip
=====================

.. c:function:: void ixgbe_ipsec_set_rx_ip(struct ixgbe_hw *hw, u16 idx, __be32 addr)

    set up the register bits to save SA IP addr info

    :param struct ixgbe_hw \*hw:
        hw specific details

    :param u16 idx:
        register index to write

    :param __be32 addr:
        IP address byte array

.. _`ixgbe_ipsec_clear_hw_tables`:

ixgbe_ipsec_clear_hw_tables
===========================

.. c:function:: void ixgbe_ipsec_clear_hw_tables(struct ixgbe_adapter *adapter)

    because some tables don't get cleared on reset

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_ipsec_stop_data`:

ixgbe_ipsec_stop_data
=====================

.. c:function:: void ixgbe_ipsec_stop_data(struct ixgbe_adapter *adapter)

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_ipsec_stop_engine`:

ixgbe_ipsec_stop_engine
=======================

.. c:function:: void ixgbe_ipsec_stop_engine(struct ixgbe_adapter *adapter)

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_ipsec_start_engine`:

ixgbe_ipsec_start_engine
========================

.. c:function:: void ixgbe_ipsec_start_engine(struct ixgbe_adapter *adapter)

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_ipsec_start_engine.note`:

NOTE
----

this increases power consumption whether being used or not

.. _`ixgbe_ipsec_restore`:

ixgbe_ipsec_restore
===================

.. c:function:: void ixgbe_ipsec_restore(struct ixgbe_adapter *adapter)

    restore the ipsec HW settings after a reset

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_ipsec_find_empty_idx`:

ixgbe_ipsec_find_empty_idx
==========================

.. c:function:: int ixgbe_ipsec_find_empty_idx(struct ixgbe_ipsec *ipsec, bool rxtable)

    find the first unused security parameter index

    :param struct ixgbe_ipsec \*ipsec:
        pointer to ipsec struct

    :param bool rxtable:
        true if we need to look in the Rx table

.. _`ixgbe_ipsec_find_empty_idx.description`:

Description
-----------

Returns the first unused index in either the Rx or Tx SA table

.. _`ixgbe_ipsec_find_rx_state`:

ixgbe_ipsec_find_rx_state
=========================

.. c:function:: struct xfrm_state *ixgbe_ipsec_find_rx_state(struct ixgbe_ipsec *ipsec, __be32 *daddr, u8 proto, __be32 spi, bool ip4)

    find the state that matches

    :param struct ixgbe_ipsec \*ipsec:
        pointer to ipsec struct

    :param __be32 \*daddr:
        inbound address to match

    :param u8 proto:
        protocol to match

    :param __be32 spi:
        SPI to match

    :param bool ip4:
        true if using an ipv4 address

.. _`ixgbe_ipsec_find_rx_state.description`:

Description
-----------

Returns a pointer to the matching SA state information

.. _`ixgbe_ipsec_parse_proto_keys`:

ixgbe_ipsec_parse_proto_keys
============================

.. c:function:: int ixgbe_ipsec_parse_proto_keys(struct xfrm_state *xs, u32 *mykey, u32 *mysalt)

    find the key and salt based on the protocol

    :param struct xfrm_state \*xs:
        pointer to xfrm_state struct

    :param u32 \*mykey:
        pointer to key array to populate

    :param u32 \*mysalt:
        pointer to salt value to populate

.. _`ixgbe_ipsec_parse_proto_keys.description`:

Description
-----------

This copies the protocol keys and salt to our own data tables.  The
82599 family only supports the one algorithm.

.. _`ixgbe_ipsec_check_mgmt_ip`:

ixgbe_ipsec_check_mgmt_ip
=========================

.. c:function:: int ixgbe_ipsec_check_mgmt_ip(struct xfrm_state *xs)

    make sure there is no clash with mgmt IP filters

    :param struct xfrm_state \*xs:
        pointer to transformer state struct

.. _`ixgbe_ipsec_add_sa`:

ixgbe_ipsec_add_sa
==================

.. c:function:: int ixgbe_ipsec_add_sa(struct xfrm_state *xs)

    program device with a security association

    :param struct xfrm_state \*xs:
        pointer to transformer state struct

.. _`ixgbe_ipsec_del_sa`:

ixgbe_ipsec_del_sa
==================

.. c:function:: void ixgbe_ipsec_del_sa(struct xfrm_state *xs)

    clear out this specific SA

    :param struct xfrm_state \*xs:
        pointer to transformer state struct

.. _`ixgbe_ipsec_offload_ok`:

ixgbe_ipsec_offload_ok
======================

.. c:function:: bool ixgbe_ipsec_offload_ok(struct sk_buff *skb, struct xfrm_state *xs)

    can this packet use the xfrm hw offload

    :param struct sk_buff \*skb:
        current data packet

    :param struct xfrm_state \*xs:
        pointer to transformer state struct

.. _`ixgbe_ipsec_tx`:

ixgbe_ipsec_tx
==============

.. c:function:: int ixgbe_ipsec_tx(struct ixgbe_ring *tx_ring, struct ixgbe_tx_buffer *first, struct ixgbe_ipsec_tx_data *itd)

    setup Tx flags for ipsec offload

    :param struct ixgbe_ring \*tx_ring:
        outgoing context

    :param struct ixgbe_tx_buffer \*first:
        current data packet

    :param struct ixgbe_ipsec_tx_data \*itd:
        ipsec Tx data for later use in building context descriptor

.. _`ixgbe_ipsec_rx`:

ixgbe_ipsec_rx
==============

.. c:function:: void ixgbe_ipsec_rx(struct ixgbe_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    decode ipsec bits from Rx descriptor

    :param struct ixgbe_ring \*rx_ring:
        receiving ring

    :param union ixgbe_adv_rx_desc \*rx_desc:
        receive data descriptor

    :param struct sk_buff \*skb:
        current data packet

.. _`ixgbe_ipsec_rx.description`:

Description
-----------

Determine if there was an ipsec encapsulation noticed, and if so set up
the resulting status for later in the receive stack.

.. _`ixgbe_init_ipsec_offload`:

ixgbe_init_ipsec_offload
========================

.. c:function:: void ixgbe_init_ipsec_offload(struct ixgbe_adapter *adapter)

    initialize security registers for IPSec operation

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_stop_ipsec_offload`:

ixgbe_stop_ipsec_offload
========================

.. c:function:: void ixgbe_stop_ipsec_offload(struct ixgbe_adapter *adapter)

    tear down the ipsec offload

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. This file was automatic generated / don't edit.

