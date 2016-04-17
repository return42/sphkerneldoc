.. -*- coding: utf-8; mode: rst -*-

===========
tty_ldisc.c
===========


.. _`tty_register_ldisc`:

tty_register_ldisc
==================

.. c:function:: int tty_register_ldisc (int disc, struct tty_ldisc_ops *new_ldisc)

    install a line discipline

    :param int disc:
        ldisc number

    :param struct tty_ldisc_ops \*new_ldisc:
        pointer to the ldisc object



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

.. c:function:: int tty_unregister_ldisc (int disc)

    unload a line discipline

    :param int disc:
        ldisc number



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

.. c:function:: struct tty_ldisc *tty_ldisc_get (struct tty_struct *tty, int disc)

    take a reference to an ldisc

    :param struct tty_struct \*tty:

        *undescribed*

    :param int disc:
        ldisc number



.. _`tty_ldisc_get.description`:

Description
-----------

Takes a reference to a line discipline. Deals with refcounts and
module locking counts.



.. _`tty_ldisc_get.returns`:

Returns
-------

-EINVAL if the discipline index is not [N_TTY..NR_LDISCS] or
if the discipline is not registered
-EAGAIN if :c:func:`request_module` failed to load or register the
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

.. c:function:: void tty_ldisc_put (struct tty_ldisc *ld)

    release the ldisc

    :param struct tty_ldisc \*ld:

        *undescribed*



.. _`tty_ldisc_put.description`:

Description
-----------


Complement of :c:func:`tty_ldisc_get`.



.. _`tty_ldisc_ref_wait`:

tty_ldisc_ref_wait
==================

.. c:function:: struct tty_ldisc *tty_ldisc_ref_wait (struct tty_struct *tty)

    wait for the tty ldisc

    :param struct tty_struct \*tty:
        tty device



.. _`tty_ldisc_ref_wait.description`:

Description
-----------

Dereference the line discipline for the terminal and take a
reference to it. If the line discipline is in flux then
wait patiently until it changes.



.. _`tty_ldisc_ref_wait.returns`:

Returns
-------

NULL if the tty has been hungup and not re-opened with
a new file descriptor, otherwise valid ldisc reference



.. _`tty_ldisc_ref_wait.note`:

Note
----

a file_operations routine (read/poll/write) should use this
function to wait for any ldisc lifetime events to finish.



.. _`tty_ldisc_ref_wait.note`:

Note
----

a file_operations routine (read/poll/write) should use this
function to wait for any ldisc lifetime events to finish.



.. _`tty_ldisc_ref`:

tty_ldisc_ref
=============

.. c:function:: struct tty_ldisc *tty_ldisc_ref (struct tty_struct *tty)

    get the tty ldisc

    :param struct tty_struct \*tty:
        tty device



.. _`tty_ldisc_ref.description`:

Description
-----------

Dereference the line discipline for the terminal and take a
reference to it. If the line discipline is in flux then
return NULL. Can be called from IRQ and timer functions.



.. _`tty_ldisc_deref`:

tty_ldisc_deref
===============

.. c:function:: void tty_ldisc_deref (struct tty_ldisc *ld)

    free a tty ldisc reference

    :param struct tty_ldisc \*ld:
        reference to free up



.. _`tty_ldisc_deref.description`:

Description
-----------

Undoes the effect of tty_ldisc_ref or tty_ldisc_ref_wait. May
be called in IRQ context.



.. _`tty_ldisc_flush`:

tty_ldisc_flush
===============

.. c:function:: void tty_ldisc_flush (struct tty_struct *tty)

    flush line discipline queue

    :param struct tty_struct \*tty:
        tty



.. _`tty_ldisc_flush.description`:

Description
-----------

Flush the line discipline queue (if any) and the tty flip buffers
for this tty.



.. _`tty_set_termios_ldisc`:

tty_set_termios_ldisc
=====================

.. c:function:: void tty_set_termios_ldisc (struct tty_struct *tty, int disc)

    set ldisc field

    :param struct tty_struct \*tty:
        tty structure

    :param int disc:
        line discipline number



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

.. c:function:: int tty_ldisc_open (struct tty_struct *tty, struct tty_ldisc *ld)

    open a line discipline

    :param struct tty_struct \*tty:
        tty we are opening the ldisc on

    :param struct tty_ldisc \*ld:
        discipline to open



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

