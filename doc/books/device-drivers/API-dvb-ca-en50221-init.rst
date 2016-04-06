
.. _API-dvb-ca-en50221-init:

===================
dvb_ca_en50221_init
===================

*man dvb_ca_en50221_init(9)*

*4.6.0-rc1*

Initialise a new DVB CA device.


Synopsis
========

.. c:function:: int dvb_ca_en50221_init( struct dvb_adapter * dvb_adapter, struct dvb_ca_en50221 * ca, int flags, int slot_count )

Arguments
=========

``dvb_adapter``
    DVB adapter to attach the new CA device to.

``ca``
    The dvb_ca instance.

``flags``
    Flags describing the CA device (DVB_CA_EN50221_FLAG_⋆).

``slot_count``
    Number of slots supported.


Description
===========

``return`` 0 on success, nonzero on failure
