
.. _API-irq-chip-retrigger-hierarchy:

============================
irq_chip_retrigger_hierarchy
============================

*man irq_chip_retrigger_hierarchy(9)*

*4.6.0-rc1*

Retrigger an interrupt in hardware


Synopsis
========

.. c:function:: int irq_chip_retrigger_hierarchy( struct irq_data * data )

Arguments
=========

``data``
    Pointer to interrupt specific data


Description
===========

Iterate through the domain hierarchy of the interrupt and check whether a hw retrigger function exists. If yes, invoke it.
