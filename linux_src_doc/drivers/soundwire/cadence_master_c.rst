.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/cadence_master.c

.. _`sdw_cdns_irq`:

sdw_cdns_irq
============

.. c:function:: irqreturn_t sdw_cdns_irq(int irq, void *dev_id)

    Cadence interrupt handler

    :param irq:
        irq number
    :type irq: int

    :param dev_id:
        irq context
    :type dev_id: void \*

.. _`sdw_cdns_thread`:

sdw_cdns_thread
===============

.. c:function:: irqreturn_t sdw_cdns_thread(int irq, void *dev_id)

    Cadence irq thread handler

    :param irq:
        irq number
    :type irq: int

    :param dev_id:
        irq context
    :type dev_id: void \*

.. _`sdw_cdns_enable_interrupt`:

sdw_cdns_enable_interrupt
=========================

.. c:function:: int sdw_cdns_enable_interrupt(struct sdw_cdns *cdns)

    Enable SDW interrupts and update config

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

.. _`sdw_cdns_pdi_init`:

sdw_cdns_pdi_init
=================

.. c:function:: int sdw_cdns_pdi_init(struct sdw_cdns *cdns, struct sdw_cdns_stream_config config)

    PDI initialization routine

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

    :param config:
        Stream configurations
    :type config: struct sdw_cdns_stream_config

.. _`sdw_cdns_init`:

sdw_cdns_init
=============

.. c:function:: int sdw_cdns_init(struct sdw_cdns *cdns)

    Cadence initialization

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

.. _`sdw_cdns_probe`:

sdw_cdns_probe
==============

.. c:function:: int sdw_cdns_probe(struct sdw_cdns *cdns)

    Cadence probe routine

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

.. _`cdns_find_pdi`:

cdns_find_pdi
=============

.. c:function:: struct sdw_cdns_pdi *cdns_find_pdi(struct sdw_cdns *cdns, unsigned int num, struct sdw_cdns_pdi *pdi)

    Find a free PDI

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

    :param num:
        Number of PDIs
    :type num: unsigned int

    :param pdi:
        PDI instances
    :type pdi: struct sdw_cdns_pdi \*

.. _`cdns_find_pdi.description`:

Description
-----------

Find and return a free PDI for a given PDI array

.. _`sdw_cdns_config_stream`:

sdw_cdns_config_stream
======================

.. c:function:: void sdw_cdns_config_stream(struct sdw_cdns *cdns, struct sdw_cdns_port *port, u32 ch, u32 dir, struct sdw_cdns_pdi *pdi)

    Configure a stream

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

    :param port:
        Cadence data port
    :type port: struct sdw_cdns_port \*

    :param ch:
        Channel count
    :type ch: u32

    :param dir:
        Data direction
    :type dir: u32

    :param pdi:
        PDI to be used
    :type pdi: struct sdw_cdns_pdi \*

.. _`cdns_get_num_pdi`:

cdns_get_num_pdi
================

.. c:function:: int cdns_get_num_pdi(struct sdw_cdns *cdns, struct sdw_cdns_pdi *pdi, unsigned int num, u32 ch_count)

    Get number of PDIs required

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

    :param pdi:
        PDI to be used
    :type pdi: struct sdw_cdns_pdi \*

    :param num:
        Number of PDIs
    :type num: unsigned int

    :param ch_count:
        Channel count
    :type ch_count: u32

.. _`sdw_cdns_get_stream`:

sdw_cdns_get_stream
===================

.. c:function:: int sdw_cdns_get_stream(struct sdw_cdns *cdns, struct sdw_cdns_streams *stream, u32 ch, u32 dir)

    Get stream information

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

    :param stream:
        Stream to be allocated
    :type stream: struct sdw_cdns_streams \*

    :param ch:
        Channel count
    :type ch: u32

    :param dir:
        Data direction
    :type dir: u32

.. _`sdw_cdns_alloc_stream`:

sdw_cdns_alloc_stream
=====================

.. c:function:: int sdw_cdns_alloc_stream(struct sdw_cdns *cdns, struct sdw_cdns_streams *stream, struct sdw_cdns_port *port, u32 ch, u32 dir)

    Allocate a stream

    :param cdns:
        Cadence instance
    :type cdns: struct sdw_cdns \*

    :param stream:
        Stream to be allocated
    :type stream: struct sdw_cdns_streams \*

    :param port:
        Cadence data port
    :type port: struct sdw_cdns_port \*

    :param ch:
        Channel count
    :type ch: u32

    :param dir:
        Data direction
    :type dir: u32

.. This file was automatic generated / don't edit.

