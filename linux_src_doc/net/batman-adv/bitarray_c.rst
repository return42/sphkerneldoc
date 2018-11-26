.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bitarray.c

.. _`batadv_bit_get_packet`:

batadv_bit_get_packet
=====================

.. c:function:: bool batadv_bit_get_packet(void *priv, unsigned long *seq_bits, s32 seq_num_diff, int set_mark)

    receive and process one packet within the sequence number window

    :param priv:
        the bat priv with all the soft interface information
    :type priv: void \*

    :param seq_bits:
        pointer to the sequence number receive packet
    :type seq_bits: unsigned long \*

    :param seq_num_diff:
        difference between the current/received sequence number and
        the last sequence number
    :type seq_num_diff: s32

    :param set_mark:
        whether this packet should be marked in seq_bits
    :type set_mark: int

.. _`batadv_bit_get_packet.return`:

Return
------

true if the window was moved (either new or very old),
false if the window was not moved/shifted.

.. This file was automatic generated / don't edit.

