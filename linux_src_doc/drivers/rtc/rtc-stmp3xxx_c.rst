.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-stmp3xxx.c

.. _`stmp3xxx_wdt_set_timeout`:

stmp3xxx_wdt_set_timeout
========================

.. c:function:: void stmp3xxx_wdt_set_timeout(struct device *dev, u32 timeout)

    configure the watchdog inside the STMP3xxx RTC

    :param struct device \*dev:
        the parent device of the watchdog (= the RTC)

    :param u32 timeout:
        the desired value for the timeout register of the watchdog.
        0 disables the watchdog

.. _`stmp3xxx_wdt_set_timeout.description`:

Description
-----------

The watchdog needs one register and two bits which are in the RTC domain.
To handle the resource conflict, the RTC driver will create another
platform_device for the watchdog driver as a child of the RTC device.
The watchdog driver is passed the below accessor function via platform_data
to configure the watchdog. Locking is not needed because accessing SET/CLR
registers is atomic.

.. This file was automatic generated / don't edit.

