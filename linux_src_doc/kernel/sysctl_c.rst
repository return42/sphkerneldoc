.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sysctl.c

.. _`proc_dostring`:

proc_dostring
=============

.. c:function:: int proc_dostring(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a string sysctl

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

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

    :param char \*\*buf:
        a kernel buffer

    :param size_t \*size:
        size of the kernel buffer

    :param unsigned long \*val:
        this is where the number will be stored

    :param bool \*neg:
        set to \ ``TRUE``\  if number is negative

    :param const char \*perm_tr:
        a vector which contains the allowed trailers

    :param unsigned perm_tr_len:
        size of the perm_tr vector

    :param char \*tr:
        pointer to store the trailer character

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

    :param void __user \*\*buf:
        the user buffer

    :param size_t \*size:
        the size of the user buffer

    :param unsigned long val:
        the integer to be converted

    :param bool neg:
        sign of the number, \ ``TRUE``\  for negative

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

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

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

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

.. _`proc_douintvec.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) unsigned integer
values from/to the user buffer, treated as an ASCII string.

Returns 0 on success.

.. _`proc_dointvec_minmax`:

proc_dointvec_minmax
====================

.. c:function:: int proc_dointvec_minmax(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of integers with min/max values

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

.. _`proc_dointvec_minmax.description`:

Description
-----------

Reads/writes up to table->maxlen/sizeof(unsigned int) integer
values from/to the user buffer, treated as an ASCII string.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success.

.. _`proc_doulongvec_minmax`:

proc_doulongvec_minmax
======================

.. c:function:: int proc_doulongvec_minmax(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos)

    read a vector of long integers with min/max values

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

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

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

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

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

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

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        pointer to the file position

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

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        the current position in the file

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

    :param struct ctl_table \*table:
        the sysctl table

    :param int write:
        %TRUE if this is a write to the sysctl file

    :param void __user \*buffer:
        the user buffer

    :param size_t \*lenp:
        the size of the user buffer

    :param loff_t \*ppos:
        file position

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

