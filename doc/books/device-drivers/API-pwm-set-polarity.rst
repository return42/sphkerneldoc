
.. _API-pwm-set-polarity:

================
pwm_set_polarity
================

*man pwm_set_polarity(9)*

*4.6.0-rc1*

configure the polarity of a PWM signal


Synopsis
========

.. c:function:: int pwm_set_polarity( struct pwm_device * pwm, enum pwm_polarity polarity )

Arguments
=========

``pwm``
    PWM device

``polarity``
    new polarity of the PWM signal


Description
===========

Note that the polarity cannot be configured while the PWM device is enabled.


Returns
=======

0 on success or a negative error code on failure.
