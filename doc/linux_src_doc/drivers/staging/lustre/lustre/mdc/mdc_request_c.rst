.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/mdc/mdc_request.c

.. _`mdc_replay_open`:

mdc_replay_open
===============

.. c:function:: void mdc_replay_open(struct ptlrpc_request *req)

    CLOSE and SETATTR-DONE_WRITING RPC chains.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`mdc_hsm_copytool_send`:

mdc_hsm_copytool_send
=====================

.. c:function:: int mdc_hsm_copytool_send(int len, void *val)

    \ ``param``\  val KUC message (kuc_hdr + hsm_action_list) \ ``param``\  len total length of message

    :param int len:
        *undescribed*

    :param void \*val:
        *undescribed*

.. _`mdc_hsm_ct_reregister`:

mdc_hsm_ct_reregister
=====================

.. c:function:: int mdc_hsm_ct_reregister(void *data, void *cb_arg)

    registering each HSM copytool running on MDC, after MDT shutdown/recovery. \ ``param``\  data copytool registration data \ ``param``\  cb_arg callback argument (obd_import)

    :param void \*data:
        *undescribed*

    :param void \*cb_arg:
        *undescribed*

.. _`mdc_cancel_weight`:

mdc_cancel_weight
=================

.. c:function:: int mdc_cancel_weight(struct ldlm_lock *lock)

    recovery, non zero value will be return if the lock can be canceled, or zero returned for not

    :param struct ldlm_lock \*lock:
        *undescribed*

.. This file was automatic generated / don't edit.

