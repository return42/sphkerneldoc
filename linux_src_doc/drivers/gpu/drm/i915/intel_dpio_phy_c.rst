.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_dpio_phy.c

.. _`bxt_ddi_phy_info`:

struct bxt_ddi_phy_info
=======================

.. c:type:: struct bxt_ddi_phy_info

    Hold info for a broxton DDI phy

.. _`bxt_ddi_phy_info.definition`:

Definition
----------

.. code-block:: c

    struct bxt_ddi_phy_info {
        bool dual_channel;
        enum dpio_phy rcomp_phy;
        int reset_delay;
        u32 pwron_mask;
        struct channel[2];
    }

.. _`bxt_ddi_phy_info.members`:

Members
-------

dual_channel
    true if this phy has a second channel.

rcomp_phy
    If -1, indicates this phy has its own rcomp resistor.Otherwise the GRC value will be copied from the phy indicated by
    this field.

reset_delay
    delay in us to wait before setting the common resetbit in BXT_PHY_CTL_FAMILY, which effectively enables the phy.

pwron_mask
    Mask with the appropriate bit set that would cause thepunit to power this phy if written to BXT_P_CR_GT_DISP_PWRON.

channel
    struct containing per channel information.

.. This file was automatic generated / don't edit.

