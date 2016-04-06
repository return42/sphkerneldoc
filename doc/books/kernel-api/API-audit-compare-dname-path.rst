
.. _API-audit-compare-dname-path:

========================
audit_compare_dname_path
========================

*man audit_compare_dname_path(9)*

*4.6.0-rc1*

compare given dentry name with last component in given path. Return of 0 indicates a match.


Synopsis
========

.. c:function:: int audit_compare_dname_path( const char * dname, const char * path, int parentlen )

Arguments
=========

``dname``
    dentry name that we're comparing

``path``
    full pathname that we're comparing

``parentlen``
    length of the parent if known. Passing in AUDIT_NAME_FULL here indicates that we must compute this value.
