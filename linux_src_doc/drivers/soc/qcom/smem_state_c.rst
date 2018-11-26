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

    :param state:
        state handle acquired by calling \ :c:func:`qcom_smem_state_get`\ 
    :type state: struct qcom_smem_state \*

    :param mask:
        bit mask for the change
    :type mask: u32

    :param value:
        new value for the masked bits
    :type value: u32

.. _`qcom_smem_state_update_bits.description`:

Description
-----------

Returns 0 on success, otherwise negative errno.

.. _`qcom_smem_state_get`:

qcom_smem_state_get
===================

.. c:function:: struct qcom_smem_state *qcom_smem_state_get(struct device *dev, const char *con_id, unsigned *bit)

    acquire handle to a state

    :param dev:
        client device pointer
    :type dev: struct device \*

    :param con_id:
        name of the state to lookup
    :type con_id: const char \*

    :param bit:
        flags from the state reference, indicating which bit's affected
    :type bit: unsigned \*

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

    :param state:
        state handle to be released
    :type state: struct qcom_smem_state \*

.. _`qcom_smem_state_register`:

qcom_smem_state_register
========================

.. c:function:: struct qcom_smem_state *qcom_smem_state_register(struct device_node *of_node, const struct qcom_smem_state_ops *ops, void *priv)

    register a new state

    :param of_node:
        of_node used for matching client lookups
    :type of_node: struct device_node \*

    :param ops:
        implementation ops
    :type ops: const struct qcom_smem_state_ops \*

    :param priv:
        implementation specific private data
    :type priv: void \*

.. _`qcom_smem_state_unregister`:

qcom_smem_state_unregister
==========================

.. c:function:: void qcom_smem_state_unregister(struct qcom_smem_state *state)

    unregister a registered state

    :param state:
        state handle to be unregistered
    :type state: struct qcom_smem_state \*

.. This file was automatic generated / don't edit.

