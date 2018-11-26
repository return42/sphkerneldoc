.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/pty.c

.. _`pty_write`:

pty_write
=========

.. c:function:: int pty_write(struct tty_struct *tty, const unsigned char *buf, int c)

    write to a pty

    :param tty:
        the tty we write from
    :type tty: struct tty_struct \*

    :param buf:
        kernel buffer of data
    :type buf: const unsigned char \*

    :param c:
        *undescribed*
    :type c: int

.. _`pty_write.description`:

Description
-----------

Our "hardware" write method. Data is coming from the ldisc which
may be in a non sleeping state. We simply throw this at the other
end of the link as if we were an IRQ handler receiving stuff for
the other side of the pty/tty pair.

.. _`pty_write_room`:

pty_write_room
==============

.. c:function:: int pty_write_room(struct tty_struct *tty)

    write space

    :param tty:
        tty we are writing from
    :type tty: struct tty_struct \*

.. _`pty_write_room.description`:

Description
-----------

Report how many bytes the ldisc can send into the queue for
the other device.

.. _`pty_chars_in_buffer`:

pty_chars_in_buffer
===================

.. c:function:: int pty_chars_in_buffer(struct tty_struct *tty)

    characters currently in our tx queue

    :param tty:
        our tty
    :type tty: struct tty_struct \*

.. _`pty_chars_in_buffer.description`:

Description
-----------

Report how much we have in the transmit queue. As everything is
instantly at the other end this is easy to implement.

.. _`pty_resize`:

pty_resize
==========

.. c:function:: int pty_resize(struct tty_struct *tty, struct winsize *ws)

    resize event

    :param tty:
        tty being resized
    :type tty: struct tty_struct \*

    :param ws:
        window size being set.
    :type ws: struct winsize \*

.. _`pty_resize.description`:

Description
-----------

Update the termios variables and send the necessary signals to
peform a terminal resize correctly

.. _`pty_start`:

pty_start
=========

.. c:function:: void pty_start(struct tty_struct *tty)

    \ :c:func:`start`\  handler pty_stop  - \ :c:func:`stop`\  handler

    :param tty:
        tty being flow-controlled
    :type tty: struct tty_struct \*

.. _`pty_start.description`:

Description
-----------

Propagates the TIOCPKT status to the master pty.

NB: only the master pty can be in packet mode so only the slave
needs \ :c:func:`start`\ /stop() handlers

.. _`pty_common_install`:

pty_common_install
==================

.. c:function:: int pty_common_install(struct tty_driver *driver, struct tty_struct *tty, bool legacy)

    set up the pty pair

    :param driver:
        the pty driver
    :type driver: struct tty_driver \*

    :param tty:
        the tty being instantiated
    :type tty: struct tty_struct \*

    :param legacy:
        true if this is BSD style
    :type legacy: bool

.. _`pty_common_install.description`:

Description
-----------

Perform the initial set up for the tty/pty pair. Called from the
tty layer when the port is first opened.

.. _`pty_common_install.locking`:

Locking
-------

the caller must hold the tty_mutex

.. _`ptm_open_peer`:

ptm_open_peer
=============

.. c:function:: int ptm_open_peer(struct file *master, struct tty_struct *tty, int flags)

    open the peer of a pty

    :param master:
        the open struct file of the ptmx device node
    :type master: struct file \*

    :param tty:
        the master of the pty being opened
    :type tty: struct tty_struct \*

    :param flags:
        the flags for open
    :type flags: int

.. _`ptm_open_peer.description`:

Description
-----------

Provide a race free way for userspace to open the slave end of a pty
(where they have the master fd and cannot access or trust the mount
namespace /dev/pts was mounted inside).

.. _`ptm_unix98_lookup`:

ptm_unix98_lookup
=================

.. c:function:: struct tty_struct *ptm_unix98_lookup(struct tty_driver *driver, struct file *file, int idx)

    find a pty master

    :param driver:
        ptm driver
    :type driver: struct tty_driver \*

    :param file:
        *undescribed*
    :type file: struct file \*

    :param idx:
        tty index
    :type idx: int

.. _`ptm_unix98_lookup.description`:

Description
-----------

Look up a pty master device. Called under the tty_mutex for now.
This provides our locking.

.. _`pts_unix98_lookup`:

pts_unix98_lookup
=================

.. c:function:: struct tty_struct *pts_unix98_lookup(struct tty_driver *driver, struct file *file, int idx)

    find a pty slave

    :param driver:
        pts driver
    :type driver: struct tty_driver \*

    :param file:
        *undescribed*
    :type file: struct file \*

    :param idx:
        tty index
    :type idx: int

.. _`pts_unix98_lookup.description`:

Description
-----------

Look up a pty master device. Called under the tty_mutex for now.
This provides our locking for the tty pointer.

.. _`ptmx_open`:

ptmx_open
=========

.. c:function:: int ptmx_open(struct inode *inode, struct file *filp)

    open a unix 98 pty master

    :param inode:
        inode of device file
    :type inode: struct inode \*

    :param filp:
        file pointer to tty
    :type filp: struct file \*

.. _`ptmx_open.description`:

Description
-----------

Allocate a unix98 pty master device from the ptmx driver.

.. _`ptmx_open.locking`:

Locking
-------

tty_mutex protects the init_dev work. tty->count should
protect the rest.
allocated_ptys_lock handles the list of free pty numbers

.. This file was automatic generated / don't edit.

