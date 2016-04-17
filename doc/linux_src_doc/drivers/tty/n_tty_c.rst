.. -*- coding: utf-8; mode: rst -*-

=======
n_tty.c
=======


.. _`n_tty_kick_worker`:

n_tty_kick_worker
=================

.. c:function:: void n_tty_kick_worker (struct tty_struct *tty)

    start input worker (if required)

    :param struct tty_struct \*tty:
        terminal



.. _`n_tty_kick_worker.description`:

Description
-----------

Re-schedules the flip buffer work if it may have stopped

Caller holds exclusive termios_rwsem
or

:c:func:`n_tty_read`/consumer path::

        holds non-exclusive termios_rwsem



.. _`n_tty_write_wakeup`:

n_tty_write_wakeup
==================

.. c:function:: void n_tty_write_wakeup (struct tty_struct *tty)

    asynchronous I/O notifier

    :param struct tty_struct \*tty:
        tty device



.. _`n_tty_write_wakeup.description`:

Description
-----------

Required for the ptys, serial driver etc. since processes
that attach themselves to the master and rely on ASYNC
IO must be woken up



.. _`put_tty_queue`:

put_tty_queue
=============

.. c:function:: void put_tty_queue (unsigned char c, struct n_tty_data *ldata)

    add character to tty

    :param unsigned char c:
        character

    :param struct n_tty_data \*ldata:
        n_tty data



.. _`put_tty_queue.description`:

Description
-----------

Add a character to the tty read_buf queue.

:c:func:`n_tty_receive_buf`/producer path::

        caller holds non-exclusive termios_rwsem



.. _`reset_buffer_flags`:

reset_buffer_flags
==================

.. c:function:: void reset_buffer_flags (struct n_tty_data *ldata)

    reset buffer state

    :param struct n_tty_data \*ldata:

        *undescribed*



.. _`reset_buffer_flags.description`:

Description
-----------

Reset the read buffer counters and clear the flags.
Called from :c:func:`n_tty_open` and :c:func:`n_tty_flush_buffer`.



.. _`reset_buffer_flags.locking`:

Locking
-------

caller holds exclusive termios_rwsem
(or locking is not required)



.. _`n_tty_flush_buffer`:

n_tty_flush_buffer
==================

.. c:function:: void n_tty_flush_buffer (struct tty_struct *tty)

    clean input queue

    :param struct tty_struct \*tty:
        terminal device



.. _`n_tty_flush_buffer.description`:

Description
-----------

Flush the input buffer. Called when the tty layer wants the
buffer flushed (eg at hangup) or when the N_TTY line discipline
internally has to clean the pending queue (for example some signals).

Holds termios_rwsem to exclude producer/consumer while
buffer indices are reset.



.. _`n_tty_flush_buffer.locking`:

Locking
-------

ctrl_lock, exclusive termios_rwsem



.. _`is_utf8_continuation`:

is_utf8_continuation
====================

.. c:function:: int is_utf8_continuation (unsigned char c)

    utf8 multibyte check

    :param unsigned char c:
        byte to check



.. _`is_utf8_continuation.description`:

Description
-----------

Returns true if the utf8 character 'c' is a multibyte continuation
character. We use this to correctly compute the on screen size
of the character when printing



.. _`is_continuation`:

is_continuation
===============

.. c:function:: int is_continuation (unsigned char c, struct tty_struct *tty)

    multibyte check

    :param unsigned char c:
        byte to check

    :param struct tty_struct \*tty:

        *undescribed*



.. _`is_continuation.description`:

Description
-----------

Returns true if the utf8 character 'c' is a multibyte continuation
character and the terminal is in unicode mode.



.. _`do_output_char`:

do_output_char
==============

.. c:function:: int do_output_char (unsigned char c, struct tty_struct *tty, int space)

    output one character

    :param unsigned char c:
        character (or partial unicode symbol)

    :param struct tty_struct \*tty:
        terminal device

    :param int space:
        space available in tty driver write buffer



.. _`do_output_char.description`:

Description
-----------

This is a helper function that handles one output character
(including special characters like TAB, CR, LF, etc.),
doing OPOST processing and putting the results in the
tty driver's write buffer.

Note that Linux currently ignores TABDLY, CRDLY, VTDLY, FFDLY
and NLDLY.  They simply aren't relevant in the world today.
If you ever need them, add them here.

