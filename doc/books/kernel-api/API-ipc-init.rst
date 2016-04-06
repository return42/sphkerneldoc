
.. _API-ipc-init:

========
ipc_init
========

*man ipc_init(9)*

*4.6.0-rc1*

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

The various sysv ipc resources (semaphores, messages and shared memory) are initialised.

A callback routine is registered into the memory hotplug notifier


chain
=====

since msgmni scales to lowmem this callback routine will be called upon successful memory add / remove to recompute msmgni.
