
.. _API-apple-gmux-present:

==================
apple_gmux_present
==================

*man apple_gmux_present(9)*

*4.6.0-rc1*

detect if gmux is built into the machine


Synopsis
========

.. c:function:: bool apple_gmux_present( void )

Arguments
=========

``void``
    no arguments


Description
===========

Drivers may use this to activate quirks specific to dual GPU MacBook Pros and Mac Pros, e.g. for deferred probing, runtime pm and backlight.


Return
======

``true`` if gmux is present and the kernel was configured with CONFIG_APPLE_GMUX, ``false`` otherwise.
