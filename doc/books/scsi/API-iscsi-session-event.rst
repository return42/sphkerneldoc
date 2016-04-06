
.. _API-iscsi-session-event:

===================
iscsi_session_event
===================

*man iscsi_session_event(9)*

*4.6.0-rc1*

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
