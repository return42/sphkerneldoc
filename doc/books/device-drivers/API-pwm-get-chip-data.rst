
.. _API-pwm-get-chip-data:

=================
pwm_get_chip_data
=================

*man pwm_get_chip_data(9)*

*4.6.0-rc1*

get private chip data for a PWM


Synopsis
========

.. c:function:: void ⋆ pwm_get_chip_data( struct pwm_device * pwm )

Arguments
=========

``pwm``
    PWM device


Returns
=======

A pointer to the chip-private data for the PWM device.
