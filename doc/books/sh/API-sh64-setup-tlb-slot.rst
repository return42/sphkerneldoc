.. -*- coding: utf-8; mode: rst -*-

.. _API-sh64-setup-tlb-slot:

===================
sh64_setup_tlb_slot
===================

*man sh64_setup_tlb_slot(9)*

*4.6.0-rc5*

Load up a translation in a wired slot.


Synopsis
========

.. c:function:: void sh64_setup_tlb_slot( unsigned long long config_addr, unsigned long eaddr, unsigned long asid, unsigned long paddr )

Arguments
=========

``config_addr``
    Address of TLB slot.

``eaddr``
    Virtual address.

``asid``
    Address Space Identifier.

``paddr``
    Physical address.


Description
===========

Load up a virtual<->physical translation for ``eaddr``\ <->``paddr`` in
the pre-allocated TLB slot ``config_addr`` (see
sh64_get_wired_dtlb_entry).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
