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

.. _`sdw_cdns_pdi_init`:

sdw_cdns_pdi_init
=================

.. c:function:: int sdw_cdns_pdi_init(struct sdw_cdns *cdns, struct sdw_cdns_stream_config config)

    PDI initialization routine

    :param struct sdw_cdns \*cdns:
        Cadence instance

    :param struct sdw_cdns_stream_config config:
        Stream configurations

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

.. _`cdns_find_pdi`:

cdns_find_pdi
=============

.. c:function:: struct sdw_cdns_pdi *cdns_find_pdi(struct sdw_cdns *cdns, unsigned int num, struct sdw_cdns_pdi *pdi)

    Find a free PDI

    :param struct sdw_cdns \*cdns:
        Cadence instance

    :param unsigned int num:
        Number of PDIs

    :param struct sdw_cdns_pdi \*pdi:
        PDI instances

.. _`cdns_find_pdi.description`:

Description
-----------

Find and return a free PDI for a given PDI array

.. _`sdw_cdns_config_stream`:

sdw_cdns_config_stream
======================

.. c:function:: void sdw_cdns_config_stream(struct sdw_cdns *cdns, struct sdw_cdns_port *port, u32 ch, u32 dir, struct sdw_cdns_pdi *pdi)

    Configure a stream

    :param struct sdw_cdns \*cdns:
        Cadence instance

    :param struct sdw_cdns_port \*port:
        Cadence data port

    :param u32 ch:
        Channel count

    :param u32 dir:
        Data direction

    :param struct sdw_cdns_pdi \*pdi:
        PDI to be used

.. _`cdns_get_num_pdi`:

cdns_get_num_pdi
================

.. c:function:: int cdns_get_num_pdi(struct sdw_cdns *cdns, struct sdw_cdns_pdi *pdi, unsigned int num, u32 ch_count)

    Get number of PDIs required

    :param struct sdw_cdns \*cdns:
        Cadence instance

    :param struct sdw_cdns_pdi \*pdi:
        PDI to be used

    :param unsigned int num:
        Number of PDIs

    :param u32 ch_count:
        Channel count

.. _`sdw_cdns_get_stream`:

sdw_cdns_get_stream
===================

.. c:function:: int sdw_cdns_get_stream(struct sdw_cdns *cdns, struct sdw_cdns_streams *stream, u32 ch, u32 dir)

    Get stream information

    :param struct sdw_cdns \*cdns:
        Cadence instance

    :param struct sdw_cdns_streams \*stream:
        Stream to be allocated

    :param u32 ch:
        Channel count

    :param u32 dir:
        Data direction

.. _`sdw_cdns_alloc_stream`:

sdw_cdns_alloc_stream
=====================

.. c:function:: int sdw_cdns_alloc_stream(struct sdw_cdns *cdns, struct sdw_cdns_streams *stream, struct sdw_cdns_port *port, u32 ch, u32 dir)

    Allocate a stream

    :param struct sdw_cdns \*cdns:
        Cadence instance

    :param struct sdw_cdns_streams \*stream:
        Stream to be allocated

    :param struct sdw_cdns_port \*port:
        Cadence data port

    :param u32 ch:
        Channel count

    :param u32 dir:
        Data direction

.. This file was automatic generated / don't edit.

