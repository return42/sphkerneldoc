
.. _API-pwm-config:

==========
pwm_config
==========

*man pwm_config(9)*

*4.6.0-rc1*

change a PWM device configuration


Synopsis
========

.. c:function:: int pwm_config( struct pwm_device * pwm, int duty_ns, int period_ns )

Arguments
=========

``pwm``
    PWM device

``duty_ns``
    "on" time (in nanoseconds)

``period_ns``
    duration (in nanoseconds) of one cycle


Returns
=======

0 on success or a negative error code on failure.
