.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-pl031.c

.. _`pl031_vendor_data`:

struct pl031_vendor_data
========================

.. c:type:: struct pl031_vendor_data

    per-vendor variations

.. _`pl031_vendor_data.definition`:

Definition
----------

.. code-block:: c

    struct pl031_vendor_data {
        struct rtc_class_ops ops;
        bool clockwatch;
        bool st_weekday;
        unsigned long irqflags;
    }

.. _`pl031_vendor_data.members`:

Members
-------

ops
    the vendor-specific operations used on this silicon version

clockwatch
    if this is an ST Microelectronics silicon version with a
    clockwatch function

st_weekday
    if this is an ST Microelectronics silicon version that need
    the weekday fix

irqflags
    special IRQ flags per variant

.. This file was automatic generated / don't edit.

