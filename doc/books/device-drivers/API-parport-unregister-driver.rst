.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-unregister-driver:

=========================
parport_unregister_driver
=========================

*man parport_unregister_driver(9)*

*4.6.0-rc5*

deregister a parallel port device driver


Synopsis
========

.. c:function:: void parport_unregister_driver( struct parport_driver * drv )

Arguments
=========

``drv``
    structure describing the driver that was given to
    ``parport_register_driver``


Description
===========

This should be called by a parallel port device driver that has
registered itself using ``parport_register_driver`` when it is about to
be unloaded.

When it returns, the driver's ``attach`` routine will no longer be
called, and for each port that ``attach`` was called for, the ``detach``
routine will have been called.

All the driver's ``attach`` and ``detach`` calls are guaranteed to have
finished by the time this function returns.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
