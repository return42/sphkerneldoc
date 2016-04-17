.. -*- coding: utf-8; mode: rst -*-

===========
do_mounts.c
===========


.. _`match_dev_by_uuid`:

match_dev_by_uuid
=================

.. c:function:: int match_dev_by_uuid (struct device *dev, const void *data)

    callback for finding a partition using its uuid

    :param struct device \*dev:
        device passed in by the caller

    :param const void \*data:
        opaque pointer to the desired struct uuidcmp to match



.. _`match_dev_by_uuid.description`:

Description
-----------

Returns 1 if the device matches, and 0 otherwise.



.. _`devt_from_partuuid`:

devt_from_partuuid
==================

.. c:function:: dev_t devt_from_partuuid (const char *uuid_str)

    looks up the dev_t of a partition by its UUID

    :param const char \*uuid_str:
        char array containing ascii UUID



.. _`devt_from_partuuid.description`:

Description
-----------

The function will return the first partition which contains a matching
UUID value in its partition_meta_info struct.  This does not search
by filesystem UUIDs.

If ``uuid_str`` is followed by a "/PARTNROFF=\ ``d``\ ", then the number will be
extracted and used as an offset from the partition identified by the UUID.

Returns the matching dev_t on success or 0 on failure.

