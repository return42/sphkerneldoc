.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-bfin.c

.. _`bfin_rtc_reset`:

bfin_rtc_reset
==============

.. c:function:: void bfin_rtc_reset(struct device *dev, u16 rtc_ictl)

    set RTC to sane/known state

    :param struct device \*dev:
        *undescribed*

    :param u16 rtc_ictl:
        *undescribed*

.. _`bfin_rtc_reset.description`:

Description
-----------

Initialize the RTC.  Enable pre-scaler to scale RTC clock
to 1Hz and clear interrupt/status registers.

.. _`bfin_rtc_interrupt`:

bfin_rtc_interrupt
==================

.. c:function:: irqreturn_t bfin_rtc_interrupt(int irq, void *dev_id)

    handle interrupt from RTC

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        *undescribed*

.. _`bfin_rtc_interrupt.description`:

Description
-----------

Since we handle all RTC events here, we have to make sure the requested
interrupt is enabled (in RTC_ICTL) as the event status register (RTC_ISTAT)
always gets updated regardless of the interrupt being enabled.  So when one
even we care about (e.g. stopwatch) goes off, we don't want to turn around
and say that other events have happened as well (e.g. second).  We do not
have to worry about pending writes to the RTC_ICTL register as interrupts
only fire if they are enabled in the RTC_ICTL register.

.. This file was automatic generated / don't edit.

