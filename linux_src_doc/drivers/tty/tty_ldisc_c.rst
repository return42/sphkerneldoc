.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_ldisc.c

.. _`tty_register_ldisc`:

tty_register_ldisc
==================

.. c:function:: int tty_register_ldisc(int disc, struct tty_ldisc_ops *new_ldisc)

    install a line discipline

    :param disc:
        ldisc number
    :type disc: int

    :param new_ldisc:
        pointer to the ldisc object
    :type new_ldisc: struct tty_ldisc_ops \*

.. _`tty_register_ldisc.description`:

Description
-----------

Installs a new line discipline into the kernel. The discipline
is set up as unreferenced and then made available to the kernel
from this point onwards.

.. _`tty_register_ldisc.locking`:

Locking
-------

takes tty_ldiscs_lock to guard against ldisc races

.. _`tty_unregister_ldisc`:

tty_unregister_ldisc
====================

.. c:function:: int tty_unregister_ldisc(int disc)

    unload a line discipline

    :param disc:
        ldisc number
    :type disc: int

.. _`tty_unregister_ldisc.description`:

Description
-----------

Remove a line discipline from the kernel providing it is not
currently in use.

.. _`tty_unregister_ldisc.locking`:

Locking
-------

takes tty_ldiscs_lock to guard against ldisc races

.. _`tty_ldisc_get`:

tty_ldisc_get
=============

.. c:function:: struct tty_ldisc *tty_ldisc_get(struct tty_struct *tty, int disc)

    take a reference to an ldisc

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param disc:
        ldisc number
    :type disc: int

.. _`tty_ldisc_get.description`:

Description
-----------

Takes a reference to a line discipline. Deals with refcounts and
module locking counts.

.. _`tty_ldisc_get.return`:

Return
------

-EINVAL if the discipline index is not [N_TTY..NR_LDISCS] or
if the discipline is not registered
-EAGAIN if \ :c:func:`request_module`\  failed to load or register the
the discipline
-ENOMEM if allocation failure

Otherwise, returns a pointer to the discipline and bumps the
ref count

.. _`tty_ldisc_get.locking`:

Locking
-------

takes tty_ldiscs_lock to guard against ldisc races

.. _`tty_ldisc_put`:

tty_ldisc_put
=============

.. c:function:: void tty_ldisc_put(struct tty_ldisc *ld)

    release the ldisc

    :param ld:
        *undescribed*
    :type ld: struct tty_ldisc \*

.. _`tty_ldisc_put.description`:

Description
-----------

Complement of \ :c:func:`tty_ldisc_get`\ .

.. _`tty_ldisc_ref_wait`:

tty_ldisc_ref_wait
==================

.. c:function:: struct tty_ldisc *tty_ldisc_ref_wait(struct tty_struct *tty)

    wait for the tty ldisc

    :param tty:
        tty device
    :type tty: struct tty_struct \*

.. _`tty_ldisc_ref_wait.description`:

Description
-----------

Dereference the line discipline for the terminal and take a
reference to it. If the line discipline is in flux then
wait patiently until it changes.

.. _`tty_ldisc_ref_wait.return`:

Return
------

NULL if the tty has been hungup and not re-opened with
a new file descriptor, otherwise valid ldisc reference

.. _`tty_ldisc_ref_wait.note`:

Note
----

Must not be called from an IRQ/timer context. The caller
must also be careful not to hold other locks that will deadlock
against a discipline change, such as an existing ldisc reference
(which we check for)

a file_operations routine (read/poll/write) should use this
function to wait for any ldisc lifetime events to finish.

.. _`tty_ldisc_ref`:

tty_ldisc_ref
=============

.. c:function:: struct tty_ldisc *tty_ldisc_ref(struct tty_struct *tty)

    get the tty ldisc

    :param tty:
        tty device
    :type tty: struct tty_struct \*

.. _`tty_ldisc_ref.description`:

Description
-----------

Dereference the line discipline for the terminal and take a
reference to it. If the line discipline is in flux then
return NULL. Can be called from IRQ and timer functions.

.. _`tty_ldisc_deref`:

tty_ldisc_deref
===============

