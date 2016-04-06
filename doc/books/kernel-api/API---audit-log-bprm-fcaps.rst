
.. _API---audit-log-bprm-fcaps:

======================
__audit_log_bprm_fcaps
======================

*man __audit_log_bprm_fcaps(9)*

*4.6.0-rc1*

store information about a loading bprm and relevant fcaps


Synopsis
========

.. c:function:: int __audit_log_bprm_fcaps( struct linux_binprm * bprm, const struct cred * new, const struct cred * old )

Arguments
=========

``bprm``
    pointer to the bprm being processed

``new``
    the proposed new credentials

``old``
    the old credentials


Description
===========

Simply check if the proc already has the caps given by the file and if not store the priv escalation info for later auditing at the end of the syscall

-Eric
