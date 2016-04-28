.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-ioc-reset:

=============
mpt_ioc_reset
=============

*man mpt_ioc_reset(9)*

*4.6.0-rc5*

Base cleanup for hard reset


Synopsis
========

.. c:function:: int mpt_ioc_reset( MPT_ADAPTER * ioc, int reset_phase )

Arguments
=========

``ioc``
    Pointer to the adapter structure

``reset_phase``
    Indicates pre- or post-reset functionality


Remark
======

Frees resources with internally generated commands.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