Returns the number of bytes of buffer space used or -1 if
no space left.



.. _`do_output_char.locking`:

Locking
-------

should be called under the output_lock to protect
the column state and space left in the buffer



.. _`process_output`:

process_output
==============

.. c:function:: int process_output (unsigned char c, struct tty_struct *tty)

    output post processor

    :param unsigned char c:
        character (or partial unicode symbol)

    :param struct tty_struct \*tty:
        terminal device



.. _`process_output.description`:

Description
-----------

Output one character with OPOST processing.
Returns -1 when the output device is full and the character
must be retried.



.. _`process_output.locking`:

Locking
-------

output_lock to protect column state and space left
(also, this is called from n_tty_write under the
tty layer write lock)



.. _`process_output_block`:

process_output_block
====================

.. c:function:: ssize_t process_output_block (struct tty_struct *tty, const unsigned char *buf, unsigned int nr)

    block post processor

    :param struct tty_struct \*tty:
        terminal device

    :param const unsigned char \*buf:
        character buffer

    :param unsigned int nr:
        number of bytes to output



.. _`process_output_block.description`:

Description
-----------

Output a block of characters with OPOST processing.
Returns the number of characters output.

This path is used to speed up block console writes, among other
things when processing blocks of output data. It handles only
the simple cases normally found and helps to generate blocks of
symbols for the console driver and thus improve performance.



.. _`process_output_block.locking`:

Locking
-------

output_lock to protect column state and space left
(also, this is called from n_tty_write under the
tty layer write lock)



.. _`__process_echoes`:

__process_echoes
================

.. c:function:: size_t __process_echoes (struct tty_struct *tty)

    write pending echo characters

    :param struct tty_struct \*tty:
        terminal device



.. _`__process_echoes.description`:

Description
-----------

Write previously buffered echo (and other ldisc-generated)
characters to the tty.

Characters generated by the ldisc (including echoes) need to
be buffered because the driver's write buffer can fill during
heavy program output.  Echoing straight to the driver will
often fail under these conditions, causing lost characters and
resulting mismatches of ldisc state information.

Since the ldisc state must represent the characters actually sent
to the driver at the time of the write, operations like certain
changes in column state are also saved in the buffer and executed
here.

A circular fifo buffer is used so that the most recent characters
are prioritized.  Also, when control characters are echoed with a
prefixed "^", the pair is treated atomically and thus not separated.



.. _`__process_echoes.locking`:

Locking
-------

callers must hold output_lock



.. _`add_echo_byte`:

add_echo_byte
=============

.. c:function:: void add_echo_byte (unsigned char c, struct n_tty_data *ldata)

    add a byte to the echo buffer

    :param unsigned char c:
        unicode byte to echo

    :param struct n_tty_data \*ldata:
        n_tty data



.. _`add_echo_byte.description`:

Description
-----------

Add a character or operation byte to the echo buffer.



.. _`echo_move_back_col`:

echo_move_back_col
==================

.. c:function:: void echo_move_back_col (struct n_tty_data *ldata)

    add operation to move back a column

    :param struct n_tty_data \*ldata:
        n_tty data



.. _`echo_move_back_col.description`:

Description
-----------

Add an operation to the echo buffer to move back one column.



.. _`echo_set_canon_col`:

echo_set_canon_col
==================

.. c:function:: void echo_set_canon_col (struct n_tty_data *ldata)

    add operation to set the canon column

    :param struct n_tty_data \*ldata:
        n_tty data



.. _`echo_set_canon_col.description`:

Description
-----------

Add an operation to the echo buffer to set the canon column
to the current column.



.. _`echo_erase_tab`:

echo_erase_tab
==============

.. c:function:: void echo_erase_tab (unsigned int num_chars, int after_tab, struct n_tty_data *ldata)

    add operation to erase a tab

    :param unsigned int num_chars:
        number of character columns already used

    :param int after_tab:
        true if num_chars starts after a previous tab

    :param struct n_tty_data \*ldata:
        n_tty data



.. _`echo_erase_tab.description`:

Description
-----------

Add an operation to the echo buffer to erase a tab.

Called by the eraser function, which knows how many character
columns have been used since either a previous tab or the start
of input.  This information will be used later, along with
canon column (if applicable), to go back the correct number
of columns.



.. _`echo_char_raw`:

echo_char_raw
=============

