
.. _API-of-pwm-get:

==========
of_pwm_get
==========

*man of_pwm_get(9)*

*4.6.0-rc1*

request a PWM via the PWM framework


Synopsis
========

.. c:function:: struct pwm_device ⋆ of_pwm_get( struct device_node * np, const char * con_id )

Arguments
=========

``np``
    device node to get the PWM from

``con_id``
    consumer name


Description
===========

Returns the PWM device parsed from the phandle and index specified in the “pwms” property of a device tree node or a negative error-code on failure. Values parsed from the device
tree are stored in the returned PWM device object.

If con_id is NULL, the first PWM device listed in the “pwms” property will be requested. Otherwise the “pwm-names” property is used to do a reverse lookup of the PWM index. This
also means that the “pwm-names” property becomes mandatory for devices that look up the PWM device via the con_id parameter.


Returns
=======

A pointer to the requested PWM device or an ``ERR_PTR``-encoded error code on failure.
