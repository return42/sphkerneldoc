.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-session-event:

===================
iscsi_session_event
===================

*man iscsi_session_event(9)*

*4.6.0-rc5*

send session destr. completion event


Synopsis
========

.. c:function:: int iscsi_session_event( struct iscsi_cls_session * session, enum iscsi_uevent_e event )

Arguments
=========

``session``
    iscsi class session

``event``
    type of event


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
