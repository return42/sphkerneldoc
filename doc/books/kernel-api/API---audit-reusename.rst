.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-reusename:

=================
__audit_reusename
=================

*man __audit_reusename(9)*

*4.6.0-rc5*

fill out filename with info from existing entry


Synopsis
========

.. c:function:: struct filename * __audit_reusename( const __user char * uptr )

Arguments
=========

``uptr``
    userland ptr to pathname


Description
===========

Search the audit_names list for the current audit context. If there is
an existing entry with a matching “uptr” then return the filename
associated with that audit_name. If not, return NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
