
.. _API-pwmchip-add-with-polarity:

=========================
pwmchip_add_with_polarity
=========================

*man pwmchip_add_with_polarity(9)*

*4.6.0-rc1*

register a new PWM chip


Synopsis
========

.. c:function:: int pwmchip_add_with_polarity( struct pwm_chip * chip, enum pwm_polarity polarity )

Arguments
=========

``chip``
    the PWM chip to add

``polarity``
    initial polarity of PWM channels


Description
===========

Register a new PWM chip. If chip->base < 0 then a dynamically assigned base will be used. The initial polarity for all channels is specified by the ``polarity`` parameter.


Returns
=======

0 on success or a negative error code on failure.
