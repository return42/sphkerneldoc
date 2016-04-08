
.. _API-irq-setup-alt-chip:

==================
irq_setup_alt_chip
==================

*man irq_setup_alt_chip(9)*

*4.6.0-rc1*

Switch to alternative chip


Synopsis
========

.. c:function:: int irq_setup_alt_chip( struct irq_data * d, unsigned int type )

Arguments
=========

``d``
    irq_data for this interrupt

``type``
    Flow type to be initialized


Description
===========

Only to be called from chip->\ ``irq_set_type`` callbacks.
