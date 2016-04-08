
.. _API-irq-set-chip-data:

=================
irq_set_chip_data
=================

*man irq_set_chip_data(9)*

*4.6.0-rc1*

set irq chip data for an irq


Synopsis
========

.. c:function:: int irq_set_chip_data( unsigned int irq, void * data )

Arguments
=========

``irq``
    Interrupt number

``data``
    Pointer to chip specific data


Description
===========

Set the hardware irq chip data for an irq
