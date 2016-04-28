.. -*- coding: utf-8; mode: rst -*-

.. _API-audit-log-format:

================
audit_log_format
================

*man audit_log_format(9)*

*4.6.0-rc5*

format a message into the audit buffer.


Synopsis
========

.. c:function:: void audit_log_format( struct audit_buffer * ab, const char * fmt, ... )

Arguments
=========

``ab``
    audit_buffer

``fmt``
    format string @...: optional parameters matching ``fmt`` string

``...``
    variable arguments


Description
===========

All the work is done in audit_log_vformat.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
