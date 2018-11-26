.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/seq_file.c

.. _`seq_open`:

seq_open
========

.. c:function:: int seq_open(struct file *file, const struct seq_operations *op)

    initialize sequential file

    :param file:
        file we initialize
    :type file: struct file \*

    :param op:
        method table describing the sequence
    :type op: const struct seq_operations \*

.. _`seq_open.description`:

Description
-----------

     \ :c:func:`seq_open`\  sets \ ``file``\ , associating it with a sequence described
     by \ ``op``\ .  \ ``op->start``\ () sets the iterator up and returns the first
     element of sequence. \ ``op->stop``\ () shuts it down.  \ ``op->next``\ ()
     returns the next element of sequence.  \ ``op->show``\ () prints element
     into the buffer.  In case of error ->start() and ->next() return
     ERR_PTR(error).  In the end of sequence they return \ ``NULL``\ . ->show()
     returns 0 in case of success and negative number in case of error.
     Returning SEQ_SKIP means "discard this element and move on".

.. _`seq_open.note`:

Note
----

\ :c:func:`seq_open`\  will allocate a struct seq_file and store its
     pointer in \ ``file->private_data``\ . This pointer should not be modified.

.. _`seq_read`:

seq_read
========

.. c:function:: ssize_t seq_read(struct file *file, char __user *buf, size_t size, loff_t *ppos)

    ->read() method for sequential files.

    :param file:
        the file to read from
    :type file: struct file \*

    :param buf:
        the buffer to read to
    :type buf: char __user \*

    :param size:
        the maximum number of bytes to read
    :type size: size_t

    :param ppos:
        the current position in the file
    :type ppos: loff_t \*

.. _`seq_read.description`:

Description
-----------

     Ready-made ->f_op->read()

.. _`seq_lseek`:

seq_lseek
=========

.. c:function:: loff_t seq_lseek(struct file *file, loff_t offset, int whence)

    ->llseek() method for sequential files.

    :param file:
        the file in question
    :type file: struct file \*

    :param offset:
        new position
    :type offset: loff_t

    :param whence:
        0 for absolute, 1 for relative position
    :type whence: int

.. _`seq_lseek.description`:

Description
-----------

     Ready-made ->f_op->llseek()

.. _`seq_release`:

seq_release
===========

.. c:function:: int seq_release(struct inode *inode, struct file *file)

    free the structures associated with sequential file.

    :param inode:
        its inode
    :type inode: struct inode \*

    :param file:
        file in question
    :type file: struct file \*

.. _`seq_release.description`:

Description
-----------

     Frees the structures associated with sequential file; can be used
     as ->f_op->release() if you don't have private data to destroy.

.. _`seq_escape`:

seq_escape
==========

.. c:function:: void seq_escape(struct seq_file *m, const char *s, const char *esc)

    print string into buffer, escaping some characters

    :param m:
        target buffer
    :type m: struct seq_file \*

    :param s:
        string
    :type s: const char \*

    :param esc:
        set of characters that need escaping
    :type esc: const char \*

.. _`seq_escape.description`:

Description
-----------

     Puts string into buffer, replacing each occurrence of character from
     \ ``esc``\  with usual octal escape.
     Use \ :c:func:`seq_has_overflowed`\  to check for errors.

.. _`mangle_path`:

mangle_path
===========

.. c:function:: char *mangle_path(char *s, const char *p, const char *esc)

    mangle and copy path to buffer beginning

    :param s:
        buffer start
    :type s: char \*

    :param p:
        beginning of path in above buffer
    :type p: const char \*

    :param esc:
        set of characters that need escaping
    :type esc: const char \*

.. _`mangle_path.description`:

Description
-----------

     Copy the path from \ ``p``\  to \ ``s``\ , replacing each occurrence of character from
     \ ``esc``\  with usual octal escape.
     Returns pointer past last written character in \ ``s``\ , or NULL in case of
     failure.

.. _`seq_path`:

seq_path
========

