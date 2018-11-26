.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/hvconsole.c

.. _`hvc_get_chars`:

hvc_get_chars
=============

.. c:function:: int hvc_get_chars(uint32_t vtermno, char *buf, int count)

    retrieve characters from firmware for denoted vterm adapter

    :param vtermno:
        The vtermno or unit_address of the adapter from which to fetch the
        data.
    :type vtermno: uint32_t

    :param buf:
        The character buffer into which to put the character data fetched from
        firmware.
    :type buf: char \*

    :param count:
        not used?
    :type count: int

.. _`hvc_put_chars`:

hvc_put_chars
=============

.. c:function:: int hvc_put_chars(uint32_t vtermno, const char *buf, int count)

    send characters to firmware for denoted vterm adapter

    :param vtermno:
        The vtermno or unit_address of the adapter from which the data
        originated.
    :type vtermno: uint32_t

    :param buf:
        The character buffer that contains the character data to send to
        firmware.
    :type buf: const char \*

    :param count:
        Send this number of characters.
    :type count: int

.. This file was automatic generated / don't edit.

