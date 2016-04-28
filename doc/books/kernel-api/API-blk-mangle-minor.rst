.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-mangle-minor:

================
blk_mangle_minor
================

*man blk_mangle_minor(9)*

*4.6.0-rc5*

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

Scatter consecutively allocated ``minor`` number apart if MANGLE_DEVT
is enabled. Mangling twice gives the original value.


RETURNS
=======

Mangled value.


CONTEXT
=======

Don't care.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
