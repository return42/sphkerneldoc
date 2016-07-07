.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.c

.. _`sdpcm_hwhdr_len`:

SDPCM_HWHDR_LEN
===============

.. c:function::  SDPCM_HWHDR_LEN()

    This is the lowest layer header wrapped on the packets transmitted between host and WiFi dongle which contains information needed for SDIO core and firmware

.. _`sdpcm_hwhdr_len.it-consists-of-3-parts`:

It consists of 3 parts
----------------------

hardware header, hardware extension header and
software header
hardware header (frame tag) - 4 bytes
Byte 0~1: Frame length
Byte 2~3: Checksum, bit-wise inverse of frame length
hardware extension header - 8 bytes
Tx glom mode only, N/A for Rx or normal Tx
Byte 0~1: Packet length excluding hw frame tag

.. _`sdpcm_hwhdr_len.byte-2`:

Byte 2
------

Reserved

Length of next data frame, reserved for Tx

.. _`sdpcm_hwhdr_len.byte-3`:

Byte 3
------

Frame flags, bit 0: last frame indication
Byte 4~5: Reserved
Byte 6~7: Tail padding length
software header - 8 bytes

Data offset

.. _`sdpcm_hwhdr_len.byte-0`:

Byte 0
------

Rx/Tx sequence number

.. _`sdpcm_hwhdr_len.byte-1`:

Byte 1
------

4 MSB Channel number, 4 LSB arbitrary flag

.. _`sdpcm_hwhdr_len.byte-4`:

Byte 4
------

Flow control bits, reserved for Tx

.. _`sdpcm_hwhdr_len.byte-5`:

Byte 5
------

Maximum Sequence number allowed by firmware for Tx, N/A for Tx packet
Byte 6~7: Reserved

.. _`brcmf_sdio_txpkt_prep`:

brcmf_sdio_txpkt_prep
=====================

.. c:function:: int brcmf_sdio_txpkt_prep(struct brcmf_sdio *bus, struct sk_buff_head *pktq, uint chan)

    packet preparation for transmit

    :param struct brcmf_sdio \*bus:
        brcmf_sdio structure pointer

    :param struct sk_buff_head \*pktq:
        packet list pointer

    :param uint chan:
        virtual channel to transmit the packet

.. _`brcmf_sdio_txpkt_prep.description`:

Description
-----------

Processes to be applied to the packet
- Align data buffer pointer
- Align data buffer length
- Prepare header

.. _`brcmf_sdio_txpkt_prep.return`:

Return
------

negative value if there is error

.. _`brcmf_sdio_txpkt_postp`:

brcmf_sdio_txpkt_postp
======================

.. c:function:: void brcmf_sdio_txpkt_postp(struct brcmf_sdio *bus, struct sk_buff_head *pktq)

    packet post processing for transmit

    :param struct brcmf_sdio \*bus:
        brcmf_sdio structure pointer

    :param struct sk_buff_head \*pktq:
        packet list pointer

.. _`brcmf_sdio_txpkt_postp.description`:

Description
-----------

Processes to be applied to the packet
- Remove head padding
- Remove tail padding

.. This file was automatic generated / don't edit.

