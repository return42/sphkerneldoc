.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-dev-info-list-find:

=======================
scsi_dev_info_list_find
=======================

*man scsi_dev_info_list_find(9)*

*4.6.0-rc5*

find a matching dev_info list entry.


Synopsis
========

.. c:function:: struct scsi_dev_info_list * scsi_dev_info_list_find( const char * vendor, const char * model, int key )

Arguments
=========

``vendor``
    vendor string

``model``
    model (product) string

``key``
    specify list to use


Description
===========

Finds the first dev_info entry matching ``vendor``, ``model`` in list
specified by ``key``.


Returns
=======

pointer to matching entry, or ERR_PTR on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
