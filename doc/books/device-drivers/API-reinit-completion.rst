.. -*- coding: utf-8; mode: rst -*-

.. _API-reinit-completion:

=================
reinit_completion
=================

*man reinit_completion(9)*

*4.6.0-rc5*

reinitialize a completion structure


Synopsis
========

.. c:function:: void reinit_completion( struct completion * x )

Arguments
=========

``x``
    pointer to completion structure that is to be reinitialized


Description
===========

This inline function should be used to reinitialize a completion
structure so it can be reused. This is especially important after
``complete_all`` is used.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
