
.. _API-pwm-request-from-chip:

=====================
pwm_request_from_chip
=====================

*man pwm_request_from_chip(9)*

*4.6.0-rc1*

request a PWM device relative to a PWM chip


Synopsis
========

.. c:function:: struct pwm_device ⋆ pwm_request_from_chip( struct pwm_chip * chip, unsigned int index, const char * label )

Arguments
=========

``chip``
    PWM chip

``index``
    per-chip index of the PWM to request

``label``
    a literal description string of this PWM


Returns
=======

A pointer to the PWM device at the given index of the given PWM chip. A negative error code is returned if the index is not valid for the specified PWM chip or if the PWM device
cannot be requested.
