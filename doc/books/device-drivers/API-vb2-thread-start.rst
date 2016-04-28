.. -*- coding: utf-8; mode: rst -*-

.. _API-vb2-thread-start:

================
vb2_thread_start
================

*man vb2_thread_start(9)*

*4.6.0-rc5*

start a thread for the given queue.


Synopsis
========

.. c:function:: int vb2_thread_start( struct vb2_queue * q, vb2_thread_fnc fnc, void * priv, const char * thread_name )

Arguments
=========

``q``
    videobuf queue

``fnc``
    callback function

``priv``
    priv pointer passed to the callback function

``thread_name``
    the name of the thread. This will be prefixed with “vb2-”.


Description
===========

This starts a thread that will queue and dequeue until an error occurs
or ``vb2_thread_stop`` is called.

This function should not be used for anything else but the videobuf2-dvb
support. If you think you have another good use-case for this, then
please contact the linux-media mailinglist first.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