.. c:function:: void echo_char_raw (unsigned char c, struct n_tty_data *ldata)

    echo a character raw

    :param unsigned char c:
        unicode byte to echo

    :param struct n_tty_data \*ldata:

        *undescribed*



.. _`echo_char_raw.description`:

Description
-----------

Echo user input back onto the screen. This must be called only when
L_ECHO(tty) is true. Called from the driver receive_buf path.

This variant does not treat control characters specially.



.. _`echo_char`:

echo_char
=========

.. c:function:: void echo_char (unsigned char c, struct tty_struct *tty)

    echo a character

    :param unsigned char c:
        unicode byte to echo

    :param struct tty_struct \*tty:
        terminal device



.. _`echo_char.description`:

Description
-----------

Echo user input back onto the screen. This must be called only when
L_ECHO(tty) is true. Called from the driver receive_buf path.

This variant tags control characters to be echoed as "^X"
(where X is the letter representing the control char).



.. _`finish_erasing`:

finish_erasing
==============

.. c:function:: void finish_erasing (struct n_tty_data *ldata)

    complete erase

    :param struct n_tty_data \*ldata:
        n_tty data



.. _`eraser`:

eraser
======

.. c:function:: void eraser (unsigned char c, struct tty_struct *tty)

    handle erase function

    :param unsigned char c:
        character input

    :param struct tty_struct \*tty:
        terminal device



.. _`eraser.description`:

Description
-----------

Perform erase and necessary output when an erase character is
present in the stream from the driver layer. Handles the complexities
of UTF-8 multibyte symbols.

:c:func:`n_tty_receive_buf`/producer path::

        caller holds non-exclusive termios_rwsem



.. _`__isig`:

__isig
======

.. c:function:: void __isig (int sig, struct tty_struct *tty)

    handle the ISIG optio

    :param int sig:
        signal

    :param struct tty_struct \*tty:
        terminal



.. _`__isig.description`:

Description
-----------

Called when a signal is being sent due to terminal input.
Called from the driver receive_buf path so serialized.

Performs input and output flush if !NOFLSH. In this context, the echo
buffer is 'output'. The signal is processed first to alert any current
readers or writers to discontinue and exit their i/o loops.



.. _`__isig.locking`:

Locking
-------

ctrl_lock



.. _`n_tty_receive_break`:

n_tty_receive_break
===================

.. c:function:: void n_tty_receive_break (struct tty_struct *tty)

    handle break

    :param struct tty_struct \*tty:
        terminal



.. _`n_tty_receive_break.description`:

Description
-----------

An RS232 break event has been hit in the incoming bitstream. This
can cause a variety of events depending upon the termios settings.

:c:func:`n_tty_receive_buf`/producer path::

        caller holds non-exclusive termios_rwsem



.. _`n_tty_receive_break.note`:

Note
----

may get exclusive termios_rwsem if flushing input buffer



.. _`n_tty_receive_overrun`:

n_tty_receive_overrun
=====================

.. c:function:: void n_tty_receive_overrun (struct tty_struct *tty)

    handle overrun reporting

    :param struct tty_struct \*tty:
        terminal



.. _`n_tty_receive_overrun.description`:

Description
-----------

Data arrived faster than we could process it. While the tty
driver has flagged this the bits that were missed are gone
forever.

Called from the receive_buf path so single threaded. Does not
need locking as num_overrun and overrun_time are function
private.



.. _`n_tty_receive_parity_error`:

n_tty_receive_parity_error
==========================

.. c:function:: void n_tty_receive_parity_error (struct tty_struct *tty, unsigned char c)

    error notifier

    :param struct tty_struct \*tty:
        terminal device

    :param unsigned char c:
        character



.. _`n_tty_receive_parity_error.description`:

Description
-----------

Process a parity error and queue the right data to indicate
the error case if necessary.

:c:func:`n_tty_receive_buf`/producer path::

        caller holds non-exclusive termios_rwsem



.. _`n_tty_receive_char_special`:

n_tty_receive_char_special
==========================

.. c:function:: int n_tty_receive_char_special (struct tty_struct *tty, unsigned char c)

    perform processing

    :param struct tty_struct \*tty:
        terminal device

    :param unsigned char c:
        character



.. _`n_tty_receive_char_special.description`:

Description
-----------

