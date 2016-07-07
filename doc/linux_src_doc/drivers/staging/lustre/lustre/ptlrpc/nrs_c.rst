.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/nrs.c

.. _`nrs_policy_stop_primary`:

nrs_policy_stop_primary
=======================

.. c:function:: void nrs_policy_stop_primary(struct ptlrpc_nrs *nrs)

    ptlrpc_nrs_pol_state::NRS_POL_STATE_STOPPING and if the policy has no pending usage references, to ptlrpc_nrs_pol_state::NRS_POL_STATE_STOPPED.

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

.. _`nrs_policy_stop_primary.description`:

Description
-----------

\param[in] nrs the NRS head to carry out this operation on

.. _`nrs_policy_start_locked`:

nrs_policy_start_locked
=======================

.. c:function:: int nrs_policy_start_locked(struct ptlrpc_nrs_policy *policy)

    response to an lprocfs command to start a policy.

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

.. _`nrs_policy_start_locked.description`:

Description
-----------

If a primary policy different to the current one is specified, this function
will transition the new policy to the
ptlrpc_nrs_pol_state::NRS_POL_STATE_STARTING and then to
ptlrpc_nrs_pol_state::NRS_POL_STATE_STARTED, and will then transition
the old primary policy (if there is one) to
ptlrpc_nrs_pol_state::NRS_POL_STATE_STOPPING, and if there are no outstanding
references on the policy to ptlrpc_nrs_pol_stae::NRS_POL_STATE_STOPPED.

If the fallback policy is specified, this is taken to indicate an instruction
to stop the current primary policy, without substituting it with another
primary policy, so the primary policy (if any) is transitioned to
ptlrpc_nrs_pol_state::NRS_POL_STATE_STOPPING, and if there are no outstanding
references on the policy to ptlrpc_nrs_pol_stae::NRS_POL_STATE_STOPPED. In
this case, the fallback policy is only left active in the NRS head.

.. _`nrs_policy_get_locked`:

nrs_policy_get_locked
=====================

.. c:function:: void nrs_policy_get_locked(struct ptlrpc_nrs_policy *policy)

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

.. _`nrs_policy_put_locked`:

nrs_policy_put_locked
=====================

.. c:function:: void nrs_policy_put_locked(struct ptlrpc_nrs_policy *policy)

    was already stopping and have no more outstanding usage references (which indicates it has no more queued or started requests, and can be safely stopped).

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

.. _`nrs_policy_find_locked`:

nrs_policy_find_locked
======================

.. c:function:: struct ptlrpc_nrs_policy *nrs_policy_find_locked(struct ptlrpc_nrs *nrs, char *name)

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

    :param char \*name:
        *undescribed*

.. _`nrs_resource_put`:

nrs_resource_put
================

.. c:function:: void nrs_resource_put(struct ptlrpc_nrs_resource *res)

    policy instance resource.

    :param struct ptlrpc_nrs_resource \*res:
        *undescribed*

.. _`nrs_resource_get`:

nrs_resource_get
================

.. c:function:: struct ptlrpc_nrs_resource *nrs_resource_get(struct ptlrpc_nrs_policy *policy, struct ptlrpc_nrs_request *nrq, bool moving_req)

    \a nrq if it is to be handled by \a policy.

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

    :param bool moving_req:
        *undescribed*

.. _`nrs_resource_get.description`:

Description
-----------

\param[in] policy      the policy
\param[in] nrq         the request
\param[in] moving_req  denotes whether this is a call to the function by
\ :c:func:`ldlm_lock_reorder_req`\ , in order to move \a nrq to
the high-priority NRS head; we should not sleep when
set.

\retval NULL           resource hierarchy references not obtained
\retval valid-pointer  the bottom level of the resource hierarchy

\see ptlrpc_nrs_pol_ops::\ :c:func:`op_res_get`\ 

.. _`nrs_resource_get_safe`:

nrs_resource_get_safe
=====================

.. c:function:: void nrs_resource_get_safe(struct ptlrpc_nrs *nrs, struct ptlrpc_nrs_request *nrq, struct ptlrpc_nrs_resource **resp, bool moving_req)

    the fallback and current primary policy (if any), that will later be used to handle request \a nrq.

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

    :param struct ptlrpc_nrs_resource \*\*resp:
        *undescribed*

    :param bool moving_req:
        *undescribed*

