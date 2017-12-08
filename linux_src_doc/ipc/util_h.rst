.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/util.h

.. _`ipc_get_maxid`:

ipc_get_maxid
=============

.. c:function:: int ipc_get_maxid(struct ipc_ids *ids)

    get the last assigned id

    :param struct ipc_ids \*ids:
        ipc identifier set

.. _`ipc_get_maxid.description`:

Description
-----------

Called with ipc_ids.rwsem held for reading.

.. This file was automatic generated / don't edit.

