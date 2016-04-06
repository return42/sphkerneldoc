
.. _API-pwm-get:

=======
pwm_get
=======

*man pwm_get(9)*

*4.6.0-rc1*

look up and request a PWM device


Synopsis
========

.. c:function:: struct pwm_device ⋆ pwm_get( struct device * dev, const char * con_id )

Arguments
=========

``dev``
    device for PWM consumer

``con_id``
    consumer name


Description
===========

Lookup is first attempted using DT. If the device was not instantiated from a device tree, a PWM chip and a relative index is looked up via a table supplied by board setup code
(see ``pwm_add_table``).

Once a PWM chip has been found the specified PWM device will be requested and is ready to be used.


Returns
=======

A pointer to the requested PWM device or an ``ERR_PTR``-encoded error code on failure.
