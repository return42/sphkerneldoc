.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/meson/meson_sm.c

.. _`meson_sm_call`:

meson_sm_call
=============

.. c:function:: int meson_sm_call(unsigned int cmd_index, u32 *ret, u32 arg0, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    generic SMC32 call to the secure-monitor

    :param unsigned int cmd_index:
        Index of the SMC32 function ID

    :param u32 \*ret:
        Returned value

    :param u32 arg0:
        SMC32 Argument 0

    :param u32 arg1:
        SMC32 Argument 1

    :param u32 arg2:
        SMC32 Argument 2

    :param u32 arg3:
        SMC32 Argument 3

    :param u32 arg4:
        SMC32 Argument 4

.. _`meson_sm_call.return`:

Return
------

0 on success, a negative value on error

.. _`meson_sm_call_read`:

meson_sm_call_read
==================

.. c:function:: int meson_sm_call_read(void *buffer, unsigned int bsize, unsigned int cmd_index, u32 arg0, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    retrieve data from secure-monitor

    :param void \*buffer:
        Buffer to store the retrieved data

    :param unsigned int bsize:
        Size of the buffer

    :param unsigned int cmd_index:
        Index of the SMC32 function ID

    :param u32 arg0:
        SMC32 Argument 0

    :param u32 arg1:
        SMC32 Argument 1

    :param u32 arg2:
        SMC32 Argument 2

    :param u32 arg3:
        SMC32 Argument 3

    :param u32 arg4:
        SMC32 Argument 4

.. _`meson_sm_call_read.return`:

Return
------

size of read data on success, a negative value on error
When 0 is returned there is no guarantee about the amount of
data read and bsize bytes are copied in buffer.

.. _`meson_sm_call_write`:

meson_sm_call_write
===================

.. c:function:: int meson_sm_call_write(void *buffer, unsigned int size, unsigned int cmd_index, u32 arg0, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    send data to secure-monitor

    :param void \*buffer:
        Buffer containing data to send

    :param unsigned int size:
        Size of the data to send

    :param unsigned int cmd_index:
        Index of the SMC32 function ID

    :param u32 arg0:
        SMC32 Argument 0

    :param u32 arg1:
        SMC32 Argument 1

    :param u32 arg2:
        SMC32 Argument 2

    :param u32 arg3:
        SMC32 Argument 3

    :param u32 arg4:
        SMC32 Argument 4

.. _`meson_sm_call_write.return`:

Return
------

size of sent data on success, a negative value on error

.. This file was automatic generated / don't edit.

