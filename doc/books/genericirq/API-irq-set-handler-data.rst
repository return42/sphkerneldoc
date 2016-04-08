
.. _API-irq-set-handler-data:

====================
irq_set_handler_data
====================

*man irq_set_handler_data(9)*

*4.6.0-rc1*

set irq handler data for an irq


Synopsis
========

.. c:function:: int irq_set_handler_data( unsigned int irq, void * data )

Arguments
=========

``irq``
    Interrupt number

``data``
    Pointer to interrupt specific data


Description
===========

Set the hardware irq controller data for an irq
