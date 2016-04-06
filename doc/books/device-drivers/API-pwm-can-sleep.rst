
.. _API-pwm-can-sleep:

=============
pwm_can_sleep
=============

*man pwm_can_sleep(9)*

*4.6.0-rc1*

report whether PWM access will sleep


Synopsis
========

.. c:function:: bool pwm_can_sleep( struct pwm_device * pwm )

Arguments
=========

``pwm``
    PWM device


Returns
=======

True if accessing the PWM can sleep, false otherwise.
