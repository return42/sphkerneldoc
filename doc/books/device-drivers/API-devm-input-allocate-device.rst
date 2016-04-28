.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-input-allocate-device:

==========================
devm_input_allocate_device
==========================

*man devm_input_allocate_device(9)*

*4.6.0-rc5*

allocate managed input device


Synopsis
========

.. c:function:: struct input_dev * devm_input_allocate_device( struct device * dev )

Arguments
=========

``dev``
    device owning the input device being created


Description
===========

Returns prepared struct input_dev or ``NULL``.

Managed input devices do not need to be explicitly unregistered or freed
as it will be done automatically when owner device unbinds from its
driver (or binding fails). Once managed input device is allocated, it is
ready to be set up and registered in the same fashion as regular input
device. There are no special devm_input_device_[un] ``register``
variants, regular ones work with both managed and unmanaged devices,
should you need them. In most cases however, managed input device need
not be explicitly unregistered or freed.


NOTE
====

the owner device is set up as parent of input device and users should
not override it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
