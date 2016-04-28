.. -*- coding: utf-8; mode: rst -*-

.. _API-init-completion:

===============
init_completion
===============

*man init_completion(9)*

*4.6.0-rc5*

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

This inline function will initialize a dynamically created completion
structure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
