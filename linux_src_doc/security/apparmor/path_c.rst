.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/path.c

.. _`d_namespace_path`:

d_namespace_path
================

.. c:function:: int d_namespace_path(const struct path *path, char *buf, char **name, int flags, const char *disconnected)

    lookup a name associated with a given path

    :param const struct path \*path:
        path to lookup  (NOT NULL)

    :param char \*buf:
        buffer to store path to  (NOT NULL)

    :param char \*\*name:
        Returns - pointer for start of path name with in \ ``buf``\  (NOT NULL)

    :param int flags:
        flags controlling path lookup

    :param const char \*disconnected:
        string to prefix to disconnected paths

.. _`d_namespace_path.description`:

Description
-----------

Handle path name lookup.

.. _`d_namespace_path.return`:

Return
------

%0 else error code if path lookup fails
When no error the path name is returned in \ ``name``\  which points to
to a position in \ ``buf``\ 

.. _`aa_path_name`:

aa_path_name
============

.. c:function:: int aa_path_name(const struct path *path, int flags, char *buffer, const char **name, const char **info, const char *disconnected)

    get the pathname to a buffer ensure dir / is appended

    :param const struct path \*path:
        path the file  (NOT NULL)

    :param int flags:
        flags controlling path name generation

    :param char \*buffer:
        buffer to put name in (NOT NULL)

    :param const char \*\*name:
        Returns - the generated path name if !error (NOT NULL)

    :param const char \*\*info:
        Returns - information on why the path lookup failed (MAYBE NULL)

    :param const char \*disconnected:
        string to prepend to disconnected paths

.. _`aa_path_name.description`:

Description
-----------

@name is a pointer to the beginning of the pathname (which usually differs
from the beginning of the buffer), or NULL.  If there is an error \ ``name``\ 
may contain a partial or invalid name that can be used for audit purposes,
but it can not be used for mediation.

We need PATH_IS_DIR to indicate whether the file is a directory or not
because the file may not yet exist, and so we cannot check the inode's
file type.

.. _`aa_path_name.return`:

Return
------

%0 else error code if could retrieve name

.. This file was automatic generated / don't edit.

