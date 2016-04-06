
.. _API-init-rcu-head-on-stack:

======================
init_rcu_head_on_stack
======================

*man init_rcu_head_on_stack(9)*

*4.6.0-rc1*

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

This function informs debugobjects of a new rcu_head structure that has been allocated as an auto variable on the stack. This function is not required for rcu_head structures
that are statically defined or that are dynamically allocated on the heap. This function has no effect for !CONFIG_DEBUG_OBJECTS_RCU_HEAD kernel builds.
