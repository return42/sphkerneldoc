.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-register-adapter:

====================
dvb_register_adapter
====================

*man dvb_register_adapter(9)*

*4.6.0-rc5*

Registers a new DVB adapter


Synopsis
========

.. c:function:: int dvb_register_adapter( struct dvb_adapter * adap, const char * name, struct module * module, struct device * device, short * adapter_nums )

Arguments
=========

``adap``
    pointer to struct dvb_adapter

``name``
    Adapter's name

``module``
    initialized with THIS_MODULE at the caller

``device``
    pointer to struct device that corresponds to the device driver

``adapter_nums``
    Array with a list of the numbers for ``dvb_register_adapter``; to
    select among them. Typically, initialized with:
    DVB_DEFINE_MOD_OPT_ADAPTER_NR(adapter_nums)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
