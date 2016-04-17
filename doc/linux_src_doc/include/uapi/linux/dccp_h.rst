.. -*- coding: utf-8; mode: rst -*-

======
dccp.h
======


.. _`dccp_hdr`:

struct dccp_hdr
===============

.. c:type:: dccp_hdr

    generic part of DCCP packet header


.. _`dccp_hdr.definition`:

Definition
----------

.. code-block:: c

  struct dccp_hdr {
    #if defined(__LITTLE_ENDIAN_BITFIELD)
    #elif defined(__BIG_ENDIAN_BITFIELD)
    #else
    #error "Adjust your \\\lt;asm/byteorder.h\\\gt; defines"
    #endif
    #if defined(__LITTLE_ENDIAN_BITFIELD)
    #elif defined(__BIG_ENDIAN_BITFIELD)
    #else
    #error "Adjust your \\\lt;asm/byteorder.h\\\gt; defines"
    #endif
  };


.. _`dccp_hdr.members`:

Members
-------




.. _`dccp_hdr.description`:

Description
-----------


``dccph_sport`` - Relevant port on the endpoint that sent this packet
``dccph_dport`` - Relevant port on the other endpoint
``dccph_doff`` - Data Offset from the start of the DCCP header, in 32-bit words
``dccph_ccval`` - Used by the HC-Sender CCID
``dccph_cscov`` - Parts of the packet that are covered by the Checksum field
``dccph_checksum`` - Internet checksum, depends on dccph_cscov
``dccph_x`` - 0 = 24 bit sequence number, 1 = 48
``dccph_type`` - packet type, see DCCP_PKT_ prefixed macros
``dccph_seq`` - sequence number high or low order 24 bits, depends on dccph_x



.. _`dccp_hdr_ext`:

struct dccp_hdr_ext
===================

.. c:type:: dccp_hdr_ext

    the low bits of a 48 bit seq packet


.. _`dccp_hdr_ext.definition`:

Definition
----------

.. code-block:: c

  struct dccp_hdr_ext {
  };


.. _`dccp_hdr_ext.members`:

Members
-------




.. _`dccp_hdr_ext.description`:

Description
-----------


``dccph_seq_low`` - low 24 bits of a 48 bit seq packet



.. _`dccp_hdr_request`:

struct dccp_hdr_request
=======================

.. c:type:: dccp_hdr_request

    Connection initiation request header


.. _`dccp_hdr_request.definition`:

Definition
----------

.. code-block:: c

  struct dccp_hdr_request {
  };


.. _`dccp_hdr_request.members`:

Members
-------




.. _`dccp_hdr_request.description`:

Description
-----------


``dccph_req_service`` - Service to which the client app wants to connect



.. _`dccp_hdr_ack_bits`:

struct dccp_hdr_ack_bits
========================

.. c:type:: dccp_hdr_ack_bits

    acknowledgment bits common to most packets


.. _`dccp_hdr_ack_bits.definition`:

Definition
----------

.. code-block:: c

  struct dccp_hdr_ack_bits {
  };


.. _`dccp_hdr_ack_bits.members`:

Members
-------




.. _`dccp_hdr_ack_bits.description`:

Description
-----------


``dccph_resp_ack_nr_high`` - 48 bit ack number high order bits, contains GSR
``dccph_resp_ack_nr_low`` - 48 bit ack number low order bits, contains GSR



.. _`dccp_hdr_response`:

struct dccp_hdr_response
========================

.. c:type:: dccp_hdr_response

    Connection initiation response header


.. _`dccp_hdr_response.definition`:

Definition
----------

.. code-block:: c

  struct dccp_hdr_response {
  };


.. _`dccp_hdr_response.members`:

Members
-------




.. _`dccp_hdr_response.description`:

Description
-----------


``dccph_resp_ack`` - 48 bit Acknowledgment Number Subheader (5.3)
``dccph_resp_service`` - Echoes the Service Code on a received DCCP-Request



.. _`dccp_hdr_reset`:

struct dccp_hdr_reset
=====================

.. c:type:: dccp_hdr_reset

    Unconditionally shut down a connection


.. _`dccp_hdr_reset.definition`:

Definition
----------

.. code-block:: c

  struct dccp_hdr_reset {
  };


.. _`dccp_hdr_reset.members`:

Members
-------




.. _`dccp_hdr_reset.description`:

Description
-----------


``dccph_reset_ack`` - 48 bit Acknowledgment Number Subheader (5.6)
``dccph_reset_code`` - one of ``dccp_reset_codes``
``dccph_reset_data`` - the Data 1 ... Data 3 fields from 5.6