.. _`nrs_resource_get_safe.description`:

Description
-----------

\param[in]  nrs  the NRS head instance that will be handling request \a nrq.
\param[in]  nrq  the request that is being handled.
\param[out] resp the array where references to the resource hierarchy are
stored.
\param[in]  moving_req  is set when obtaining resources while moving a
request from a policy on the regular NRS head to a
policy on the HP NRS head (via
\ :c:func:`ldlm_lock_reorder_req`\ ). It signifies that
allocations to get resources should be atomic; for
a full explanation, see comment in
ptlrpc_nrs_pol_ops::\ :c:func:`op_res_get`\ .

.. _`nrs_resource_put_safe`:

nrs_resource_put_safe
=====================

.. c:function:: void nrs_resource_put_safe(struct ptlrpc_nrs_resource **resp)

    longer required; used when request handling has been completed, or the request is moving to the high priority NRS head.

    :param struct ptlrpc_nrs_resource \*\*resp:
        *undescribed*

.. _`nrs_resource_put_safe.description`:

Description
-----------

\param resp  the resource hierarchy that is being released

\see \ :c:func:`ptlrpc_nrs_req_finalize`\ 

.. _`nrs_request_get`:

nrs_request_get
===============

.. c:function:: struct ptlrpc_nrs_request *nrs_request_get(struct ptlrpc_nrs_policy *policy, bool peek, bool force)

    request should be removed in the 'handling' case.

    :param struct ptlrpc_nrs_policy \*policy:
        *undescribed*

    :param bool peek:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`nrs_request_get.description`:

Description
-----------

Calling into this function implies we already know the policy has a request
waiting to be handled.

\param[in] policy the policy from which a request
\param[in] peek   when set, signifies that we just want to examine the
request, and not handle it, so the request is not removed
from the policy.
\param[in] force  when set, it will force a policy to return a request if it
has one pending

\retval the NRS request to be handled

.. _`nrs_request_enqueue`:

nrs_request_enqueue
===================

.. c:function:: void nrs_request_enqueue(struct ptlrpc_nrs_request *nrq)

    which resources where earlier obtained via \ :c:func:`nrs_resource_get_safe`\ . The function attempts to enqueue the request first on the primary policy (if any), since this is the preferred choice.

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

.. _`nrs_request_enqueue.description`:

Description
-----------

\param nrq the request being enqueued

\see \ :c:func:`nrs_resource_get_safe`\ 

.. _`nrs_request_stop`:

nrs_request_stop
================

.. c:function:: void nrs_request_stop(struct ptlrpc_nrs_request *nrq)

    :param struct ptlrpc_nrs_request \*nrq:
        *undescribed*

.. _`nrs_request_stop.description`:

Description
-----------

\param[in] nrs the request that has been handled; can be used for
job/resource control.

\see \ :c:func:`ptlrpc_nrs_req_stop_nolock`\ 

.. _`nrs_policy_ctl`:

nrs_policy_ctl
==============

.. c:function:: int nrs_policy_ctl(struct ptlrpc_nrs *nrs, char *name, enum ptlrpc_nrs_ctl opc, void *arg)

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

    :param char \*name:
        *undescribed*

    :param enum ptlrpc_nrs_ctl opc:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`nrs_policy_ctl.description`:

Description
-----------

Handles opcodes that are common to all policy types within NRS core, and
passes any unknown opcodes to the policy-specific control function.

\param[in]     nrs  the NRS head this policy belongs to.
\param[in]     name the human-readable policy name; should be the same as
ptlrpc_nrs_pol_desc::pd_name.
\param[in]     opc  the opcode of the operation being carried out.
\param[in,out] arg  can be used to pass information in and out between when
carrying an operation; usually data that is private to
the policy at some level, or generic policy status
information.

\retval -ve error condition
\retval   0 operation was carried out successfully

.. _`nrs_policy_unregister`:

nrs_policy_unregister
=====================

.. c:function:: int nrs_policy_unregister(struct ptlrpc_nrs *nrs, char *name)

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

    :param char \*name:
        *undescribed*

.. _`nrs_policy_unregister.description`:

Description
-----------

\param[in] nrs  the NRS head this policy belongs to.
\param[in] name the human-readable policy name; should be the same as
ptlrpc_nrs_pol_desc::pd_name

\retval -ve error
\retval   0 success

.. _`nrs_policy_register`:

