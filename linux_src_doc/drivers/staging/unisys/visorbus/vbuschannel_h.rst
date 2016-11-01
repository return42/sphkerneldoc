.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visorbus/vbuschannel.h

.. _`vbuschannel_sanitize_buffer`:

vbuschannel_sanitize_buffer
===========================

.. c:function:: int vbuschannel_sanitize_buffer(char *p, int remain, char *src, int srcmax)

    remove non-printable chars from buffer

    :param char \*p:
        destination buffer where chars are written to

    :param int remain:
        number of bytes that can be written starting at #p

    :param char \*src:
        pointer to source buffer

    :param int srcmax:
        number of valid characters at #src

.. _`vbuschannel_sanitize_buffer.description`:

Description
-----------

Reads chars from the buffer at \ ``src``\  for \ ``srcmax``\  bytes, and writes to
the buffer at \ ``p``\ , which is \ ``remain``\  bytes long, ensuring never to
overflow the buffer at \ ``p``\ , using the following rules:
- printable characters are simply copied from the buffer at \ ``src``\  to the
buffer at \ ``p``\ 
- intervening streaks of non-printable characters in the buffer at \ ``src``\ 
are replaced with a single space in the buffer at \ ``p``\ 
Note that we pay no attention to '\0'-termination.

Pass \ ``p``\  == NULL and \ ``remain``\  == 0 for this special behavior -- In this
case, we simply return the number of bytes that WOULD HAVE been written
to a buffer at \ ``p``\ , had it been infinitely big.

.. _`vbuschannel_sanitize_buffer.return`:

Return
------

the number of bytes written to \ ``p``\  (or WOULD HAVE been written to
\ ``p``\ , as described in the previous paragraph)

.. _`vbuschannel_itoa`:

vbuschannel_itoa
================

.. c:function:: int vbuschannel_itoa(char *p, int remain, int num)

    convert non-negative int to string

    :param char \*p:
        destination string

    :param int remain:
        max number of bytes that can be written to \ ``p``\ 

    :param int num:
        input int to convert

.. _`vbuschannel_itoa.description`:

Description
-----------

Converts the non-negative value at \ ``num``\  to an ascii decimal string
at \ ``p``\ , writing at most \ ``remain``\  bytes.  Note there is NO '\0' termination
written to \ ``p``\ .

.. _`vbuschannel_itoa.return`:

Return
------

number of bytes written to \ ``p``\ 

.. _`vbuschannel_devinfo_to_string`:

vbuschannel_devinfo_to_string
=============================

.. c:function:: int vbuschannel_devinfo_to_string(struct ultra_vbus_deviceinfo *devinfo, char *p, int remain, int devix)

    format a struct ultra_vbus_deviceinfo to a printable string

    :param struct ultra_vbus_deviceinfo \*devinfo:
        the struct ultra_vbus_deviceinfo to format

    :param char \*p:
        destination string area

    :param int remain:
        size of destination string area in bytes

    :param int devix:
        the device index to be included in the output data, or -1 if no
        device index is to be included

.. _`vbuschannel_devinfo_to_string.description`:

Description
-----------

Reads \ ``devInfo``\ , and converts its contents to a printable string at \ ``p``\ ,
writing at most \ ``remain``\  bytes. Note there is NO '\0' termination
written to \ ``p``\ .

.. _`vbuschannel_devinfo_to_string.return`:

Return
------

number of bytes written to \ ``p``\ 

.. This file was automatic generated / don't edit.

