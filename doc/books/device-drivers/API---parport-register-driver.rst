.. -*- coding: utf-8; mode: rst -*-

.. _API---parport-register-driver:

=========================
__parport_register_driver
=========================

*man __parport_register_driver(9)*

*4.6.0-rc5*

register a parallel port device driver


Synopsis
========

.. c:function:: int __parport_register_driver( struct parport_driver * drv, struct module * owner, const char * mod_name )

Arguments
=========

``drv``
    structure describing the driver

``owner``
    owner module of drv

``mod_name``
    module name string


Description
===========

This can be called by a parallel port device driver in order to receive
notifications about ports being found in the system, as well as ports no
longer available.

If devmodel is true then the new device model is used for registration.

The ``drv`` structure is allocated by the caller and must not be
deallocated until after calling ``parport_unregister_driver``.


If using the non device model
=============================

The driver's ``attach`` function may block. The port that ``attach`` is
given will be valid for the duration of the callback, but if the driver
wants to take a copy of the pointer it must call ``parport_get_port`` to
do so. Calling ``parport_register_device`` on that port will do this for
you.

The driver's ``detach`` function may block. The port that ``detach`` is
given will be valid for the duration of the callback, but if the driver
wants to take a copy of the pointer it must call ``parport_get_port`` to
do so.

Returns 0 on success. The non device model will always succeeds. but the
new device model can fail and will return the error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
