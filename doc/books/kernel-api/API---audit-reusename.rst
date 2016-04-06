
.. _API---audit-reusename:

=================
__audit_reusename
=================

*man __audit_reusename(9)*

*4.6.0-rc1*

fill out filename with info from existing entry


Synopsis
========

.. c:function:: struct filename ⋆ __audit_reusename( const __user char * uptr )

Arguments
=========

``uptr``
    userland ptr to pathname


Description
===========

Search the audit_names list for the current audit context. If there is an existing entry with a matching “uptr” then return the filename associated with that audit_name. If not,
return NULL.
