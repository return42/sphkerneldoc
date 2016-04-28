.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-unregister-driver:

======================
uart_unregister_driver
======================

*man uart_unregister_driver(9)*

*4.6.0-rc5*

remove a driver from the uart core layer


Synopsis
========

.. c:function:: void uart_unregister_driver( struct uart_driver * drv )

Arguments
=========

``drv``
    low level driver structure


Description
===========

Remove all references to a driver from the core driver. The low level
driver must have removed all its ports via the ``uart_remove_one_port``
if it registered them with ``uart_add_one_port``. (ie, drv->port ==
NULL)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
