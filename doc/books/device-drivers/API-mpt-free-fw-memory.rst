.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-free-fw-memory:

==================
mpt_free_fw_memory
==================

*man mpt_free_fw_memory(9)*

*4.6.0-rc5*

free firmware memory


Synopsis
========

.. c:function:: void mpt_free_fw_memory( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure


Description
===========

If alt_img is NULL, delete from ioc structure. Else, delete a secondary
image in same format.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
