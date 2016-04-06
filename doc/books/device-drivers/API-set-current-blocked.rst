
.. _API-set-current-blocked:

===================
set_current_blocked
===================

*man set_current_blocked(9)*

*4.6.0-rc1*

change current->blocked mask


Synopsis
========

.. c:function:: void set_current_blocked( sigset_t * newset )

Arguments
=========

``newset``
    new mask


Description
===========

It is wrong to change ->blocked directly, this helper should be used to ensure the process can't miss a shared signal we are going to block.
