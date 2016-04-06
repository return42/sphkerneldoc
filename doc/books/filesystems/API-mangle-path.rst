
.. _API-mangle-path:

===========
mangle_path
===========

*man mangle_path(9)*

*4.6.0-rc1*

mangle and copy path to buffer beginning


Synopsis
========

.. c:function:: char ⋆ mangle_path( char * s, const char * p, const char * esc )

Arguments
=========

``s``
    buffer start

``p``
    beginning of path in above buffer

``esc``
    set of characters that need escaping


Description
===========

Copy the path from ``p`` to ``s``, replacing each occurrence of character from ``esc`` with usual octal escape. Returns pointer past last written character in ``s``, or NULL in
case of failure.
