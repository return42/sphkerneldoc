.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/info.h

.. _`snd_iprintf`:

snd_iprintf
===========

.. c:function::  snd_iprintf( buf,  fmt,  args...)

    printf on the procfs buffer

    :param buf:
        the procfs buffer
    :type buf: 

    :param fmt:
        the printf format
    :type fmt: 

.. _`snd_iprintf.description`:

Description
-----------

Outputs the string on the procfs buffer just like \ :c:func:`printf`\ .

.. _`snd_iprintf.return`:

Return
------

zero for success, or a negative error code.

.. This file was automatic generated / don't edit.

