.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/cadence_master.c

.. _`sdw_cdns_irq`:

sdw_cdns_irq
============

.. c:function:: irqreturn_t sdw_cdns_irq(int irq, void *dev_id)

    Cadence interrupt handler

    :param int irq:
        irq number

    :param void \*dev_id:
        irq context

.. _`sdw_cdns_thread`:

sdw_cdns_thread
===============

.. c:function:: irqreturn_t sdw_cdns_thread(int irq, void *dev_id)

    Cadence irq thread handler

    :param int irq:
        irq number

    :param void \*dev_id:
        irq context

.. _`sdw_cdns_enable_interrupt`:

sdw_cdns_enable_interrupt
=========================

.. c:function:: int sdw_cdns_enable_interrupt(struct sdw_cdns *cdns)

    Enable SDW interrupts and update config

    :param struct sdw_cdns \*cdns:
        Cadence instance

.. _`sdw_cdns_init`:

sdw_cdns_init
=============

.. c:function:: int sdw_cdns_init(struct sdw_cdns *cdns)

    Cadence initialization

    :param struct sdw_cdns \*cdns:
        Cadence instance

.. _`sdw_cdns_probe`:

sdw_cdns_probe
==============

.. c:function:: int sdw_cdns_probe(struct sdw_cdns *cdns)

    Cadence probe routine

    :param struct sdw_cdns \*cdns:
        Cadence instance

.. This file was automatic generated / don't edit.