nrs_policy_register
===================

.. c:function:: int nrs_policy_register(struct ptlrpc_nrs *nrs, struct ptlrpc_nrs_pol_desc *desc)

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

    :param struct ptlrpc_nrs_pol_desc \*desc:
        *undescribed*

.. _`nrs_policy_register.description`:

Description
-----------

\param[in] nrs   the NRS head on which the policy will be registered.
\param[in] desc  the policy descriptor from which the information will be
obtained to register the policy.

\retval -ve error
\retval   0 success

.. _`ptlrpc_nrs_req_add_nolock`:

ptlrpc_nrs_req_add_nolock
=========================

.. c:function:: void ptlrpc_nrs_req_add_nolock(struct ptlrpc_request *req)

    to.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_nrs_req_add_nolock.description`:

Description
-----------

\param[in] req the request to enqueue.

.. _`ptlrpc_nrs_hpreq_add_nolock`:

ptlrpc_nrs_hpreq_add_nolock
===========================

.. c:function:: void ptlrpc_nrs_hpreq_add_nolock(struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_nrs_hpreq_add_nolock.description`:

Description
-----------

\param req the request to enqueue.

.. _`nrs_policy_compatible`:

nrs_policy_compatible
=====================

.. c:function:: bool nrs_policy_compatible(const struct ptlrpc_service *svc, const struct ptlrpc_nrs_pol_desc *desc)

    \a desc is adequate for use with service \a svc.

    :param const struct ptlrpc_service \*svc:
        *undescribed*

    :param const struct ptlrpc_nrs_pol_desc \*desc:
        *undescribed*

.. _`nrs_policy_compatible.description`:

Description
-----------

\param[in] svc  the service
\param[in] desc the policy descriptor

\retval false the policy is not compatible with the service
\retval true  the policy is compatible with the service

.. _`nrs_register_policies_locked`:

nrs_register_policies_locked
============================

.. c:function:: int nrs_register_policies_locked(struct ptlrpc_nrs *nrs)

    \a nrs.

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

.. _`nrs_register_policies_locked.description`:

Description
-----------

\param[in] nrs the NRS head

\retval -ve error
\retval   0 success

\pre mutex_is_locked(\ :c:type:`nrs_core.nrs_mutex <nrs_core>`\ )

\see \ :c:func:`ptlrpc_service_nrs_setup`\ 

.. _`nrs_svcpt_setup_locked0`:

nrs_svcpt_setup_locked0
=======================

.. c:function:: int nrs_svcpt_setup_locked0(struct ptlrpc_nrs *nrs, struct ptlrpc_service_part *svcpt)

    compatible policies in NRS core, with the NRS head.

    :param struct ptlrpc_nrs \*nrs:
        *undescribed*

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. _`nrs_svcpt_setup_locked0.description`:

Description
-----------

\param[in] nrs   the NRS head
\param[in] svcpt the PTLRPC service partition to setup

\retval -ve error
\retval   0 success

\pre mutex_is_locked(\ :c:type:`nrs_core.nrs_mutex <nrs_core>`\ )

.. _`nrs_svcpt_setup_locked`:

nrs_svcpt_setup_locked
======================

.. c:function:: int nrs_svcpt_setup_locked(struct ptlrpc_service_part *svcpt)

    priority NRS head (if the service handles high-priority RPCs), and then registers all available compatible policies on those NRS heads.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. _`nrs_svcpt_setup_locked.description`:

Description
-----------

\param[in,out] svcpt the PTLRPC service partition to setup

\pre mutex_is_locked(\ :c:type:`nrs_core.nrs_mutex <nrs_core>`\ )

.. _`nrs_svcpt_cleanup_locked`:

nrs_svcpt_cleanup_locked
========================

.. c:function:: void nrs_svcpt_cleanup_locked(struct ptlrpc_service_part *svcpt)

    called at PTLRPC service unregistration time.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

.. _`nrs_svcpt_cleanup_locked.description`:

Description
-----------

\param[in] svcpt the PTLRPC service partition

\pre mutex_is_locked(\ :c:type:`nrs_core.nrs_mutex <nrs_core>`\ )

.. _`nrs_policy_find_desc_locked`:

nrs_policy_find_desc_locked
===========================

.. c:function:: struct ptlrpc_nrs_pol_desc *nrs_policy_find_desc_locked(const char *name)

    :param const char \*name:
        *undescribed*

