.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bitarray.h

.. _`batadv_test_bit`:

batadv_test_bit
===============

.. c:function:: bool batadv_test_bit(const unsigned long *seq_bits, u32 last_seqno, u32 curr_seqno)

    check if bit is set in the current window

    :param const unsigned long \*seq_bits:
        pointer to the sequence number receive packet

    :param u32 last_seqno:
        latest sequence number in seq_bits

    :param u32 curr_seqno:
        sequence number to test for

.. _`batadv_test_bit.return`:

Return
------

true if the corresponding bit in the given seq_bits indicates true
and curr_seqno is within range of last_seqno. Otherwise returns false.

.. _`batadv_set_bit`:

batadv_set_bit
==============

.. c:function:: void batadv_set_bit(unsigned long *seq_bits, s32 n)

    Turn corresponding bit on, so we can remember that we got the packet

    :param unsigned long \*seq_bits:
        bitmap of the packet receive window

    :param s32 n:
        relative sequence number of newly received packet

.. This file was automatic generated / don't edit.

