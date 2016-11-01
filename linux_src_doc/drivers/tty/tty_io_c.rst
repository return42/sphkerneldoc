.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_io.c

.. _`free_tty_struct`:

free_tty_struct
===============

.. c:function:: void free_tty_struct(struct tty_struct *tty)

    free a disused tty

    :param struct tty_struct \*tty:
        tty struct to free

.. _`free_tty_struct.description`:

Description
-----------

Free the write buffers, tty queue and tty memory itself.

.. _`free_tty_struct.locking`:

Locking
-------

none. Must be called after tty is definitely unused

.. _`tty_free_file`:

tty_free_file
=============

.. c:function:: void tty_free_file(struct file *file)

    free file->private_data

    :param struct file \*file:
        *undescribed*

.. _`tty_free_file.description`:

Description
-----------

This shall be used only for fail path handling when tty_add_file was not
called yet.

.. _`tty_name`:

tty_name
========

.. c:function:: const char *tty_name(const struct tty_struct *tty)

    return tty naming

    :param const struct tty_struct \*tty:
        tty structure

.. _`tty_name.description`:

Description
-----------

Convert a tty structure into a name. The name reflects the kernel
naming policy and if udev is in use may not reflect user space

.. _`tty_name.locking`:

Locking
-------

none

.. _`get_tty_driver`:

get_tty_driver
==============

.. c:function:: struct tty_driver *get_tty_driver(dev_t device, int *index)

    find device of a tty

    :param dev_t device:
        *undescribed*

    :param int \*index:
        returns the index of the tty

.. _`get_tty_driver.description`:

Description
-----------

This routine returns a tty driver structure, given a device number
and also passes back the index number.

.. _`get_tty_driver.locking`:

Locking
-------

caller must hold tty_mutex

.. _`tty_find_polling_driver`:

tty_find_polling_driver
=======================

.. c:function:: struct tty_driver *tty_find_polling_driver(char *name, int *line)

    find device of a polled tty

    :param char \*name:
        name string to match

    :param int \*line:
        pointer to resulting tty line nr

.. _`tty_find_polling_driver.description`:

Description
-----------

This routine returns a tty driver structure, given a name
and the condition that the tty driver is capable of polled
operation.

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

.. _`tty_wakeup`:

tty_wakeup
==========

.. c:function:: void tty_wakeup(struct tty_struct *tty)

    request more data

    :param struct tty_struct \*tty:
        terminal

.. _`tty_wakeup.description`:

Description
-----------

Internal and external helper for wakeups of tty. This function
informs the line discipline if present that the driver is ready
to receive more output data.

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

.. _`__tty_hangup`:

__tty_hangup
============

.. c:function:: void __tty_hangup(struct tty_struct *tty, int exit_session)

    actual handler for hangup events

    :param struct tty_struct \*tty:
        *undescribed*

    :param int exit_session:
        *undescribed*

.. _`__tty_hangup.description`:

Description
-----------

This can be called by a "kworker" kernel thread.  That is process
synchronous but doesn't hold any locks, so we need to make sure we
have the appropriate locks for what we're doing.

The hangup event clears any pending redirections onto the hung up
device. It ensures future writes will error and it does the needed
line discipline hangup and signal delivery. The tty object itself
remains intact.

.. _`__tty_hangup.locking`:

Locking
-------

BTM
redirect lock for undoing redirection
file list lock for manipulating list of ttys
tty_ldiscs_lock from called functions
termios_rwsem resetting termios data
tasklist_lock to walk task list for hangup event
->siglock to protect ->signal/->sighand

.. _`tty_hangup`:

tty_hangup
==========

.. c:function:: void tty_hangup(struct tty_struct *tty)

    trigger a hangup event

    :param struct tty_struct \*tty:
        tty to hangup

.. _`tty_hangup.description`:

Description
-----------

A carrier loss (virtual or otherwise) has occurred on this like
schedule a hangup sequence to run after this event.

.. _`tty_vhangup`:

tty_vhangup
===========

.. c:function:: void tty_vhangup(struct tty_struct *tty)

    process vhangup

    :param struct tty_struct \*tty:
        tty to hangup

.. _`tty_vhangup.description`:

Description
-----------

The user has asked via system call for the terminal to be hung up.
We do this synchronously so that when the syscall returns the process
is complete. That guarantee is necessary for security reasons.

