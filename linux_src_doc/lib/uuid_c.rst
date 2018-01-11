.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/uuid.c

.. _`generate_random_uuid`:

generate_random_uuid
====================

.. c:function:: void generate_random_uuid(unsigned char uuid)

    generate a random UUID

    :param unsigned char uuid:
        where to put the generated UUID

.. _`generate_random_uuid.description`:

Description
-----------

Random UUID interface

Used to create a Boot ID or a filesystem UUID/GUID, but can be
useful for other kernel drivers.

.. _`uuid_is_valid`:

uuid_is_valid
=============

.. c:function:: bool uuid_is_valid(const char *uuid)

    checks if a UUID string is valid

    :param const char \*uuid:
        UUID string to check

.. _`uuid_is_valid.it-checks-if-the-uuid-string-is-following-the-format`:

It checks if the UUID string is following the format
----------------------------------------------------

     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

where x is a hex digit.

.. _`uuid_is_valid.return`:

Return
------

true if input is valid UUID string.

.. This file was automatic generated / don't edit.

