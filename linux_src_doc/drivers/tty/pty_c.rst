.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/pty.c

.. _`pty_write`:

pty_write
=========

.. c:function:: int pty_write(struct tty_struct *tty, const unsigned char *buf, int c)

    write to a pty

    :param struct tty_struct \*tty:
        the tty we write from

    :param const unsigned char \*buf:
        kernel buffer of data

    :param int c:
        *undescribed*

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

    :param struct tty_struct \*tty:
        tty we are writing from

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

    :param struct tty_struct \*tty:
        our tty

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

    :param struct tty_struct \*tty:
        tty being resized

    :param struct winsize \*ws:
        window size being set.

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

    :param struct tty_struct \*tty:
        tty being flow-controlled

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

    :param struct tty_driver \*driver:
        the pty driver

    :param struct tty_struct \*tty:
        the tty being instantiated

    :param bool legacy:
        true if this is BSD style

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

    :param struct file \*master:
        the open struct file of the ptmx device node

    :param struct tty_struct \*tty:
        the master of the pty being opened

    :param int flags:
        the flags for open

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

    :param struct tty_driver \*driver:
        ptm driver

    :param struct file \*file:
        *undescribed*

    :param int idx:
        tty index

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

    :param struct tty_driver \*driver:
        pts driver

    :param struct file \*file:
        *undescribed*

    :param int idx:
        tty index

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

    :param struct inode \*inode:
        inode of device file

    :param struct file \*filp:
        file pointer to tty

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

