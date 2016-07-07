.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/smem_state.c

.. _`qcom_smem_state`:

struct qcom_smem_state
======================

.. c:type:: struct qcom_smem_state

    state context

.. _`qcom_smem_state.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smem_state {
        struct kref refcount;
        bool orphan;
        struct list_head list;
        struct device_node *of_node;
        void *priv;
        struct qcom_smem_state_ops ops;
    }

.. _`qcom_smem_state.members`:

Members
-------

refcount
    refcount for the state

orphan
    boolean indicator that this state has been unregistered

list
    entry in smem_states list

of_node
    of_node to use for matching the state in DT

priv
    implementation private data

ops
    ops for the state

.. _`qcom_smem_state_update_bits`:

qcom_smem_state_update_bits
===========================

.. c:function:: int qcom_smem_state_update_bits(struct qcom_smem_state *state, u32 mask, u32 value)

    update the masked bits in state with value

    :param struct qcom_smem_state \*state:
        state handle acquired by calling \ :c:func:`qcom_smem_state_get`\ 

    :param u32 mask:
        bit mask for the change

    :param u32 value:
        new value for the masked bits

.. _`qcom_smem_state_update_bits.description`:

Description
-----------

Returns 0 on success, otherwise negative errno.

.. _`qcom_smem_state_get`:

qcom_smem_state_get
===================

.. c:function:: struct qcom_smem_state *qcom_smem_state_get(struct device *dev, const char *con_id, unsigned *bit)

    acquire handle to a state

    :param struct device \*dev:
        client device pointer

    :param const char \*con_id:
        name of the state to lookup

    :param unsigned \*bit:
        flags from the state reference, indicating which bit's affected

.. _`qcom_smem_state_get.description`:

Description
-----------

Returns handle to the state, or \ :c:func:`ERR_PTR`\ . \ :c:func:`qcom_smem_state_put`\  must be
called to release the returned state handle.

.. _`qcom_smem_state_put`:

qcom_smem_state_put
===================

.. c:function:: void qcom_smem_state_put(struct qcom_smem_state *state)

    release state handle

    :param struct qcom_smem_state \*state:
        state handle to be released

.. _`qcom_smem_state_register`:

qcom_smem_state_register
========================

.. c:function:: struct qcom_smem_state *qcom_smem_state_register(struct device_node *of_node, const struct qcom_smem_state_ops *ops, void *priv)

    register a new state

    :param struct device_node \*of_node:
        of_node used for matching client lookups

    :param const struct qcom_smem_state_ops \*ops:
        implementation ops

    :param void \*priv:
        implementation specific private data

.. _`qcom_smem_state_unregister`:

qcom_smem_state_unregister
==========================

.. c:function:: void qcom_smem_state_unregister(struct qcom_smem_state *state)

    unregister a registered state

    :param struct qcom_smem_state \*state:
        state handle to be unregistered

.. This file was automatic generated / don't edit.