.. _`tty_vhangup_self`:

tty_vhangup_self
================

.. c:function:: void tty_vhangup_self( void)

    process vhangup for own ctty

    :param  void:
        no arguments

.. _`tty_vhangup_self.description`:

Description
-----------

Perform a vhangup on the current controlling tty

.. _`tty_vhangup_session`:

tty_vhangup_session
===================

.. c:function:: void tty_vhangup_session(struct tty_struct *tty)

    hangup session leader exit

    :param struct tty_struct \*tty:
        tty to hangup

.. _`tty_vhangup_session.description`:

Description
-----------

The session leader is exiting and hanging up its controlling terminal.
Every process in the foreground process group is signalled SIGHUP.

We do this synchronously so that when the syscall returns the process
is complete. That guarantee is necessary for security reasons.

.. _`tty_hung_up_p`:

tty_hung_up_p
=============

.. c:function:: int tty_hung_up_p(struct file *filp)

    was tty hung up

    :param struct file \*filp:
        file pointer of tty

.. _`tty_hung_up_p.description`:

Description
-----------

Return true if the tty has been subject to a vhangup or a carrier
loss

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

BTM is taken for hysterical raisins, and held when
called from \ :c:func:`no_tty`\ .
tty_mutex is taken to protect tty
->siglock is taken to protect ->signal/->sighand
tasklist_lock is taken to walk process list for sessions
->siglock is taken to protect ->signal/->sighand

.. _`__stop_tty`:

__stop_tty
==========

.. c:function:: void __stop_tty(struct tty_struct *tty)

    propagate flow control

    :param struct tty_struct \*tty:
        tty to stop

.. _`__stop_tty.description`:

Description
-----------

Perform flow control to the driver. May be called
on an already stopped device and will not re-call the driver
method.

This functionality is used by both the line disciplines for
halting incoming flow and by the driver. It may therefore be
called from any context, may be under the tty atomic_write_lock
but not always.

.. _`__stop_tty.locking`:

Locking
-------

flow_lock

.. _`__start_tty`:

__start_tty
===========

.. c:function:: void __start_tty(struct tty_struct *tty)

    propagate flow control

    :param struct tty_struct \*tty:
        tty to start

.. _`__start_tty.description`:

Description
-----------

Start a tty that has been stopped if at all possible. If this
tty was previous stopped and is now being started, the driver
start method is invoked and the line discipline woken.

.. _`__start_tty.locking`:

Locking
-------

flow_lock

.. _`tty_read`:

tty_read
========

