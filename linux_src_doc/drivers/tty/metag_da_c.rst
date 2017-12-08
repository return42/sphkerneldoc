.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/metag_da.c

.. _`dashtty_port`:

struct dashtty_port
===================

.. c:type:: struct dashtty_port

    Wrapper struct for dashtty tty_port.

.. _`dashtty_port.definition`:

Definition
----------

.. code-block:: c

    struct dashtty_port {
        struct tty_port port;
        spinlock_t rx_lock;
        void *rx_buf;
        struct mutex xmit_lock;
        unsigned int xmit_cnt;
        unsigned int xmit_head;
        unsigned int xmit_tail;
        struct completion xmit_empty;
    }

.. _`dashtty_port.members`:

Members
-------

port
    TTY port data

rx_lock
    Lock for rx_buf.
    This protects between the poll timer and user context.
    It's also held during read SWITCH operations.

rx_buf
    Read buffer

xmit_lock
    Lock for xmit\_\*, and port.xmit_buf.
    This protects between user context and kernel thread.
    It's also held during write SWITCH operations.

xmit_cnt
    Size of xmit buffer contents

xmit_head
    Head of xmit buffer where data is written

xmit_tail
    Tail of xmit buffer where data is read

xmit_empty
    Completion for xmit buffer being empty

.. _`find_channel_to_poll`:

find_channel_to_poll
====================

.. c:function:: int find_channel_to_poll( void)

    Returns number of the next channel to poll.

    :param  void:
        no arguments

.. _`find_channel_to_poll.return`:

Return
------

The number of the next channel to poll, or -1 if none need
polling.

.. _`put_channel_data`:

put_channel_data
================

.. c:function:: int put_channel_data(unsigned int chan)

    Write out a block of channel data.

    :param unsigned int chan:
        DA channel number.

.. _`put_channel_data.description`:

Description
-----------

Write a single block of data out to the debug adapter. If the circular buffer
is wrapped then only the first block is written.

.. _`put_channel_data.return`:

Return
------

1 if the remote buffer was too full to accept data.
0 otherwise.

.. _`put_data`:

put_data
========

.. c:function:: int put_data(void *arg)

    Kernel thread to write out blocks of channel data to DA.

    :param void \*arg:
        Unused.

.. _`put_data.description`:

Description
-----------

This kernel thread runs while \ ``dashtty_xmit_cnt``\  != 0, and loops over the
channels to write out any buffered data. If any of the channels stall due to
the remote buffer being full, a hold off happens to allow the debugger to
drain the buffer.

.. _`dashtty_put_timer`:

dashtty_put_timer
=================

.. c:function:: void dashtty_put_timer(struct timer_list *unused)

    Delayed wake up of kernel thread.

    :param struct timer_list \*unused:
        *undescribed*

.. _`dashtty_put_timer.description`:

Description
-----------

This timer function wakes up the kernel thread if any data exists in the
buffers. It is used to delay the expensive writeout until the writer has
stopped writing.

.. This file was automatic generated / don't edit.

