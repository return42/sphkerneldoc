.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/seq_file.c

.. _`seq_open`:

seq_open
========

.. c:function:: int seq_open(struct file *file, const struct seq_operations *op)

    initialize sequential file

    :param struct file \*file:
        file we initialize

    :param const struct seq_operations \*op:
        method table describing the sequence

.. _`seq_open.description`:

Description
-----------

\ :c:func:`seq_open`\  sets \ ``file``\ , associating it with a sequence described
by \ ``op``\ .  \ ``op``\ ->\ :c:func:`start`\  sets the iterator up and returns the first
element of sequence. \ ``op``\ ->\ :c:func:`stop`\  shuts it down.  \ ``op``\ ->\ :c:func:`next`\ 
returns the next element of sequence.  \ ``op``\ ->\ :c:func:`show`\  prints element
into the buffer.  In case of error ->\ :c:func:`start`\  and ->\ :c:func:`next`\  return
ERR_PTR(error).  In the end of sequence they return \ ``NULL``\ . ->\ :c:func:`show`\ 
returns 0 in case of success and negative number in case of error.
Returning SEQ_SKIP means "discard this element and move on".

.. _`seq_open.note`:

Note
----

\ :c:func:`seq_open`\  will allocate a struct seq_file and store its
pointer in \ ``file``\ ->private_data. This pointer should not be modified.

.. _`seq_read`:

seq_read
========

.. c:function:: ssize_t seq_read(struct file *file, char __user *buf, size_t size, loff_t *ppos)

    ->\ :c:func:`read`\  method for sequential files.

    :param struct file \*file:
        the file to read from

    :param char __user \*buf:
        the buffer to read to

    :param size_t size:
        the maximum number of bytes to read

    :param loff_t \*ppos:
        the current position in the file

.. _`seq_read.description`:

Description
-----------

Ready-made ->f_op->\ :c:func:`read`\ 

.. _`seq_lseek`:

seq_lseek
=========

.. c:function:: loff_t seq_lseek(struct file *file, loff_t offset, int whence)

    ->\ :c:func:`llseek`\  method for sequential files.

    :param struct file \*file:
        the file in question

    :param loff_t offset:
        new position

    :param int whence:
        0 for absolute, 1 for relative position

.. _`seq_lseek.description`:

Description
-----------

Ready-made ->f_op->\ :c:func:`llseek`\ 

.. _`seq_release`:

seq_release
===========

.. c:function:: int seq_release(struct inode *inode, struct file *file)

    free the structures associated with sequential file.

    :param struct inode \*inode:
        its inode

    :param struct file \*file:
        file in question

.. _`seq_release.description`:

Description
-----------

Frees the structures associated with sequential file; can be used
as ->f_op->\ :c:func:`release`\  if you don't have private data to destroy.

.. _`seq_escape`:

seq_escape
==========

.. c:function:: void seq_escape(struct seq_file *m, const char *s, const char *esc)

    print string into buffer, escaping some characters

    :param struct seq_file \*m:
        target buffer

    :param const char \*s:
        string

    :param const char \*esc:
        set of characters that need escaping

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

    :param char \*s:
        buffer start

    :param const char \*p:
        beginning of path in above buffer

    :param const char \*esc:
        set of characters that need escaping

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

    :param struct seq_file \*m:
        the seq_file handle

    :param const struct path \*path:
        the struct path to print

    :param const char \*esc:
        set of characters to escape in the output

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

    :param struct seq_file \*m:
        the seq_file handle

    :param struct file \*file:
        the struct file to print

    :param const char \*esc:
        set of characters to escape in the output

.. _`seq_file_path.description`:

Description
-----------

return the absolute path to the file.

.. _`seq_write`:

seq_write
=========

.. c:function:: int seq_write(struct seq_file *seq, const void *data, size_t len)

    write arbitrary data to buffer

    :param struct seq_file \*seq:
        seq_file identifying the buffer to which data should be written

    :param const void \*data:
        data address

    :param size_t len:
        number of bytes

.. _`seq_write.description`:

Description
-----------

Return 0 on success, non-zero otherwise.

.. _`seq_pad`:

seq_pad
=======

.. c:function:: void seq_pad(struct seq_file *m, char c)

    write padding spaces to buffer

    :param struct seq_file \*m:
        seq_file identifying the buffer to which data should be written

    :param char c:
        the byte to append after padding if non-zero

