
.. _API-iscsi-find-flashnode-sess:

=========================
iscsi_find_flashnode_sess
=========================

*man iscsi_find_flashnode_sess(9)*

*4.6.0-rc1*

finds flashnode session entry


Synopsis
========

.. c:function:: struct device ⋆ iscsi_find_flashnode_sess( struct Scsi_Host * shost, void * data, int (*fn) struct device *dev, void *data )

Arguments
=========

``shost``
    pointer to host data

``data``
    pointer to data containing value to use for comparison

``fn``
    function pointer that does actual comparison


Description
===========

Finds the flashnode session object comparing the data passed using logic defined in passed function pointer


Returns
=======

pointer to found flashnode session device object on success ``NULL`` on failure
