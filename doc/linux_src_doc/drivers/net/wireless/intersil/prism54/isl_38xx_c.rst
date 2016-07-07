.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intersil/prism54/isl_38xx.c

.. _`isl38xx_disable_interrupts`:

isl38xx_disable_interrupts
==========================

.. c:function:: void isl38xx_disable_interrupts(void __iomem *device)

    disable all interrupts

    :param void __iomem \*device:
        pci memory base address

.. _`isl38xx_disable_interrupts.description`:

Description
-----------

Instructs the device to disable all interrupt reporting by asserting
the IRQ line. New events may still show up in the interrupt identification
register located at offset \ ``ISL38XX_INT_IDENT_REG``\ .

.. This file was automatic generated / don't edit.

