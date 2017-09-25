.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/tee.h

.. _`tee_ioctl_version_data`:

struct tee_ioctl_version_data
=============================

.. c:type:: struct tee_ioctl_version_data

    TEE version

.. _`tee_ioctl_version_data.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_version_data {
        __u32 impl_id;
        __u32 impl_caps;
        __u32 gen_caps;
    }

.. _`tee_ioctl_version_data.members`:

Members
-------

impl_id
    [out] TEE implementation id

impl_caps
    [out] Implementation specific capabilities

gen_caps
    [out] Generic capabilities, defined by TEE_GEN_CAPS\_\* above

.. _`tee_ioctl_version_data.description`:

Description
-----------

Identifies the TEE implementation, \ ``impl_id``\  is one of TEE_IMPL_ID\_\* above.
\ ``impl_caps``\  is implementation specific, for example TEE_OPTEE_CAP\_\*
is valid when \ ``impl_id``\  == TEE_IMPL_ID_OPTEE.

.. _`tee_ioc_version`:

TEE_IOC_VERSION
===============

.. c:function::  TEE_IOC_VERSION()

    query version of TEE

.. _`tee_ioc_version.description`:

Description
-----------

Takes a tee_ioctl_version_data struct and returns with the TEE version
data filled in.

.. _`tee_ioctl_shm_alloc_data`:

struct tee_ioctl_shm_alloc_data
===============================

.. c:type:: struct tee_ioctl_shm_alloc_data

    Shared memory allocate argument

.. _`tee_ioctl_shm_alloc_data.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_shm_alloc_data {
        __u64 size;
        __u32 flags;
        __s32 id;
    }

.. _`tee_ioctl_shm_alloc_data.members`:

Members
-------

size
    [in/out] Size of shared memory to allocate

flags
    [in/out] Flags to/from allocation.

id
    [out] Identifier of the shared memory

.. _`tee_ioctl_shm_alloc_data.description`:

Description
-----------

The flags field should currently be zero as input. Updated by the call
with actual flags as defined by TEE_IOCTL_SHM\_\* above.
This structure is used as argument for TEE_IOC_SHM_ALLOC below.

.. _`tee_ioc_shm_alloc`:

TEE_IOC_SHM_ALLOC
=================

.. c:function::  TEE_IOC_SHM_ALLOC()

    allocate shared memory

.. _`tee_ioc_shm_alloc.description`:

Description
-----------

Allocates shared memory between the user space process and secure OS.

Returns a file descriptor on success or < 0 on failure

The returned file descriptor is used to map the shared memory into user
space. The shared memory is freed when the descriptor is closed and the
memory is unmapped.

.. _`tee_ioctl_buf_data`:

struct tee_ioctl_buf_data
=========================

.. c:type:: struct tee_ioctl_buf_data

    Variable sized buffer

.. _`tee_ioctl_buf_data.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_buf_data {
        __u64 buf_ptr;
        __u64 buf_len;
    }

.. _`tee_ioctl_buf_data.members`:

Members
-------

buf_ptr
    [in] A \__user pointer to a buffer

buf_len
    [in] Length of the buffer above

.. _`tee_ioctl_buf_data.description`:

Description
-----------

Used as argument for TEE_IOC_OPEN_SESSION, TEE_IOC_INVOKE,
TEE_IOC_SUPPL_RECV, and TEE_IOC_SUPPL_SEND below.

.. _`tee_ioctl_param`:

struct tee_ioctl_param
======================

.. c:type:: struct tee_ioctl_param

    parameter

.. _`tee_ioctl_param.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_param {
        __u64 attr;
        __u64 a;
        __u64 b;
        __u64 c;
    }

.. _`tee_ioctl_param.members`:

Members
-------

attr
    attributes

a
    if a memref, offset into the shared memory object, else a value parameter

b
    if a memref, size of the buffer, else a value parameter

c
    if a memref, shared memory identifier, else a value parameter

.. _`tee_ioctl_param.description`:

Description
-----------

@attr & TEE_PARAM_ATTR_TYPE_MASK indicates if memref or value is used in
the union. TEE_PARAM_ATTR_TYPE_VALUE\_\* indicates value and
TEE_PARAM_ATTR_TYPE_MEMREF\_\* indicates memref. TEE_PARAM_ATTR_TYPE_NONE
indicates that none of the members are used.

Shared memory is allocated with TEE_IOC_SHM_ALLOC which returns an
identifier representing the shared memory object. A memref can reference
a part of a shared memory by specifying an offset (@a) and size (@b) of
the object. To supply the entire shared memory object set the offset
(@a) to 0 and size (@b) to the previously returned size of the object.

.. _`tee_ioctl_open_session_arg`:

struct tee_ioctl_open_session_arg
=================================

.. c:type:: struct tee_ioctl_open_session_arg

    Open session argument

