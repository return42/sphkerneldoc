.. -*- coding: utf-8; mode: rst -*-

.. _API-pwmchip-add:

===========
pwmchip_add
===========

*man pwmchip_add(9)*

*4.6.0-rc5*

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

Register a new PWM chip. If chip->base < 0 then a dynamically assigned
base will be used. The initial polarity for all channels is normal.


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
