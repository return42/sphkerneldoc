.. -*- coding: utf-8; mode: rst -*-

.. _API-serial8250-unregister-port:

==========================
serial8250_unregister_port
==========================

*man serial8250_unregister_port(9)*

*4.6.0-rc5*

remove a 16x50 serial port at runtime


Synopsis
========

.. c:function:: void serial8250_unregister_port( int line )

Arguments
=========

``line``
    serial line number


Description
===========

Remove one serial port. This may not be called from interrupt context.
We hand the port back to the our control.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