.. _`tee_ioctl_open_session_arg.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_open_session_arg {
        __u8 uuid[TEE_IOCTL_UUID_LEN];
        __u8 clnt_uuid[TEE_IOCTL_UUID_LEN];
        __u32 clnt_login;
        __u32 cancel_id;
        __u32 session;
        __u32 ret;
        __u32 ret_origin;
        __u32 num_params;
        struct tee_ioctl_param params[];
    }

.. _`tee_ioctl_open_session_arg.members`:

Members
-------

uuid
    [in] UUID of the Trusted Application

clnt_uuid
    [in] UUID of client

clnt_login
    [in] Login class of client, TEE_IOCTL_LOGIN\_\* above

cancel_id
    [in] Cancellation id, a unique value to identify this request

session
    [out] Session id

ret
    [out] return value
    \ ``ret_origin``\   [out] origin of the return value
    \ ``num_params``\   [in] number of parameters following this struct

ret_origin
    *undescribed*

num_params
    *undescribed*

params
    *undescribed*

.. _`tee_ioc_open_session`:

TEE_IOC_OPEN_SESSION
====================

.. c:function::  TEE_IOC_OPEN_SESSION()

    opens a session to a Trusted Application

.. _`tee_ioc_open_session.description`:

Description
-----------

Takes a struct tee_ioctl_buf_data which contains a struct
tee_ioctl_open_session_arg followed by any array of struct
tee_ioctl_param

.. _`tee_ioctl_invoke_arg`:

struct tee_ioctl_invoke_arg
===========================

.. c:type:: struct tee_ioctl_invoke_arg

    Invokes a function in a Trusted Application

.. _`tee_ioctl_invoke_arg.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_invoke_arg {
        __u32 func;
        __u32 session;
        __u32 cancel_id;
        __u32 ret;
        __u32 ret_origin;
        __u32 num_params;
        struct tee_ioctl_param params[];
    }

.. _`tee_ioctl_invoke_arg.members`:

Members
-------

func
    [in] Trusted Application function, specific to the TA

session
    [in] Session id

cancel_id
    [in] Cancellation id, a unique value to identify this request

ret
    [out] return value
    \ ``ret_origin``\   [out] origin of the return value
    \ ``num_params``\   [in] number of parameters following this struct

ret_origin
    *undescribed*

num_params
    *undescribed*

params
    *undescribed*

.. _`tee_ioc_invoke`:

TEE_IOC_INVOKE
==============

.. c:function::  TEE_IOC_INVOKE()

    Invokes a function in a Trusted Application

.. _`tee_ioc_invoke.description`:

Description
-----------

Takes a struct tee_ioctl_buf_data which contains a struct
tee_invoke_func_arg followed by any array of struct tee_param

.. _`tee_ioctl_cancel_arg`:

struct tee_ioctl_cancel_arg
===========================

.. c:type:: struct tee_ioctl_cancel_arg

    Cancels an open session or invoke ioctl

.. _`tee_ioctl_cancel_arg.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_cancel_arg {
        __u32 cancel_id;
        __u32 session;
    }

.. _`tee_ioctl_cancel_arg.members`:

Members
-------

cancel_id
    [in] Cancellation id, a unique value to identify this request

session
    [in] Session id, if the session is opened, else set to 0

.. _`tee_ioc_cancel`:

TEE_IOC_CANCEL
==============

.. c:function::  TEE_IOC_CANCEL()

    Cancels an open session or invoke

.. _`tee_ioctl_close_session_arg`:

struct tee_ioctl_close_session_arg
==================================

.. c:type:: struct tee_ioctl_close_session_arg

    Closes an open session

.. _`tee_ioctl_close_session_arg.definition`:

Definition
----------

.. code-block:: c

    struct tee_ioctl_close_session_arg {
        __u32 session;
    }

.. _`tee_ioctl_close_session_arg.members`:

Members
-------

session
    [in] Session id

.. _`tee_ioc_close_session`:

TEE_IOC_CLOSE_SESSION
=====================

.. c:function::  TEE_IOC_CLOSE_SESSION()

    Closes a session

.. _`tee_iocl_supp_recv_arg`:

struct tee_iocl_supp_recv_arg
=============================

.. c:type:: struct tee_iocl_supp_recv_arg

    Receive a request for a supplicant function

.. _`tee_iocl_supp_recv_arg.definition`:

Definition
----------

.. code-block:: c

    struct tee_iocl_supp_recv_arg {
        __u32 func;
        __u32 num_params;
        struct tee_ioctl_param params[];
    }

.. _`tee_iocl_supp_recv_arg.members`:

Members
-------

func
    [in] supplicant function
    \ ``num_params``\   [in/out] number of parameters following this struct

num_params
    *undescribed*

params
    *undescribed*

.. _`tee_iocl_supp_recv_arg.description`:

Description
-----------

@num_params is the number of params that tee-supplicant has room to
receive when input, \ ``num_params``\  is the number of actual params
tee-supplicant receives when output.

.. _`tee_ioc_suppl_recv`:

TEE_IOC_SUPPL_RECV
==================

.. c:function::  TEE_IOC_SUPPL_RECV()

    Receive a request for a supplicant function

.. _`tee_ioc_suppl_recv.description`:

Description
-----------

Takes a struct tee_ioctl_buf_data which contains a struct
tee_iocl_supp_recv_arg followed by any array of struct tee_param

.. _`tee_iocl_supp_send_arg`:

struct tee_iocl_supp_send_arg
=============================

.. c:type:: struct tee_iocl_supp_send_arg

    Send a response to a received request

.. _`tee_iocl_supp_send_arg.definition`:

Definition
----------

.. code-block:: c

    struct tee_iocl_supp_send_arg {
        __u32 ret;
        __u32 num_params;
        struct tee_ioctl_param params[];
    }

.. _`tee_iocl_supp_send_arg.members`:

Members
-------

ret
    [out] return value
    \ ``num_params``\   [in] number of parameters following this struct

num_params
    *undescribed*

params
    *undescribed*

.. _`tee_ioc_suppl_send`:

TEE_IOC_SUPPL_SEND
==================

.. c:function::  TEE_IOC_SUPPL_SEND()

    Receive a request for a supplicant function

.. _`tee_ioc_suppl_send.description`:

Description
-----------

Takes a struct tee_ioctl_buf_data which contains a struct
tee_iocl_supp_send_arg followed by any array of struct tee_param

.. This file was automatic generated / don't edit.

