.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/char/ctrlchar.c

.. _`ctrlchar_handle`:

ctrlchar_handle
===============

.. c:function:: unsigned int ctrlchar_handle(const unsigned char *buf, int len, struct tty_struct *tty)

    :param buf:
        *undescribed*
    :type buf: const unsigned char \*

    :param len:
        *undescribed*
    :type len: int

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`ctrlchar_handle.description`:

Description
-----------

\ ``param``\  buf Console input buffer.
\ ``param``\  len Length of valid data in buffer.
\ ``param``\  tty The tty struct for this console.
\ ``return``\  CTRLCHAR_NONE, if nothing matched,
CTRLCHAR_SYSRQ, if sysrq was encountered
otherwise char to be inserted logically or'ed
with CTRLCHAR_CTRL

.. This file was automatic generated / don't edit.

