
.. _API---audit-log-capset:

==================
__audit_log_capset
==================

*man __audit_log_capset(9)*

*4.6.0-rc1*

store information about the arguments to the capset syscall


Synopsis
========

.. c:function:: void __audit_log_capset( const struct cred * new, const struct cred * old )

Arguments
=========

``new``
    the new credentials

``old``
    the old (current) credentials


Description
===========

Record the arguments userspace sent to sys_capset for later printing by the audit system if applicable
