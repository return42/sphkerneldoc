
.. _API-iscsi-find-flashnode-conn:

=========================
iscsi_find_flashnode_conn
=========================

*man iscsi_find_flashnode_conn(9)*

*4.6.0-rc1*

finds flashnode connection entry


Synopsis
========

.. c:function:: struct device ⋆ iscsi_find_flashnode_conn( struct iscsi_bus_flash_session * fnode_sess )

Arguments
=========

``fnode_sess``
    pointer to parent flashnode session entry


Description
===========

Finds the flashnode connection object comparing the data passed using logic defined in passed function pointer


Returns
=======

pointer to found flashnode connection device object on success ``NULL`` on failure
