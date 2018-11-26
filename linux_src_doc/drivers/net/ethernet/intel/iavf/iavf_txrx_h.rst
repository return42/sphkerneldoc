.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/iavf/iavf_txrx.h

.. _`iavf_test_staterr`:

iavf_test_staterr
=================

.. c:function:: bool iavf_test_staterr(union iavf_rx_desc *rx_desc, const u64 stat_err_bits)

    tests bits in Rx descriptor status and error fields

    :param rx_desc:
        pointer to receive descriptor (in le64 format)
    :type rx_desc: union iavf_rx_desc \*

    :param stat_err_bits:
        value to mask
    :type stat_err_bits: const u64

.. _`iavf_test_staterr.description`:

Description
-----------

This function does some fast chicanery in order to return the
value of the mask which is really only used for boolean tests.
The status_error_len doesn't need to be shifted because it begins
at offset zero.

.. _`iavf_txd_use_count`:

iavf_txd_use_count
==================

.. c:function:: unsigned int iavf_txd_use_count(unsigned int size)

    estimate the number of descriptors needed for Tx

    :param size:
        transmit request size in bytes
    :type size: unsigned int

.. _`iavf_txd_use_count.description`:

Description
-----------

Due to hardware alignment restrictions (4K alignment), we need to
assume that we can have no more than 12K of data per descriptor, even
though each descriptor can take up to 16K - 1 bytes of aligned memory.
Thus, we need to divide by 12K. But division is slow! Instead,
we decompose the operation into shifts and one relatively cheap
multiply operation.

To divide by 12K, we first divide by 4K, then divide by 3:
To divide by 4K, shift right by 12 bits
To divide by 3, multiply by 85, then divide by 256
(Divide by 256 is done by shifting right by 8 bits)
Finally, we add one to round up. Because 256 isn't an exact multiple of
3, we'll underestimate near each multiple of 12K. This is actually more
accurate as we have 4K - 1 of wiggle room that we can fit into the last
segment.  For our purposes this is accurate out to 1M which is orders of
magnitude greater than our largest possible GSO size.

.. _`iavf_txd_use_count.this-would-then-be-implemented-as`:

This would then be implemented as
---------------------------------

return (((size >> 12) \* 85) >> 8) + 1;

Since multiplication and division are commutative, we can reorder

.. _`iavf_txd_use_count.operations-into`:

operations into
---------------

return ((size \* 85) >> 20) + 1;

.. _`iavf_xmit_descriptor_count`:

iavf_xmit_descriptor_count
==========================

.. c:function:: int iavf_xmit_descriptor_count(struct sk_buff *skb)

    calculate number of Tx descriptors needed

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

.. _`iavf_xmit_descriptor_count.description`:

Description
-----------

Returns number of data descriptors needed for this skb. Returns 0 to indicate
there is not enough descriptors available in this ring since we need at least
one descriptor.

.. _`iavf_maybe_stop_tx`:

iavf_maybe_stop_tx
==================

.. c:function:: int iavf_maybe_stop_tx(struct iavf_ring *tx_ring, int size)

    1st level check for Tx stop conditions

    :param tx_ring:
        the ring to be checked
    :type tx_ring: struct iavf_ring \*

    :param size:
        the size buffer we want to assure is available
    :type size: int

.. _`iavf_maybe_stop_tx.description`:

Description
-----------

Returns 0 if stop is not needed

.. _`iavf_chk_linearize`:

iavf_chk_linearize
==================

.. c:function:: bool iavf_chk_linearize(struct sk_buff *skb, int count)

    Check if there are more than 8 fragments per packet

    :param skb:
        send buffer
    :type skb: struct sk_buff \*

    :param count:
        number of buffers used
    :type count: int

.. _`iavf_chk_linearize.note`:

Note
----

Our HW can't scatter-gather more than 8 fragments to build
a packet on the wire and so we need to figure out the cases where we
need to linearize the skb.

.. This file was automatic generated / don't edit.

