.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/path.c

.. _`d_namespace_path`:

d_namespace_path
================

.. c:function:: int d_namespace_path(const struct path *path, char *buf, char **name, int flags, const char *disconnected)

    lookup a name associated with a given path

    :param path:
        path to lookup  (NOT NULL)
    :type path: const struct path \*

    :param buf:
        buffer to store path to  (NOT NULL)
    :type buf: char \*

    :param name:
        Returns - pointer for start of path name with in \ ``buf``\  (NOT NULL)
    :type name: char \*\*

    :param flags:
        flags controlling path lookup
    :type flags: int

    :param disconnected:
        string to prefix to disconnected paths
    :type disconnected: const char \*

.. _`d_namespace_path.description`:

Description
-----------

Handle path name lookup.

.. _`d_namespace_path.return`:

Return
------

\ ``0``\  else error code if path lookup fails
When no error the path name is returned in \ ``name``\  which points to
to a position in \ ``buf``\ 

.. _`aa_path_name`:

aa_path_name
============

.. c:function:: int aa_path_name(const struct path *path, int flags, char *buffer, const char **name, const char **info, const char *disconnected)

    get the pathname to a buffer ensure dir / is appended

    :param path:
        path the file  (NOT NULL)
    :type path: const struct path \*

    :param flags:
        flags controlling path name generation
    :type flags: int

    :param buffer:
        buffer to put name in (NOT NULL)
    :type buffer: char \*

    :param name:
        Returns - the generated path name if !error (NOT NULL)
    :type name: const char \*\*

    :param info:
        Returns - information on why the path lookup failed (MAYBE NULL)
    :type info: const char \*\*

    :param disconnected:
        string to prepend to disconnected paths
    :type disconnected: const char \*

.. _`aa_path_name.description`:

Description
-----------

\ ``name``\  is a pointer to the beginning of the pathname (which usually differs
from the beginning of the buffer), or NULL.  If there is an error \ ``name``\ 
may contain a partial or invalid name that can be used for audit purposes,
but it can not be used for mediation.

We need PATH_IS_DIR to indicate whether the file is a directory or not
because the file may not yet exist, and so we cannot check the inode's
file type.

.. _`aa_path_name.return`:

Return
------

\ ``0``\  else error code if could retrieve name

.. This file was automatic generated / don't edit.

