.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/stream.c

.. _`sk_stream_write_space`:

sk_stream_write_space
=====================

.. c:function:: void sk_stream_write_space(struct sock *sk)

    stream socket write_space callback.

    :param sk:
        socket
    :type sk: struct sock \*

.. _`sk_stream_write_space.description`:

Description
-----------

FIXME: write proper description

.. _`sk_stream_wait_connect`:

sk_stream_wait_connect
======================

.. c:function:: int sk_stream_wait_connect(struct sock *sk, long *timeo_p)

    Wait for a socket to get into the connected state

    :param sk:
        sock to wait on
    :type sk: struct sock \*

    :param timeo_p:
        for how long to wait
    :type timeo_p: long \*

.. _`sk_stream_wait_connect.description`:

Description
-----------

Must be called with the socket locked.

.. _`sk_stream_closing`:

sk_stream_closing
=================

.. c:function:: int sk_stream_closing(struct sock *sk)

    Return 1 if we still have things to send in our buffers.

    :param sk:
        socket to verify
    :type sk: struct sock \*

.. _`sk_stream_wait_memory`:

sk_stream_wait_memory
=====================

.. c:function:: int sk_stream_wait_memory(struct sock *sk, long *timeo_p)

    Wait for more memory for a socket

    :param sk:
        socket to wait for memory
    :type sk: struct sock \*

    :param timeo_p:
        for how long
    :type timeo_p: long \*

.. This file was automatic generated / don't edit.