Process an individual character of input received from the driver.
This is serialized with respect to itself by the rules for the
driver above.

:c:func:`n_tty_receive_buf`/producer path::

        caller holds non-exclusive termios_rwsem
        publishes canon_head if canonical mode is active

Returns 1 if LNEXT was received, else returns 0



.. _`n_tty_receive_buf_common`:

n_tty_receive_buf_common
========================

.. c:function:: int n_tty_receive_buf_common (struct tty_struct *tty, const unsigned char *cp, char *fp, int count, int flow)

    process input

    :param struct tty_struct \*tty:
        device to receive input

    :param const unsigned char \*cp:
        input chars

    :param char \*fp:
        flags for each char (if NULL, all chars are TTY_NORMAL)

    :param int count:
        number of input chars in ``cp``

    :param int flow:

        *undescribed*



.. _`n_tty_receive_buf_common.description`:

Description
-----------

Called by the terminal driver when a block of characters has
been received. This function must be called from soft contexts
not from interrupt context. The driver is responsible for making
calls one at a time and in order (or using flush_to_ldisc)

Returns the # of input chars from ``cp`` which were processed.

In canonical mode, the maximum line length is 4096 chars (including
the line termination char); lines longer than 4096 chars are
truncated. After 4095 chars, input data is still processed but
not stored. Overflow processing ensures the tty can always
receive more input until at least one line can be read.

In non-canonical mode, the read buffer will only accept 4095 chars;
this provides the necessary space for a newline char if the input
mode is switched to canonical.

Note it is possible for the read buffer to _contain_ 4096 chars
in non-canonical mode: the read buffer could already contain the
maximum canon line of 4096 chars when the mode is switched to
non-canonical.

:c:func:`n_tty_receive_buf`/producer path::

        claims non-exclusive termios_rwsem
        publishes commit_head or canon_head



.. _`n_tty_set_termios`:

n_tty_set_termios
=================

.. c:function:: void n_tty_set_termios (struct tty_struct *tty, struct ktermios *old)

    termios data changed

    :param struct tty_struct \*tty:
        terminal

    :param struct ktermios \*old:
        previous data



.. _`n_tty_set_termios.description`:

Description
-----------

Called by the tty layer when the user changes termios flags so
that the line discipline can plan ahead. This function cannot sleep
and is protected from re-entry by the tty layer. The user is
guaranteed that this function will not be re-entered or in progress
when the ldisc is closed.



.. _`n_tty_set_termios.locking`:

Locking
-------

Caller holds tty->termios_rwsem



.. _`n_tty_close`:

n_tty_close
===========

.. c:function:: void n_tty_close (struct tty_struct *tty)

    close the ldisc for this tty

    :param struct tty_struct \*tty:
        device



.. _`n_tty_close.description`:

Description
-----------

Called from the terminal layer when this line discipline is
being shut down, either because of a close or becsuse of a
discipline change. The function will not be called while other
ldisc methods are in progress.



.. _`n_tty_open`:

n_tty_open
==========

.. c:function:: int n_tty_open (struct tty_struct *tty)

    open an ldisc

    :param struct tty_struct \*tty:
        terminal to open



.. _`n_tty_open.description`:

Description
-----------

Called when this line discipline is being attached to the
terminal device. Can sleep. Called serialized so that no
other events will occur in parallel. No further open will occur
until a close.



.. _`copy_from_read_buf`:

copy_from_read_buf
==================

.. c:function:: int copy_from_read_buf (struct tty_struct *tty, unsigned char __user **b, size_t *nr)

    copy read data directly

    :param struct tty_struct \*tty:
        terminal device

    :param unsigned char __user \*\*b:
        user data

    :param size_t \*nr:
        size of data



.. _`copy_from_read_buf.description`:

Description
-----------

Helper function to speed up n_tty_read.  It is only called when
ICANON is off; it copies characters straight from the tty queue to
user space directly.  It can be profitably called twice; once to
drain the space from the tail pointer to the (physical) end of the
buffer, and once to drain the space from the (physical) beginning of
the buffer to head pointer.

Called under the ldata->atomic_read_lock sem

:c:func:`n_tty_read`/consumer path::

        caller holds non-exclusive termios_rwsem
        read_tail published



.. _`canon_copy_from_read_buf`:

canon_copy_from_read_buf
========================

