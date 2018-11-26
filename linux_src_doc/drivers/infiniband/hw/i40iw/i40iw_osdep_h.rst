.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_osdep.h

.. _`set_32bit_val`:

set_32bit_val
=============

.. c:function:: void set_32bit_val(u32 *wqe_words, u32 byte_index, u32 value)

    set 32 value to hw wqe

    :param wqe_words:
        wqe addr to write
    :type wqe_words: u32 \*

    :param byte_index:
        index in wqe
    :type byte_index: u32

    :param value:
        value to write
    :type value: u32

.. _`get_64bit_val`:

get_64bit_val
=============

.. c:function:: void get_64bit_val(u64 *wqe_words, u32 byte_index, u64 *value)

    read 64 bit value from wqe

    :param wqe_words:
        wqe addr
    :type wqe_words: u64 \*

    :param byte_index:
        index to read from
    :type byte_index: u32

    :param value:
        read value
    :type value: u64 \*

.. _`get_32bit_val`:

get_32bit_val
=============

.. c:function:: void get_32bit_val(u32 *wqe_words, u32 byte_index, u32 *value)

    read 32 bit value from wqe

    :param wqe_words:
        wqe addr
    :type wqe_words: u32 \*

    :param byte_index:
        index to reaad from
    :type byte_index: u32

    :param value:
        return 32 bit value
    :type value: u32 \*

.. This file was automatic generated / don't edit.

