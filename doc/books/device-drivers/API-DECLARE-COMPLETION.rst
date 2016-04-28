.. -*- coding: utf-8; mode: rst -*-

.. _API-DECLARE-COMPLETION:

==================
DECLARE_COMPLETION
==================

*man DECLARE_COMPLETION(9)*

*4.6.0-rc5*

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

This macro declares and initializes a completion structure. Generally
used for static declarations. You should use the _ONSTACK variant for
automatic variables.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
