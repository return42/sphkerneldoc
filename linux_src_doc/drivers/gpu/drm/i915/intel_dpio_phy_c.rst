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

channel
    struct containing per channel information.

.. This file was automatic generated / don't edit.

