.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/chip.h

.. _`brcmf_chip`:

struct brcmf_chip
=================

.. c:type:: struct brcmf_chip

    chip level information.

.. _`brcmf_chip.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_chip {
        u32 chip;
        u32 chiprev;
        u32 cc_caps;
        u32 cc_caps_ext;
        u32 pmucaps;
        u32 pmurev;
        u32 rambase;
        u32 ramsize;
        u32 srsize;
        char name[8];
    }

.. _`brcmf_chip.members`:

Members
-------

chip
    chip identifier.

chiprev
    chip revision.

cc_caps
    chipcommon core capabilities.

cc_caps_ext
    chipcommon core extended capabilities.

pmucaps
    PMU capabilities.

pmurev
    PMU revision.

rambase
    RAM base address (only applicable for ARM CR4 chips).

ramsize
    amount of RAM on chip including retention.

srsize
    amount of retention RAM on chip.

name
    string representation of the chip identifier.

.. _`brcmf_core`:

struct brcmf_core
=================

.. c:type:: struct brcmf_core

    core related information.

.. _`brcmf_core.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_core {
        u16 id;
        u16 rev;
        u32 base;
    }

.. _`brcmf_core.members`:

Members
-------

id
    core identifier.

rev
    core revision.

base
    base address of core register space.

.. _`brcmf_buscore_ops`:

struct brcmf_buscore_ops
========================

.. c:type:: struct brcmf_buscore_ops

    buscore specific callbacks.

.. _`brcmf_buscore_ops.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_buscore_ops {
        u32 (* read32) (void *ctx, u32 addr);
        void (* write32) (void *ctx, u32 addr, u32 value);
        int (* prepare) (void *ctx);
        int (* reset) (void *ctx, struct brcmf_chip *chip);
        int (* setup) (void *ctx, struct brcmf_chip *chip);
        void (* activate) (void *ctx, struct brcmf_chip *chip, u32 rstvec);
    }

.. _`brcmf_buscore_ops.members`:

Members
-------

read32
    read 32-bit value over bus.

write32
    write 32-bit value over bus.

prepare
    prepare bus for core configuration.

reset
    *undescribed*

setup
    bus-specific core setup.

activate
    *undescribed*

.. This file was automatic generated / don't edit.

