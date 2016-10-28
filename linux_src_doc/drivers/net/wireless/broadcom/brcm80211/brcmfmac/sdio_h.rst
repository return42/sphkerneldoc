.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/sdio.h

.. _`brcmf_sdiod_state`:

enum brcmf_sdiod_state
======================

.. c:type:: enum brcmf_sdiod_state

    the state of the bus.

.. _`brcmf_sdiod_state.definition`:

Definition
----------

.. code-block:: c

    enum brcmf_sdiod_state {
        BRCMF_SDIOD_DOWN,
        BRCMF_SDIOD_DATA,
        BRCMF_SDIOD_NOMEDIUM
    };

.. _`brcmf_sdiod_state.constants`:

Constants
---------

BRCMF_SDIOD_DOWN
    Device can be accessed, no DPC.

BRCMF_SDIOD_DATA
    Ready for data transfers, DPC enabled.

BRCMF_SDIOD_NOMEDIUM
    No medium access to dongle possible.

.. This file was automatic generated / don't edit.

