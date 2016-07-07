.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/dm-ioctl.c

.. _`dm_copy_name_and_uuid`:

dm_copy_name_and_uuid
=====================

.. c:function:: int dm_copy_name_and_uuid(struct mapped_device *md, char *name, char *uuid)

    Copy mapped device name & uuid into supplied buffers

    :param struct mapped_device \*md:
        Pointer to mapped_device

    :param char \*name:
        Buffer (size DM_NAME_LEN) for name

    :param char \*uuid:
        Buffer (size DM_UUID_LEN) for uuid or empty string if uuid not defined

.. This file was automatic generated / don't edit.

