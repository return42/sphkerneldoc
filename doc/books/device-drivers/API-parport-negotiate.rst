
.. _API-parport-negotiate:

=================
parport_negotiate
=================

*man parport_negotiate(9)*

*4.6.0-rc1*

negotiate an IEEE 1284 mode


Synopsis
========

.. c:function:: int parport_negotiate( struct parport * port, int mode )

Arguments
=========

``port``
    port to use

``mode``
    mode to negotiate to


Description
===========

Use this to negotiate to a particular IEEE 1284 transfer mode. The ``mode`` parameter should be one of the constants in parport.h starting ``IEEE1284_MODE_xxx``.

The return value is 0 if the peripheral has accepted the negotiation to the mode specified, -1 if the peripheral is not IEEE 1284 compliant (or not present), or 1 if the peripheral
has rejected the negotiation.
