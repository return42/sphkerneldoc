.. -*- coding: utf-8; mode: rst -*-

.. _API-airq-iv-create:

==============
airq_iv_create
==============

*man airq_iv_create(9)*

*4.6.0-rc5*

create an interrupt vector


Synopsis
========

.. c:function:: struct airq_iv * airq_iv_create( unsigned long bits, unsigned long flags )

Arguments
=========

``bits``
    number of bits in the interrupt vector

``flags``
    allocation flags


Description
===========

Returns a pointer to an interrupt vector structure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
