.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_osdep.h

.. _`set_32bit_val`:

set_32bit_val
=============

.. c:function:: void set_32bit_val(u32 *wqe_words, u32 byte_index, u32 value)

    set 32 value to hw wqe

    :param u32 \*wqe_words:
        wqe addr to write

    :param u32 byte_index:
        index in wqe

    :param u32 value:
        value to write

.. _`get_64bit_val`:

get_64bit_val
=============

.. c:function:: void get_64bit_val(u64 *wqe_words, u32 byte_index, u64 *value)

    read 64 bit value from wqe

    :param u64 \*wqe_words:
        wqe addr

    :param u32 byte_index:
        index to read from

    :param u64 \*value:
        read value

.. _`get_32bit_val`:

get_32bit_val
=============

.. c:function:: void get_32bit_val(u32 *wqe_words, u32 byte_index, u32 *value)

    read 32 bit value from wqe

    :param u32 \*wqe_words:
        wqe addr

    :param u32 byte_index:
        index to reaad from

    :param u32 \*value:
        return 32 bit value

.. This file was automatic generated / don't edit.

