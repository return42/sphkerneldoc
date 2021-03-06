.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/vt/vt_ioctl.c

.. _`vt_event_post`:

vt_event_post
=============

.. c:function:: void vt_event_post(unsigned int event, unsigned int old, unsigned int new)

    :param event:
        the event that occurred
    :type event: unsigned int

    :param old:
        old console
    :type old: unsigned int

    :param new:
        new console
    :type new: unsigned int

.. _`vt_event_post.description`:

Description
-----------

Post an VT event to interested VT handlers

.. _`vt_event_wait`:

vt_event_wait
=============

.. c:function:: void vt_event_wait(struct vt_event_wait *vw)

    wait for an event

    :param vw:
        our event
    :type vw: struct vt_event_wait \*

.. _`vt_event_wait.description`:

Description
-----------

Waits for an event to occur which completes our vt_event_wait
structure. On return the structure has wv->done set to 1 for success
or 0 if some event such as a signal ended the wait.

.. _`vt_event_wait_ioctl`:

vt_event_wait_ioctl
===================

.. c:function:: int vt_event_wait_ioctl(struct vt_event __user *event)

    event ioctl handler

    :param event:
        *undescribed*
    :type event: struct vt_event __user \*

.. _`vt_event_wait_ioctl.description`:

Description
-----------

Implement the VT_WAITEVENT ioctl using the VT event interface

.. _`vt_waitactive`:

vt_waitactive
=============

.. c:function:: int vt_waitactive(int n)

    active console wait

    :param n:
        new console
    :type n: int

.. _`vt_waitactive.description`:

Description
-----------

Helper for event waits. Used to implement the legacy
event waiting ioctls in terms of events

.. This file was automatic generated / don't edit.

