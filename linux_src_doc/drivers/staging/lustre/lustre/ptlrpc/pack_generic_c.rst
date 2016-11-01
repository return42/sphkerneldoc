.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/pack_generic.c

.. _`lustre_msg_buflen`:

lustre_msg_buflen
=================

.. c:function:: u32 lustre_msg_buflen(struct lustre_msg *m, u32 n)

    return the length of buffer \a n in message \a m \param m lustre_msg (request or reply) to look at \param n message index (base 0)

    :param struct lustre_msg \*m:
        *undescribed*

    :param u32 n:
        *undescribed*

.. _`lustre_msg_buflen.description`:

Description
-----------

returns zero for non-existent message indices

.. _`do_set_info_async`:

do_set_info_async
=================

.. c:function:: int do_set_info_async(struct obd_import *imp, int opcode, int version, u32 keylen, void *key, u32 vallen, void *val, struct ptlrpc_request_set *set)

    :param struct obd_import \*imp:
        *undescribed*

    :param int opcode:
        *undescribed*

    :param int version:
        *undescribed*

    :param u32 keylen:
        *undescribed*

    :param void \*key:
        *undescribed*

    :param u32 vallen:
        *undescribed*

    :param void \*val:
        *undescribed*

    :param struct ptlrpc_request_set \*set:
        *undescribed*

.. _`do_set_info_async.description`:

Description
-----------

This may go from client to server or server to client.

.. This file was automatic generated / don't edit.

