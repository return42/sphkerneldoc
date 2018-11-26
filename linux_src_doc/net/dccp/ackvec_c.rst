.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ackvec.c

.. _`dccp_ackvec_update_records`:

dccp_ackvec_update_records
==========================

.. c:function:: int dccp_ackvec_update_records(struct dccp_ackvec *av, u64 seqno, u8 nonce_sum)

    Record information about sent Ack Vectors

    :param av:
        Ack Vector records to update
    :type av: struct dccp_ackvec \*

    :param seqno:
        Sequence number of the packet carrying the Ack Vector just sent
    :type seqno: u64

    :param nonce_sum:
        The sum of all buffer nonces contained in the Ack Vector
    :type nonce_sum: u8

.. _`dccp_ackvec_update_old`:

dccp_ackvec_update_old
======================

.. c:function:: void dccp_ackvec_update_old(struct dccp_ackvec *av, s64 distance, u64 seqno, enum dccp_ackvec_states state)

    Update previous state as per RFC 4340, 11.4.1

    :param av:
        non-empty buffer to update
    :type av: struct dccp_ackvec \*

    :param distance:
        negative or zero distance of \ ``seqno``\  from buf_ackno downward
    :type distance: s64

    :param seqno:
        the (old) sequence number whose record is to be updated
    :type seqno: u64

    :param state:
        state in which packet carrying \ ``seqno``\  was received
    :type state: enum dccp_ackvec_states

.. _`dccp_ackvec_add_new`:

dccp_ackvec_add_new
===================

.. c:function:: void dccp_ackvec_add_new(struct dccp_ackvec *av, u32 num_packets, u64 seqno, enum dccp_ackvec_states state)

    Record one or more new entries in Ack Vector buffer

    :param av:
        container of buffer to update (can be empty or non-empty)
    :type av: struct dccp_ackvec \*

    :param num_packets:
        number of packets to register (must be >= 1)
    :type num_packets: u32

    :param seqno:
        sequence number of the first packet in \ ``num_packets``\ 
    :type seqno: u64

    :param state:
        state in which packet carrying \ ``seqno``\  was received
    :type state: enum dccp_ackvec_states

.. _`dccp_ackvec_input`:

dccp_ackvec_input
=================

.. c:function:: void dccp_ackvec_input(struct dccp_ackvec *av, struct sk_buff *skb)

    Register incoming packet in the buffer

    :param av:
        *undescribed*
    :type av: struct dccp_ackvec \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`dccp_ackvec_clear_state`:

dccp_ackvec_clear_state
=======================

.. c:function:: void dccp_ackvec_clear_state(struct dccp_ackvec *av, const u64 ackno)

    Perform house-keeping / garbage-collection This routine is called when the peer acknowledges the receipt of Ack Vectors up to and including \ ``ackno``\ . While based on on section A.3 of RFC 4340, here are additional precautions to prevent corrupted buffer state. In particular, we use tail_ackno to identify outdated records; it always marks the earliest packet of group (2) in 11.4.2.

    :param av:
        *undescribed*
    :type av: struct dccp_ackvec \*

    :param ackno:
        *undescribed*
    :type ackno: const u64

.. This file was automatic generated / don't edit.

