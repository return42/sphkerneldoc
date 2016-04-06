
.. _API-blk-mangle-minor:

================
blk_mangle_minor
================

*man blk_mangle_minor(9)*

*4.6.0-rc1*

scatter minor numbers apart


Synopsis
========

.. c:function:: int blk_mangle_minor( int minor )

Arguments
=========

``minor``
    minor number to mangle


Description
===========

Scatter consecutively allocated ``minor`` number apart if MANGLE_DEVT is enabled. Mangling twice gives the original value.


RETURNS
=======

Mangled value.


CONTEXT
=======

Don't care.
