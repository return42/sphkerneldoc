
.. _API-DECLARE-COMPLETION-ONSTACK:

==========================
DECLARE_COMPLETION_ONSTACK
==========================

*man DECLARE_COMPLETION_ONSTACK(9)*

*4.6.0-rc1*

declare and initialize a completion structure


Synopsis
========

.. c:function:: DECLARE_COMPLETION_ONSTACK( work )

Arguments
=========

``work``
    identifier for the completion structure


Description
===========

This macro declares and initializes a completion structure on the kernel stack.
