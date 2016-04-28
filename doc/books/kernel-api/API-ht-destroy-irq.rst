.. -*- coding: utf-8; mode: rst -*-

.. _API-ht-destroy-irq:

==============
ht_destroy_irq
==============

*man ht_destroy_irq(9)*

*4.6.0-rc5*

destroy an irq created with ht_create_irq


Synopsis
========

.. c:function:: void ht_destroy_irq( unsigned int irq )

Arguments
=========

``irq``
    irq to be destroyed


Description
===========

This reverses ht_create_irq removing the specified irq from existence.
The irq should be free before this happens.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
