.. -*- coding: utf-8; mode: rst -*-

.. _API-audit-log:

=========
audit_log
=========

*man audit_log(9)*

*4.6.0-rc5*

Log an audit record


Synopsis
========

.. c:function:: void audit_log( struct audit_context * ctx, gfp_t gfp_mask, int type, const char * fmt, ... )

Arguments
=========

``ctx``
    audit context

``gfp_mask``
    type of allocation

``type``
    audit message type

``fmt``
    format string to use @...: variable parameters matching the format
    string

``...``
    variable arguments


Description
===========

This is a convenience function that calls audit_log_start,
audit_log_vformat, and audit_log_end. It may be called in any
context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
