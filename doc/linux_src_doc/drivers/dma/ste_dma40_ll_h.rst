.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ste_dma40_ll.h

.. _`d40_phy_lli`:

struct d40_phy_lli
==================

.. c:type:: struct d40_phy_lli

    The basic configuration register for each physical channel.

.. _`d40_phy_lli.definition`:

Definition
----------

.. code-block:: c

    struct d40_phy_lli {
        u32 reg_cfg;
        u32 reg_elt;
        u32 reg_ptr;
        u32 reg_lnk;
    }

.. _`d40_phy_lli.members`:

Members
-------

reg_cfg
    The configuration register.

reg_elt
    The element register.

reg_ptr
    The pointer register.

reg_lnk
    The link register.

.. _`d40_phy_lli.description`:

Description
-----------

These registers are set up for both physical and logical transfers
Note that the bit in each register means differently in logical and
physical(standard) mode.

This struct must be 16 bytes aligned, and only contain physical registers
since it will be directly accessed by the DMA.

.. _`d40_phy_lli_bidir`:

struct d40_phy_lli_bidir
========================

.. c:type:: struct d40_phy_lli_bidir

    struct for a transfer.

.. _`d40_phy_lli_bidir.definition`:

Definition
----------

.. code-block:: c

    struct d40_phy_lli_bidir {
        struct d40_phy_lli *src;
        struct d40_phy_lli *dst;
    }

.. _`d40_phy_lli_bidir.members`:

Members
-------

src
    Register settings for src channel.

dst
    Register settings for dst channel.

.. _`d40_phy_lli_bidir.description`:

Description
-----------

All DMA transfers have a source and a destination.

.. _`d40_log_lli`:

struct d40_log_lli
==================

.. c:type:: struct d40_log_lli

    logical lli configuration

.. _`d40_log_lli.definition`:

Definition
----------

.. code-block:: c

    struct d40_log_lli {
        u32 lcsp02;
        u32 lcsp13;
    }

.. _`d40_log_lli.members`:

Members
-------

lcsp02
    Either maps to register lcsp0 if src or lcsp2 if dst.

lcsp13
    Either maps to register lcsp1 if src or lcsp3 if dst.

.. _`d40_log_lli.description`:

Description
-----------

This struct must be 8 bytes aligned since it will be accessed directy by
the DMA. Never add any none hw mapped registers to this struct.

.. _`d40_log_lli_bidir`:

struct d40_log_lli_bidir
========================

.. c:type:: struct d40_log_lli_bidir

    For both src and dst

.. _`d40_log_lli_bidir.definition`:

Definition
----------

.. code-block:: c

    struct d40_log_lli_bidir {
        struct d40_log_lli *src;
        struct d40_log_lli *dst;
    }

.. _`d40_log_lli_bidir.members`:

Members
-------

src
    pointer to src lli configuration.

dst
    pointer to dst lli configuration.

.. _`d40_log_lli_bidir.description`:

Description
-----------

You always have a src and a dst when doing DMA transfers.

.. _`d40_log_lli_full`:

struct d40_log_lli_full
=======================

.. c:type:: struct d40_log_lli_full

    LCPA layout

.. _`d40_log_lli_full.definition`:

Definition
----------

.. code-block:: c

    struct d40_log_lli_full {
        u32 lcsp0;
        u32 lcsp1;
        u32 lcsp2;
        u32 lcsp3;
    }

.. _`d40_log_lli_full.members`:

Members
-------

lcsp0
    Logical Channel Standard Param 0 - Src.

lcsp1
    Logical Channel Standard Param 1 - Src.

lcsp2
    Logical Channel Standard Param 2 - Dst.

lcsp3
    Logical Channel Standard Param 3 - Dst.

.. _`d40_log_lli_full.description`:

Description
-----------

This struct maps to LCPA physical memory layout. Must map to
the hw.

.. _`d40_def_lcsp`:

struct d40_def_lcsp
===================

.. c:type:: struct d40_def_lcsp

    Default LCSP1 and LCSP3 settings

.. _`d40_def_lcsp.definition`:

Definition
----------

.. code-block:: c

    struct d40_def_lcsp {
        u32 lcsp3;
        u32 lcsp1;
    }

.. _`d40_def_lcsp.members`:

Members
-------

lcsp3
    The default configuration for dst.

lcsp1
    The default configuration for src.

.. This file was automatic generated / don't edit.

