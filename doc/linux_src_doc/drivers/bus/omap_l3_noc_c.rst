.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/omap_l3_noc.c

.. _`l3_handle_target`:

l3_handle_target
================

.. c:function:: int l3_handle_target(struct omap_l3 *l3, void __iomem *base, struct l3_flagmux_data *flag_mux, int err_src)

    Handle Target specific parse and reporting

    :param struct omap_l3 \*l3:
        pointer to l3 struct

    :param void __iomem \*base:
        base address of clkdm

    :param struct l3_flagmux_data \*flag_mux:
        flagmux corresponding to the event

    :param int err_src:
        error source index of the slave (target)

.. _`l3_handle_target.this-does-the-second-part-of-the-error-interrupt-handling`:

This does the second part of the error interrupt handling
---------------------------------------------------------

3) Parse in the slave information
4) Print the logged information.
5) Add dump stack to provide kernel trace.
6) Clear the source if known.

.. _`l3_handle_target.this-handles-two-types-of-errors`:

This handles two types of errors
--------------------------------

1) Custom errors in L3 :
Target like DMM/FW/EMIF generates SRESP=ERR error
2) Standard L3 error:
- Unsupported CMD.
L3 tries to access target while it is idle
- OCP disconnect.
- Address hole error:
If DSS/ISS/FDIF/USBHOSTFS access a target where they
do not have connectivity, the error is logged in
their default target which is DMM2.

On High Secure devices, firewall errors are possible and those
can be trapped as well. But the trapping is implemented as part
secure software and hence need not be implemented here.

.. _`l3_interrupt_handler`:

l3_interrupt_handler
====================

.. c:function:: irqreturn_t l3_interrupt_handler(int irq, void *_l3)

    interrupt handler for l3 events

    :param int irq:
        irq number

    :param void \*_l3:
        pointer to l3 structure

.. _`l3_interrupt_handler.description`:

Description
-----------

Interrupt Handler for L3 error detection.
1) Identify the L3 clockdomain partition to which the error belongs to.
2) Identify the slave where the error information is logged
... handle the slave event..
7) if the slave is unknown, mask out the slave.

.. _`l3_resume_noirq`:

l3_resume_noirq
===============

.. c:function:: int l3_resume_noirq(struct device *dev)

    resume function for l3_noc

    :param struct device \*dev:
        pointer to l3_noc device structure

.. _`l3_resume_noirq.description`:

Description
-----------

We only have the resume handler only since we
have already maintained the delta register
configuration as part of configuring the system

.. This file was automatic generated / don't edit.

