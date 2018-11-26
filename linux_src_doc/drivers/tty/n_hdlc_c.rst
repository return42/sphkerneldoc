.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/n_hdlc.c

.. _`n_hdlc`:

struct n_hdlc
=============

.. c:type:: struct n_hdlc

    per device instance data structure \ ``magic``\  - magic value for structure \ ``flags``\  - miscellaneous control flags \ ``tty``\  - ptr to TTY structure \ ``backup_tty``\  - TTY to use if tty gets closed \ ``tbusy``\  - reentrancy flag for tx wakeup code

.. _`n_hdlc.definition`:

Definition
----------

.. code-block:: c

    struct n_hdlc {
        int magic;
        __u32 flags;
        struct tty_struct *tty;
        struct tty_struct *backup_tty;
        int tbusy;
        int woke_up;
        struct n_hdlc_buf_list tx_buf_list;
        struct n_hdlc_buf_list rx_buf_list;
        struct n_hdlc_buf_list tx_free_buf_list;
        struct n_hdlc_buf_list rx_free_buf_list;
    }

.. _`n_hdlc.members`:

Members
-------

magic
    *undescribed*

flags
    *undescribed*

tty
    *undescribed*

backup_tty
    *undescribed*

tbusy
    *undescribed*

woke_up
    describe this field
    \ ``tx_buf_list``\  - list of pending transmit frame buffers
    \ ``rx_buf_list``\  - list of received frame buffers
    \ ``tx_free_buf_list``\  - list unused transmit frame buffers
    \ ``rx_free_buf_list``\  - list unused received frame buffers

tx_buf_list
    *undescribed*

rx_buf_list
    *undescribed*

tx_free_buf_list
    *undescribed*

rx_free_buf_list
    *undescribed*

.. _`n_hdlc_release`:

n_hdlc_release
==============

.. c:function:: void n_hdlc_release(struct n_hdlc *n_hdlc)

    release an n_hdlc per device line discipline info structure \ ``n_hdlc``\  - per device line discipline info structure

    :param n_hdlc:
        *undescribed*
    :type n_hdlc: struct n_hdlc \*

.. _`n_hdlc_tty_close`:

n_hdlc_tty_close
================

.. c:function:: void n_hdlc_tty_close(struct tty_struct *tty)

    line discipline close \ ``tty``\  - pointer to tty info structure

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`n_hdlc_tty_close.description`:

Description
-----------

Called when the line discipline is changed to something
else, the tty is closed, or the tty detects a hangup.

.. _`n_hdlc_tty_open`:

n_hdlc_tty_open
===============

.. c:function:: int n_hdlc_tty_open(struct tty_struct *tty)

    called when line discipline changed to n_hdlc \ ``tty``\  - pointer to tty info structure

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`n_hdlc_tty_open.description`:

Description
-----------

Returns 0 if success, otherwise error code

.. _`n_hdlc_send_frames`:

n_hdlc_send_frames
==================

.. c:function:: void n_hdlc_send_frames(struct n_hdlc *n_hdlc, struct tty_struct *tty)

    send frames on pending send buffer list \ ``n_hdlc``\  - pointer to ldisc instance data \ ``tty``\  - pointer to tty instance data

    :param n_hdlc:
        *undescribed*
    :type n_hdlc: struct n_hdlc \*

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`n_hdlc_send_frames.description`:

Description
-----------

Send frames on pending send buffer list until the driver does not accept a
frame (busy) this function is called after adding a frame to the send buffer
list and by the tty wakeup callback.

.. _`n_hdlc_tty_wakeup`:

n_hdlc_tty_wakeup
=================

.. c:function:: void n_hdlc_tty_wakeup(struct tty_struct *tty)

    Callback for transmit wakeup \ ``tty``\  - pointer to associated tty instance data

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`n_hdlc_tty_wakeup.description`:

Description
-----------

Called when low level device driver can accept more send data.

.. _`n_hdlc_tty_receive`:

n_hdlc_tty_receive
==================

.. c:function:: void n_hdlc_tty_receive(struct tty_struct *tty, const __u8 *data, char *flags, int count)

    Called by tty driver when receive data is available \ ``tty``\  - pointer to tty instance data \ ``data``\  - pointer to received data \ ``flags``\  - pointer to flags for data \ ``count``\  - count of received data in bytes

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param data:
        *undescribed*
    :type data: const __u8 \*

    :param flags:
        *undescribed*
    :type flags: char \*

    :param count:
        *undescribed*
    :type count: int

.. _`n_hdlc_tty_receive.description`:

Description
-----------

Called by tty low level driver when receive data is available. Data is
interpreted as one HDLC frame.

.. _`n_hdlc_tty_read`:

n_hdlc_tty_read
===============

