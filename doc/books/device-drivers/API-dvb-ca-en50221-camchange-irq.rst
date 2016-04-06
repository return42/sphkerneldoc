
.. _API-dvb-ca-en50221-camchange-irq:

============================
dvb_ca_en50221_camchange_irq
============================

*man dvb_ca_en50221_camchange_irq(9)*

*4.6.0-rc1*

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
    One of the DVB_CA_CAMCHANGE_⋆ values