.. c:function:: void tty_ldisc_deref(struct tty_ldisc *ld)

    free a tty ldisc reference

    :param ld:
        reference to free up
    :type ld: struct tty_ldisc \*

.. _`tty_ldisc_deref.description`:

Description
-----------

Undoes the effect of tty_ldisc_ref or tty_ldisc_ref_wait. May
be called in IRQ context.

.. _`tty_ldisc_flush`:

tty_ldisc_flush
===============

.. c:function:: void tty_ldisc_flush(struct tty_struct *tty)

    flush line discipline queue

    :param tty:
        tty
    :type tty: struct tty_struct \*

.. _`tty_ldisc_flush.description`:

Description
-----------

Flush the line discipline queue (if any) and the tty flip buffers
for this tty.

.. _`tty_set_termios_ldisc`:

tty_set_termios_ldisc
=====================

.. c:function:: void tty_set_termios_ldisc(struct tty_struct *tty, int disc)

    set ldisc field

    :param tty:
        tty structure
    :type tty: struct tty_struct \*

    :param disc:
        line discipline number
    :type disc: int

.. _`tty_set_termios_ldisc.description`:

Description
-----------

This is probably overkill for real world processors but
they are not on hot paths so a little discipline won't do
any harm.

The line discipline-related tty_struct fields are reset to
prevent the ldisc driver from re-using stale information for
the new ldisc instance.

.. _`tty_set_termios_ldisc.locking`:

Locking
-------

takes termios_rwsem

.. _`tty_ldisc_open`:

tty_ldisc_open
==============

.. c:function:: int tty_ldisc_open(struct tty_struct *tty, struct tty_ldisc *ld)

    open a line discipline

    :param tty:
        tty we are opening the ldisc on
    :type tty: struct tty_struct \*

    :param ld:
        discipline to open
    :type ld: struct tty_ldisc \*

.. _`tty_ldisc_open.description`:

Description
-----------

A helper opening method. Also a convenient debugging and check
point.

.. _`tty_ldisc_open.locking`:

Locking
-------

always called with BTM already held.

.. _`tty_ldisc_close`:

tty_ldisc_close
===============

.. c:function:: void tty_ldisc_close(struct tty_struct *tty, struct tty_ldisc *ld)

    close a line discipline

    :param tty:
        tty we are opening the ldisc on
    :type tty: struct tty_struct \*

    :param ld:
        discipline to close
    :type ld: struct tty_ldisc \*

.. _`tty_ldisc_close.description`:

Description
-----------

A helper close method. Also a convenient debugging and check
point.

.. _`tty_ldisc_failto`:

tty_ldisc_failto
================

.. c:function:: int tty_ldisc_failto(struct tty_struct *tty, int ld)

    helper for ldisc failback

    :param tty:
        tty to open the ldisc on
    :type tty: struct tty_struct \*

    :param ld:
        ldisc we are trying to fail back to
    :type ld: int

.. _`tty_ldisc_failto.description`:

Description
-----------

Helper to try and recover a tty when switching back to the old
ldisc fails and we need something attached.

.. _`tty_ldisc_restore`:

tty_ldisc_restore
=================

.. c:function:: void tty_ldisc_restore(struct tty_struct *tty, struct tty_ldisc *old)

    helper for tty ldisc change

    :param tty:
        tty to recover
    :type tty: struct tty_struct \*

    :param old:
        previous ldisc
    :type old: struct tty_ldisc \*

.. _`tty_ldisc_restore.description`:

Description
-----------

Restore the previous line discipline or N_TTY when a line discipline
change fails due to an open error

.. _`tty_set_ldisc`:

tty_set_ldisc
=============

.. c:function:: int tty_set_ldisc(struct tty_struct *tty, int disc)

    set line discipline

    :param tty:
        the terminal to set
    :type tty: struct tty_struct \*

    :param disc:
        *undescribed*
    :type disc: int

.. _`tty_set_ldisc.description`:

Description
-----------

Set the discipline of a tty line. Must be called from a process
context. The ldisc change logic has to protect itself against any
overlapping ldisc change (including on the other end of pty pairs),
the close of one side of a tty/pty pair, and eventually hangup.

.. _`tty_ldisc_kill`:

