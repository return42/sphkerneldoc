
.. _API-scsi-dev-info-list-find:

=======================
scsi_dev_info_list_find
=======================

*man scsi_dev_info_list_find(9)*

*4.6.0-rc1*

find a matching dev_info list entry.


Synopsis
========

.. c:function:: struct scsi_dev_info_list ⋆ scsi_dev_info_list_find( const char * vendor, const char * model, int key )

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

Finds the first dev_info entry matching ``vendor``, ``model`` in list specified by ``key``.


Returns
=======

pointer to matching entry, or ERR_PTR on failure.
