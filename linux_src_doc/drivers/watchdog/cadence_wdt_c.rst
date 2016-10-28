.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/cadence_wdt.c

.. _`cdns_wdt`:

struct cdns_wdt
===============

.. c:type:: struct cdns_wdt

    Watchdog device structure

.. _`cdns_wdt.definition`:

Definition
----------

.. code-block:: c

    struct cdns_wdt {
        void __iomem *regs;
        bool rst;
        struct clk *clk;
        u32 prescaler;
        u32 ctrl_clksel;
        spinlock_t io_lock;
        struct watchdog_device cdns_wdt_device;
    }

.. _`cdns_wdt.members`:

Members
-------

regs
    baseaddress of device

rst
    reset flag

clk
    struct clk \* of a clock source

prescaler
    for saving prescaler value

ctrl_clksel
    counter clock prescaler selection

io_lock
    spinlock for IO register access

cdns_wdt_device
    watchdog device structure

.. _`cdns_wdt.description`:

Description
-----------

Structure containing parameters specific to cadence watchdog.

.. _`cdns_wdt_stop`:

cdns_wdt_stop
=============

.. c:function:: int cdns_wdt_stop(struct watchdog_device *wdd)

    Stop the watchdog.

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`cdns_wdt_stop.description`:

Description
-----------

Read the contents of the ZMR register, clear the WDEN bit
in the register and set the access key for successful write.

.. _`cdns_wdt_stop.return`:

Return
------

always 0

.. _`cdns_wdt_reload`:

cdns_wdt_reload
===============

.. c:function:: int cdns_wdt_reload(struct watchdog_device *wdd)

    Reload the watchdog timer (i.e. pat the watchdog).

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`cdns_wdt_reload.description`:

Description
-----------

Write the restart key value (0x00001999) to the restart register.

.. _`cdns_wdt_reload.return`:

Return
------

always 0

.. _`cdns_wdt_start`:

cdns_wdt_start
==============

.. c:function:: int cdns_wdt_start(struct watchdog_device *wdd)

    Enable and start the watchdog.

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`cdns_wdt_start.the-counter-value-is-calculated-according-to-the-formula`:

The counter value is calculated according to the formula
--------------------------------------------------------

calculated count = (timeout \* clock) / prescaler + 1.
The calculated count is divided by 0x1000 to obtain the field value
to write to counter control register.
Clears the contents of prescaler and counter reset value. Sets the
prescaler to 4096 and the calculated count and access key
to write to CCR Register.
Sets the WDT (WDEN bit) and either the Reset signal(RSTEN bit)
or Interrupt signal(IRQEN) with a specified cycles and the access
key to write to ZMR Register.

.. _`cdns_wdt_start.return`:

Return
------

always 0

.. _`cdns_wdt_settimeout`:

cdns_wdt_settimeout
===================

.. c:function:: int cdns_wdt_settimeout(struct watchdog_device *wdd, unsigned int new_time)

    Set a new timeout value for the watchdog device.

    :param struct watchdog_device \*wdd:
        watchdog device

    :param unsigned int new_time:
        new timeout value that needs to be set

.. _`cdns_wdt_settimeout.return`:

Return
------

0 on success

Update the watchdog_device timeout with new value which is used when
cdns_wdt_start is called.

.. _`cdns_wdt_irq_handler`:

cdns_wdt_irq_handler
====================

.. c:function:: irqreturn_t cdns_wdt_irq_handler(int irq, void *dev_id)

    Notifies of watchdog timeout.

    :param int irq:
        interrupt number

    :param void \*dev_id:
        pointer to a platform device structure

.. _`cdns_wdt_irq_handler.return`:

Return
------

IRQ_HANDLED

The handler is invoked when the watchdog times out and a
reset on timeout has not been enabled.

.. _`cdns_wdt_probe`:

cdns_wdt_probe
==============

.. c:function:: int cdns_wdt_probe(struct platform_device *pdev)

    Probe call for the device.

    :param struct platform_device \*pdev:
        handle to the platform device structure.

.. _`cdns_wdt_probe.return`:

Return
------

0 on success, negative error otherwise.

It does all the memory allocation and registration for the device.

.. _`cdns_wdt_remove`:

cdns_wdt_remove
===============

.. c:function:: int cdns_wdt_remove(struct platform_device *pdev)

    Probe call for the device.

    :param struct platform_device \*pdev:
        handle to the platform device structure.

.. _`cdns_wdt_remove.return`:

Return
------

0 on success, otherwise negative error.

Unregister the device after releasing the resources.

.. _`cdns_wdt_shutdown`:

cdns_wdt_shutdown
=================

.. c:function:: void cdns_wdt_shutdown(struct platform_device *pdev)

    Stop the device.

    :param struct platform_device \*pdev:
        handle to the platform structure.

.. _`cdns_wdt_suspend`:

cdns_wdt_suspend
================

.. c:function:: int __maybe_unused cdns_wdt_suspend(struct device *dev)

    Stop the device.

    :param struct device \*dev:
        handle to the device structure.

.. _`cdns_wdt_suspend.return`:

Return
------

0 always.

.. _`cdns_wdt_resume`:

cdns_wdt_resume
===============

.. c:function:: int __maybe_unused cdns_wdt_resume(struct device *dev)

    Resume the device.

    :param struct device \*dev:
        handle to the device structure.

.. _`cdns_wdt_resume.return`:

Return
------

0 on success, errno otherwise.

.. This file was automatic generated / don't edit.

