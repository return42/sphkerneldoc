
.. _API-z8530-init:

==========
z8530_init
==========

*man z8530_init(9)*

*4.6.0-rc1*

Initialise a Z8530 device


Synopsis
========

.. c:function:: int z8530_init( struct z8530_dev * dev )

Arguments
=========

``dev``
    Z8530 device to initialise.


Description
===========

Configure up a Z8530/Z85C30 or Z85230 chip. We check the device is present, identify the type and then program it to hopefully keep quite and behave. This matters a lot, a Z8530 in
the wrong state will sometimes get into stupid modes generating 10Khz interrupt streams and the like.

We set the interrupt handler up to discard any events, in case we get them during reset or setp.

Return 0 for success, or a negative value indicating the problem in errno form.