.. c:function:: ssize_t tty_read(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    read method for tty device files

    :param struct file \*file:
        pointer to tty file

    :param char __user \*buf:
        user buffer

    :param size_t count:
        size of user buffer

    :param loff_t \*ppos:
        unused

.. _`tty_read.description`:

Description
-----------

Perform the read system call function on this terminal device. Checks
for hung up devices before calling the line discipline method.

.. _`tty_read.locking`:

Locking
-------

Locks the line discipline internally while needed. Multiple
read calls may be outstanding in parallel.

.. _`tty_write_message`:

tty_write_message
=================

.. c:function:: void tty_write_message(struct tty_struct *tty, char *msg)

    write a message to a certain tty, not just the console.

    :param struct tty_struct \*tty:
        the destination tty_struct

    :param char \*msg:
        the message to write

.. _`tty_write_message.description`:

Description
-----------

This is used for messages that need to be redirected to a specific tty.
We don't put it into the syslog queue right now maybe in the future if
really needed.

We must still hold the BTM and test the CLOSING flag for the moment.

.. _`tty_write`:

tty_write
=========

.. c:function:: ssize_t tty_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    write method for tty device file

    :param struct file \*file:
        tty file pointer

    :param const char __user \*buf:
        user data to write

    :param size_t count:
        bytes to write

    :param loff_t \*ppos:
        unused

.. _`tty_write.description`:

Description
-----------

Write data to a tty device via the line discipline.

.. _`tty_write.locking`:

Locking
-------

Locks the line discipline as required
Writes to the tty driver are serialized by the atomic_write_lock
and are then processed in chunks to the device. The line discipline
write method will not be invoked in parallel for each device.

.. _`tty_send_xchar`:

tty_send_xchar
==============

.. c:function:: int tty_send_xchar(struct tty_struct *tty, char ch)

    send priority character

    :param struct tty_struct \*tty:
        *undescribed*

    :param char ch:
        *undescribed*

.. _`tty_send_xchar.description`:

Description
-----------

Send a high priority character to the tty even if stopped

.. _`tty_send_xchar.locking`:

Locking
-------

none for xchar method, write ordering for write method.

.. _`pty_line_name`:

pty_line_name
=============

.. c:function:: void pty_line_name(struct tty_driver *driver, int index, char *p)

    generate name for a pty

    :param struct tty_driver \*driver:
        the tty driver in use

    :param int index:
        the minor number

    :param char \*p:
        output buffer of at least 6 bytes

.. _`pty_line_name.description`:

Description
-----------

Generate a name from a driver reference and write it to the output
buffer.

.. _`pty_line_name.locking`:

Locking
-------

None

.. _`tty_line_name`:

tty_line_name
=============

.. c:function:: ssize_t tty_line_name(struct tty_driver *driver, int index, char *p)

    generate name for a tty

    :param struct tty_driver \*driver:
        the tty driver in use

    :param int index:
        the minor number

    :param char \*p:
        output buffer of at least 7 bytes

.. _`tty_line_name.description`:

Description
-----------

Generate a name from a driver reference and write it to the output
buffer.

.. _`tty_line_name.locking`:

Locking
-------

None

.. _`tty_driver_lookup_tty`:

tty_driver_lookup_tty
=====================

.. c:function:: struct tty_struct *tty_driver_lookup_tty(struct tty_driver *driver, struct file *file, int idx)

    find an existing tty, if any

    :param struct tty_driver \*driver:
        the driver for the tty

    :param struct file \*file:
        *undescribed*

    :param int idx:
        the minor number

.. _`tty_driver_lookup_tty.description`:

Description
-----------

Return the tty, if found. If not found, return NULL or \ :c:func:`ERR_PTR`\  if the
driver \ :c:func:`lookup`\  method returns an error.

.. _`tty_driver_lookup_tty.locking`:

Locking
-------

tty_mutex must be held. If the tty is found, bump the tty kref.

.. _`tty_init_termios`:

tty_init_termios
================

.. c:function:: void tty_init_termios(struct tty_struct *tty)

    helper for termios setup

    :param struct tty_struct \*tty:
        the tty to set up

.. _`tty_init_termios.description`:

Description
-----------

Initialise the termios structures for this tty. Thus runs under
the tty_mutex currently so we can be relaxed about ordering.

.. _`tty_driver_install_tty`:

tty_driver_install_tty
======================

.. c:function:: int tty_driver_install_tty(struct tty_driver *driver, struct tty_struct *tty)

    install a tty entry in the driver

    :param struct tty_driver \*driver:
        the driver for the tty

    :param struct tty_struct \*tty:
        the tty

.. _`tty_driver_install_tty.description`:

Description
-----------

Install a tty object into the driver tables. The tty->index field
will be set by the time this is called. This method is responsible
for ensuring any need additional structures are allocated and
configured.

.. _`tty_driver_install_tty.locking`:

Locking
-------

tty_mutex for now

.. _`tty_driver_remove_tty`:

tty_driver_remove_tty
=====================

.. c:function:: void tty_driver_remove_tty(struct tty_driver *driver, struct tty_struct *tty)

    remove a tty from the driver tables

    :param struct tty_driver \*driver:
        the driver for the tty

    :param struct tty_struct \*tty:
        *undescribed*

.. _`tty_driver_remove_tty.description`:

Description
-----------

Remvoe a tty object from the driver tables. The tty->index field
will be set by the time this is called.

.. _`tty_driver_remove_tty.locking`:

Locking
-------

tty_mutex for now

.. _`tty_init_dev`:

tty_init_dev
============

.. c:function:: struct tty_struct *tty_init_dev(struct tty_driver *driver, int idx)

    initialise a tty device

    :param struct tty_driver \*driver:
        tty driver we are opening a device on

    :param int idx:
        device index

.. _`tty_init_dev.description`:

Description
-----------

Prepare a tty device. This may not be a "new" clean device but
could also be an active device. The pty drivers require special
handling because of this.

.. _`tty_init_dev.locking`:

Locking
-------

The function is called under the tty_mutex, which
protects us from the tty struct or driver itself going away.

On exit the tty device has the line discipline attached and
a reference count of 1. If a pair was created for pty/tty use
and the other was a pty master then it too has a reference count of 1.

WSH 06/09/97: Rewritten to remove races and properly clean up after a
failed open.  The new code protects the open with a mutex, so it's
really quite straightforward.  The mutex locking can probably be
relaxed for the (most common) case of reopening a tty.

.. _`tty_flush_works`:

tty_flush_works
===============

.. c:function:: void tty_flush_works(struct tty_struct *tty)

    flush all works of a tty/pty pair

    :param struct tty_struct \*tty:
        tty device to flush works for (or either end of a pty pair)

.. _`tty_flush_works.description`:

Description
-----------

Sync flush all works belonging to \ ``tty``\  (and the 'other' tty).

.. _`release_one_tty`:

release_one_tty
===============

.. c:function:: void release_one_tty(struct work_struct *work)

    release tty structure memory

    :param struct work_struct \*work:
        *undescribed*

.. _`release_one_tty.description`:

Description
-----------

Releases memory associated with a tty structure, and clears out the
driver table slots. This function is called when a device is no longer
in use. It also gets called when setup of a device fails.

.. _`release_one_tty.locking`:

Locking
-------

takes the file list lock internally when working on the list
of ttys that the driver keeps.

This method gets called from a work queue so that the driver private
cleanup ops can sleep (needed for USB at least)

.. _`tty_kref_put`:

tty_kref_put
============

.. c:function:: void tty_kref_put(struct tty_struct *tty)

    release a tty kref

    :param struct tty_struct \*tty:
        tty device

.. _`tty_kref_put.description`:

Description
-----------

Release a reference to a tty device and if need be let the kref
layer destruct the object for us

.. _`release_tty`:

release_tty
===========

.. c:function:: void release_tty(struct tty_struct *tty, int idx)

    release tty structure memory

    :param struct tty_struct \*tty:
        *undescribed*

    :param int idx:
        *undescribed*

.. _`release_tty.description`:

Description
-----------

Release both \ ``tty``\  and a possible linked partner (think pty pair),
and decrement the refcount of the backing module.

.. _`release_tty.locking`:

Locking
-------

tty_mutex
takes the file list lock internally when working on the list
of ttys that the driver keeps.

.. _`tty_release_checks`:

tty_release_checks
==================

.. c:function:: int tty_release_checks(struct tty_struct *tty, int idx)

    check a tty before real release

    :param struct tty_struct \*tty:
        tty to check

    :param int idx:
        index of the tty

.. _`tty_release_checks.description`:

Description
-----------

Performs some paranoid checking before true release of the \ ``tty``\ .
This is a no-op unless TTY_PARANOIA_CHECK is defined.

.. _`tty_release`:

tty_release
===========

.. c:function:: int tty_release(struct inode *inode, struct file *filp)

    vfs callback for close

    :param struct inode \*inode:
        inode of tty

    :param struct file \*filp:
        file pointer for handle to tty

.. _`tty_release.description`:

Description
-----------

Called the last time each file handle is closed that references
this tty. There may however be several such references.

.. _`tty_release.locking`:

Locking
-------

Takes bkl. See tty_release_dev

Even releasing the tty structures is a tricky business.. We have
to be very careful that the structures are all released at the
same time, as interrupts might otherwise get the wrong pointers.

WSH 09/09/97: rewritten to avoid some nasty race conditions that could
lead to double frees or releasing memory still in use.

.. _`tty_open_current_tty`:

tty_open_current_tty
====================

.. c:function:: struct tty_struct *tty_open_current_tty(dev_t device, struct file *filp)

    get locked tty of current task

    :param dev_t device:
        device number

    :param struct file \*filp:
        file pointer to tty

.. _`tty_open_current_tty.description`:

Description
-----------

Performs a re-open of the current task's controlling tty.

We cannot return driver and index like for the other nodes because
devpts will not work then. It expects inodes to be from devpts FS.

.. _`tty_lookup_driver`:

tty_lookup_driver
=================

.. c:function:: struct tty_driver *tty_lookup_driver(dev_t device, struct file *filp, int *index)

    lookup a tty driver for a given device file

    :param dev_t device:
        device number

    :param struct file \*filp:
        file pointer to tty

    :param int \*index:
        index for the device in the \ ``return``\  driver

.. _`tty_lookup_driver.description`:

Description
-----------

If \ ``return``\  is not erroneous, the caller is responsible to decrement the
refcount by tty_driver_kref_put.

.. _`tty_lookup_driver.locking`:

Locking
-------

tty_mutex protects get_tty_driver

.. _`tty_open_by_driver`:

tty_open_by_driver
==================

.. c:function:: struct tty_struct *tty_open_by_driver(dev_t device, struct inode *inode, struct file *filp)

    open a tty device

    :param dev_t device:
        dev_t of device to open

    :param struct inode \*inode:
        inode of device file

    :param struct file \*filp:
        file pointer to tty

.. _`tty_open_by_driver.description`:

Description
-----------

Performs the driver lookup, checks for a reopen, or otherwise
performs the first-time tty initialization.

Returns the locked initialized or re-opened \ :c:type:`struct tty_struct <tty_struct>`\ 

.. _`tty_open_by_driver.claims-the-global-tty_mutex-to-serialize`:

Claims the global tty_mutex to serialize
----------------------------------------

- concurrent first-time tty initialization
- concurrent tty driver removal w/ lookup
- concurrent tty removal from driver table

.. _`tty_open`:

tty_open
========

.. c:function:: int tty_open(struct inode *inode, struct file *filp)

    open a tty device

    :param struct inode \*inode:
        inode of device file

    :param struct file \*filp:
        file pointer to tty

.. _`tty_open.description`:

Description
-----------

tty_open and tty_release keep up the tty count that contains the
number of opens done on a tty. We cannot use the inode-count, as
different inodes might point to the same tty.

Open-counting is needed for pty masters, as well as for keeping

.. _`tty_open.track-of-serial-lines`:

track of serial lines
---------------------

DTR is dropped when the last close happens.
(This is not done solely through tty->count, now.  - Ted 1/27/92)

The termios state of a pty is reset on first open so that
settings don't persist across reuse.

.. _`tty_open.locking`:

Locking
-------

tty_mutex protects tty, tty_lookup_driver and tty_init_dev.
tty->count should protect the rest.
->siglock protects ->signal/->sighand

.. _`tty_open.note`:

Note
----

the tty_unlock/lock cases without a ref are only safe due to
tty_mutex

.. _`tty_poll`:

tty_poll
========

.. c:function:: unsigned int tty_poll(struct file *filp, poll_table *wait)

    check tty status

    :param struct file \*filp:
        file being polled

    :param poll_table \*wait:
        poll wait structures to update

.. _`tty_poll.description`:

Description
-----------

Call the line discipline polling method to obtain the poll
status of the device.

.. _`tty_poll.locking`:

Locking
-------

locks called line discipline but ldisc poll method
may be re-entered freely by other callers.

.. _`tiocsti`:

tiocsti
=======

.. c:function:: int tiocsti(struct tty_struct *tty, char __user *p)

    fake input character

    :param struct tty_struct \*tty:
        tty to fake input into

    :param char __user \*p:
        pointer to character

.. _`tiocsti.description`:

Description
-----------

Fake input to a tty device. Does the necessary locking and
input management.

.. _`tiocsti.fixme`:

FIXME
-----

does not honour flow control ??

may race normal receive processing

.. _`tiocsti.locking`:

Locking
-------

Called functions take tty_ldiscs_lock
current->signal->tty check is safe without locks

.. _`tiocgwinsz`:

tiocgwinsz
==========

.. c:function:: int tiocgwinsz(struct tty_struct *tty, struct winsize __user *arg)

    implement window query ioctl \ ``tty``\ ; tty

    :param struct tty_struct \*tty:
        *undescribed*

    :param struct winsize __user \*arg:
        user buffer for result

.. _`tiocgwinsz.description`:

Description
-----------

Copies the kernel idea of the window size into the user buffer.

.. _`tiocgwinsz.locking`:

Locking
-------

tty->winsize_mutex is taken to ensure the winsize data
is consistent.

.. _`tty_do_resize`:

tty_do_resize
=============

.. c:function:: int tty_do_resize(struct tty_struct *tty, struct winsize *ws)

    resize event

    :param struct tty_struct \*tty:
        tty being resized

    :param struct winsize \*ws:
        *undescribed*

.. _`tty_do_resize.description`:

Description
-----------

Update the termios variables and send the necessary signals to
peform a terminal resize correctly

.. _`tiocswinsz`:

tiocswinsz
==========

.. c:function:: int tiocswinsz(struct tty_struct *tty, struct winsize __user *arg)

    implement window size set ioctl \ ``tty``\ ; tty side of tty

    :param struct tty_struct \*tty:
        *undescribed*

    :param struct winsize __user \*arg:
        user buffer for result

.. _`tiocswinsz.description`:

Description
-----------

Copies the user idea of the window size to the kernel. Traditionally
this is just advisory information but for the Linux console it
actually has driver level meaning and triggers a VC resize.

.. _`tiocswinsz.locking`:

Locking
-------

Driver dependent. The default do_resize method takes the
tty termios mutex and ctrl_lock. The console takes its own lock
then calls into the default method.

.. _`tioccons`:

tioccons
========

.. c:function:: int tioccons(struct file *file)

    allow admin to move logical console

    :param struct file \*file:
        the file to become console

.. _`tioccons.description`:

Description
-----------

Allow the administrator to move the redirected console device

.. _`tioccons.locking`:

Locking
-------

uses redirect_lock to guard the redirect information

.. _`fionbio`:

fionbio
=======

.. c:function:: int fionbio(struct file *file, int __user *p)

    non blocking ioctl

    :param struct file \*file:
        file to set blocking value

    :param int __user \*p:
        user parameter

.. _`fionbio.description`:

Description
-----------

Historical tty interfaces had a blocking control ioctl before
the generic functionality existed. This piece of history is preserved
in the expected tty API of posix OS's.

.. _`fionbio.locking`:

Locking
-------

none, the open file handle ensures it won't go away.

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

.. _`tiocsetd`:

tiocsetd
========

.. c:function:: int tiocsetd(struct tty_struct *tty, int __user *p)

    set line discipline

    :param struct tty_struct \*tty:
        tty device

    :param int __user \*p:
        pointer to user data

.. _`tiocsetd.description`:

Description
-----------

Set the line discipline according to user request.

.. _`tiocsetd.locking`:

Locking
-------

see tty_set_ldisc, this function is just a helper

.. _`tiocgetd`:

tiocgetd
========

.. c:function:: int tiocgetd(struct tty_struct *tty, int __user *p)

    get line discipline

    :param struct tty_struct \*tty:
        tty device

    :param int __user \*p:
        pointer to user data

.. _`tiocgetd.description`:

Description
-----------

Retrieves the line discipline id directly from the ldisc.

.. _`tiocgetd.locking`:

Locking
-------

waits for ldisc reference (in case the line discipline
is changing or the tty is being hungup)

.. _`send_break`:

send_break
==========

.. c:function:: int send_break(struct tty_struct *tty, unsigned int duration)

    performed time break

    :param struct tty_struct \*tty:
        device to break on

    :param unsigned int duration:
        timeout in mS

.. _`send_break.description`:

Description
-----------

Perform a timed break on hardware that lacks its own driver level
timed break functionality.

.. _`send_break.locking`:

Locking
-------

atomic_write_lock serializes

.. _`tty_tiocmget`:

tty_tiocmget
============

.. c:function:: int tty_tiocmget(struct tty_struct *tty, int __user *p)

    get modem status

    :param struct tty_struct \*tty:
        tty device

    :param int __user \*p:
        pointer to result

.. _`tty_tiocmget.description`:

Description
-----------

Obtain the modem status bits from the tty driver if the feature
is supported. Return -EINVAL if it is not available.

.. _`tty_tiocmget.locking`:

Locking
-------

none (up to the driver)

.. _`tty_tiocmset`:

tty_tiocmset
============

.. c:function:: int tty_tiocmset(struct tty_struct *tty, unsigned int cmd, unsigned __user *p)

    set modem status

    :param struct tty_struct \*tty:
        tty device

    :param unsigned int cmd:
        command - clear bits, set bits or set all

    :param unsigned __user \*p:
        pointer to desired bits

.. _`tty_tiocmset.description`:

Description
-----------

Set the modem status bits from the tty driver if the feature
is supported. Return -EINVAL if it is not available.

.. _`tty_tiocmset.locking`:

Locking
-------

none (up to the driver)

.. _`alloc_tty_struct`:

alloc_tty_struct
================

.. c:function:: struct tty_struct *alloc_tty_struct(struct tty_driver *driver, int idx)

    :param struct tty_driver \*driver:
        *undescribed*

    :param int idx:
        *undescribed*

.. _`alloc_tty_struct.description`:

Description
-----------

This subroutine allocates and initializes a tty structure.

.. _`alloc_tty_struct.locking`:

Locking
-------

none - tty in question is not exposed at this point

.. _`tty_put_char`:

tty_put_char
============

.. c:function:: int tty_put_char(struct tty_struct *tty, unsigned char ch)

    write one character to a tty

    :param struct tty_struct \*tty:
        tty

    :param unsigned char ch:
        character

.. _`tty_put_char.description`:

Description
-----------

Write one byte to the tty using the provided put_char method
if present. Returns the number of characters successfully output.

.. _`tty_put_char.note`:

Note
----

the specific put_char operation in the driver layer may go
away soon. Don't call it directly, use this method

.. _`tty_register_device`:

tty_register_device
===================

.. c:function:: struct device *tty_register_device(struct tty_driver *driver, unsigned index, struct device *device)

    register a tty device

    :param struct tty_driver \*driver:
        the tty driver that describes the tty device

    :param unsigned index:
        the index in the tty driver for this tty device

    :param struct device \*device:
        a struct device that is associated with this tty device.
        This field is optional, if there is no known struct device
        for this tty device it can be set to NULL safely.

.. _`tty_register_device.description`:

Description
-----------

Returns a pointer to the struct device for this tty device
(or ERR_PTR(-EFOO) on error).

This call is required to be made to register an individual tty device
if the tty driver's flags have the TTY_DRIVER_DYNAMIC_DEV bit set.  If
that bit is not set, this function should not be called by a tty
driver.

.. _`tty_register_device.locking`:

Locking
-------

??

.. _`tty_register_device_attr`:

tty_register_device_attr
========================

.. c:function:: struct device *tty_register_device_attr(struct tty_driver *driver, unsigned index, struct device *device, void *drvdata, const struct attribute_group **attr_grp)

    register a tty device

    :param struct tty_driver \*driver:
        the tty driver that describes the tty device

    :param unsigned index:
        the index in the tty driver for this tty device

    :param struct device \*device:
        a struct device that is associated with this tty device.
        This field is optional, if there is no known struct device
        for this tty device it can be set to NULL safely.

    :param void \*drvdata:
        Driver data to be set to device.

    :param const struct attribute_group \*\*attr_grp:
        Attribute group to be set on device.

.. _`tty_register_device_attr.description`:

Description
-----------

Returns a pointer to the struct device for this tty device
(or ERR_PTR(-EFOO) on error).

This call is required to be made to register an individual tty device
if the tty driver's flags have the TTY_DRIVER_DYNAMIC_DEV bit set.  If
that bit is not set, this function should not be called by a tty
driver.

.. _`tty_register_device_attr.locking`:

Locking
-------

??

.. _`tty_unregister_device`:

tty_unregister_device
=====================

.. c:function:: void tty_unregister_device(struct tty_driver *driver, unsigned index)

    unregister a tty device

    :param struct tty_driver \*driver:
        the tty driver that describes the tty device

    :param unsigned index:
        the index in the tty driver for this tty device

.. _`tty_unregister_device.description`:

Description
-----------

If a tty device is registered with a call to \ :c:func:`tty_register_device`\  then
this function must be called when the tty device is gone.

.. _`tty_unregister_device.locking`:

Locking
-------

??

.. _`__tty_alloc_driver`:

__tty_alloc_driver
==================

.. c:function:: struct tty_driver *__tty_alloc_driver(unsigned int lines, struct module *owner, unsigned long flags)

    - allocate tty driver

    :param unsigned int lines:
        count of lines this driver can handle at most

    :param struct module \*owner:
        module which is repsonsible for this driver

    :param unsigned long flags:
        some of TTY_DRIVER\_\* flags, will be set in driver->flags

.. _`__tty_alloc_driver.description`:

Description
-----------

This should not be called directly, some of the provided macros should be
used instead. Use IS_ERR and friends on \ ``retval``\ .

.. This file was automatic generated / don't edit.

