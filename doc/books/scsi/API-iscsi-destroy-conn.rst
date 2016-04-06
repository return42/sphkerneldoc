
.. _API-iscsi-destroy-conn:

==================
iscsi_destroy_conn
==================

*man iscsi_destroy_conn(9)*

*4.6.0-rc1*

destroy iscsi class connection


Synopsis
========

.. c:function:: int iscsi_destroy_conn( struct iscsi_cls_conn * conn )

Arguments
=========

``conn``
    iscsi cls session


Description
===========

This can be called from a LLD or iscsi_transport.
