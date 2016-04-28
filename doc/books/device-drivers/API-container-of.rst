.. -*- coding: utf-8; mode: rst -*-

.. _API-container-of:

============
container_of
============

*man container_of(9)*

*4.6.0-rc5*

cast a member of a structure out to the containing structure


Synopsis
========

.. c:function:: container_of( ptr, type, member )

Arguments
=========

``ptr``
    the pointer to the member.

``type``
    the type of the container struct this is embedded in.

``member``
    the name of the member within the struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
