.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/it87_wdt.c

.. _`wdt_set_timeout`:

wdt_set_timeout
===============

.. c:function:: int wdt_set_timeout(struct watchdog_device *wdd, unsigned int t)

    set a new timeout value with watchdog ioctl

    :param struct watchdog_device \*wdd:
        *undescribed*

    :param unsigned int t:
        timeout value in seconds

.. _`wdt_set_timeout.description`:

Description
-----------

The hardware device has a 8 or 16 bit watchdog timer (depends on
chip version) that can be configured to count seconds or minutes.

Used within WDIOC_SETTIMEOUT watchdog device ioctl.

.. This file was automatic generated / don't edit.

