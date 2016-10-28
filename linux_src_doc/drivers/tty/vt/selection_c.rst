.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/vt/selection.c

.. _`clear_selection`:

clear_selection
===============

.. c:function:: void clear_selection( void)

    remove current selection

    :param  void:
        no arguments

.. _`clear_selection.description`:

Description
-----------

Remove the current selection highlight, if any from the console
holding the selection. The caller must hold the console lock.

.. _`sel_loadlut`:

sel_loadlut
===========

.. c:function:: int sel_loadlut(char __user *p)

    load the LUT table

    :param char __user \*p:
        user table

.. _`sel_loadlut.description`:

Description
-----------

Load the LUT table from user space. The caller must hold the console
lock. Make a temporary copy so a partial update doesn't make a mess.

.. _`set_selection`:

set_selection
=============

.. c:function:: int set_selection(const struct tiocl_selection __user *sel, struct tty_struct *tty)

    set the current selection.

    :param const struct tiocl_selection __user \*sel:
        user selection info

    :param struct tty_struct \*tty:
        the console tty

.. _`set_selection.description`:

Description
-----------

Invoked by the ioctl handle for the vt layer.

The entire selection process is managed under the console_lock. It's
a lot under the lock but its hardly a performance path

.. This file was automatic generated / don't edit.

