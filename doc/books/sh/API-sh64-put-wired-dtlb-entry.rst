.. -*- coding: utf-8; mode: rst -*-

.. _API-sh64-put-wired-dtlb-entry:

=========================
sh64_put_wired_dtlb_entry
=========================

*man sh64_put_wired_dtlb_entry(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
