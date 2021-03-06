.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/hvc/hvc_console.c

.. _`hvc_set_winsz`:

hvc_set_winsz
=============

.. c:function:: void hvc_set_winsz(struct work_struct *work)

    Resize the hvc tty terminal window.

    :param work:
        work structure.
    :type work: struct work_struct \*

.. _`hvc_set_winsz.description`:

Description
-----------

The routine shall not be called within an atomic context because it
might sleep.

.. _`hvc_set_winsz.locking`:

Locking
-------

hp->lock

.. _`__hvc_resize`:

\__hvc_resize
=============

.. c:function:: void __hvc_resize(struct hvc_struct *hp, struct winsize ws)

    Update terminal window size information.

    :param hp:
        HVC console pointer
    :type hp: struct hvc_struct \*

    :param ws:
        Terminal window size structure
    :type ws: struct winsize

.. _`__hvc_resize.description`:

Description
-----------

Stores the specified window size information in the hvc structure of \ ``hp``\ .
The function schedule the tty resize update.

.. _`__hvc_resize.locking`:

Locking
-------

Locking free; the function MUST be called holding hp->lock

.. This file was automatic generated / don't edit.

