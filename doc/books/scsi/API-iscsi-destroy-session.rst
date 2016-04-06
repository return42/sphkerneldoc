
.. _API-iscsi-destroy-session:

=====================
iscsi_destroy_session
=====================

*man iscsi_destroy_session(9)*

*4.6.0-rc1*

destroy iscsi session


Synopsis
========

.. c:function:: int iscsi_destroy_session( struct iscsi_cls_session * session )

Arguments
=========

``session``
    iscsi_session


Description
===========

Can be called by a LLD or iscsi_transport. There must not be any running connections.
