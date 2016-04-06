
.. _API-devm-pwm-put:

============
devm_pwm_put
============

*man devm_pwm_put(9)*

*4.6.0-rc1*

resource managed ``pwm_put``


Synopsis
========

.. c:function:: void devm_pwm_put( struct device * dev, struct pwm_device * pwm )

Arguments
=========

``dev``
    device for PWM consumer

``pwm``
    PWM device


Description
===========

Release a PWM previously allocated using ``devm_pwm_get``. Calling this function is usually not needed because devm-allocated resources are automatically released on driver detach.
