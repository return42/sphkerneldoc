.. -*- coding: utf-8; mode: rst -*-

.. _API-irq-set-handler-data:

====================
irq_set_handler_data
====================

*man irq_set_handler_data(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
