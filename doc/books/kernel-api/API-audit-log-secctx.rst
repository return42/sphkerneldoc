
.. _API-audit-log-secctx:

================
audit_log_secctx
================

*man audit_log_secctx(9)*

*4.6.0-rc1*

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

This is a helper function that calls security_secid_to_secctx to convert secid to secctx and then adds the (converted) SELinux context to the audit log by calling
audit_log_format, thus also preventing leak of internal secid to userspace. If secid cannot be converted audit_panic is called.
