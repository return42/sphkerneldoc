
.. _API-pwm-request:

===========
pwm_request
===========

*man pwm_request(9)*

*4.6.0-rc1*

request a PWM device


Synopsis
========

.. c:function:: struct pwm_device ⋆ pwm_request( int pwm, const char * label )

Arguments
=========

``pwm``
    global PWM device index

``label``
    PWM device label


Description
===========

This function is deprecated, use ``pwm_get`` instead.


Returns
=======

A pointer to a PWM device or an ``ERR_PTR``-encoded error code on failure.
