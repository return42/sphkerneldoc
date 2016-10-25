.. -*- coding: utf-8; mode: rst -*-

.. _drivers:

************************
RapidIO driver interface
************************

Drivers are provided a set of calls in order to interface with the
subsystem to gather info on devices, request/map memory region
resources, and manage mailboxes/doorbells.


.. _Functions:

Functions
=========


.. kernel-doc:: include/linux/rio_drv.h
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/rapidio/rio-driver.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/rapidio/rio.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