.. c:function:: ssize_t n_hdlc_tty_read(struct tty_struct *tty, struct file *file, __u8 __user *buf, size_t nr)

    Called to retrieve one frame of data (if available) \ ``tty``\  - pointer to tty instance data \ ``file``\  - pointer to open file object \ ``buf``\  - pointer to returned data buffer \ ``nr``\  - size of returned data buffer

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param file:
        *undescribed*
    :type file: struct file \*

    :param buf:
        *undescribed*
    :type buf: __u8 __user \*

    :param nr:
        *undescribed*
    :type nr: size_t

.. _`n_hdlc_tty_read.description`:

Description
-----------

Returns the number of bytes returned or error code.

.. _`n_hdlc_tty_write`:

n_hdlc_tty_write
================

.. c:function:: ssize_t n_hdlc_tty_write(struct tty_struct *tty, struct file *file, const unsigned char *data, size_t count)

    write a single frame of data to device \ ``tty``\  - pointer to associated tty device instance data \ ``file``\  - pointer to file object data \ ``data``\  - pointer to transmit data (one frame) \ ``count``\  - size of transmit frame in bytes

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param file:
        *undescribed*
    :type file: struct file \*

    :param data:
        *undescribed*
    :type data: const unsigned char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`n_hdlc_tty_write.description`:

Description
-----------

Returns the number of bytes written (or error code).

.. _`n_hdlc_tty_ioctl`:

n_hdlc_tty_ioctl
================

.. c:function:: int n_hdlc_tty_ioctl(struct tty_struct *tty, struct file *file, unsigned int cmd, unsigned long arg)

    process IOCTL system call for the tty device. \ ``tty``\  - pointer to tty instance data \ ``file``\  - pointer to open file object for device \ ``cmd``\  - IOCTL command code \ ``arg``\  - argument for IOCTL call (cmd dependent)

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param file:
        *undescribed*
    :type file: struct file \*

    :param cmd:
        *undescribed*
    :type cmd: unsigned int

    :param arg:
        *undescribed*
    :type arg: unsigned long

.. _`n_hdlc_tty_ioctl.description`:

Description
-----------

Returns command dependent result.

.. _`n_hdlc_tty_poll`:

n_hdlc_tty_poll
===============

.. c:function:: __poll_t n_hdlc_tty_poll(struct tty_struct *tty, struct file *filp, poll_table *wait)

    TTY callback for poll system call \ ``tty``\  - pointer to tty instance data \ ``filp``\  - pointer to open file object for device \ ``poll_table``\  - wait queue for operations

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param wait:
        *undescribed*
    :type wait: poll_table \*

.. _`n_hdlc_tty_poll.description`:

Description
-----------

Determine which operations (read/write) will not block and return info
to caller.
Returns a bit mask containing info on which ops will not block.

.. _`n_hdlc_alloc`:

n_hdlc_alloc
============

.. c:function:: struct n_hdlc *n_hdlc_alloc( void)

    allocate an n_hdlc instance data structure

    :param void:
        no arguments
    :type void: 

.. _`n_hdlc_alloc.description`:

Description
-----------

Returns a pointer to newly created structure if success, otherwise \ ``NULL``\ 

.. _`n_hdlc_buf_return`:

n_hdlc_buf_return
=================

.. c:function:: void n_hdlc_buf_return(struct n_hdlc_buf_list *buf_list, struct n_hdlc_buf *buf)

    put the HDLC buffer after the head of the specified list \ ``buf_list``\  - pointer to the buffer list \ ``buf``\  - pointer to the buffer

    :param buf_list:
        *undescribed*
    :type buf_list: struct n_hdlc_buf_list \*

    :param buf:
        *undescribed*
    :type buf: struct n_hdlc_buf \*

.. _`n_hdlc_buf_put`:

n_hdlc_buf_put
==============

.. c:function:: void n_hdlc_buf_put(struct n_hdlc_buf_list *buf_list, struct n_hdlc_buf *buf)

    add specified HDLC buffer to tail of specified list \ ``buf_list``\  - pointer to buffer list \ ``buf``\  - pointer to buffer

    :param buf_list:
        *undescribed*
    :type buf_list: struct n_hdlc_buf_list \*

    :param buf:
        *undescribed*
    :type buf: struct n_hdlc_buf \*

.. _`n_hdlc_buf_get`:

n_hdlc_buf_get
==============

.. c:function:: struct n_hdlc_buf *n_hdlc_buf_get(struct n_hdlc_buf_list *buf_list)

    remove and return an HDLC buffer from list \ ``buf_list``\  - pointer to HDLC buffer list

    :param buf_list:
        *undescribed*
    :type buf_list: struct n_hdlc_buf_list \*

.. _`n_hdlc_buf_get.description`:

Description
-----------

Remove and return an HDLC buffer from the head of the specified HDLC buffer
list.
Returns a pointer to HDLC buffer if available, otherwise \ ``NULL``\ .

.. This file was automatic generated / don't edit.