.. c:function:: int seq_path(struct seq_file *m, const struct path *path, const char *esc)

    seq_file interface to print a pathname

    :param m:
        the seq_file handle
    :type m: struct seq_file \*

    :param path:
        the struct path to print
    :type path: const struct path \*

    :param esc:
        set of characters to escape in the output
    :type esc: const char \*

.. _`seq_path.description`:

Description
-----------

return the absolute path of 'path', as represented by the
dentry / mnt pair in the path parameter.

.. _`seq_file_path`:

seq_file_path
=============

.. c:function:: int seq_file_path(struct seq_file *m, struct file *file, const char *esc)

    seq_file interface to print a pathname of a file

    :param m:
        the seq_file handle
    :type m: struct seq_file \*

    :param file:
        the struct file to print
    :type file: struct file \*

    :param esc:
        set of characters to escape in the output
    :type esc: const char \*

.. _`seq_file_path.description`:

Description
-----------

return the absolute path to the file.

.. _`seq_put_decimal_ull_width`:

seq_put_decimal_ull_width
=========================

.. c:function:: void seq_put_decimal_ull_width(struct seq_file *m, const char *delimiter, unsigned long long num, unsigned int width)

    only 'unsigned long long' is supported.

    :param m:
        seq_file identifying the buffer to which data should be written
    :type m: struct seq_file \*

    :param delimiter:
        a string which is printed before the number
    :type delimiter: const char \*

    :param num:
        the number
    :type num: unsigned long long

    :param width:
        a minimum field width
    :type width: unsigned int

.. _`seq_put_decimal_ull_width.description`:

Description
-----------

This routine will put strlen(delimiter) + number into seq_filed.
This routine is very quick when you show lots of numbers.
In usual cases, it will be better to use \ :c:func:`seq_printf`\ . It's easier to read.

.. _`seq_put_hex_ll`:

seq_put_hex_ll
==============

.. c:function:: void seq_put_hex_ll(struct seq_file *m, const char *delimiter, unsigned long long v, unsigned int width)

    put a number in hexadecimal notation

    :param m:
        seq_file identifying the buffer to which data should be written
    :type m: struct seq_file \*

    :param delimiter:
        a string which is printed before the number
    :type delimiter: const char \*

    :param v:
        the number
    :type v: unsigned long long

    :param width:
        a minimum field width
    :type width: unsigned int

.. _`seq_put_hex_ll.description`:

Description
-----------

seq_put_hex_ll(m, "", v, 8) is equal to seq_printf(m, "%08llx", v)

This routine is very quick when you show lots of numbers.
In usual cases, it will be better to use \ :c:func:`seq_printf`\ . It's easier to read.

.. _`seq_write`:

seq_write
=========

.. c:function:: int seq_write(struct seq_file *seq, const void *data, size_t len)

    write arbitrary data to buffer

    :param seq:
        seq_file identifying the buffer to which data should be written
    :type seq: struct seq_file \*

    :param data:
        data address
    :type data: const void \*

    :param len:
        number of bytes
    :type len: size_t

.. _`seq_write.description`:

Description
-----------

Return 0 on success, non-zero otherwise.

.. _`seq_pad`:

seq_pad
=======

.. c:function:: void seq_pad(struct seq_file *m, char c)

    write padding spaces to buffer

    :param m:
        seq_file identifying the buffer to which data should be written
    :type m: struct seq_file \*

    :param c:
        the byte to append after padding if non-zero
    :type c: char

.. _`seq_hlist_start`:

seq_hlist_start
===============

