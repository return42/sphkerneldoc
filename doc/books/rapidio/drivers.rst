.. -*- coding: utf-8; mode: rst -*-

.. _drivers:

========================
RapidIO driver interface
========================

Drivers are provided a set of calls in order to interface with the
subsystem to gather info on devices, request/map memory region
resources, and manage mailboxes/doorbells.


.. _Functions:

Functions
=========


.. kernel-doc:: include/linux/rio_drv.h
    :internal:

.. kernel-doc:: drivers/rapidio/rio-driver.c
    :export:

.. kernel-doc:: drivers/rapidio/rio.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
