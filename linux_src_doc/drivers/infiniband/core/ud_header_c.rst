.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/ud_header.c

.. _`ib_ud_header_init`:

ib_ud_header_init
=================

.. c:function:: int ib_ud_header_init(int payload_bytes, int lrh_present, int eth_present, int vlan_present, int grh_present, int ip_version, int udp_present, int immediate_present, struct ib_ud_header *header)

    Initialize UD header structure

    :param payload_bytes:
        Length of packet payload
    :type payload_bytes: int

    :param lrh_present:
        specify if LRH is present
    :type lrh_present: int

    :param eth_present:
        specify if Eth header is present
    :type eth_present: int

    :param vlan_present:
        packet is tagged vlan
    :type vlan_present: int

    :param grh_present:
        GRH flag (if non-zero, GRH will be included)
    :type grh_present: int

    :param ip_version:
        if non-zero, IP header, V4 or V6, will be included
    :type ip_version: int

    :param udp_present:
        if non-zero, UDP header will be included
    :type udp_present: int

    :param immediate_present:
        specify if immediate data is present
    :type immediate_present: int

    :param header:
        Structure to initialize
    :type header: struct ib_ud_header \*

.. _`ib_ud_header_pack`:

ib_ud_header_pack
=================

.. c:function:: int ib_ud_header_pack(struct ib_ud_header *header, void *buf)

    Pack UD header struct into wire format

    :param header:
        UD header struct
    :type header: struct ib_ud_header \*

    :param buf:
        Buffer to pack into
    :type buf: void \*

.. _`ib_ud_header_pack.description`:

Description
-----------

\ :c:func:`ib_ud_header_pack`\  packs the UD header structure \ ``header``\  into wire
format in the buffer \ ``buf``\ .

.. _`ib_ud_header_unpack`:

ib_ud_header_unpack
===================

.. c:function:: int ib_ud_header_unpack(void *buf, struct ib_ud_header *header)

    Unpack UD header struct from wire format

    :param buf:
        Buffer to pack into
    :type buf: void \*

    :param header:
        UD header struct
    :type header: struct ib_ud_header \*

.. _`ib_ud_header_unpack.description`:

Description
-----------

\ :c:func:`ib_ud_header_pack`\  unpacks the UD header structure \ ``header``\  from wire
format in the buffer \ ``buf``\ .

.. This file was automatic generated / don't edit.

