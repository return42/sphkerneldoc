.. -*- coding: utf-8; mode: rst -*-
.. src-file: ipc/util.h

.. _`ipc_get_maxidx`:

ipc_get_maxidx
==============

.. c:function:: int ipc_get_maxidx(struct ipc_ids *ids)

    get the highest assigned index

    :param ids:
        ipc identifier set
    :type ids: struct ipc_ids \*

.. _`ipc_get_maxidx.description`:

Description
-----------

Called with ipc_ids.rwsem held for reading.

.. This file was automatic generated / don't edit.