.. _`nrs_policy_find_desc_locked.description`:

Description
-----------

\param[in] name the policy name

\retval the policy descriptor
\retval NULL

.. _`nrs_policy_unregister_locked`:

nrs_policy_unregister_locked
============================

.. c:function:: int nrs_policy_unregister_locked(struct ptlrpc_nrs_pol_desc *desc)

    PTLRPC services.

    :param struct ptlrpc_nrs_pol_desc \*desc:
        *undescribed*

.. _`nrs_policy_unregister_locked.description`:

Description
-----------

\param[in] desc the policy descriptor to unregister

\retval -ve error
\retval  0  successfully unregistered policy on all supported NRS heads

\pre mutex_is_locked(\ :c:type:`nrs_core.nrs_mutex <nrs_core>`\ )
\pre mutex_is_locked(\ :c:type:`struct ptlrpc_all_services_mutex <ptlrpc_all_services_mutex>`)

.. _`ptlrpc_nrs_policy_register`:

ptlrpc_nrs_policy_register
==========================

.. c:function:: int ptlrpc_nrs_policy_register(struct ptlrpc_nrs_pol_conf *conf)

    :param struct ptlrpc_nrs_pol_conf \*conf:
        *undescribed*

.. _`ptlrpc_nrs_policy_register.description`:

Description
-----------

The function will only succeed if policy registration with all compatible
service partitions (if any) is successful.

N.B. This function should be called either at ptlrpc module initialization
time when registering a policy that ships with NRS core, or in a
module's \ :c:func:`init`\  function for policies registering from other modules.

\param[in] conf configuration information for the new policy to register

\retval -ve error
\retval   0 success

.. _`ptlrpc_service_nrs_setup`:

ptlrpc_service_nrs_setup
========================

.. c:function:: int ptlrpc_service_nrs_setup(struct ptlrpc_service *svc)

    all compatible policies on those NRS heads.

    :param struct ptlrpc_service \*svc:
        *undescribed*

.. _`ptlrpc_service_nrs_setup.description`:

Description
-----------

To be called from within ptl
\param[in] svc the service to setup

\retval -ve error, the calling logic should eventually call
\ :c:func:`ptlrpc_service_nrs_cleanup`\  to undo any work performed
by this function.

\see \ :c:func:`ptlrpc_register_service`\ 
\see \ :c:func:`ptlrpc_service_nrs_cleanup`\ 

.. _`ptlrpc_service_nrs_cleanup`:

ptlrpc_service_nrs_cleanup
==========================

.. c:function:: void ptlrpc_service_nrs_cleanup(struct ptlrpc_service *svc)

    :param struct ptlrpc_service \*svc:
        *undescribed*

.. _`ptlrpc_service_nrs_cleanup.description`:

Description
-----------

\param[in] svc the PTLRPC service to unregister

.. _`ptlrpc_nrs_req_initialize`:

ptlrpc_nrs_req_initialize
=========================

.. c:function:: void ptlrpc_nrs_req_initialize(struct ptlrpc_service_part *svcpt, struct ptlrpc_request *req, bool hp)

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param bool hp:
        *undescribed*

.. _`ptlrpc_nrs_req_initialize.description`:

Description
-----------

These could be either on the regular or HP NRS head of \a svcpt; resources
taken on the regular head can later be swapped for HP head resources by
\ :c:func:`ldlm_lock_reorder_req`\ .

\param[in] svcpt the service partition
\param[in] req   the request
\param[in] hp    which NRS head of \a svcpt to use

.. _`ptlrpc_nrs_req_finalize`:

ptlrpc_nrs_req_finalize
=======================

