.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/d_path.c

.. _`prepend_name`:

prepend_name
============

.. c:function:: int prepend_name(char **buffer, int *buflen, const struct qstr *name)

    prepend a pathname in front of current buffer pointer

    :param char \*\*buffer:
        buffer pointer

    :param int \*buflen:
        allocated length of the buffer

    :param const struct qstr \*name:
        name string and length qstr structure

.. _`prepend_name.description`:

Description
-----------

With RCU path tracing, it may race with \ :c:func:`d_move`\ . Use \ :c:func:`READ_ONCE`\  to
make sure that either the old or the new name pointer and length are
fetched. However, there may be mismatch between length and pointer.
The length cannot be trusted, we need to copy it byte-by-byte until
the length is reached or a null byte is found. It also prepends "/" at
the beginning of the name. The sequence number check at the caller will
retry it again when a \ :c:func:`d_move`\  does happen. So any garbage in the buffer
due to mismatched pointer and length will be discarded.

Load acquire is needed to make sure that we see that terminating NUL.

.. _`prepend_path`:

prepend_path
============

.. c:function:: int prepend_path(const struct path *path, const struct path *root, char **buffer, int *buflen)

    Prepend path string to a buffer

    :param const struct path \*path:
        the dentry/vfsmount to report

    :param const struct path \*root:
        root vfsmnt/dentry

    :param char \*\*buffer:
        pointer to the end of the buffer

    :param int \*buflen:
        pointer to buffer length

.. _`prepend_path.description`:

Description
-----------

The function will first try to write out the pathname without taking any
lock other than the RCU read lock to make sure that dentries won't go away.
It only checks the sequence number of the global rename_lock as any change
in the dentry's d_seq will be preceded by changes in the rename_lock
sequence number. If the sequence number had been changed, it will restart
the whole pathname back-tracing sequence again by taking the rename_lock.
In this case, there is no need to take the RCU read lock as the recursive
parent pointer references will keep the dentry chain alive as long as no
rename operation is performed.

.. _`__d_path`:

\__d_path
=========

.. c:function:: char *__d_path(const struct path *path, const struct path *root, char *buf, int buflen)

    return the path of a dentry

    :param const struct path \*path:
        the dentry/vfsmount to report

    :param const struct path \*root:
        root vfsmnt/dentry

    :param char \*buf:
        buffer to return value in

    :param int buflen:
        buffer length

.. _`__d_path.description`:

Description
-----------

Convert a dentry into an ASCII path name.

Returns a pointer into the buffer or an error code if the
path was too long.

"buflen" should be positive.

If the path is not reachable from the supplied root, return \ ``NULL``\ .

.. _`d_path`:

d_path
======

.. c:function:: char *d_path(const struct path *path, char *buf, int buflen)

    return the path of a dentry

    :param const struct path \*path:
        path to report

    :param char \*buf:
        buffer to return value in

    :param int buflen:
        buffer length

.. _`d_path.description`:

Description
-----------

Convert a dentry into an ASCII path name. If the entry has been deleted
the string " (deleted)" is appended. Note that this is ambiguous.

Returns a pointer into the buffer or an error code if the path was
too long. Note: Callers should use the returned pointer, not the passed
in buffer, to use the name! The implementation often starts at an offset
into the buffer, and may leave 0 bytes at the start.

"buflen" should be positive.

.. This file was automatic generated / don't edit.

