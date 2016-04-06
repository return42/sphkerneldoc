
.. _API-mpt-ioc-reset:

=============
mpt_ioc_reset
=============

*man mpt_ioc_reset(9)*

*4.6.0-rc1*

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
