.. -*- coding: utf-8; mode: rst -*-

.. _API-xprt-wait-for-buffer-space:

==========================
xprt_wait_for_buffer_space
==========================

*man xprt_wait_for_buffer_space(9)*

*4.6.0-rc5*

wait for transport output buffer to clear


Synopsis
========

.. c:function:: void xprt_wait_for_buffer_space( struct rpc_task * task, rpc_action action )

Arguments
=========

``task``
    task to be put to sleep

``action``
    function pointer to be executed after wait


Description
===========

Note that we only set the timer for the case of ``RPC_IS_SOFT``, since
we don't in general want to force a socket disconnection due to an
incomplete RPC call transmission.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
