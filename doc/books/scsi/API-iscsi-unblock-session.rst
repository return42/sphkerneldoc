.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-unblock-session:

=====================
iscsi_unblock_session
=====================

*man iscsi_unblock_session(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
