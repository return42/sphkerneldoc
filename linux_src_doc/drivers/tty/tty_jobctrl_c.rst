.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_jobctrl.c

.. _`__tty_check_change`:

__tty_check_change
==================

.. c:function:: int __tty_check_change(struct tty_struct *tty, int sig)

    check for POSIX terminal changes

    :param struct tty_struct \*tty:
        tty to check

    :param int sig:
        *undescribed*

.. _`__tty_check_change.description`:

Description
-----------

If we try to write to, or set the state of, a terminal and we're
not in the foreground, send a SIGTTOU.  If the signal is blocked or
ignored, go ahead and perform the operation.  (POSIX 7.2)

.. _`__tty_check_change.locking`:

Locking
-------

ctrl_lock

.. _`__proc_set_tty`:

__proc_set_tty
==============

.. c:function:: void __proc_set_tty(struct tty_struct *tty)

    set the controlling terminal

    :param struct tty_struct \*tty:
        *undescribed*

.. _`__proc_set_tty.description`:

Description
-----------

Only callable by the session leader and only if it does not already have
a controlling terminal.

.. _`__proc_set_tty.caller-must-hold`:

Caller must hold
----------------

tty_lock()
a readlock on tasklist_lock
sighand lock

.. _`tty_signal_session_leader`:

tty_signal_session_leader
=========================

.. c:function:: int tty_signal_session_leader(struct tty_struct *tty, int exit_session)

    sends SIGHUP to session leader \ ``tty``\             controlling tty \ ``exit_session``\    if non-zero, signal all foreground group processes

    :param struct tty_struct \*tty:
        *undescribed*

    :param int exit_session:
        *undescribed*

.. _`tty_signal_session_leader.description`:

Description
-----------

Send SIGHUP and SIGCONT to the session leader and its process group.
Optionally, signal all processes in the foreground process group.

Returns the number of processes in the session with this tty
as their controlling terminal. This value is used to drop
tty references for those processes.

.. _`disassociate_ctty`:

disassociate_ctty
=================

.. c:function:: void disassociate_ctty(int on_exit)

    disconnect controlling tty

    :param int on_exit:
        true if exiting so need to "hang up" the session

.. _`disassociate_ctty.description`:

Description
-----------

This function is typically called only by the session leader, when
it wants to disassociate itself from its controlling tty.

.. _`disassociate_ctty.it-performs-the-following-functions`:

It performs the following functions
-----------------------------------

(1)  Sends a SIGHUP and SIGCONT to the foreground process group
(2)  Clears the tty from being controlling the session
(3)  Clears the controlling tty for all processes in the
session group.

The argument on_exit is set to 1 if called when a process is
exiting; it is 0 if called by the ioctl TIOCNOTTY.

.. _`disassociate_ctty.locking`:

Locking
-------

BTM is taken for hysterical raisons, and held when
called from \ :c:func:`no_tty`\ .
tty_mutex is taken to protect tty
->siglock is taken to protect ->signal/->sighand
tasklist_lock is taken to walk process list for sessions
->siglock is taken to protect ->signal/->sighand

.. _`tiocsctty`:

tiocsctty
=========

.. c:function:: int tiocsctty(struct tty_struct *tty, struct file *file, int arg)

    set controlling tty

    :param struct tty_struct \*tty:
        tty structure

    :param struct file \*file:
        *undescribed*

    :param int arg:
        user argument

.. _`tiocsctty.description`:

Description
-----------

This ioctl is used to manage job control. It permits a session
leader to set this tty as the controlling tty for the session.

.. _`tiocsctty.locking`:

Locking
-------

Takes \ :c:func:`tty_lock`\  to serialize \ :c:func:`proc_set_tty`\  for this tty
Takes tasklist_lock internally to walk sessions
Takes ->siglock() when updating signal->tty

.. _`tty_get_pgrp`:

tty_get_pgrp
============

.. c:function:: struct pid *tty_get_pgrp(struct tty_struct *tty)

    return a ref counted pgrp pid

    :param struct tty_struct \*tty:
        tty to read

.. _`tty_get_pgrp.description`:

Description
-----------

Returns a refcounted instance of the pid struct for the process
group controlling the tty.

.. _`tiocgpgrp`:

tiocgpgrp
=========

.. c:function:: int tiocgpgrp(struct tty_struct *tty, struct tty_struct *real_tty, pid_t __user *p)

    get process group

    :param struct tty_struct \*tty:
        tty passed by user

    :param struct tty_struct \*real_tty:
        tty side of the tty passed by the user if a pty else the tty

    :param pid_t __user \*p:
        returned pid

.. _`tiocgpgrp.description`:

Description
-----------

Obtain the process group of the tty. If there is no process group
return an error.

.. _`tiocgpgrp.locking`:

Locking
-------

none. Reference to current->signal->tty is safe.

.. _`tiocspgrp`:

tiocspgrp
=========

.. c:function:: int tiocspgrp(struct tty_struct *tty, struct tty_struct *real_tty, pid_t __user *p)

    attempt to set process group

    :param struct tty_struct \*tty:
        tty passed by user

    :param struct tty_struct \*real_tty:
        tty side device matching tty passed by user

    :param pid_t __user \*p:
        pid pointer

.. _`tiocspgrp.description`:

Description
-----------

Set the process group of the tty to the session passed. Only
permitted where the tty session is our session.

.. _`tiocspgrp.locking`:

Locking
-------

RCU, ctrl lock

.. _`tiocgsid`:

tiocgsid
========

.. c:function:: int tiocgsid(struct tty_struct *tty, struct tty_struct *real_tty, pid_t __user *p)

    get session id

    :param struct tty_struct \*tty:
        tty passed by user

    :param struct tty_struct \*real_tty:
        tty side of the tty passed by the user if a pty else the tty

    :param pid_t __user \*p:
        pointer to returned session id

.. _`tiocgsid.description`:

Description
-----------

Obtain the session id of the tty. If there is no session
return an error.

.. _`tiocgsid.locking`:

Locking
-------

none. Reference to current->signal->tty is safe.

.. This file was automatic generated / don't edit.

