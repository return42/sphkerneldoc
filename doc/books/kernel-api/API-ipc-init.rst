.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-init:

========
ipc_init
========

*man ipc_init(9)*

*4.6.0-rc5*

initialise ipc subsystem


Synopsis
========

.. c:function:: int ipc_init( void )

Arguments
=========

``void``
    no arguments


Description
===========

The various sysv ipc resources (semaphores, messages and shared memory)
are initialised.

A callback routine is registered into the memory hotplug notifier


chain
=====

since msgmni scales to lowmem this callback routine will be called upon
successful memory add / remove to recompute msmgni.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
