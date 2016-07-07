.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/hvconsole.c

.. _`hvc_get_chars`:

hvc_get_chars
=============

.. c:function:: int hvc_get_chars(uint32_t vtermno, char *buf, int count)

    retrieve characters from firmware for denoted vterm adapter

    :param uint32_t vtermno:
        The vtermno or unit_address of the adapter from which to fetch the
        data.

    :param char \*buf:
        The character buffer into which to put the character data fetched from
        firmware.

    :param int count:
        not used?

.. _`hvc_put_chars`:

hvc_put_chars
=============

.. c:function:: int hvc_put_chars(uint32_t vtermno, const char *buf, int count)

    send characters to firmware for denoted vterm adapter

    :param uint32_t vtermno:
        The vtermno or unit_address of the adapter from which the data
        originated.

    :param const char \*buf:
        The character buffer that contains the character data to send to
        firmware.

    :param int count:
        Send this number of characters.

.. This file was automatic generated / don't edit.

