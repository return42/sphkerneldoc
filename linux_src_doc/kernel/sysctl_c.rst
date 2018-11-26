.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sysctl.c

.. _`sysctl_writes_mode`:

enum sysctl_writes_mode
=======================

.. c:type:: enum sysctl_writes_mode

    supported sysctl write modes

.. _`sysctl_writes_mode.definition`:

Definition
----------

.. code-block:: c

    enum sysctl_writes_mode {
        SYSCTL_WRITES_LEGACY,
        SYSCTL_WRITES_WARN,
        SYSCTL_WRITES_STRICT
    };

.. _`sysctl_writes_mode.constants`:

Constants
---------

SYSCTL_WRITES_LEGACY
    each write syscall must fully contain the sysctl value
    to be written, and multiple writes on the same sysctl file descriptor
    will rewrite the sysctl value, regardless of file position. No warning
    is issued when the initial position is not 0.

SYSCTL_WRITES_WARN
    same as above but warn when the initial file position is
    not 0.

SYSCTL_WRITES_STRICT
    writes to numeric sysctl entries must always be at
    file position 0 and the value must be fully contained in the buffer
    sent to the write syscall. If dealing with strings respect the file
    position, but restrict this to the max length of the buffer, anything
    passed the max lenght will be ignored. Multiple writes will append
    to the buffer.

.. _`sysctl_writes_mode.description`:

Description
-----------

These write modes control how current file position affects the behavior of
updating sysctl values through the proc interface on each write.

.. _`proc_first_pos_non_zero_ignore`:

proc_first_pos_non_zero_ignore
==============================

.. c:function:: bool proc_first_pos_non_zero_ignore(loff_t *ppos, struct ctl_table *table)

    check if first position is allowed

    :param ppos:
        file position
    :type ppos: loff_t \*

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

.. _`proc_first_pos_non_zero_ignore.description`:

Description
-----------

Returns true if the first position is non-zero and the sysctl_writes_strict
mode indicates this is not allowed for numeric input types. String proc
handlers can ignore the return value.

.. _`proc_dostring`:

proc_dostring
=============

