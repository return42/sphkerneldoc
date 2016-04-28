.. -*- coding: utf-8; mode: rst -*-

.. _API-pwm-get-chip-data:

=================
pwm_get_chip_data
=================

*man pwm_get_chip_data(9)*

*4.6.0-rc5*

get private chip data for a PWM


Synopsis
========

.. c:function:: void * pwm_get_chip_data( struct pwm_device * pwm )

Arguments
=========

``pwm``
    PWM device


Returns
=======

A pointer to the chip-private data for the PWM device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
