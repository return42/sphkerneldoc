.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/sp805_wdt.c

.. _`sp805_wdt`:

struct sp805_wdt
================

.. c:type:: struct sp805_wdt

    sp805 wdt device structure

.. _`sp805_wdt.definition`:

Definition
----------

.. code-block:: c

    struct sp805_wdt {
        struct watchdog_device wdd;
        spinlock_t lock;
        void __iomem *base;
        struct clk *clk;
        struct amba_device *adev;
        unsigned int load_val;
    }

.. _`sp805_wdt.members`:

Members
-------

wdd
    instance of struct watchdog_device

lock
    spin lock protecting dev structure and io access

base
    base address of wdt

clk
    clock structure of wdt

adev
    amba device structure of wdt

load_val
    load value to be set for current timeout

.. This file was automatic generated / don't edit.

