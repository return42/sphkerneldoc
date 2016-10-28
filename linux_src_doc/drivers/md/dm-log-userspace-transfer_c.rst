.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/dm-log-userspace-transfer.c

.. _`dm_consult_userspace`:

dm_consult_userspace
====================

.. c:function:: int dm_consult_userspace(const char *uuid, uint64_t luid, int request_type, char *data, size_t data_size, char *rdata, size_t *rdata_size)

    :param const char \*uuid:
        log's universal unique identifier (must be DM_UUID_LEN in size)

    :param uint64_t luid:
        log's local unique identifier

    :param int request_type:
        found in include/linux/dm-log-userspace.h

    :param char \*data:
        data to tx to the server

    :param size_t data_size:
        size of data in bytes

    :param char \*rdata:
        place to put return data from server

    :param size_t \*rdata_size:
        value-result (amount of space given/amount of space used)

.. _`dm_consult_userspace.description`:

Description
-----------

rdata_size is undefined on failure.

Memory used to communicate with userspace is zero'ed
before populating to ensure that no unwanted bits leak
from kernel space to user-space.  All userspace log communications
between kernel and user space go through this function.

.. _`dm_consult_userspace.return`:

Return
------

0 on success, -EXXX on failure

.. This file was automatic generated / don't edit.

