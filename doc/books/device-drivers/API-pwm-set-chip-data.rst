
.. _API-pwm-set-chip-data:

=================
pwm_set_chip_data
=================

*man pwm_set_chip_data(9)*

*4.6.0-rc1*

set private chip data for a PWM


Synopsis
========

.. c:function:: int pwm_set_chip_data( struct pwm_device * pwm, void * data )

Arguments
=========

``pwm``
    PWM device

``data``
    pointer to chip-specific data


Returns
=======

0 on success or a negative error code on failure.
