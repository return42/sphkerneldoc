.. -*- coding: utf-8; mode: rst -*-

.. _API-dvb-ca-en50221-camchange-irq:

============================
dvb_ca_en50221_camchange_irq
============================

*man dvb_ca_en50221_camchange_irq(9)*

*4.6.0-rc5*

A CAMCHANGE IRQ has occurred.


Synopsis
========

.. c:function:: void dvb_ca_en50221_camchange_irq( struct dvb_ca_en50221 * pubca, int slot, int change_type )

Arguments
=========

``pubca``
    CA instance.

``slot``
    Slot concerned.

``change_type``
    One of the DVB_CA_CAMCHANGE_* values


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
