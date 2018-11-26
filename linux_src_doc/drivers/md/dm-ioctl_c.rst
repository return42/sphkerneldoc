.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/dm-ioctl.c

.. _`dm_copy_name_and_uuid`:

dm_copy_name_and_uuid
=====================

.. c:function:: int dm_copy_name_and_uuid(struct mapped_device *md, char *name, char *uuid)

    Copy mapped device name & uuid into supplied buffers

    :param md:
        Pointer to mapped_device
    :type md: struct mapped_device \*

    :param name:
        Buffer (size DM_NAME_LEN) for name
    :type name: char \*

    :param uuid:
        Buffer (size DM_UUID_LEN) for uuid or empty string if uuid not defined
    :type uuid: char \*

.. This file was automatic generated / don't edit.

