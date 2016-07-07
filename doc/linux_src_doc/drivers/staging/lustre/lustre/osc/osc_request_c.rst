.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/osc/osc_request.c

.. _`osc_build_rpc`:

osc_build_rpc
=============

.. c:function:: int osc_build_rpc(const struct lu_env *env, struct client_obd *cli, struct list_head *ext_list, int cmd)

    that the total pages in this list are NOT over max pages per RPC. Extents in the list must be in OES_RPC state.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct client_obd \*cli:
        *undescribed*

    :param struct list_head \*ext_list:
        *undescribed*

    :param int cmd:
        *undescribed*

.. _`osc_cancel_weight`:

osc_cancel_weight
=================

.. c:function:: int osc_cancel_weight(struct ldlm_lock *lock)

    during recovery, see bug16774 for detailed information.

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`osc_cancel_weight.description`:

Description
-----------

\retval zero the lock can't be canceled
\retval other ok to cancel

.. This file was automatic generated / don't edit.