.. _`seq_hlist_start`:

seq_hlist_start
===============

.. c:function:: struct hlist_node *seq_hlist_start(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist

    :param struct hlist_head \*head:
        the head of the hlist

    :param loff_t pos:
        the start position of the sequence

.. _`seq_hlist_start.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`start`\ .

.. _`seq_hlist_start_head`:

seq_hlist_start_head
====================

.. c:function:: struct hlist_node *seq_hlist_start_head(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist

    :param struct hlist_head \*head:
        the head of the hlist

    :param loff_t pos:
        the start position of the sequence

.. _`seq_hlist_start_head.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`start`\ . Call this function if you want to
print a header at the top of the output.

.. _`seq_hlist_next`:

seq_hlist_next
==============

.. c:function:: struct hlist_node *seq_hlist_next(void *v, struct hlist_head *head, loff_t *ppos)

    move to the next position of the hlist

    :param void \*v:
        the current iterator

    :param struct hlist_head \*head:
        the head of the hlist

    :param loff_t \*ppos:
        the current position

.. _`seq_hlist_next.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`next`\ .

.. _`seq_hlist_start_rcu`:

seq_hlist_start_rcu
===================

.. c:function:: struct hlist_node *seq_hlist_start_rcu(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist protected by RCU

    :param struct hlist_head \*head:
        the head of the hlist

    :param loff_t pos:
        the start position of the sequence

.. _`seq_hlist_start_rcu.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`start`\ .

This list-traversal primitive may safely run concurrently with
the \_rcu list-mutation primitives such as \ :c:func:`hlist_add_head_rcu`\ 
as long as the traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`seq_hlist_start_head_rcu`:

seq_hlist_start_head_rcu
========================

.. c:function:: struct hlist_node *seq_hlist_start_head_rcu(struct hlist_head *head, loff_t pos)

    start an iteration of a hlist protected by RCU

    :param struct hlist_head \*head:
        the head of the hlist

    :param loff_t pos:
        the start position of the sequence

.. _`seq_hlist_start_head_rcu.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`start`\ . Call this function if you want to
print a header at the top of the output.

This list-traversal primitive may safely run concurrently with
the \_rcu list-mutation primitives such as \ :c:func:`hlist_add_head_rcu`\ 
as long as the traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`seq_hlist_next_rcu`:

seq_hlist_next_rcu
==================

.. c:function:: struct hlist_node *seq_hlist_next_rcu(void *v, struct hlist_head *head, loff_t *ppos)

    move to the next position of the hlist protected by RCU

    :param void \*v:
        the current iterator

    :param struct hlist_head \*head:
        the head of the hlist

    :param loff_t \*ppos:
        the current position

.. _`seq_hlist_next_rcu.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`next`\ .

This list-traversal primitive may safely run concurrently with
the \_rcu list-mutation primitives such as \ :c:func:`hlist_add_head_rcu`\ 
as long as the traversal is guarded by \ :c:func:`rcu_read_lock`\ .

.. _`seq_hlist_start_percpu`:

seq_hlist_start_percpu
======================

.. c:function:: struct hlist_node *seq_hlist_start_percpu(struct hlist_head __percpu *head, int *cpu, loff_t pos)

    start an iteration of a percpu hlist array

    :param struct hlist_head __percpu \*head:
        pointer to percpu array of struct hlist_heads

    :param int \*cpu:
        pointer to cpu "cursor"

    :param loff_t pos:
        start position of sequence

.. _`seq_hlist_start_percpu.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`start`\ .

.. _`seq_hlist_next_percpu`:

seq_hlist_next_percpu
=====================

.. c:function:: struct hlist_node *seq_hlist_next_percpu(void *v, struct hlist_head __percpu *head, int *cpu, loff_t *pos)

    move to the next position of the percpu hlist array

    :param void \*v:
        pointer to current hlist_node

    :param struct hlist_head __percpu \*head:
        pointer to percpu array of struct hlist_heads

    :param int \*cpu:
        pointer to cpu "cursor"

    :param loff_t \*pos:
        start position of sequence

.. _`seq_hlist_next_percpu.description`:

Description
-----------

Called at seq_file->op->\ :c:func:`next`\ .

.. This file was automatic generated / don't edit.

