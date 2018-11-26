.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_ipsec.c

.. _`ixgbe_ipsec_set_tx_sa`:

ixgbe_ipsec_set_tx_sa
=====================

.. c:function:: void ixgbe_ipsec_set_tx_sa(struct ixgbe_hw *hw, u16 idx, u32 key, u32 salt)

    set the Tx SA registers

    :param hw:
        hw specific details
    :type hw: struct ixgbe_hw \*

    :param idx:
        register index to write
    :type idx: u16

    :param key:
        key byte array
    :type key: u32

    :param salt:
        salt bytes
    :type salt: u32

.. _`ixgbe_ipsec_set_rx_item`:

ixgbe_ipsec_set_rx_item
=======================

.. c:function:: void ixgbe_ipsec_set_rx_item(struct ixgbe_hw *hw, u16 idx, enum ixgbe_ipsec_tbl_sel tbl)

    set an Rx table item

    :param hw:
        hw specific details
    :type hw: struct ixgbe_hw \*

    :param idx:
        register index to write
    :type idx: u16

    :param tbl:
        table selector
    :type tbl: enum ixgbe_ipsec_tbl_sel

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

    :param hw:
        hw specific details
    :type hw: struct ixgbe_hw \*

    :param idx:
        register index to write
    :type idx: u16

    :param spi:
        security parameter index
    :type spi: __be32

    :param key:
        key byte array
    :type key: u32

    :param salt:
        salt bytes
    :type salt: u32

    :param mode:
        rx decrypt control bits
    :type mode: u32

    :param ip_idx:
        index into IP table for related IP address
    :type ip_idx: u32

.. _`ixgbe_ipsec_set_rx_ip`:

ixgbe_ipsec_set_rx_ip
=====================

.. c:function:: void ixgbe_ipsec_set_rx_ip(struct ixgbe_hw *hw, u16 idx, __be32 addr)

    set up the register bits to save SA IP addr info

    :param hw:
        hw specific details
    :type hw: struct ixgbe_hw \*

    :param idx:
        register index to write
    :type idx: u16

    :param addr:
        IP address byte array
    :type addr: __be32

.. _`ixgbe_ipsec_clear_hw_tables`:

ixgbe_ipsec_clear_hw_tables
===========================

.. c:function:: void ixgbe_ipsec_clear_hw_tables(struct ixgbe_adapter *adapter)

    because some tables don't get cleared on reset

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ipsec_stop_data`:

ixgbe_ipsec_stop_data
=====================

.. c:function:: void ixgbe_ipsec_stop_data(struct ixgbe_adapter *adapter)

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ipsec_stop_engine`:

ixgbe_ipsec_stop_engine
=======================

.. c:function:: void ixgbe_ipsec_stop_engine(struct ixgbe_adapter *adapter)

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ipsec_start_engine`:

ixgbe_ipsec_start_engine
========================

.. c:function:: void ixgbe_ipsec_start_engine(struct ixgbe_adapter *adapter)

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ipsec_start_engine.note`:

NOTE
----

this increases power consumption whether being used or not

.. _`ixgbe_ipsec_restore`:

ixgbe_ipsec_restore
===================

