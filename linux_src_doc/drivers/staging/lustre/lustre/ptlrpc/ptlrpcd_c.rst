.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/ptlrpcd.c

.. _`ptlrpcd_steal_rqset`:

ptlrpcd_steal_rqset
===================

.. c:function:: int ptlrpcd_steal_rqset(struct ptlrpc_request_set *des, struct ptlrpc_request_set *src)

    :param struct ptlrpc_request_set \*des:
        *undescribed*

    :param struct ptlrpc_request_set \*src:
        *undescribed*

.. _`ptlrpcd_add_req`:

ptlrpcd_add_req
===============

.. c:function:: void ptlrpcd_add_req(struct ptlrpc_request *req)

    ptlrpcd_check->\ :c:func:`ptlrpc_check_set`\ .

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpcd_check`:

ptlrpcd_check
=============

.. c:function:: int ptlrpcd_check(struct lu_env *env, struct ptlrpcd_ctl *pc)

    Returns 1 if yes.

    :param struct lu_env \*env:
        *undescribed*

    :param struct ptlrpcd_ctl \*pc:
        *undescribed*

.. _`ptlrpcd`:

ptlrpcd
=======

.. c:function:: int ptlrpcd(void *arg)

    ptlrpc's code paths like to execute in process context, so we have this thread which spins on a set which contains the rpcs and sends them.

    :param void \*arg:
        *undescribed*

.. This file was automatic generated / don't edit.

