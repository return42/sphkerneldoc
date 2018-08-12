.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/qcom/qdsp6/q6routing.c

.. _`q6routing_stream_open`:

q6routing_stream_open
=====================

.. c:function:: int q6routing_stream_open(int fedai_id, int perf_mode, int stream_id, int stream_type)

    Register a new stream for route setup

    :param int fedai_id:
        Frontend dai id.

    :param int perf_mode:
        Performance mode.

    :param int stream_id:
        ASM stream id to map.

    :param int stream_type:
        Direction of stream

.. _`q6routing_stream_open.return`:

Return
------

Will be an negative on error or a zero on success.

.. _`q6routing_stream_close`:

q6routing_stream_close
======================

.. c:function:: void q6routing_stream_close(int fedai_id, int stream_type)

    Deregister a stream

    :param int fedai_id:
        Frontend dai id.

    :param int stream_type:
        Direction of stream

.. _`q6routing_stream_close.return`:

Return
------

Will be an negative on error or a zero on success.

.. This file was automatic generated / don't edit.

