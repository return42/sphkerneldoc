.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-power-wait:

==============
snd_power_wait
==============

*man snd_power_wait(9)*

*4.6.0-rc5*

wait until the power-state is changed.


Synopsis
========

.. c:function:: int snd_power_wait( struct snd_card * card, unsigned int power_state )

Arguments
=========

``card``
    soundcard structure

``power_state``
    expected power state


Description
===========

Waits until the power-state is changed.


Return
======

Zero if successful, or a negative error code.


Note
====

the power lock must be active before call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
