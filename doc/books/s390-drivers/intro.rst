.. -*- coding: utf-8; mode: rst -*-

.. _intro:

************
Introduction
************

This document describes the interfaces available for device drivers that
drive s390 based channel attached I/O devices. This includes interfaces
for interaction with the hardware and interfaces for interacting with
the common driver core. Those interfaces are provided by the s390 common
I/O layer.

The document assumes a familarity with the technical terms associated
with the s390 channel I/O architecture. For a description of this
architecture, please refer to the "z/Architecture: Principles of
Operation", IBM publication no. SA22-7832.

While most I/O devices on a s390 system are typically driven through the
channel I/O mechanism described here, there are various other methods
(like the diag interface). These are out of the scope of this document.

Some additional information can also be found in the kernel source under
Documentation/s390/driver-model.txt.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
