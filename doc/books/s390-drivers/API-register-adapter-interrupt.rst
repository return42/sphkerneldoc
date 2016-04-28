.. -*- coding: utf-8; mode: rst -*-

.. _API-register-adapter-interrupt:

==========================
register_adapter_interrupt
==========================

*man register_adapter_interrupt(9)*

*4.6.0-rc5*

register adapter interrupt handler


Synopsis
========

.. c:function:: int register_adapter_interrupt( struct airq_struct * airq )

Arguments
=========

``airq``
    pointer to adapter interrupt descriptor


Description
===========

Returns 0 on success, or -EINVAL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