.. c:function:: void ixgbe_ipsec_restore(struct ixgbe_adapter *adapter)

    restore the ipsec HW settings after a reset

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_ipsec_restore.description`:

Description
-----------

Reload the HW tables from the SW tables after they've been bashed
by a chip reset.

Any VF entries are removed from the SW and HW tables since either
(a) the VF also gets reset on PF reset and will ask again for the
offloads, or (b) the VF has been removed by a change in the num_vfs.

.. _`ixgbe_ipsec_find_empty_idx`:

ixgbe_ipsec_find_empty_idx
==========================

.. c:function:: int ixgbe_ipsec_find_empty_idx(struct ixgbe_ipsec *ipsec, bool rxtable)

    find the first unused security parameter index

    :param ipsec:
        pointer to ipsec struct
    :type ipsec: struct ixgbe_ipsec \*

    :param rxtable:
        true if we need to look in the Rx table
    :type rxtable: bool

.. _`ixgbe_ipsec_find_empty_idx.description`:

Description
-----------

Returns the first unused index in either the Rx or Tx SA table

.. _`ixgbe_ipsec_find_rx_state`:

ixgbe_ipsec_find_rx_state
=========================

.. c:function:: struct xfrm_state *ixgbe_ipsec_find_rx_state(struct ixgbe_ipsec *ipsec, __be32 *daddr, u8 proto, __be32 spi, bool ip4)

    find the state that matches

    :param ipsec:
        pointer to ipsec struct
    :type ipsec: struct ixgbe_ipsec \*

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
        true if using an ipv4 address
    :type ip4: bool

.. _`ixgbe_ipsec_find_rx_state.description`:

Description
-----------

Returns a pointer to the matching SA state information

.. _`ixgbe_ipsec_parse_proto_keys`:

ixgbe_ipsec_parse_proto_keys
============================

.. c:function:: int ixgbe_ipsec_parse_proto_keys(struct xfrm_state *xs, u32 *mykey, u32 *mysalt)

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

    :param xs:
        pointer to transformer state struct
    :type xs: struct xfrm_state \*

.. _`ixgbe_ipsec_add_sa`:

ixgbe_ipsec_add_sa
==================

.. c:function:: int ixgbe_ipsec_add_sa(struct xfrm_state *xs)

    program device with a security association

    :param xs:
        pointer to transformer state struct
    :type xs: struct xfrm_state \*

.. _`ixgbe_ipsec_del_sa`:

ixgbe_ipsec_del_sa
==================

.. c:function:: void ixgbe_ipsec_del_sa(struct xfrm_state *xs)

    clear out this specific SA

    :param xs:
        pointer to transformer state struct
    :type xs: struct xfrm_state \*

.. _`ixgbe_ipsec_offload_ok`:

ixgbe_ipsec_offload_ok
======================

.. c:function:: bool ixgbe_ipsec_offload_ok(struct sk_buff *skb, struct xfrm_state *xs)

    can this packet use the xfrm hw offload

    :param skb:
        current data packet
    :type skb: struct sk_buff \*

    :param xs:
        pointer to transformer state struct
    :type xs: struct xfrm_state \*

.. _`ixgbe_ipsec_vf_clear`:

ixgbe_ipsec_vf_clear
====================

.. c:function:: void ixgbe_ipsec_vf_clear(struct ixgbe_adapter *adapter, u32 vf)

    clear the tables of data for a VF

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

    :param vf:
        VF id to be removed
    :type vf: u32

.. _`ixgbe_ipsec_vf_add_sa`:

ixgbe_ipsec_vf_add_sa
=====================

.. c:function:: int ixgbe_ipsec_vf_add_sa(struct ixgbe_adapter *adapter, u32 *msgbuf, u32 vf)

    translate VF request to SA add

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

    :param msgbuf:
        The message buffer
    :type msgbuf: u32 \*

    :param vf:
        the VF index
    :type vf: u32

.. _`ixgbe_ipsec_vf_add_sa.description`:

Description
-----------

Make up a new xs and algorithm info from the data sent by the VF.
We only need to sketch in just enough to set up the HW offload.
Put the resulting offload_handle into the return message to the VF.

Returns 0 or error value

.. _`ixgbe_ipsec_vf_del_sa`:

ixgbe_ipsec_vf_del_sa
=====================

.. c:function:: int ixgbe_ipsec_vf_del_sa(struct ixgbe_adapter *adapter, u32 *msgbuf, u32 vf)

    translate VF request to SA delete

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

    :param msgbuf:
        The message buffer
    :type msgbuf: u32 \*

    :param vf:
        the VF index
    :type vf: u32

.. _`ixgbe_ipsec_vf_del_sa.description`:

Description
-----------

Given the offload_handle sent by the VF, look for the related SA table
entry and use its xs field to call for a delete of the SA.

.. _`ixgbe_ipsec_vf_del_sa.note`:

Note
----

We silently ignore requests to delete entries that are already
set to unused because when a VF is set to "DOWN", the PF first
gets a reset and clears all the VF's entries; then the VF's
XFRM stack sends individual deletes for each entry, which the
reset already removed.  In the future it might be good to try to
optimize this so not so many unnecessary delete messages are sent.

Returns 0 or error value

.. _`ixgbe_ipsec_tx`:

ixgbe_ipsec_tx
==============

.. c:function:: int ixgbe_ipsec_tx(struct ixgbe_ring *tx_ring, struct ixgbe_tx_buffer *first, struct ixgbe_ipsec_tx_data *itd)

    setup Tx flags for ipsec offload

    :param tx_ring:
        outgoing context
    :type tx_ring: struct ixgbe_ring \*

    :param first:
        current data packet
    :type first: struct ixgbe_tx_buffer \*

    :param itd:
        ipsec Tx data for later use in building context descriptor
    :type itd: struct ixgbe_ipsec_tx_data \*

.. _`ixgbe_ipsec_rx`:

ixgbe_ipsec_rx
==============

.. c:function:: void ixgbe_ipsec_rx(struct ixgbe_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    decode ipsec bits from Rx descriptor

    :param rx_ring:
        receiving ring
    :type rx_ring: struct ixgbe_ring \*

    :param rx_desc:
        receive data descriptor
    :type rx_desc: union ixgbe_adv_rx_desc \*

    :param skb:
        current data packet
    :type skb: struct sk_buff \*

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

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_stop_ipsec_offload`:

ixgbe_stop_ipsec_offload
========================

.. c:function:: void ixgbe_stop_ipsec_offload(struct ixgbe_adapter *adapter)

    tear down the ipsec offload

    :param adapter:
        board private structure
    :type adapter: struct ixgbe_adapter \*

.. This file was automatic generated / don't edit.

