.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-mbigen.c

.. _`irq_event_id_shift`:

IRQ_EVENT_ID_SHIFT
==================

.. c:function::  IRQ_EVENT_ID_SHIFT()

    bit[21:12]:  event id value bit[11:0]:   device id

.. _`reg_mbigen_clear_offset`:

REG_MBIGEN_CLEAR_OFFSET
=======================

.. c:function::  REG_MBIGEN_CLEAR_OFFSET()

    This register is used to clear the status of interrupt

.. _`reg_mbigen_type_offset`:

REG_MBIGEN_TYPE_OFFSET
======================

.. c:function::  REG_MBIGEN_TYPE_OFFSET()

    This register is used to configure interrupt trigger type

.. _`mbigen_device`:

struct mbigen_device
====================

.. c:type:: struct mbigen_device

    holds the information of mbigen device.

.. _`mbigen_device.definition`:

Definition
----------

.. code-block:: c

    struct mbigen_device {
        struct platform_device *pdev;
        void __iomem *base;
    }

.. _`mbigen_device.members`:

Members
-------

pdev
    pointer to the platform device structure of mbigen chip.

base
    mapped address of this mbigen chip.

.. This file was automatic generated / don't edit.

