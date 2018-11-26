.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/n_tracerouter.c

.. _`n_tracerouter_open`:

n_tracerouter_open
==================

.. c:function:: int n_tracerouter_open(struct tty_struct *tty)

    Called when a tty is opened by a SW entity.

    :param tty:
        terminal device to the ldisc.
    :type tty: struct tty_struct \*

.. _`n_tracerouter_open.return`:

Return
------

0 for success.

.. _`n_tracerouter_open.caveats`:

Caveats
-------

This should only be opened one time per SW entity.

.. _`n_tracerouter_close`:

n_tracerouter_close
===================

.. c:function:: void n_tracerouter_close(struct tty_struct *tty)

    close connection

    :param tty:
        terminal device to the ldisc.
    :type tty: struct tty_struct \*

.. _`n_tracerouter_close.description`:

Description
-----------

Called when a software entity wants to close a connection.

.. _`n_tracerouter_read`:

n_tracerouter_read
==================

.. c:function:: ssize_t n_tracerouter_read(struct tty_struct *tty, struct file *file, unsigned char __user *buf, size_t nr)

    read request from user space

    :param tty:
        terminal device passed into the ldisc.
    :type tty: struct tty_struct \*

    :param file:
        pointer to open file object.
    :type file: struct file \*

    :param buf:
        pointer to the data buffer that gets eventually returned.
    :type buf: unsigned char __user \*

    :param nr:
        number of bytes of the data buffer that is returned.
    :type nr: size_t

.. _`n_tracerouter_read.description`:

Description
-----------

function that allows \ :c:func:`read`\  functionality in userspace. By default if this
is not implemented it returns -EIO. This module is functioning like a
router via \ :c:func:`n_tracerouter_receivebuf`\ , and there is no real requirement
to implement this function. However, an error return value other than
-EIO should be used just to show that there was an intent not to have
this function implemented.  Return value based on \ :c:func:`read`\  man pages.

.. _`n_tracerouter_read.return`:

Return
------

-EINVAL

.. _`n_tracerouter_write`:

n_tracerouter_write
===================

.. c:function:: ssize_t n_tracerouter_write(struct tty_struct *tty, struct file *file, const unsigned char *buf, size_t nr)

    Function that allows \ :c:func:`write`\  in userspace.

    :param tty:
        terminal device passed into the ldisc.
    :type tty: struct tty_struct \*

    :param file:
        pointer to open file object.
    :type file: struct file \*

    :param buf:
        pointer to the data buffer that gets eventually returned.
    :type buf: const unsigned char \*

    :param nr:
        number of bytes of the data buffer that is returned.
    :type nr: size_t

.. _`n_tracerouter_write.description`:

Description
-----------

By default if this is not implemented, it returns -EIO.
This should not be implemented, ever, because
1. this driver is functioning like a router via
\ :c:func:`n_tracerouter_receivebuf`\ 
2. No writes to HW will ever go through this line discpline driver.
However, an error return value other than -EIO should be used
just to show that there was an intent not to have this function
implemented.  Return value based on \ :c:func:`write`\  man pages.

.. _`n_tracerouter_write.return`:

Return
------

-EINVAL

.. _`n_tracerouter_receivebuf`:

n_tracerouter_receivebuf
========================

.. c:function:: void n_tracerouter_receivebuf(struct tty_struct *tty, const unsigned char *cp, char *fp, int count)

    Routing function for driver.

    :param tty:
        terminal device passed into the ldisc.  It's assumed
        tty will never be NULL.
    :type tty: struct tty_struct \*

    :param cp:
        buffer, block of characters to be eventually read by
        someone, somewhere (user \ :c:func:`read`\  call or some kernel function).
    :type cp: const unsigned char \*

    :param fp:
        flag buffer.
    :type fp: char \*

    :param count:
        number of characters (aka, bytes) in cp.
    :type count: int

.. _`n_tracerouter_receivebuf.description`:

Description
-----------

This function takes the input buffer, cp, and passes it to
an external API function for processing.

.. _`n_tracerouter_init`:

n_tracerouter_init
==================

.. c:function:: int n_tracerouter_init( void)

    module initialisation

    :param void:
        no arguments
    :type void: 

.. _`n_tracerouter_init.description`:

Description
-----------

Registers this module as a line discipline driver.

.. _`n_tracerouter_init.return`:

Return
------

0 for success, any other value error.

.. _`n_tracerouter_exit`:

n_tracerouter_exit
==================

.. c:function:: void __exit n_tracerouter_exit( void)

    module unload

    :param void:
        no arguments
    :type void: 

.. _`n_tracerouter_exit.description`:

Description
-----------

Removes this module as a line discipline driver.

.. This file was automatic generated / don't edit.

