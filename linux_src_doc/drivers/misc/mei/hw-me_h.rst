.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hw-me.h

.. _`mei_me_hw`:

struct mei_me_hw
================

.. c:type:: struct mei_me_hw

    me hw specific data

.. _`mei_me_hw.definition`:

Definition
----------

.. code-block:: c

    struct mei_me_hw {
        const struct mei_cfg *cfg;
        void __iomem *mem_addr;
        enum mei_pg_state pg_state;
        bool d0i3_supported;
    }

.. _`mei_me_hw.members`:

Members
-------

cfg
    per device generation config and ops

mem_addr
    io memory address

pg_state
    power gating state

d0i3_supported
    di03 support

.. _`mei_cfg_idx`:

enum mei_cfg_idx
================

.. c:type:: enum mei_cfg_idx

    indices to platform specific configurations.

.. _`mei_cfg_idx.definition`:

Definition
----------

.. code-block:: c

    enum mei_cfg_idx {
        MEI_ME_UNDEF_CFG,
        MEI_ME_ICH_CFG,
        MEI_ME_ICH10_CFG,
        MEI_ME_PCH_CFG,
        MEI_ME_PCH_CPT_PBG_CFG,
        MEI_ME_PCH8_CFG,
        MEI_ME_PCH8_SPS_CFG,
        MEI_ME_NUM_CFG
    };

.. _`mei_cfg_idx.constants`:

Constants
---------

MEI_ME_UNDEF_CFG
    Lower sentinel.

MEI_ME_ICH_CFG
    I/O Controller Hub legacy devices.

MEI_ME_ICH10_CFG
    I/O Controller Hub platforms Gen10

MEI_ME_PCH_CFG
    Platform Controller Hub platforms (Up to Gen8).

MEI_ME_PCH_CPT_PBG_CFG
    Platform Controller Hub workstations
    with quirk for Node Manager exclusion.

MEI_ME_PCH8_CFG
    Platform Controller Hub Gen8 and newer
    client platforms.

MEI_ME_PCH8_SPS_CFG
    Platform Controller Hub Gen8 and newer
    servers platforms with quirk for
    SPS firmware exclusion.

MEI_ME_NUM_CFG
    Upper Sentinel.

.. _`mei_cfg_idx.note`:

Note
----

has to be synchronized with mei_cfg_list[]

.. This file was automatic generated / don't edit.

