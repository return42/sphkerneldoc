.. -*- coding: utf-8; mode: rst -*-

.. _API-pwm-set-chip-data:

=================
pwm_set_chip_data
=================

*man pwm_set_chip_data(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
