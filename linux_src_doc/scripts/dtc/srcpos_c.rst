.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/srcpos.c

.. _`try_open`:

try_open
========

.. c:function:: char *try_open(const char *dirname, const char *fname, FILE **fp)

    :param dirname:
        *undescribed*
    :type dirname: const char \*

    :param fname:
        *undescribed*
    :type fname: const char \*

    :param fp:
        *undescribed*
    :type fp: FILE \*\*

.. _`try_open.description`:

Description
-----------

If the filename is an absolute path, then dirname is ignored. If it is a
relative path, then we look in that directory for the file.

\ ``param``\  dirname       Directory to look in, or NULL for none
\ ``param``\  fname         Filename to look for
\ ``param``\  fp            Set to NULL if file did not open
\ ``return``\  allocated filename on success (caller must free), NULL on failure

.. _`fopen_any_on_path`:

fopen_any_on_path
=================

.. c:function:: char *fopen_any_on_path(const char *fname, FILE **fp)

    :param fname:
        *undescribed*
    :type fname: const char \*

    :param fp:
        *undescribed*
    :type fp: FILE \*\*

.. _`fopen_any_on_path.description`:

Description
-----------

If it is a relative filename, we search the full search path for it.

\ ``param``\  fname Filename to open
\ ``param``\  fp    Returns pointer to opened FILE, or NULL on failure
\ ``return``\  pointer to allocated filename, which caller must free

.. This file was automatic generated / don't edit.

