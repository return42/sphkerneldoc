
.. _API-iscsi-unblock-session:

=====================
iscsi_unblock_session
=====================

*man iscsi_unblock_session(9)*

*4.6.0-rc1*

set a session as logged in and start IO.


Synopsis
========

.. c:function:: void iscsi_unblock_session( struct iscsi_cls_session * session )

Arguments
=========

``session``
    iscsi session


Description
===========

Mark a session as ready to accept IO.
