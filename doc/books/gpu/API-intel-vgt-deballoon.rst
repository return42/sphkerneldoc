.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-vgt-deballoon:

===================
intel_vgt_deballoon
===================

*man intel_vgt_deballoon(9)*

*4.6.0-rc5*

deballoon reserved graphics address trunks


Synopsis
========

.. c:function:: void intel_vgt_deballoon( void )

Arguments
=========

``void``
    no arguments


Description
===========

This function is called to deallocate the ballooned-out graphic memory,
when driver is unloaded or when ballooning fails.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
