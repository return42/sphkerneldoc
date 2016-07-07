.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/dccp.h

.. _`dccp_hdr`:

struct dccp_hdr
===============

.. c:type:: struct dccp_hdr

    generic part of DCCP packet header

.. _`dccp_hdr.definition`:

Definition
----------

.. code-block:: c

    struct dccp_hdr {
        __be16 dccph_sport;
        __be16 dccph_dport;
        __u8 dccph_doff;
        #if defined(__LITTLE_ENDIAN_BITFIELD)
        __u8 dccph_cscov:4:4;
        __u8 dccph_ccval:4;
        #elif defined(__BIG_ENDIAN_BITFIELD)
        __u8 dccph_ccval:4;
        __u8 dccph_cscov:4:4;
        #else
        #error "Adjust your <asm/byteorder.h> defines"
        #endif
        __sum16 dccph_checksum;
        #if defined(__LITTLE_ENDIAN_BITFIELD)
        __u8 dccph_x:3:4:1;
        __u8 dccph_type:3:4;
        __u8 dccph_reserved:3;
        #elif defined(__BIG_ENDIAN_BITFIELD)
        __u8 dccph_reserved:3;
        __u8 dccph_type:3:4;
        __u8 dccph_x:3:4:1;
        #else
        #error "Adjust your <asm/byteorder.h> defines"
        #endif
        __u8 dccph_seq2;
        __be16 dccph_seq;
    }

.. _`dccp_hdr.members`:

Members
-------

dccph_sport
    *undescribed*

dccph_dport
    *undescribed*

dccph_doff
    *undescribed*

dccph_cscov
    *undescribed*

dccph_ccval
    *undescribed*

dccph_ccval
    *undescribed*

dccph_cscov
    *undescribed*

dccph_checksum
    *undescribed*

dccph_x
    *undescribed*

dccph_type
    *undescribed*

dccph_reserved
    *undescribed*

dccph_reserved
    *undescribed*

dccph_type
    *undescribed*

dccph_x
    *undescribed*

dccph_seq2
    *undescribed*

dccph_seq
    *undescribed*

.. _`dccp_hdr.description`:

Description
-----------

\ ``dccph_sport``\  - Relevant port on the endpoint that sent this packet
\ ``dccph_dport``\  - Relevant port on the other endpoint
\ ``dccph_doff``\  - Data Offset from the start of the DCCP header, in 32-bit words
\ ``dccph_ccval``\  - Used by the HC-Sender CCID
\ ``dccph_cscov``\  - Parts of the packet that are covered by the Checksum field
\ ``dccph_checksum``\  - Internet checksum, depends on dccph_cscov
\ ``dccph_x``\  - 0 = 24 bit sequence number, 1 = 48
\ ``dccph_type``\  - packet type, see DCCP_PKT\_ prefixed macros
\ ``dccph_seq``\  - sequence number high or low order 24 bits, depends on dccph_x

.. _`dccp_hdr_ext`:

struct dccp_hdr_ext
===================

.. c:type:: struct dccp_hdr_ext

    the low bits of a 48 bit seq packet

.. _`dccp_hdr_ext.definition`:

Definition
----------

.. code-block:: c

    struct dccp_hdr_ext {
        __be32 dccph_seq_low;
    }

.. _`dccp_hdr_ext.members`:

Members
-------

dccph_seq_low
    *undescribed*

.. _`dccp_hdr_ext.description`:

Description
-----------

\ ``dccph_seq_low``\  - low 24 bits of a 48 bit seq packet

.. _`dccp_hdr_request`:

struct dccp_hdr_request
=======================

.. c:type:: struct dccp_hdr_request

    Connection initiation request header

.. _`dccp_hdr_request.definition`:

Definition
----------

.. code-block:: c

    struct dccp_hdr_request {
        __be32 dccph_req_service;
    }

.. _`dccp_hdr_request.members`:

Members
-------

dccph_req_service
    *undescribed*

.. _`dccp_hdr_request.description`:

Description
-----------

\ ``dccph_req_service``\  - Service to which the client app wants to connect

.. _`dccp_hdr_ack_bits`:

struct dccp_hdr_ack_bits
========================

.. c:type:: struct dccp_hdr_ack_bits

    acknowledgment bits common to most packets

.. _`dccp_hdr_ack_bits.definition`:

Definition
----------

.. code-block:: c

    struct dccp_hdr_ack_bits {
        __be16 dccph_reserved1;
        __be16 dccph_ack_nr_high;
        __be32 dccph_ack_nr_low;
    }

.. _`dccp_hdr_ack_bits.members`:

Members
-------

dccph_reserved1
    *undescribed*

dccph_ack_nr_high
    *undescribed*

dccph_ack_nr_low
    *undescribed*

.. _`dccp_hdr_ack_bits.description`:

Description
-----------

\ ``dccph_resp_ack_nr_high``\  - 48 bit ack number high order bits, contains GSR
\ ``dccph_resp_ack_nr_low``\  - 48 bit ack number low order bits, contains GSR

.. _`dccp_hdr_response`:

struct dccp_hdr_response
========================

.. c:type:: struct dccp_hdr_response

    Connection initiation response header

.. _`dccp_hdr_response.definition`:

Definition
----------

.. code-block:: c

    struct dccp_hdr_response {
        struct dccp_hdr_ack_bits dccph_resp_ack;
        __be32 dccph_resp_service;
    }

.. _`dccp_hdr_response.members`:

Members
-------

dccph_resp_ack
    *undescribed*

dccph_resp_service
    *undescribed*

.. _`dccp_hdr_response.description`:

Description
-----------

\ ``dccph_resp_ack``\  - 48 bit Acknowledgment Number Subheader (5.3)
\ ``dccph_resp_service``\  - Echoes the Service Code on a received DCCP-Request

.. _`dccp_hdr_reset`:

struct dccp_hdr_reset
=====================

.. c:type:: struct dccp_hdr_reset

    Unconditionally shut down a connection

.. _`dccp_hdr_reset.definition`:

Definition
----------

.. code-block:: c

    struct dccp_hdr_reset {
        struct dccp_hdr_ack_bits dccph_reset_ack;
        __u8 dccph_reset_code;
        __u8 dccph_reset_data[3];
    }

.. _`dccp_hdr_reset.members`:

Members
-------

dccph_reset_ack
    *undescribed*

dccph_reset_code
    *undescribed*

.. _`dccp_hdr_reset.description`:

Description
-----------

\ ``dccph_reset_ack``\  - 48 bit Acknowledgment Number Subheader (5.6)
\ ``dccph_reset_code``\  - one of \ ``dccp_reset_codes``\ 
\ ``dccph_reset_data``\  - the Data 1 ... Data 3 fields from 5.6

.. This file was automatic generated / don't edit.

