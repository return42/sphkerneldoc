.. -*- coding: utf-8; mode: rst -*-

.. _API-input-free-minor:

================
input_free_minor
================

*man input_free_minor(9)*

*4.6.0-rc5*

release previously allocated minor


Synopsis
========

.. c:function:: void input_free_minor( unsigned int minor )

Arguments
=========

``minor``
    minor to be released


Description
===========

This function releases previously allocated input minor so that it can
be reused later.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
