.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_hwmod_reset.c

.. _`omap_hwmod_aess_preprogram`:

omap_hwmod_aess_preprogram
==========================

.. c:function:: int omap_hwmod_aess_preprogram(struct omap_hwmod *oh)

    enable AESS internal autogating

    :param oh:
        struct omap_hwmod \*
    :type oh: struct omap_hwmod \*

.. _`omap_hwmod_aess_preprogram.description`:

Description
-----------

The AESS will not IdleAck to the PRCM until its internal autogating
is enabled.  Since internal autogating is disabled by default after
AESS reset, we must enable autogating after the hwmod code resets
the AESS.  Returns 0.

.. _`omap_rtc_wait_not_busy`:

omap_rtc_wait_not_busy
======================

.. c:function:: void omap_rtc_wait_not_busy(struct omap_hwmod *oh)

    Wait for the RTC BUSY flag

    :param oh:
        struct omap_hwmod \*
    :type oh: struct omap_hwmod \*

.. _`omap_rtc_wait_not_busy.description`:

Description
-----------

For updating certain RTC registers, the MPU must wait
for the BUSY status in OMAP_RTC_STATUS_REG to become zero.
Once the BUSY status is zero, there is a 15 microseconds access
period in which the MPU can program.

.. _`omap_hwmod_rtc_unlock`:

omap_hwmod_rtc_unlock
=====================

.. c:function:: void omap_hwmod_rtc_unlock(struct omap_hwmod *oh)

    Unlock the Kicker mechanism.

    :param oh:
        struct omap_hwmod \*
    :type oh: struct omap_hwmod \*

.. _`omap_hwmod_rtc_unlock.description`:

Description
-----------

RTC IP have kicker feature. This prevents spurious writes to its registers.
In order to write into any of the RTC registers, KICK values has te be
written in respective KICK registers. This is needed for hwmod to write into
sysconfig register.

.. _`omap_hwmod_rtc_lock`:

omap_hwmod_rtc_lock
===================

.. c:function:: void omap_hwmod_rtc_lock(struct omap_hwmod *oh)

    Lock the Kicker mechanism.

    :param oh:
        struct omap_hwmod \*
    :type oh: struct omap_hwmod \*

.. _`omap_hwmod_rtc_lock.description`:

Description
-----------

RTC IP have kicker feature. This prevents spurious writes to its registers.
Once the RTC registers are written, KICK mechanism needs to be locked,
in order to prevent any spurious writes. This function locks back the RTC
registers once hwmod completes its write into sysconfig register.

.. This file was automatic generated / don't edit.

