.. -*- coding: utf-8; mode: rst -*-

.. _API-init-rcu-head-on-stack:

======================
init_rcu_head_on_stack
======================

*man init_rcu_head_on_stack(9)*

*4.6.0-rc5*

initialize on-stack rcu_head for debugobjects


Synopsis
========

.. c:function:: void init_rcu_head_on_stack( struct rcu_head * head )

Arguments
=========

``head``
    pointer to rcu_head structure to be initialized


Description
===========

This function informs debugobjects of a new rcu_head structure that has
been allocated as an auto variable on the stack. This function is not
required for rcu_head structures that are statically defined or that
are dynamically allocated on the heap. This function has no effect for
!CONFIG_DEBUG_OBJECTS_RCU_HEAD kernel builds.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
