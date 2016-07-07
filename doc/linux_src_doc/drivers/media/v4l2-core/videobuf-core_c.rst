.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/videobuf-core.c

.. _`__videobuf_free`:

__videobuf_free
===============

.. c:function:: int __videobuf_free(struct videobuf_queue *q)

    free all the buffers and their control structures

    :param struct videobuf_queue \*q:
        *undescribed*

.. _`__videobuf_free.description`:

Description
-----------

This function can only be called if streaming/reading is off, i.e. no buffers
are under control of the driver.

.. This file was automatic generated / don't edit.

