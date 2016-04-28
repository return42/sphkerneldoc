.. -*- coding: utf-8; mode: rst -*-

.. _API-audit-log-secctx:

================
audit_log_secctx
================

*man audit_log_secctx(9)*

*4.6.0-rc5*

Converts and logs SELinux context


Synopsis
========

.. c:function:: void audit_log_secctx( struct audit_buffer * ab, u32 secid )

Arguments
=========

``ab``
    audit_buffer

``secid``
    security number


Description
===========

This is a helper function that calls security_secid_to_secctx to
convert secid to secctx and then adds the (converted) SELinux context to
the audit log by calling audit_log_format, thus also preventing leak
of internal secid to userspace. If secid cannot be converted
audit_panic is called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
