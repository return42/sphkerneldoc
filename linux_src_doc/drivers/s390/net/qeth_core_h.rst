.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/qeth_core.h

.. _`qeth_tx_timeout`:

QETH_TX_TIMEOUT
===============

.. c:function::  QETH_TX_TIMEOUT()

.. _`qeth_cmd_buffer_no`:

QETH_CMD_BUFFER_NO
==================

.. c:function::  QETH_CMD_BUFFER_NO()

.. _`qeth_get_elements_for_range`:

qeth_get_elements_for_range
===========================

.. c:function:: int qeth_get_elements_for_range(addr_t start, addr_t end)

    find number of SBALEs to cover range.

    :param start:
        Start of the address range.
    :type start: addr_t

    :param end:
        Address after the end of the range.
    :type end: addr_t

.. _`qeth_get_elements_for_range.description`:

Description
-----------

Returns the number of pages, and thus QDIO buffer elements, needed to cover
the specified address range.

.. This file was automatic generated / don't edit.

