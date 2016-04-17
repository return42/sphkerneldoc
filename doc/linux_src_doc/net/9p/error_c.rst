.. -*- coding: utf-8; mode: rst -*-

=======
error.c
=======


.. _`errormap`:

struct errormap
===============

.. c:type:: errormap

    map string errors from Plan 9 to Linux numeric ids


.. _`errormap.definition`:

Definition
----------

.. code-block:: c

  struct errormap {
    char * name;
    int val;
    int namelen;
    struct hlist_node list;
  };


.. _`errormap.members`:

Members
-------

:``name``:
    string sent over 9P

:``val``:
    numeric id most closely representing ``name``

:``namelen``:
    length of string

:``list``:
    hash-table list for string lookup




.. _`p9_error_init`:

p9_error_init
=============

.. c:function:: int p9_error_init ( void)

    preload mappings into hash list

    :param void:
        no arguments



.. _`p9_errstr2errno`:

p9_errstr2errno
===============

.. c:function:: int p9_errstr2errno (char *errstr, int len)

    convert error string to error number

    :param char \*errstr:
        error string

    :param int len:
        length of error string

