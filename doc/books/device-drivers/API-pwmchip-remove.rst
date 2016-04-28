.. -*- coding: utf-8; mode: rst -*-

.. _API-pwmchip-remove:

==============
pwmchip_remove
==============

*man pwmchip_remove(9)*

*4.6.0-rc5*

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

Removes a PWM chip. This function may return busy if the PWM chip
provides a PWM device that is still requested.


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
