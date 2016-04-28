.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-close:

=============
parport_close
=============

*man parport_close(9)*

*4.6.0-rc5*

close a device opened with ``parport_open``


Synopsis
========

.. c:function:: void parport_close( struct pardevice * dev )

Arguments
=========

``dev``
    device to close


Description
===========

This is to ``parport_open`` as ``parport_unregister_device`` is to
``parport_register_device``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
