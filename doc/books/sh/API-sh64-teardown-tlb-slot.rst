.. -*- coding: utf-8; mode: rst -*-

.. _API-sh64-teardown-tlb-slot:

======================
sh64_teardown_tlb_slot
======================

*man sh64_teardown_tlb_slot(9)*

*4.6.0-rc5*

Teardown a translation.


Synopsis
========

.. c:function:: void sh64_teardown_tlb_slot( unsigned long long config_addr )

Arguments
=========

``config_addr``
    Address of TLB slot.


Description
===========

Teardown any existing mapping in the TLB slot ``config_addr``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
