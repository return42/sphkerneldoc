
.. _API-pwm-enable:

==========
pwm_enable
==========

*man pwm_enable(9)*

*4.6.0-rc1*

start a PWM output toggling


Synopsis
========

.. c:function:: int pwm_enable( struct pwm_device * pwm )

Arguments
=========

``pwm``
    PWM device


Returns
=======

0 on success or a negative error code on failure.
