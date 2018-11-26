.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_audit.c

.. _`tty_audit_buf_push`:

tty_audit_buf_push
==================

.. c:function:: void tty_audit_buf_push(struct tty_audit_buf *buf)

    Push buffered data out

    :param buf:
        *undescribed*
    :type buf: struct tty_audit_buf \*

.. _`tty_audit_buf_push.description`:

Description
-----------

Generate an audit message from the contents of \ ``buf``\ , which is owned by
the current task.  \ ``buf->mutex``\  must be locked.

.. _`tty_audit_exit`:

tty_audit_exit
==============

.. c:function:: void tty_audit_exit( void)

    Handle a task exit

    :param void:
        no arguments
    :type void: 

.. _`tty_audit_exit.description`:

Description
-----------

Make sure all buffered data is written out and deallocate the buffer.
Only needs to be called if current->signal->tty_audit_buf != \ ``NULL``\ .

The process is single-threaded at this point; no other threads share
current->signal.

.. _`tty_audit_fork`:

tty_audit_fork
==============

.. c:function:: void tty_audit_fork(struct signal_struct *sig)

    Copy TTY audit state for a new task

    :param sig:
        *undescribed*
    :type sig: struct signal_struct \*

.. _`tty_audit_fork.description`:

Description
-----------

Set up TTY audit state in \ ``sig``\  from current.  \ ``sig``\  needs no locking.

.. _`tty_audit_tiocsti`:

tty_audit_tiocsti
=================

.. c:function:: void tty_audit_tiocsti(struct tty_struct *tty, char ch)

    Log TIOCSTI

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param ch:
        *undescribed*
    :type ch: char

.. _`tty_audit_push`:

tty_audit_push
==============

.. c:function:: int tty_audit_push( void)

    Flush current's pending audit data

    :param void:
        no arguments
    :type void: 

.. _`tty_audit_push.description`:

Description
-----------

Returns 0 if success, -EPERM if tty audit is disabled

.. _`tty_audit_buf_get`:

tty_audit_buf_get
=================

.. c:function:: struct tty_audit_buf *tty_audit_buf_get( void)

    Get an audit buffer.

    :param void:
        no arguments
    :type void: 

.. _`tty_audit_buf_get.description`:

Description
-----------

Get an audit buffer, allocate it if necessary.  Return \ ``NULL``\ 
if out of memory or ERR_PTR(-ESRCH) if \ :c:func:`tty_audit_exit`\  has already
occurred.  Otherwise, return a new reference to the buffer.

.. _`tty_audit_add_data`:

tty_audit_add_data
==================

.. c:function:: void tty_audit_add_data(struct tty_struct *tty, const void *data, size_t size)

    Add data for TTY auditing.

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param data:
        *undescribed*
    :type data: const void \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`tty_audit_add_data.description`:

Description
-----------

Audit \ ``data``\  of \ ``size``\  from \ ``tty``\ , if necessary.

.. This file was automatic generated / don't edit.

