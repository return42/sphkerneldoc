.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/ud_header.c

.. _`ib_ud_header_init`:

ib_ud_header_init
=================

.. c:function:: int ib_ud_header_init(int payload_bytes, int lrh_present, int eth_present, int vlan_present, int grh_present, int ip_version, int udp_present, int immediate_present, struct ib_ud_header *header)

    Initialize UD header structure

    :param int payload_bytes:
        Length of packet payload

    :param int lrh_present:
        specify if LRH is present

    :param int eth_present:
        specify if Eth header is present

    :param int vlan_present:
        packet is tagged vlan

    :param int grh_present:
        GRH flag (if non-zero, GRH will be included)

    :param int ip_version:
        if non-zero, IP header, V4 or V6, will be included

    :param int udp_present:
        if non-zero, UDP header will be included

    :param int immediate_present:
        specify if immediate data is present

    :param struct ib_ud_header \*header:
        Structure to initialize

.. _`ib_ud_header_pack`:

ib_ud_header_pack
=================

.. c:function:: int ib_ud_header_pack(struct ib_ud_header *header, void *buf)

    Pack UD header struct into wire format

    :param struct ib_ud_header \*header:
        UD header struct

    :param void \*buf:
        Buffer to pack into

.. _`ib_ud_header_pack.description`:

Description
-----------

ib_ud_header_pack() packs the UD header structure \ ``header``\  into wire
format in the buffer \ ``buf``\ .

.. _`ib_ud_header_unpack`:

ib_ud_header_unpack
===================

.. c:function:: int ib_ud_header_unpack(void *buf, struct ib_ud_header *header)

    Unpack UD header struct from wire format

    :param void \*buf:
        Buffer to pack into

    :param struct ib_ud_header \*header:
        UD header struct

.. _`ib_ud_header_unpack.description`:

Description
-----------

ib_ud_header_pack() unpacks the UD header structure \ ``header``\  from wire
format in the buffer \ ``buf``\ .

.. This file was automatic generated / don't edit.

