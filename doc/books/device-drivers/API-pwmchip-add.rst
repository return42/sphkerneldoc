
.. _API-pwmchip-add:

===========
pwmchip_add
===========

*man pwmchip_add(9)*

*4.6.0-rc1*

register a new PWM chip


Synopsis
========

.. c:function:: int pwmchip_add( struct pwm_chip * chip )

Arguments
=========

``chip``
    the PWM chip to add


Description
===========

Register a new PWM chip. If chip->base < 0 then a dynamically assigned base will be used. The initial polarity for all channels is normal.


Returns
=======

0 on success or a negative error code on failure.
