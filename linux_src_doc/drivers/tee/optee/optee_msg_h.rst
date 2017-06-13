.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/optee_msg.h

.. _`optee_msg_param_tmem`:

struct optee_msg_param_tmem
===========================

.. c:type:: struct optee_msg_param_tmem

    temporary memory reference parameter

.. _`optee_msg_param_tmem.definition`:

Definition
----------

.. code-block:: c

    struct optee_msg_param_tmem {
        u64 buf_ptr;
        u64 size;
        u64 shm_ref;
    }

.. _`optee_msg_param_tmem.members`:

Members
-------

buf_ptr
    Address of the buffer

size
    Size of the buffer

shm_ref
    Temporary shared memory reference, pointer to a struct tee_shm

.. _`optee_msg_param_tmem.description`:

Description
-----------

Secure and normal world communicates pointers as physical address
instead of the virtual address. This is because secure and normal world
have completely independent memory mapping. Normal world can even have a
hypervisor which need to translate the guest physical address (AKA IPA
in ARM documentation) to a real physical address before passing the
structure to secure world.

.. _`optee_msg_param_rmem`:

struct optee_msg_param_rmem
===========================

.. c:type:: struct optee_msg_param_rmem

    registered memory reference parameter

.. _`optee_msg_param_rmem.definition`:

Definition
----------

.. code-block:: c

    struct optee_msg_param_rmem {
        u64 offs;
        u64 size;
        u64 shm_ref;
    }

.. _`optee_msg_param_rmem.members`:

Members
-------

offs
    Offset into shared memory reference

size
    Size of the buffer

shm_ref
    Shared memory reference, pointer to a struct tee_shm

.. _`optee_msg_param_value`:

struct optee_msg_param_value
============================

.. c:type:: struct optee_msg_param_value

    opaque value parameter

.. _`optee_msg_param_value.definition`:

Definition
----------

.. code-block:: c

    struct optee_msg_param_value {
        u64 a;
        u64 b;
        u64 c;
    }

.. _`optee_msg_param_value.members`:

Members
-------

a
    *undescribed*

b
    *undescribed*

c
    *undescribed*

.. _`optee_msg_param_value.description`:

Description
-----------

Value parameters are passed unchecked between normal and secure world.

.. _`optee_msg_param`:

struct optee_msg_param
======================

.. c:type:: struct optee_msg_param

    parameter used together with struct optee_msg_arg

.. _`optee_msg_param.definition`:

Definition
----------

.. code-block:: c

    struct optee_msg_param {
        u64 attr;
        union u;
    }

.. _`optee_msg_param.members`:

Members
-------

attr
    attributes

u
    *undescribed*

.. _`optee_msg_param.description`:

Description
-----------

@attr & OPTEE_MSG_ATTR_TYPE_MASK indicates if tmem, rmem or value is used in
the union. OPTEE_MSG_ATTR_TYPE_VALUE\_\* indicates value,
OPTEE_MSG_ATTR_TYPE_TMEM\_\* indicates tmem and
OPTEE_MSG_ATTR_TYPE_RMEM\_\* indicates rmem.
OPTEE_MSG_ATTR_TYPE_NONE indicates that none of the members are used.

.. _`optee_msg_arg`:

struct optee_msg_arg
====================

.. c:type:: struct optee_msg_arg

    call argument

.. _`optee_msg_arg.definition`:

Definition
----------

.. code-block:: c

    struct optee_msg_arg {
        u32 cmd;
        u32 func;
        u32 session;
        u32 cancel_id;
        u32 pad;
        u32 ret;
        u32 ret_origin;
        u32 num_params;
        struct optee_msg_param params;
    }

.. _`optee_msg_arg.members`:

Members
-------

cmd
    Command, one of OPTEE_MSG_CMD\_\* or OPTEE_MSG_RPC_CMD\_\*

func
    Trusted Application function, specific to the Trusted Application,
    used if cmd == OPTEE_MSG_CMD_INVOKE_COMMAND

session
    In parameter for all OPTEE_MSG_CMD\_\* except
    OPTEE_MSG_CMD_OPEN_SESSION where it's an output parameter instead

cancel_id
    Cancellation id, a unique value to identify this request

pad
    *undescribed*

ret
    return value

ret_origin
    origin of the return value

num_params
    number of parameters supplied to the OS Command

params
    the parameters supplied to the OS Command

.. _`optee_msg_arg.description`:

Description
-----------

All normal calls to Trusted OS uses this struct. If cmd requires further
information than what these field holds it can be passed as a parameter
tagged as meta (setting the OPTEE_MSG_ATTR_META bit in corresponding
attrs field). All parameters tagged as meta has to come first.

Temp memref parameters can be fragmented if supported by the Trusted OS
(when optee_smc.h is bearer of this protocol this is indicated with
OPTEE_SMC_SEC_CAP_UNREGISTERED_SHM). If a logical memref parameter is
fragmented then has all but the last fragment the
OPTEE_MSG_ATTR_FRAGMENT bit set in attrs. Even if a memref is fragmented
it will still be presented as a single logical memref to the Trusted
Application.

.. _`optee_msg_get_arg_size`:

OPTEE_MSG_GET_ARG_SIZE
======================

.. c:function::  OPTEE_MSG_GET_ARG_SIZE( num_params)

    return size of struct optee_msg_arg

    :param  num_params:
        Number of parameters embedded in the struct optee_msg_arg

.. _`optee_msg_get_arg_size.description`:

Description
-----------

Returns the size of the struct optee_msg_arg together with the number
of embedded parameters.

.. This file was automatic generated / don't edit.

