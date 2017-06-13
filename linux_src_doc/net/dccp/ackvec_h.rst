.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ackvec.h

.. _`dccp_ackvec`:

struct dccp_ackvec
==================

.. c:type:: struct dccp_ackvec

    Ack Vector main data structure

.. _`dccp_ackvec.definition`:

Definition
----------

.. code-block:: c

    struct dccp_ackvec {
        u8 av_buf;
        u16 av_buf_head;
        u16 av_buf_tail;
        u64 av_buf_ackno:48;
        u64 av_tail_ackno:48;
        bool av_buf_nonce;
        u8 av_overflow:1;
        struct list_head av_records;
    }

.. _`dccp_ackvec.members`:

Members
-------

av_buf
    circular buffer storage area

av_buf_head
    head index; begin of live portion in \ ``av_buf``\ 

av_buf_tail
    tail index; first index \_after\_ the live portion in \ ``av_buf``\ 

av_buf_ackno
    highest seqno of acknowledgeable packet recorded in \ ``av_buf``\ 

av_tail_ackno
    lowest  seqno of acknowledgeable packet recorded in \ ``av_buf``\ 

av_buf_nonce
    ECN nonce sums, each covering subsequent segments of up to
    \ ``DCCP_SINGLE_OPT_MAXLEN``\  cells in the live portion of \ ``av_buf``\ 

av_overflow
    if 1 then buf_head == buf_tail indicates buffer wraparound

av_records
    list of \ ``dccp_ackvec_record``\  (Ack Vectors sent previously)

.. _`dccp_ackvec.description`:

Description
-----------

This implements a fixed-size circular buffer within an array and is largely
based on Appendix A of RFC 4340.

.. _`dccp_ackvec_record`:

struct dccp_ackvec_record
=========================

.. c:type:: struct dccp_ackvec_record

    Records information about sent Ack Vectors

.. _`dccp_ackvec_record.definition`:

Definition
----------

.. code-block:: c

    struct dccp_ackvec_record {
        struct list_head avr_node;
        u64 avr_ack_seqno:48;
        u64 avr_ack_ackno:48;
        u16 avr_ack_ptr;
        u8 avr_ack_runlen;
        u8 avr_ack_nonce:1;
    }

.. _`dccp_ackvec_record.members`:

Members
-------

avr_node
    the list node in \ ``av_records``\ 

avr_ack_seqno
    sequence number of the packet the Ack Vector was sent on

avr_ack_ackno
    the Ack number that this record/Ack Vector refers to

avr_ack_ptr
    pointer into \ ``av_buf``\  where this record starts

avr_ack_runlen
    run length of \ ``avr_ack_ptr``\  at the time of sending

avr_ack_nonce
    the sum of \ ``av_buf_nonce``\ 's at the time this record was sent

.. _`dccp_ackvec_record.description`:

Description
-----------

These list entries define the additional information which the HC-Receiver
keeps about recently-sent Ack Vectors; again refer to RFC 4340, Appendix A.

The list as a whole is sorted in descending order by \ ``avr_ack_seqno``\ .

.. _`dccp_ackvec_parsed`:

struct dccp_ackvec_parsed
=========================

.. c:type:: struct dccp_ackvec_parsed

    Record offsets of Ack Vectors in skb

.. _`dccp_ackvec_parsed.definition`:

Definition
----------

.. code-block:: c

    struct dccp_ackvec_parsed {
        u8 *vec;
        u8 *len;
        u8 * nonce:1;
        struct list_head node;
    }

.. _`dccp_ackvec_parsed.members`:

Members
-------

vec
    start of vector (offset into skb)

len
    length of \ ``vec``\ 

nonce
    whether \ ``vec``\  had an ECN nonce of 0 or 1

node
    FIFO - arranged in descending order of ack_ackno

.. _`dccp_ackvec_parsed.description`:

Description
-----------

This structure is used by CCIDs to access Ack Vectors in a received skb.

.. This file was automatic generated / don't edit.

