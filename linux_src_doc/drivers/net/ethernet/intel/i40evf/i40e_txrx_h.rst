.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40evf/i40e_txrx.h

.. _`i40e_test_staterr`:

i40e_test_staterr
=================

.. c:function:: bool i40e_test_staterr(union i40e_rx_desc *rx_desc, const u64 stat_err_bits)

    tests bits in Rx descriptor status and error fields

    :param union i40e_rx_desc \*rx_desc:
        pointer to receive descriptor (in le64 format)

    :param const u64 stat_err_bits:
        value to mask

.. _`i40e_test_staterr.description`:

Description
-----------

This function does some fast chicanery in order to return the
value of the mask which is really only used for boolean tests.
The status_error_len doesn't need to be shifted because it begins
at offset zero.

.. _`i40e_get_head`:

i40e_get_head
=============

.. c:function:: u32 i40e_get_head(struct i40e_ring *tx_ring)

    Retrieve head from head writeback

    :param struct i40e_ring \*tx_ring:
        Tx ring to fetch head of

.. _`i40e_get_head.description`:

Description
-----------

Returns value of Tx ring head based on value stored
in head write-back location

.. _`i40e_xmit_descriptor_count`:

i40e_xmit_descriptor_count
==========================

.. c:function:: int i40e_xmit_descriptor_count(struct sk_buff *skb)

    calculate number of Tx descriptors needed

    :param struct sk_buff \*skb:
        send buffer

.. _`i40e_xmit_descriptor_count.description`:

Description
-----------

Returns number of data descriptors needed for this skb. Returns 0 to indicate
there is not enough descriptors available in this ring since we need at least
one descriptor.

.. _`i40e_maybe_stop_tx`:

i40e_maybe_stop_tx
==================

.. c:function:: int i40e_maybe_stop_tx(struct i40e_ring *tx_ring, int size)

    1st level check for Tx stop conditions

    :param struct i40e_ring \*tx_ring:
        the ring to be checked

    :param int size:
        the size buffer we want to assure is available

.. _`i40e_maybe_stop_tx.description`:

Description
-----------

Returns 0 if stop is not needed

.. _`i40e_chk_linearize`:

i40e_chk_linearize
==================

.. c:function:: bool i40e_chk_linearize(struct sk_buff *skb, int count)

    Check if there are more than 8 fragments per packet

    :param struct sk_buff \*skb:
        send buffer

    :param int count:
        number of buffers used

.. _`i40e_chk_linearize.note`:

Note
----

Our HW can't scatter-gather more than 8 fragments to build
a packet on the wire and so we need to figure out the cases where we
need to linearize the skb.

.. _`i40e_rx_is_fcoe`:

i40e_rx_is_fcoe
===============

.. c:function:: bool i40e_rx_is_fcoe(u16 ptype)

    returns true if the Rx packet type is FCoE

    :param u16 ptype:
        the packet type field from Rx descriptor write-back

.. _`txring_txq`:

txring_txq
==========

.. c:function:: struct netdev_queue *txring_txq(const struct i40e_ring *ring)

    Find the netdev Tx ring based on the i40e Tx ring

    :param const struct i40e_ring \*ring:
        Tx ring to find the netdev equivalent of

.. This file was automatic generated / don't edit.