.. c:function:: void ptlrpc_nrs_req_finalize(struct ptlrpc_request *req)

    handled.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_nrs_req_finalize.description`:

Description
-----------

\param[in] req the request

\see \ :c:func:`ptlrpc_server_finish_request`\ 

.. _`ptlrpc_nrs_req_add`:

ptlrpc_nrs_req_add
==================

.. c:function:: void ptlrpc_nrs_req_add(struct ptlrpc_service_part *svcpt, struct ptlrpc_request *req, bool hp)

    priority NRS head of service partition \a svcpt.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param bool hp:
        *undescribed*

.. _`ptlrpc_nrs_req_add.description`:

Description
-----------

\param[in] svcpt the service partition
\param[in] req   the request to be enqueued
\param[in] hp    whether to enqueue the request on the regular or
high-priority NRS head.

.. _`ptlrpc_nrs_req_get_nolock0`:

ptlrpc_nrs_req_get_nolock0
==========================

.. c:function:: struct ptlrpc_request *ptlrpc_nrs_req_get_nolock0(struct ptlrpc_service_part *svcpt, bool hp, bool peek, bool force)

    \a svcpt.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param bool hp:
        *undescribed*

    :param bool peek:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`ptlrpc_nrs_req_get_nolock0.description`:

Description
-----------

\param[in] svcpt the service partition
\param[in] hp    whether to obtain a request from the regular or
high-priority NRS head.
\param[in] peek  when set, signifies that we just want to examine the
request, and not handle it, so the request is not removed
from the policy.
\param[in] force when set, it will force a policy to return a request if it
has one pending

\retval the  request to be handled
\retval NULL the head has no requests to serve

.. _`ptlrpc_nrs_req_pending_nolock`:

ptlrpc_nrs_req_pending_nolock
=============================

.. c:function:: bool ptlrpc_nrs_req_pending_nolock(struct ptlrpc_service_part *svcpt, bool hp)

    policies of service partition's \a svcpt NRS head specified by \a hp. Should be called while holding ptlrpc_service_part::scp_req_lock to get a reliable result.

    :param struct ptlrpc_service_part \*svcpt:
        *undescribed*

    :param bool hp:
        *undescribed*

.. _`ptlrpc_nrs_req_pending_nolock.description`:

Description
-----------

\param[in] svcpt the service partition to enquire.
\param[in] hp    whether the regular or high-priority NRS head is to be
enquired.

\retval false the indicated NRS head has no enqueued requests.
\retval true  the indicated NRS head has some enqueued requests.

.. _`ptlrpc_nrs_policy_control`:

ptlrpc_nrs_policy_control
=========================

.. c:function:: int ptlrpc_nrs_policy_control(const struct ptlrpc_service *svc, enum ptlrpc_nrs_queue_type queue, char *name, enum ptlrpc_nrs_ctl opc, bool single, void *arg)

    human-readable \a name, on either all partitions, or only on the first partition of service \a svc.

    :param const struct ptlrpc_service \*svc:
        *undescribed*

    :param enum ptlrpc_nrs_queue_type queue:
        *undescribed*

    :param char \*name:
        *undescribed*

    :param enum ptlrpc_nrs_ctl opc:
        *undescribed*

    :param bool single:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`ptlrpc_nrs_policy_control.description`:

Description
-----------

\param[in]     svc    the service the policy belongs to.
\param[in]     queue  whether to carry out the command on the policy which
belongs to the regular, high-priority, or both NRS
heads of service partitions of \a svc.
\param[in]     name   the policy to act upon, by human-readable name
\param[in]     opc    the opcode of the operation to carry out
\param[in]     single when set, the operation will only be carried out on the
NRS heads of the first service partition of \a svc.
This is useful for some policies which e.g. share
identical values on the same parameters of different
service partitions; when reading these parameters via
lprocfs, these policies may just want to obtain and
print out the values from the first service partition.
Storing these values centrally elsewhere then could be
another solution for this.
\param[in,out] arg    can be used as a generic in/out buffer between control
operations and the user environment.

\retval -ve error condition
\retval   0 operation was carried out successfully

.. _`ptlrpc_nrs_init`:

ptlrpc_nrs_init
===============

.. c:function:: int ptlrpc_nrs_init( void)

    policies \e nrs_core.nrs_policies.

    :param  void:
        no arguments

.. _`ptlrpc_nrs_init.description`:

Description
-----------

\retval 0 all policies have been registered successfully
\retval -ve error

.. _`ptlrpc_nrs_fini`:

ptlrpc_nrs_fini
===============

.. c:function:: void ptlrpc_nrs_fini( void)

    :nrs_policies, and frees the policy descriptors.

    :param  void:
        no arguments

.. _`ptlrpc_nrs_fini.description`:

Description
-----------

Since all PTLRPC services are stopped at this point, there are no more
instances of any policies, because each service will have stopped its policy
instances in \ :c:func:`ptlrpc_service_nrs_cleanup`\ , so we just need to free the
descriptors here.

.. This file was automatic generated / don't edit.

