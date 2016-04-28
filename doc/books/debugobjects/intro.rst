.. -*- coding: utf-8; mode: rst -*-

.. _intro:

============
Introduction
============

debugobjects is a generic infrastructure to track the life time of
kernel objects and validate the operations on those.

debugobjects is useful to check for the following error patterns:

-  Activation of uninitialized objects

-  Initialization of active objects

-  Usage of freed/destroyed objects

debugobjects is not changing the data structure of the real object so it
can be compiled in with a minimal runtime impact and enabled on demand
with a kernel command line option.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
