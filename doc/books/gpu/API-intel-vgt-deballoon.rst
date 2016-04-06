
.. _API-intel-vgt-deballoon:

===================
intel_vgt_deballoon
===================

*man intel_vgt_deballoon(9)*

*4.6.0-rc1*

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

This function is called to deallocate the ballooned-out graphic memory, when driver is unloaded or when ballooning fails.
