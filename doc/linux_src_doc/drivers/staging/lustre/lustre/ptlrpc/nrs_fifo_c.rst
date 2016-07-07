.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/nrs_fifo.c

.. _`nrs_fifo_start`:

nrs_fifo_start
==============

.. c:function:: int nrs_fifo_start(struct ptlrpc_nrs_policy *policy)

    ptlrpc_nrs_pol_state::NRS_POL_STATE_STARTED; allocates and initializes a policy-specific private data structure.

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

.. _`nrs_fifo_start.description`:

Description
-----------

\param[in] policy The policy to start

\retval -ENOMEM OOM error
\retval  0      success

\see \ :c:func:`nrs_policy_register`\ 
\see \ :c:func:`nrs_policy_ctl`\ 

.. _`nrs_fifo_stop`:

nrs_fifo_stop
=============

.. c:function:: void nrs_fifo_stop(struct ptlrpc_nrs_policy *policy)

    ptlrpc_nrs_pol_state::NRS_POL_STATE_STOPPED; deallocates the policy-specific private data structure.

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

.. _`nrs_fifo_stop.description`:

Description
-----------

\param[in] policy The policy to stop

\see \ :c:func:`nrs_policy_stop0`\ 

.. _`nrs_fifo_res_get`:

nrs_fifo_res_get
================

.. c:function:: int nrs_fifo_res_get(struct ptlrpc_nrs_policy *policy, struct ptlrpc_nrs_request *nrq, const struct ptlrpc_nrs_resource *parent, struct ptlrpc_nrs_resource **resp, bool moving_req)

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

    :param const struct ptlrpc_nrs_resource \*parent:
        *undescribed*

    :param struct ptlrpc_nrs_resource \*\*resp:
        *undescribed*

    :param bool moving_req:
        *undescribed*

.. _`nrs_fifo_res_get.description`:

Description
-----------

\param[in]  policy     The policy on which the request is being asked for
\param[in]  nrq        The request for which resources are being taken
\param[in]  parent     Parent resource, unused in this policy
\param[out] resp       Resources references are placed in this array
\param[in]  moving_req Signifies limited caller context; unused in this
policy

\retval 1 The FIFO policy only has a one-level resource hierarchy, as since
it implements a simple scheduling algorithm in which request
priority is determined on the request arrival order, it does not
need to maintain a set of resources that would otherwise be used
to calculate a request's priority.

\see \ :c:func:`nrs_resource_get_safe`\ 

.. _`nrs_fifo_req_get`:

nrs_fifo_req_get
================

.. c:function:: struct ptlrpc_nrs_request *nrs_fifo_req_get(struct ptlrpc_nrs_policy *policy, bool peek, bool force)

    peeking; removes the request from the policy when it is to be handled.

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param bool peek:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`nrs_fifo_req_get.description`:

Description
-----------

\param[in] policy The policy
\param[in] peek   When set, signifies that we just want to examine the
request, and not handle it, so the request is not removed
from the policy.
\param[in] force  Force the policy to return a request; unused in this
policy

\retval The request to be handled; this is the next request in the FIFO
queue

\see \ :c:func:`ptlrpc_nrs_req_get_nolock`\ 
\see \ :c:func:`nrs_request_get`\ 

.. _`nrs_fifo_req_add`:

nrs_fifo_req_add
================

.. c:function:: int nrs_fifo_req_add(struct ptlrpc_nrs_policy *policy, struct ptlrpc_nrs_request *nrq)

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

.. _`nrs_fifo_req_add.description`:

Description
-----------

\param[in] policy The policy
\param[in] nrq    The request to add

\retval 0 success; \ :c:func:`nrs_request_enqueue`\  assumes this function will always
succeed

.. _`nrs_fifo_req_del`:

nrs_fifo_req_del
================

.. c:function:: void nrs_fifo_req_del(struct ptlrpc_nrs_policy *policy, struct ptlrpc_nrs_request *nrq)

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

.. _`nrs_fifo_req_del.description`:

Description
-----------

\param[in] policy The policy
\param[in] nrq    The request to remove

.. _`nrs_fifo_req_stop`:

nrs_fifo_req_stop
=================

.. c:function:: void nrs_fifo_req_stop(struct ptlrpc_nrs_policy *policy, struct ptlrpc_nrs_request *nrq)

    handled.

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

.. _`nrs_fifo_req_stop.description`:

Description
-----------

\param[in] policy The policy handling the request
\param[in] nrq    The request being handled

\see \ :c:func:`ptlrpc_server_finish_request`\ 
\see \ :c:func:`ptlrpc_nrs_req_stop_nolock`\ 

.. This file was automatic generated / don't edit.

