.. -*- coding: utf-8; mode: rst -*-

.. _API-auditsc-get-stamp:

=================
auditsc_get_stamp
=================

*man auditsc_get_stamp(9)*

*4.6.0-rc5*

get local copies of audit_context values


Synopsis
========

.. c:function:: int auditsc_get_stamp( struct audit_context * ctx, struct timespec * t, unsigned int * serial )

Arguments
=========

``ctx``
    audit_context for the task

``t``
    timespec to store time recorded in the audit_context

``serial``
    serial value that is recorded in the audit_context


Description
===========

Also sets the context as auditable.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
