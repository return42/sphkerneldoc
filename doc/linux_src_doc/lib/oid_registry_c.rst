.. -*- coding: utf-8; mode: rst -*-

==============
oid_registry.c
==============


.. _`look_up_oid`:

look_up_OID
===========

.. c:function:: enum OID look_up_OID (const void *data, size_t datasize)

    Find an OID registration for the specified data

    :param const void \*data:
        Binary representation of the OID

    :param size_t datasize:
        Size of the binary representation



.. _`sprint_oid`:

sprint_OID
==========

.. c:function:: int sprint_OID (enum OID oid, char *buffer, size_t bufsize)

    Print an Object Identifier into a buffer

    :param enum OID oid:
        The OID to print

    :param char \*buffer:
        The buffer to render into

    :param size_t bufsize:
        The size of the buffer



.. _`sprint_oid.description`:

Description
-----------

The OID is rendered into the buffer in "a.b.c.d" format and the number of
bytes is returned.

