.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-destroy-session:

=====================
iscsi_destroy_session
=====================

*man iscsi_destroy_session(9)*

*4.6.0-rc5*

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

Can be called by a LLD or iscsi_transport. There must not be any
running connections.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
