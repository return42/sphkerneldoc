.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_hdmi_tx3g0c55phy.c

.. _`disable_pll_rejection`:

disable_pll_rejection
=====================

.. c:function:: bool disable_pll_rejection(struct sti_hdmi *hdmi)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. _`disable_pll_rejection.description`:

Description
-----------

return true if the pll has been disabled

.. _`enable_pll_rejection`:

enable_pll_rejection
====================

.. c:function:: bool enable_pll_rejection(struct sti_hdmi *hdmi)

    clock input to the new PHY PLL that generates the serializer clock (TMDS\*10) and the TMDS clock which is now fed back into the HDMI formatter instead of the TMDS clock line from ClockGenB.

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. _`enable_pll_rejection.description`:

Description
-----------

return true if pll has been correctly set

.. _`sti_hdmi_tx3g0c55phy_start`:

sti_hdmi_tx3g0c55phy_start
==========================

.. c:function:: bool sti_hdmi_tx3g0c55phy_start(struct sti_hdmi *hdmi)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. _`sti_hdmi_tx3g0c55phy_start.description`:

Description
-----------

Return false if an error occur

.. _`sti_hdmi_tx3g0c55phy_stop`:

sti_hdmi_tx3g0c55phy_stop
=========================

.. c:function:: void sti_hdmi_tx3g0c55phy_stop(struct sti_hdmi *hdmi)

    :param struct sti_hdmi \*hdmi:
        pointer on the hdmi internal structure

.. This file was automatic generated / don't edit.

