.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/winucase.c

.. _`cifs_toupper`:

cifs_toupper
============

.. c:function:: wchar_t cifs_toupper(wchar_t in)

    convert a wchar_t from lower to uppercase

    :param in:
        character to convert from lower to uppercase
    :type in: wchar_t

.. _`cifs_toupper.description`:

Description
-----------

This function consults the static tables above to convert a wchar_t from
lower to uppercase. In the event that there is no mapping, the original
"in" character is returned.

.. This file was automatic generated / don't edit.

