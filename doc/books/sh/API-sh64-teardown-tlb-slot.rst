
.. _API-sh64-teardown-tlb-slot:

======================
sh64_teardown_tlb_slot
======================

*man sh64_teardown_tlb_slot(9)*

*4.6.0-rc1*

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
