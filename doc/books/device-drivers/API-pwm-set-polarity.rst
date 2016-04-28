.. -*- coding: utf-8; mode: rst -*-

.. _API-pwm-set-polarity:

================
pwm_set_polarity
================

*man pwm_set_polarity(9)*

*4.6.0-rc5*

configure the polarity of a PWM signal


Synopsis
========

.. c:function:: int pwm_set_polarity( struct pwm_device * pwm, enum pwm_polarity polarity )

Arguments
=========

``pwm``
    PWM device

``polarity``
    new polarity of the PWM signal


Description
===========

Note that the polarity cannot be configured while the PWM device is
enabled.


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
