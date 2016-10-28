.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcdc.c

.. _`brcmf_proto_bcdc_header`:

struct brcmf_proto_bcdc_header
==============================

.. c:type:: struct brcmf_proto_bcdc_header

    BCDC header format

.. _`brcmf_proto_bcdc_header.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_proto_bcdc_header {
        u8 flags;
        u8 priority;
        u8 flags2;
        u8 data_offset;
    }

.. _`brcmf_proto_bcdc_header.members`:

Members
-------

flags
    flags contain protocol and checksum info.

priority
    802.1d priority and USB flow control info (bit 4:7).

flags2
    additional flags containing dongle interface index.

data_offset
    start of packet data. header is following by firmware signals.

.. This file was automatic generated / don't edit.

