.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_ct.c

.. _`intel_guc_ct_init_early`:

intel_guc_ct_init_early
=======================

.. c:function:: void intel_guc_ct_init_early(struct intel_guc_ct *ct)

    Initialize CT state without requiring device access

    :param struct intel_guc_ct \*ct:
        pointer to CT struct

.. _`ctb-host-to-guc-request`:

CTB Host to GuC request
=======================

Format of the CTB Host to GuC request message is as follows::

+------------+---------+---------+---------+---------+
\|   msg[0]   \|   [1]   \|   [2]   \|   ...   \|  [n-1]  \|
+------------+---------+---------+---------+---------+
\|   MESSAGE  \|       MESSAGE PAYLOAD                 \|
+   HEADER   +---------+---------+---------+---------+
\|            \|    0    \|    1    \|   ...   \|    n    \|
+============+=========+=========+=========+=========+
\|  len >= 1  \|  FENCE  \|     request specific data   \|
+------+-----+---------+---------+---------+---------+

^-----------------len-------------------^

.. _`wait_for_ctb_desc_update`:

wait_for_ctb_desc_update
========================

.. c:function:: int wait_for_ctb_desc_update(struct guc_ct_buffer_desc *desc, u32 fence, u32 *status)

    Wait for the CT buffer descriptor update.

    :param struct guc_ct_buffer_desc \*desc:
        buffer descriptor

    :param u32 fence:
        response fence

    :param u32 \*status:
        placeholder for status

.. _`wait_for_ctb_desc_update.description`:

Description
-----------

Guc will update CT buffer descriptor with new fence and status
after processing the command identified by the fence. Wait for
specified fence and then read from the descriptor status of the
command.

.. _`wait_for_ctb_desc_update.return`:

Return
------

\*    0 response received (status is valid)
\*    -ETIMEDOUT no response within hardcoded timeout
\*    -EPROTO no response, CT buffer is in error

.. _`wait_for_ct_request_update`:

wait_for_ct_request_update
==========================

.. c:function:: int wait_for_ct_request_update(struct ct_request *req, u32 *status)

    Wait for CT request state update.

    :param struct ct_request \*req:
        pointer to pending request

    :param u32 \*status:
        placeholder for status

.. _`wait_for_ct_request_update.description`:

Description
-----------

For each sent request, Guc shall send bac CT response message.
Our message handler will update status of tracked request once
response message with given fence is received. Wait here and
check for valid response status value.

.. _`wait_for_ct_request_update.return`:

Return
------

\*    0 response received (status is valid)
\*    -ETIMEDOUT no response within hardcoded timeout

.. _`ctb-guc-to-host-response`:

CTB GuC to Host response
========================

Format of the CTB GuC to Host response message is as follows::

+------------+---------+---------+---------+---------+---------+
\|   msg[0]   \|   [1]   \|   [2]   \|   [3]   \|   ...   \|  [n-1]  \|
+------------+---------+---------+---------+---------+---------+
\|   MESSAGE  \|       MESSAGE PAYLOAD                           \|
+   HEADER   +---------+---------+---------+---------+---------+
\|            \|    0    \|    1    \|    2    \|   ...   \|    n    \|
+============+=========+=========+=========+=========+=========+
\|  len >= 2  \|  FENCE  \|  STATUS \|   response specific data    \|
+------+-----+---------+---------+---------+---------+---------+

^-----------------------len-----------------------^

.. _`ctb-guc-to-host-request`:

CTB GuC to Host request
=======================

Format of the CTB GuC to Host request message is as follows::

+------------+---------+---------+---------+---------+---------+
\|   msg[0]   \|   [1]   \|   [2]   \|   [3]   \|   ...   \|  [n-1]  \|
+------------+---------+---------+---------+---------+---------+
\|   MESSAGE  \|       MESSAGE PAYLOAD                           \|
+   HEADER   +---------+---------+---------+---------+---------+
\|            \|    0    \|    1    \|    2    \|   ...   \|    n    \|
+============+=========+=========+=========+=========+=========+
\|     len    \|            request specific data                \|
+------+-----+---------+---------+---------+---------+---------+

^-----------------------len-----------------------^

.. _`intel_guc_ct_enable`:

intel_guc_ct_enable
===================

.. c:function:: int intel_guc_ct_enable(struct intel_guc_ct *ct)

    Enable buffer based command transport.

    :param struct intel_guc_ct \*ct:
        pointer to CT struct

.. _`intel_guc_ct_enable.description`:

Description
-----------

Shall only be called for platforms with HAS_GUC_CT.

.. _`intel_guc_ct_enable.return`:

Return
------

0 on success, a negative errno code on failure.

.. _`intel_guc_ct_disable`:

intel_guc_ct_disable
====================

.. c:function:: void intel_guc_ct_disable(struct intel_guc_ct *ct)

    Disable buffer based command transport.

    :param struct intel_guc_ct \*ct:
        pointer to CT struct

.. _`intel_guc_ct_disable.description`:

Description
-----------

Shall only be called for platforms with HAS_GUC_CT.

.. This file was automatic generated / don't edit.