.. c:function:: int proc_dostring(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a string sysctl

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_dostring.description`:

Description
-----------

Reads/writes a string from/to the user buffer. If the kernel
buffer provided is not large enough to hold the string, the
string is truncated. The copied string is \ ``NULL-terminated``\ .
If the string is being read by the user process, it is copied
and a newline '\n' is added. It is truncated if the buffer is
not large enough.

Returns 0 on success.

.. _`proc_get_long`:

proc_get_long
=============

.. c:function:: int proc_get_long(char **buf, size_t *size, unsigned long *val, bool *neg, const char *perm_tr, unsigned perm_tr_len, char *tr)

    reads an ASCII formatted integer from a user buffer

    :param buf:
        a kernel buffer
    :type buf: char \*\*

    :param size:
        size of the kernel buffer
    :type size: size_t \*

    :param val:
        this is where the number will be stored
    :type val: unsigned long \*

    :param neg:
        set to \ ``TRUE``\  if number is negative
    :type neg: bool \*

    :param perm_tr:
        a vector which contains the allowed trailers
    :type perm_tr: const char \*

    :param perm_tr_len:
        size of the perm_tr vector
    :type perm_tr_len: unsigned

    :param tr:
        pointer to store the trailer character
    :type tr: char \*

.. _`proc_get_long.description`:

Description
-----------

In case of success \ ``0``\  is returned and \ ``buf``\  and \ ``size``\  are updated with
the amount of bytes read. If \ ``tr``\  is non-NULL and a trailing
character exists (size is non-zero after returning from this
function), \ ``tr``\  is updated with the trailing character.

.. _`proc_put_long`:

proc_put_long
=============

.. c:function:: int proc_put_long(void __user **buf, size_t *size, unsigned long val, bool neg)

    converts an integer to a decimal ASCII formatted string

    :param buf:
        the user buffer
    :type buf: void __user \*\*

    :param size:
        the size of the user buffer
    :type size: size_t \*

    :param val:
        the integer to be converted
    :type val: unsigned long

    :param neg:
        sign of the number, \ ``TRUE``\  for negative
    :type neg: bool

.. _`proc_put_long.description`:

Description
-----------

In case of success \ ``0``\  is returned and \ ``buf``\  and \ ``size``\  are updated with
the amount of bytes written.

.. _`proc_dointvec`:

proc_dointvec
=============

.. c:function:: int proc_dointvec(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of integers

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_dointvec.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.

Returns 0 on success.

.. _`proc_douintvec`:

proc_douintvec
==============

.. c:function:: int proc_douintvec(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of unsigned integers

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_douintvec.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) unsigned integer
values from/to the user buffer, treated as an ASCII string.

Returns 0 on success.

.. _`do_proc_dointvec_minmax_conv_param`:

struct do_proc_dointvec_minmax_conv_param
=========================================

.. c:type:: struct do_proc_dointvec_minmax_conv_param

    \ :c:func:`proc_dointvec_minmax`\  range checking structure

.. _`do_proc_dointvec_minmax_conv_param.definition`:

Definition
----------

.. code-block:: c

    struct do_proc_dointvec_minmax_conv_param {
        int *min;
        int *max;
    }

.. _`do_proc_dointvec_minmax_conv_param.members`:

Members
-------

min
    pointer to minimum allowable value

max
    pointer to maximum allowable value

.. _`do_proc_dointvec_minmax_conv_param.description`:

Description
-----------

The do_proc_dointvec_minmax_conv_param structure provides the
minimum and maximum values for doing range checking for those sysctl
parameters that use the \ :c:func:`proc_dointvec_minmax`\  handler.

.. _`proc_dointvec_minmax`:

proc_dointvec_minmax
====================

.. c:function:: int proc_dointvec_minmax(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of integers with min/max values

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_dointvec_minmax.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success or -EINVAL on write when the range check fails.

.. _`do_proc_douintvec_minmax_conv_param`:

struct do_proc_douintvec_minmax_conv_param
==========================================

.. c:type:: struct do_proc_douintvec_minmax_conv_param

    \ :c:func:`proc_douintvec_minmax`\  range checking structure

.. _`do_proc_douintvec_minmax_conv_param.definition`:

Definition
----------

.. code-block:: c

    struct do_proc_douintvec_minmax_conv_param {
        unsigned int *min;
        unsigned int *max;
    }

.. _`do_proc_douintvec_minmax_conv_param.members`:

Members
-------

min
    pointer to minimum allowable value

max
    pointer to maximum allowable value

.. _`do_proc_douintvec_minmax_conv_param.description`:

Description
-----------

The do_proc_douintvec_minmax_conv_param structure provides the
minimum and maximum values for doing range checking for those sysctl
parameters that use the \ :c:func:`proc_douintvec_minmax`\  handler.

.. _`proc_douintvec_minmax`:

proc_douintvec_minmax
=====================

.. c:function:: int proc_douintvec_minmax(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of unsigned ints with min/max values

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_douintvec_minmax.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) unsigned integer
values from/to the user buffer, treated as an ASCII string. Negative
strings are not allowed.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max). There is a final sanity
check for UINT_MAX to avoid having to support wrap around uses from
userspace.

Returns 0 on success or -ERANGE on write when the range check fails.

.. _`proc_doulongvec_minmax`:

proc_doulongvec_minmax
======================

.. c:function:: int proc_doulongvec_minmax(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of long integers with min/max values

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_doulongvec_minmax.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned long) unsigned long
values from/to the user buffer, treated as an ASCII string.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success.

.. _`proc_doulongvec_ms_jiffies_minmax`:

proc_doulongvec_ms_jiffies_minmax
=================================

.. c:function:: int proc_doulongvec_ms_jiffies_minmax(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of millisecond values with min/max values

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_doulongvec_ms_jiffies_minmax.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned long) unsigned long
values from/to the user buffer, treated as an ASCII string. The values
are treated as milliseconds, and converted to jiffies when they are stored.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success.

.. _`proc_dointvec_jiffies`:

proc_dointvec_jiffies
=====================

.. c:function:: int proc_dointvec_jiffies(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of integers as seconds

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_dointvec_jiffies.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.
The values read are assumed to be in seconds, and are converted into
jiffies.

Returns 0 on success.

.. _`proc_dointvec_userhz_jiffies`:

proc_dointvec_userhz_jiffies
============================

.. c:function:: int proc_dointvec_userhz_jiffies(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of integers as 1/USER_HZ seconds

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        pointer to the file position
    :type ppos: loff_t \*

.. _`proc_dointvec_userhz_jiffies.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.
The values read are assumed to be in 1/USER_HZ seconds, and
are converted into jiffies.

Returns 0 on success.

.. _`proc_dointvec_ms_jiffies`:

proc_dointvec_ms_jiffies
========================

.. c:function:: int proc_dointvec_ms_jiffies(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of integers as 1 milliseconds

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        the current position in the file
    :type ppos: loff_t \*

.. _`proc_dointvec_ms_jiffies.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.
The values read are assumed to be in 1/1000 seconds, and
are converted into jiffies.

Returns 0 on success.

.. _`proc_do_large_bitmap`:

proc_do_large_bitmap
====================

.. c:function:: int proc_do_large_bitmap(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read/write from/to a large bitmap

    :param table:
        the sysctl table
    :type table: struct ctl_table \*

    :param write:
        \ ``TRUE``\  if this is a write to the sysctl file
    :type write: int

    :param buffer:
        the user buffer
    :type buffer: void __user \*

    :param lenp:
        the size of the user buffer
    :type lenp: size_t \*

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`proc_do_large_bitmap.description`:

Description
-----------

The bitmap is stored at table->data and the bitmap length (in bits)
in table->maxlen.

We use a range comma separated format (e.g. 1,3-4,10-10) so that
large bitmaps may be represented in a compact manner. Writing into
the file will clear the bitmap then update it with the given input.

Returns 0 on success.

.. This file was automatic generated / don't edit.

