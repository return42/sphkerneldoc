.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-destroy-conn:

==================
iscsi_destroy_conn
==================

*man iscsi_destroy_conn(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
