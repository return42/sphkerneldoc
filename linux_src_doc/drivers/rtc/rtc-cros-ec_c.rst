.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-cros-ec.c

.. _`cros_ec_rtc`:

struct cros_ec_rtc
==================

.. c:type:: struct cros_ec_rtc

    Driver data for EC RTC

.. _`cros_ec_rtc.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_rtc {
        struct cros_ec_device *cros_ec;
        struct rtc_device *rtc;
        struct notifier_block notifier;
        u32 saved_alarm;
    }

.. _`cros_ec_rtc.members`:

Members
-------

cros_ec
    Pointer to EC device

rtc
    Pointer to RTC device

notifier
    Notifier info for responding to EC events

saved_alarm
    Alarm to restore when interrupts are reenabled

.. This file was automatic generated / don't edit.

