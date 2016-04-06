
.. _API-init-completion:

===============
init_completion
===============

*man init_completion(9)*

*4.6.0-rc1*

Initialize a dynamically allocated completion


Synopsis
========

.. c:function:: void init_completion( struct completion * x )

Arguments
=========

``x``
    pointer to completion structure that is to be initialized


Description
===========

This inline function will initialize a dynamically created completion structure.
