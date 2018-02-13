.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/bcmsdh.c

.. _`brcmf_sdiod_sglist_rw`:

brcmf_sdiod_sglist_rw
=====================

.. c:function:: int brcmf_sdiod_sglist_rw(struct brcmf_sdio_dev *sdiodev, struct sdio_func *func, bool write, u32 addr, struct sk_buff_head *pktlist)

    SDIO interface function for block data access

    :param struct brcmf_sdio_dev \*sdiodev:
        brcmfmac sdio device

    :param struct sdio_func \*func:
        SDIO function

    :param bool write:
        direction flag

    :param u32 addr:
        dongle memory address as source/destination

    :param struct sk_buff_head \*pktlist:
        *undescribed*

.. _`brcmf_sdiod_sglist_rw.description`:

Description
-----------

This function takes the respbonsibility as the interface function to MMC
stack for block data access. It assumes that the skb passed down by the
caller has already been padded and aligned.

.. This file was automatic generated / don't edit.