.. c:function:: void tty_ldisc_close (struct tty_struct *tty, struct tty_ldisc *ld)

    close a line discipline

    :param struct tty_struct \*tty:
        tty we are opening the ldisc on

    :param struct tty_ldisc \*ld:
        discipline to close



.. _`tty_ldisc_close.description`:

Description
-----------

A helper close method. Also a convenient debugging and check
point.



.. _`tty_ldisc_restore`:

tty_ldisc_restore
=================

.. c:function:: void tty_ldisc_restore (struct tty_struct *tty, struct tty_ldisc *old)

    helper for tty ldisc change

    :param struct tty_struct \*tty:
        tty to recover

    :param struct tty_ldisc \*old:
        previous ldisc



.. _`tty_ldisc_restore.description`:

Description
-----------

Restore the previous line discipline or N_TTY when a line discipline
change fails due to an open error



.. _`tty_set_ldisc`:

tty_set_ldisc
=============

.. c:function:: int tty_set_ldisc (struct tty_struct *tty, int disc)

    set line discipline

    :param struct tty_struct \*tty:
        the terminal to set

    :param int disc:

        *undescribed*



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

.. c:function:: void tty_ldisc_kill (struct tty_struct *tty)

    teardown ldisc

    :param struct tty_struct \*tty:
        tty being released



.. _`tty_ldisc_kill.description`:

Description
-----------

Perform final close of the ldisc and reset tty->ldisc



.. _`tty_reset_termios`:

tty_reset_termios
=================

.. c:function:: void tty_reset_termios (struct tty_struct *tty)

    reset terminal state

    :param struct tty_struct \*tty:
        tty to reset



.. _`tty_reset_termios.description`:

Description
-----------

Restore a terminal to the driver default state.



.. _`tty_ldisc_reinit`:

tty_ldisc_reinit
================

.. c:function:: int tty_ldisc_reinit (struct tty_struct *tty, int disc)

    reinitialise the tty ldisc

    :param struct tty_struct \*tty:
        tty to reinit

    :param int disc:
        line discipline to reinitialize



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

.. c:function:: void tty_ldisc_hangup (struct tty_struct *tty, bool reinit)

    hangup ldisc reset

    :param struct tty_struct \*tty:
        tty being hung up

    :param bool reinit:

        *undescribed*



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

In the pty pair case this occurs in the :c:func:`close` path of the
tty itself so we must be careful about locking rules.



.. _`tty_ldisc_setup`:

tty_ldisc_setup
===============

.. c:function:: int tty_ldisc_setup (struct tty_struct *tty, struct tty_struct *o_tty)

    open line discipline

    :param struct tty_struct \*tty:
        tty being shut down

    :param struct tty_struct \*o_tty:
        pair tty for pty/tty pairs



.. _`tty_ldisc_setup.description`:

Description
-----------

Called during the initial open of a tty/pty pair in order to set up the
line disciplines and bind them to the tty. This has no locking issues
as the device isn't yet active.



.. _`tty_ldisc_release`:

tty_ldisc_release
=================

.. c:function:: void tty_ldisc_release (struct tty_struct *tty)

    release line discipline

    :param struct tty_struct \*tty:
        tty being shut down (or one end of pty pair)



.. _`tty_ldisc_release.description`:

Description
-----------

Called during the final close of a tty or a pty pair in order to shut
down the line discpline layer. On exit, each tty's ldisc is NULL.



.. _`tty_ldisc_init`:

tty_ldisc_init
==============

.. c:function:: void tty_ldisc_init (struct tty_struct *tty)

    ldisc setup for new tty

    :param struct tty_struct \*tty:
        tty being allocated



.. _`tty_ldisc_init.description`:

Description
-----------

Set up the line discipline objects for a newly allocated tty. Note that
the tty structure is not completely set up when this call is made.



.. _`tty_ldisc_deinit`:

tty_ldisc_deinit
================

.. c:function:: void tty_ldisc_deinit (struct tty_struct *tty)

    ldisc cleanup for new tty

    :param struct tty_struct \*tty:
        tty that was allocated recently



.. _`tty_ldisc_deinit.description`:

Description
-----------

The tty structure must not becompletely set up (tty_ldisc_setup) when
this call is made.