.. c:function:: int canon_copy_from_read_buf (struct tty_struct *tty, unsigned char __user **b, size_t *nr)

    copy read data in canonical mode

    :param struct tty_struct \*tty:
        terminal device

    :param unsigned char __user \*\*b:
        user data

    :param size_t \*nr:
        size of data



.. _`canon_copy_from_read_buf.description`:

Description
-----------

Helper function for n_tty_read.  It is only called when ICANON is on;
it copies one line of input up to and including the line-delimiting
character into the user-space buffer.



.. _`canon_copy_from_read_buf.nb`:

NB
--

When termios is changed from non-canonical to canonical mode and
the read buffer contains data, :c:func:`n_tty_set_termios` simulates an EOF
push (as if C-d were input) _without_ the DISABLED_CHAR in the buffer.
This causes data already processed as input to be immediately available
as input although a newline has not been received.

Called under the atomic_read_lock mutex

:c:func:`n_tty_read`/consumer path:
caller holds non-exclusive termios_rwsem
read_tail published



.. _`job_control`:

job_control
===========

.. c:function:: int job_control (struct tty_struct *tty, struct file *file)

    check job control

    :param struct tty_struct \*tty:
        tty

    :param struct file \*file:
        file handle



.. _`job_control.description`:

Description
-----------

Perform job control management checks on this file/tty descriptor
and if appropriate send any needed signals and return a negative
error code if action should be taken.



.. _`job_control.locking`:

Locking
-------

redirected write test is safe
current->signal->tty check is safe
ctrl_lock to safely reference tty->pgrp



.. _`n_tty_read`:

n_tty_read
==========

.. c:function:: ssize_t n_tty_read (struct tty_struct *tty, struct file *file, unsigned char __user *buf, size_t nr)

    read function for tty

    :param struct tty_struct \*tty:
        tty device

    :param struct file \*file:
        file object

    :param unsigned char __user \*buf:
        userspace buffer pointer

    :param size_t nr:
        size of I/O



.. _`n_tty_read.description`:

Description
-----------

Perform reads for the line discipline. We are guaranteed that the
line discipline will not be closed under us but we may get multiple
parallel readers and must handle this ourselves. We may also get
a hangup. Always called in user context, may sleep.

This code must be sure never to sleep through a hangup.

:c:func:`n_tty_read`/consumer path::

        claims non-exclusive termios_rwsem
        publishes read_tail



.. _`n_tty_write`:

n_tty_write
===========

.. c:function:: ssize_t n_tty_write (struct tty_struct *tty, struct file *file, const unsigned char *buf, size_t nr)

    write function for tty

    :param struct tty_struct \*tty:
        tty device

    :param struct file \*file:
        file object

    :param const unsigned char \*buf:
        userspace buffer pointer

    :param size_t nr:
        size of I/O



.. _`n_tty_write.description`:

Description
-----------

Write function of the terminal device.  This is serialized with
respect to other write callers but not to termios changes, reads
and other such events.  Since the receive code will echo characters,
thus calling driver write methods, the output_lock is used in
the output processing functions called here as well as in the
echo processing function to protect the column state and space
left in the buffer.

This code must be sure never to sleep through a hangup.



.. _`n_tty_write.locking`:

Locking
-------

output_lock to protect column state and space left
(note that the process_output\*() functions take this
lock themselves)



.. _`n_tty_poll`:

n_tty_poll
==========

.. c:function:: unsigned int n_tty_poll (struct tty_struct *tty, struct file *file, poll_table *wait)

    poll method for N_TTY

    :param struct tty_struct \*tty:
        terminal device

    :param struct file \*file:
        file accessing it

    :param poll_table \*wait:
        poll table



.. _`n_tty_poll.description`:

Description
-----------

Called when the line discipline is asked to :c:func:`poll` for data or
for special events. This code is not serialized with respect to
other events save open/close.

This code must be sure never to sleep through a hangup.
Called without the kernel lock held - fine



.. _`n_tty_inherit_ops`:

n_tty_inherit_ops
=================

.. c:function:: void n_tty_inherit_ops (struct tty_ldisc_ops *ops)

    inherit N_TTY methods

    :param struct tty_ldisc_ops \*ops:
        struct tty_ldisc_ops where to save N_TTY methods



.. _`n_tty_inherit_ops.description`:

Description
-----------

Enables a 'subclass' line discipline to 'inherit' N_TTY methods.