.. c:function:: struct hlist_node *seq_hlist_start(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist

    :param head:
        the head of the hlist
    :type head: struct hlist_head \*

    :param pos:
        the start position of the sequence
    :type pos: loff_t

.. _`seq_hlist_start.description`:

Description
-----------

Called at seq_file->op->start().

.. _`seq_hlist_start_head`:

seq_hlist_start_head
====================

.. c:function:: struct hlist_node *seq_hlist_start_head(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist

    :param head:
        the head of the hlist
    :type head: struct hlist_head \*

    :param pos:
        the start position of the sequence
    :type pos: loff_t

.. _`seq_hlist_start_head.description`:

Description
-----------

Called at seq_file->op->start(). Call this function if you want to
print a header at the top of the output.

.. _`seq_hlist_next`:

seq_hlist_next
==============

.. c:function:: struct hlist_node *seq_hlist_next(void *v, struct hlist_head *head, loff_t *ppos)

    move to the next position of the hlist

    :param v:
        the current iterator
    :type v: void \*

    :param head:
        the head of the hlist
    :type head: struct hlist_head \*

    :param ppos:
        the current position
    :type ppos: loff_t \*

.. _`seq_hlist_next.description`:

Description
-----------

Called at seq_file->op->next().

.. _`seq_hlist_start_rcu`:

seq_hlist_start_rcu
===================

.. c:function:: struct hlist_node *seq_hlist_start_rcu(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist protected by RCU

    :param head:
        the head of the hlist
    :type head: struct hlist_head \*

    :param pos:
        the start position of the sequence
    :type pos: loff_t

.. _`seq_hlist_start_rcu.description`:

Description
-----------

Called at seq_file->op->start().

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as \ :c:func:`hlist_add_head_rcu`\ 
as long as the traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`seq_hlist_start_head_rcu`:

seq_hlist_start_head_rcu
========================

.. c:function:: struct hlist_node *seq_hlist_start_head_rcu(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist protected by RCU

    :param head:
        the head of the hlist
    :type head: struct hlist_head \*

    :param pos:
        the start position of the sequence
    :type pos: loff_t

.. _`seq_hlist_start_head_rcu.description`:

Description
-----------

Called at seq_file->op->start(). Call this function if you want to
print a header at the top of the output.

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as \ :c:func:`hlist_add_head_rcu`\ 
as long as the traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`seq_hlist_next_rcu`:

seq_hlist_next_rcu
==================

.. c:function:: struct hlist_node *seq_hlist_next_rcu(void *v, struct hlist_head *head, loff_t *ppos)

    move to the next position of the hlist protected by RCU

    :param v:
        the current iterator
    :type v: void \*

    :param head:
        the head of the hlist
    :type head: struct hlist_head \*

    :param ppos:
        the current position
    :type ppos: loff_t \*

.. _`seq_hlist_next_rcu.description`:

Description
-----------

Called at seq_file->op->next().

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as \ :c:func:`hlist_add_head_rcu`\ 
as long as the traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`seq_hlist_start_percpu`:

seq_hlist_start_percpu
======================

.. c:function:: struct hlist_node *seq_hlist_start_percpu(struct hlist_head __percpu *head, int *cpu, loff_t pos)

    start an iteration of a percpu hlist array

    :param head:
        pointer to percpu array of struct hlist_heads
    :type head: struct hlist_head __percpu \*

    :param cpu:
        pointer to cpu "cursor"
    :type cpu: int \*

    :param pos:
        start position of sequence
    :type pos: loff_t

.. _`seq_hlist_start_percpu.description`:

Description
-----------

Called at seq_file->op->start().

.. _`seq_hlist_next_percpu`:

seq_hlist_next_percpu
=====================

.. c:function:: struct hlist_node *seq_hlist_next_percpu(void *v, struct hlist_head __percpu *head, int *cpu, loff_t *pos)

    move to the next position of the percpu hlist array

    :param v:
        pointer to current hlist_node
    :type v: void \*

    :param head:
        pointer to percpu array of struct hlist_heads
    :type head: struct hlist_head __percpu \*

    :param cpu:
        pointer to cpu "cursor"
    :type cpu: int \*

    :param pos:
        start position of sequence
    :type pos: loff_t \*

.. _`seq_hlist_next_percpu.description`:

Description
-----------

Called at seq_file->op->next().

.. This file was automatic generated / don't edit.

