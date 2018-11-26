.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/tcp_cdg.c

.. _`nexp_u32`:

nexp_u32
========

.. c:function:: u32 __pure nexp_u32(u32 ux)

    negative base-e exponential

    :param ux:
        x in units of micro
    :type ux: u32

.. _`nexp_u32.description`:

Description
-----------

Returns exp(ux \* -1e-6) \* U32_MAX.

.. This file was automatic generated / don't edit.

