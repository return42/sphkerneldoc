.. -*- coding: utf-8; mode: rst -*-

.. _API-pwm-config:

==========
pwm_config
==========

*man pwm_config(9)*

*4.6.0-rc5*

change a PWM device configuration


Synopsis
========

.. c:function:: int pwm_config( struct pwm_device * pwm, int duty_ns, int period_ns )

Arguments
=========

``pwm``
    PWM device

``duty_ns``
    "on" time (in nanoseconds)

``period_ns``
    duration (in nanoseconds) of one cycle


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
