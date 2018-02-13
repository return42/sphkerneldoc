.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/mdc/mdc_request.c

.. _`mdc_read_page_remote`:

mdc_read_page_remote
====================

.. c:function:: int mdc_read_page_remote(void *data, struct page *page0)

    :param void \*data:
        *undescribed*

    :param struct page \*page0:
        *undescribed*

.. _`mdc_read_page_remote.description`:

Description
-----------

Page in MDS_READPAGE RPC is packed in LU_PAGE_SIZE, and each page contains
a header lu_dirpage which describes the start/end hash, and whether this
page is empty (contains no dir entry) or hash collide with next page.
After client receives reply, several pages will be integrated into dir page
in PAGE_SIZE (if PAGE_SIZE greater than LU_PAGE_SIZE), and the
lu_dirpage for this integrated page will be adjusted.

.. _`mdc_read_page`:

mdc_read_page
=============

.. c:function:: int mdc_read_page(struct obd_export *exp, struct md_op_data *op_data, struct md_callback *cb_op, __u64 hash_offset, struct page **ppage)

    server and add into the cache.

    :param struct obd_export \*exp:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param struct md_callback \*cb_op:
        *undescribed*

    :param __u64 hash_offset:
        *undescribed*

    :param struct page \*\*ppage:
        *undescribed*

.. _`mdc_read_page.description`:

Description
-----------

\param[in] exp       MDC export
\param[in] op_data   client MD stack parameters, transferring parameters
between different layers on client MD stack.
\param[in] cb_op     callback required for ldlm lock enqueue during
read page
\param[in] hash_offset the hash offset of the page to be read
\param[in] ppage     the page to be read

retval               = 0 get the page successfully
errno(<0) get the page failed

.. _`mdc_hsm_copytool_send`:

mdc_hsm_copytool_send
=====================

.. c:function:: int mdc_hsm_copytool_send(size_t len, void *val)

    \ ``param``\  val KUC message (kuc_hdr + hsm_action_list) \ ``param``\  len total length of message

    :param size_t len:
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

