.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/srcpos.h

.. _`srcfile_relative_open`:

srcfile_relative_open
=====================

.. c:function:: FILE *srcfile_relative_open(const char *fname, char **fullnamep)

    :param fname:
        *undescribed*
    :type fname: const char \*

    :param fullnamep:
        *undescribed*
    :type fullnamep: char \*\*

.. _`srcfile_relative_open.description`:

Description
-----------

If the source file is a relative pathname, then it is searched for in the
current directory (the directory of the last source file read) and after
that in the search path.

We work through the search path in order from the first path specified to
the last.

If the file is not found, then this function does not return, but calls
\ :c:func:`die`\ .

\ ``param``\  fname         Filename to search
\ ``param``\  fullnamep     If non-NULL, it is set to the allocated filename of the
file that was opened. The caller is then responsible
for freeing the pointer.
\ ``return``\  pointer to opened FILE

.. _`srcfile_add_search_path`:

srcfile_add_search_path
=======================

.. c:function:: void srcfile_add_search_path(const char *dirname)

    :param dirname:
        *undescribed*
    :type dirname: const char \*

.. _`srcfile_add_search_path.description`:

Description
-----------

The new path is added at the end of the list.

\ ``param``\  dirname       Directory to add

.. This file was automatic generated / don't edit.

