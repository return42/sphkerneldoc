.. -*- coding: utf-8; mode: rst -*-

===============
videobuf-core.c
===============



.. _xref___videobuf_free:

__videobuf_free
===============

.. c:function:: int __videobuf_free (struct videobuf_queue * q)

    free all the buffers and their control structures

    :param struct videobuf_queue * q:

        _undescribed_



Description
-----------



This function can only be called if streaming/reading is off, i.e. no buffers
are under control of the driver.


