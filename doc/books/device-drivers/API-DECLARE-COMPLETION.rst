
.. _API-DECLARE-COMPLETION:

==================
DECLARE_COMPLETION
==================

*man DECLARE_COMPLETION(9)*

*4.6.0-rc1*

declare and initialize a completion structure


Synopsis
========

.. c:function:: DECLARE_COMPLETION( work )

Arguments
=========

``work``
    identifier for the completion structure


Description
===========

This macro declares and initializes a completion structure. Generally used for static declarations. You should use the _ONSTACK variant for automatic variables.
