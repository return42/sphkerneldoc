.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/msg.h

.. _`buf_headroom`:

BUF_HEADROOM
============

.. c:function::  BUF_HEADROOM()

.. _`buf_headroom.description`:

Description
-----------

TIPC message buffer headroom reserves space for the worst-case
link-level device header (in case the message is sent off-node).

.. _`buf_headroom.note`:

Note
----

Headroom should be a multiple of 4 to ensure the TIPC header fields
are word aligned for quicker access

.. This file was automatic generated / don't edit.

