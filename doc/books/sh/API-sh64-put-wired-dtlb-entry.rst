
.. _API-sh64-put-wired-dtlb-entry:

=========================
sh64_put_wired_dtlb_entry
=========================

*man sh64_put_wired_dtlb_entry(9)*

*4.6.0-rc1*

Free a wired (locked-in) entry in the DTLB.


Synopsis
========

.. c:function:: int sh64_put_wired_dtlb_entry( unsigned long long entry )

Arguments
=========

``entry``
    Address of TLB slot.


Description
===========

Works like a stack, last one to allocate must be first one to free.
