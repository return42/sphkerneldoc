.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/meson/meson_sm.c

.. _`meson_sm_call`:

meson_sm_call
=============

.. c:function:: int meson_sm_call(unsigned int cmd_index, u32 *ret, u32 arg0, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    generic SMC32 call to the secure-monitor

    :param cmd_index:
        Index of the SMC32 function ID
    :type cmd_index: unsigned int

    :param ret:
        Returned value
    :type ret: u32 \*

    :param arg0:
        SMC32 Argument 0
    :type arg0: u32

    :param arg1:
        SMC32 Argument 1
    :type arg1: u32

    :param arg2:
        SMC32 Argument 2
    :type arg2: u32

    :param arg3:
        SMC32 Argument 3
    :type arg3: u32

    :param arg4:
        SMC32 Argument 4
    :type arg4: u32

.. _`meson_sm_call.return`:

Return
------

0 on success, a negative value on error

.. _`meson_sm_call_read`:

meson_sm_call_read
==================

.. c:function:: int meson_sm_call_read(void *buffer, unsigned int bsize, unsigned int cmd_index, u32 arg0, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    retrieve data from secure-monitor

    :param buffer:
        Buffer to store the retrieved data
    :type buffer: void \*

    :param bsize:
        Size of the buffer
    :type bsize: unsigned int

    :param cmd_index:
        Index of the SMC32 function ID
    :type cmd_index: unsigned int

    :param arg0:
        SMC32 Argument 0
    :type arg0: u32

    :param arg1:
        SMC32 Argument 1
    :type arg1: u32

    :param arg2:
        SMC32 Argument 2
    :type arg2: u32

    :param arg3:
        SMC32 Argument 3
    :type arg3: u32

    :param arg4:
        SMC32 Argument 4
    :type arg4: u32

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

    :param buffer:
        Buffer containing data to send
    :type buffer: void \*

    :param size:
        Size of the data to send
    :type size: unsigned int

    :param cmd_index:
        Index of the SMC32 function ID
    :type cmd_index: unsigned int

    :param arg0:
        SMC32 Argument 0
    :type arg0: u32

    :param arg1:
        SMC32 Argument 1
    :type arg1: u32

    :param arg2:
        SMC32 Argument 2
    :type arg2: u32

    :param arg3:
        SMC32 Argument 3
    :type arg3: u32

    :param arg4:
        SMC32 Argument 4
    :type arg4: u32

.. _`meson_sm_call_write.return`:

Return
------

size of sent data on success, a negative value on error

.. This file was automatic generated / don't edit.

