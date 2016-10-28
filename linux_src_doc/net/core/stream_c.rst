.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/stream.c

.. _`sk_stream_write_space`:

sk_stream_write_space
=====================

.. c:function:: void sk_stream_write_space(struct sock *sk)

    stream socket write_space callback.

    :param struct sock \*sk:
        socket

.. _`sk_stream_write_space.fixme`:

FIXME
-----

write proper description

.. _`sk_stream_wait_connect`:

sk_stream_wait_connect
======================

.. c:function:: int sk_stream_wait_connect(struct sock *sk, long *timeo_p)

    Wait for a socket to get into the connected state

    :param struct sock \*sk:
        sock to wait on

    :param long \*timeo_p:
        for how long to wait

.. _`sk_stream_wait_connect.description`:

Description
-----------

Must be called with the socket locked.

.. _`sk_stream_closing`:

sk_stream_closing
=================

.. c:function:: int sk_stream_closing(struct sock *sk)

    Return 1 if we still have things to send in our buffers.

    :param struct sock \*sk:
        socket to verify

.. _`sk_stream_wait_memory`:

sk_stream_wait_memory
=====================

.. c:function:: int sk_stream_wait_memory(struct sock *sk, long *timeo_p)

    Wait for more memory for a socket

    :param struct sock \*sk:
        socket to wait for memory

    :param long \*timeo_p:
        for how long

.. This file was automatic generated / don't edit.

