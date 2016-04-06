
.. _API-dvb-register-adapter:

====================
dvb_register_adapter
====================

*man dvb_register_adapter(9)*

*4.6.0-rc1*

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
    Array with a list of the numbers for ``dvb_register_adapter``; to select among them. Typically, initialized with: DVB_DEFINE_MOD_OPT_ADAPTER_NR(adapter_nums)