tty_ldisc_kill
==============

.. c:function:: void tty_ldisc_kill(struct tty_struct *tty)

    teardown ldisc

    :param tty:
        tty being released
    :type tty: struct tty_struct \*

.. _`tty_ldisc_kill.description`:

Description
-----------

Perform final close of the ldisc and reset tty->ldisc

.. _`tty_reset_termios`:

tty_reset_termios
=================

.. c:function:: void tty_reset_termios(struct tty_struct *tty)

    reset terminal state

    :param tty:
        tty to reset
    :type tty: struct tty_struct \*

.. _`tty_reset_termios.description`:

Description
-----------

Restore a terminal to the driver default state.

.. _`tty_ldisc_reinit`:

tty_ldisc_reinit
================

.. c:function:: int tty_ldisc_reinit(struct tty_struct *tty, int disc)

    reinitialise the tty ldisc

    :param tty:
        tty to reinit
    :type tty: struct tty_struct \*

    :param disc:
        line discipline to reinitialize
    :type disc: int

.. _`tty_ldisc_reinit.description`:

Description
-----------

Completely reinitialize the line discipline state, by closing the
current instance, if there is one, and opening a new instance. If
an error occurs opening the new non-N_TTY instance, the instance
is dropped and tty->ldisc reset to NULL. The caller can then retry
with N_TTY instead.

Returns 0 if successful, otherwise error code < 0

.. _`tty_ldisc_hangup`:

tty_ldisc_hangup
================

.. c:function:: void tty_ldisc_hangup(struct tty_struct *tty, bool reinit)

    hangup ldisc reset

    :param tty:
        tty being hung up
    :type tty: struct tty_struct \*

    :param reinit:
        *undescribed*
    :type reinit: bool

.. _`tty_ldisc_hangup.description`:

Description
-----------

Some tty devices reset their termios when they receive a hangup
event. In that situation we must also switch back to N_TTY properly
before we reset the termios data.

.. _`tty_ldisc_hangup.locking`:

Locking
-------

We can take the ldisc mutex as the rest of the code is
careful to allow for this.

In the pty pair case this occurs in the \ :c:func:`close`\  path of the
tty itself so we must be careful about locking rules.

.. _`tty_ldisc_setup`:

tty_ldisc_setup
===============

.. c:function:: int tty_ldisc_setup(struct tty_struct *tty, struct tty_struct *o_tty)

    open line discipline

    :param tty:
        tty being shut down
    :type tty: struct tty_struct \*

    :param o_tty:
        pair tty for pty/tty pairs
    :type o_tty: struct tty_struct \*

.. _`tty_ldisc_setup.description`:

Description
-----------

Called during the initial open of a tty/pty pair in order to set up the
line disciplines and bind them to the tty. This has no locking issues
as the device isn't yet active.

.. _`tty_ldisc_release`:

tty_ldisc_release
=================

.. c:function:: void tty_ldisc_release(struct tty_struct *tty)

    release line discipline

    :param tty:
        tty being shut down (or one end of pty pair)
    :type tty: struct tty_struct \*

.. _`tty_ldisc_release.description`:

Description
-----------

Called during the final close of a tty or a pty pair in order to shut
down the line discpline layer. On exit, each tty's ldisc is NULL.

.. _`tty_ldisc_init`:

tty_ldisc_init
==============

.. c:function:: int tty_ldisc_init(struct tty_struct *tty)

    ldisc setup for new tty

    :param tty:
        tty being allocated
    :type tty: struct tty_struct \*

.. _`tty_ldisc_init.description`:

Description
-----------

Set up the line discipline objects for a newly allocated tty. Note that
the tty structure is not completely set up when this call is made.

.. _`tty_ldisc_deinit`:

tty_ldisc_deinit
================

.. c:function:: void tty_ldisc_deinit(struct tty_struct *tty)

    ldisc cleanup for new tty

    :param tty:
        tty that was allocated recently
    :type tty: struct tty_struct \*

.. _`tty_ldisc_deinit.description`:

Description
-----------

The tty structure must not becompletely set up (tty_ldisc_setup) when
this call is made.

.. This file was automatic generated / don't edit.

