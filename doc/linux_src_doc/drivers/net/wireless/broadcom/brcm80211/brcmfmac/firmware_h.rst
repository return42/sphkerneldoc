.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.h

.. _`brcmf_firmware_mapping`:

struct brcmf_firmware_mapping
=============================

.. c:type:: struct brcmf_firmware_mapping

    Used to map chipid/revmask to firmware filename and nvram filename. Each bus type implementation should create a table of firmware mappings (using the macros defined below).

.. _`brcmf_firmware_mapping.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_firmware_mapping {
        u32 chipid;
        u32 revmask;
        const char *fw;
        const char *nvram;
    }

.. _`brcmf_firmware_mapping.members`:

Members
-------

chipid
    ID of chip.

revmask
    bitmask of revisions, e.g. 0x10 means rev 4 only, 0xf means rev 0-3

fw
    name of the firmware file.

nvram
    name of nvram file.

.. This file was automatic generated / don't edit.

