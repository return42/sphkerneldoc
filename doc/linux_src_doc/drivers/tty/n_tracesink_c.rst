.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/n_tracesink.c

.. _`n_tracesink_open`:

n_tracesink_open
================

.. c:function:: int n_tracesink_open(struct tty_struct *tty)

    Called when a tty is opened by a SW entity.

    :param struct tty_struct \*tty:
        terminal device to the ldisc.

.. _`n_tracesink_open.return`:

Return
------

0 for success,
-EFAULT = couldn't get a tty kref n_tracesink will sit
on top of
-EEXIST = \ :c:func:`open`\  called successfully once and it cannot
be called again.

.. _`n_tracesink_open.caveats`:

Caveats
-------

\ :c:func:`open`\  should only be successful the first time a
SW entity calls it.

.. _`n_tracesink_close`:

n_tracesink_close
=================

.. c:function:: void n_tracesink_close(struct tty_struct *tty)

    close connection

    :param struct tty_struct \*tty:
        terminal device to the ldisc.

.. _`n_tracesink_close.description`:

Description
-----------

Called when a software entity wants to close a connection.

.. _`n_tracesink_read`:

n_tracesink_read
================

.. c:function:: ssize_t n_tracesink_read(struct tty_struct *tty, struct file *file, unsigned char __user *buf, size_t nr)

    read request from user space

    :param struct tty_struct \*tty:
        terminal device passed into the ldisc.

    :param struct file \*file:
        pointer to open file object.

    :param unsigned char __user \*buf:
        pointer to the data buffer that gets eventually returned.

    :param size_t nr:
        number of bytes of the data buffer that is returned.

.. _`n_tracesink_read.description`:

Description
-----------

function that allows \ :c:func:`read`\  functionality in userspace. By default if this
is not implemented it returns -EIO. This module is functioning like a
router via \ :c:func:`n_tracesink_receivebuf`\ , and there is no real requirement
to implement this function. However, an error return value other than
-EIO should be used just to show that there was an intent not to have
this function implemented.  Return value based on \ :c:func:`read`\  man pages.

.. _`n_tracesink_read.return`:

Return
------

-EINVAL

.. _`n_tracesink_write`:

n_tracesink_write
=================

.. c:function:: ssize_t n_tracesink_write(struct tty_struct *tty, struct file *file, const unsigned char *buf, size_t nr)

    Function that allows \ :c:func:`write`\  in userspace.

    :param struct tty_struct \*tty:
        terminal device passed into the ldisc.

    :param struct file \*file:
        pointer to open file object.

    :param const unsigned char \*buf:
        pointer to the data buffer that gets eventually returned.

    :param size_t nr:
        number of bytes of the data buffer that is returned.

.. _`n_tracesink_write.description`:

Description
-----------

By default if this is not implemented, it returns -EIO.
This should not be implemented, ever, because
1. this driver is functioning like a router via
\ :c:func:`n_tracesink_receivebuf`\ 
2. No writes to HW will ever go through this line discpline driver.
However, an error return value other than -EIO should be used
just to show that there was an intent not to have this function
implemented.  Return value based on \ :c:func:`write`\  man pages.

.. _`n_tracesink_write.return`:

Return
------

-EINVAL

.. _`n_tracesink_datadrain`:

n_tracesink_datadrain
=====================

.. c:function:: void n_tracesink_datadrain(u8 *buf, int count)

    Kernel API function used to route trace debugging data to user-defined port like USB.

    :param u8 \*buf:
        Trace debuging data buffer to write to tty target
        port. Null value will return with no write occurring.

    :param int count:
        Size of buf. Value of 0 or a negative number will
        return with no write occuring.

.. _`n_tracesink_datadrain.caveat`:

Caveat
------

If this line discipline does not set the tty it sits
on top of via an \ :c:func:`open`\  call, this API function will not
call the tty's \ :c:func:`write`\  call because it will have no pointer
to call the \ :c:func:`write`\ .

.. _`n_tracesink_init`:

n_tracesink_init
================

.. c:function:: int n_tracesink_init( void)

    module initialisation

    :param  void:
        no arguments

.. _`n_tracesink_init.description`:

Description
-----------

Registers this module as a line discipline driver.

.. _`n_tracesink_init.return`:

Return
------

0 for success, any other value error.

.. _`n_tracesink_exit`:

n_tracesink_exit
================

.. c:function:: void __exit n_tracesink_exit( void)

    module unload

    :param  void:
        no arguments

.. _`n_tracesink_exit.description`:

Description
-----------

Removes this module as a line discipline driver.

.. This file was automatic generated / don't edit.

