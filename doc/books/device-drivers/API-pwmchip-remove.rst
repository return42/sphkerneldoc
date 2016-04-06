
.. _API-pwmchip-remove:

==============
pwmchip_remove
==============

*man pwmchip_remove(9)*

*4.6.0-rc1*

remove a PWM chip


Synopsis
========

.. c:function:: int pwmchip_remove( struct pwm_chip * chip )

Arguments
=========

``chip``
    the PWM chip to remove


Description
===========

Removes a PWM chip. This function may return busy if the PWM chip provides a PWM device that is still requested.


Returns
=======

0 on success or a negative error code on failure.
