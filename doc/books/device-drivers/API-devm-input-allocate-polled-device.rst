
.. _API-devm-input-allocate-polled-device:

=================================
devm_input_allocate_polled_device
=================================

*man devm_input_allocate_polled_device(9)*

*4.6.0-rc1*

allocate managed polled device


Synopsis
========

.. c:function:: struct input_polled_dev ⋆ devm_input_allocate_polled_device( struct device * dev )

Arguments
=========

``dev``
    device owning the polled device being created


Description
===========

Returns prepared ``struct input_polled_dev`` or ``NULL``.

Managed polled input devices do not need to be explicitly unregistered or freed as it will be done automatically when owner device unbinds from ⋆ its driver (or binding fails).
Once such managed polled device is allocated, it is ready to be set up and registered in the same fashion as regular polled input devices (using ``input_register_polled_device``
function).

If you want to manually unregister and free such managed polled devices, it can be still done by calling ``input_unregister_polled_device`` and ``input_free_polled_device``,
although it is rarely needed.


NOTE
====

the owner device is set up as parent of input device and users should not override it.
