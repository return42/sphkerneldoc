.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/oid_registry.c

.. _`look_up_oid`:

look_up_OID
===========

.. c:function:: enum OID look_up_OID(const void *data, size_t datasize)

    Find an OID registration for the specified data

    :param data:
        Binary representation of the OID
    :type data: const void \*

    :param datasize:
        Size of the binary representation
    :type datasize: size_t

.. _`sprint_oid`:

sprint_OID
==========

.. c:function:: int sprint_OID(enum OID oid, char *buffer, size_t bufsize)

    Print an Object Identifier into a buffer

    :param oid:
        The OID to print
    :type oid: enum OID

    :param buffer:
        The buffer to render into
    :type buffer: char \*

    :param bufsize:
        The size of the buffer
    :type bufsize: size_t

.. _`sprint_oid.description`:

Description
-----------

The OID is rendered into the buffer in "a.b.c.d" format and the number of
bytes is returned.

.. This file was automatic generated / don't edit.

