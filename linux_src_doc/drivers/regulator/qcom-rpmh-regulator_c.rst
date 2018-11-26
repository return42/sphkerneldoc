.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/qcom-rpmh-regulator.c

.. _`rpmh_regulator_type`:

enum rpmh_regulator_type
========================

.. c:type:: enum rpmh_regulator_type

    supported RPMh accelerator types \ ``VRM``\ :        RPMh VRM accelerator which supports voting on enable, voltage, and mode of LDO, SMPS, and BOB type PMIC regulators. \ ``XOB``\ :        RPMh XOB accelerator which supports voting on the enable state of PMIC regulators.

.. _`rpmh_regulator_type.definition`:

Definition
----------

.. code-block:: c

    enum rpmh_regulator_type {
        VRM,
        XOB
    };

.. _`rpmh_regulator_type.constants`:

Constants
---------

VRM
    *undescribed*

XOB
    *undescribed*

.. _`rpmh_vreg_hw_data`:

struct rpmh_vreg_hw_data
========================

.. c:type:: struct rpmh_vreg_hw_data

    RPMh regulator hardware configurations

.. _`rpmh_vreg_hw_data.definition`:

Definition
----------

.. code-block:: c

    struct rpmh_vreg_hw_data {
        enum rpmh_regulator_type regulator_type;
        const struct regulator_ops *ops;
        const struct regulator_linear_range voltage_range;
        int n_voltages;
        int hpm_min_load_uA;
        const int *pmic_mode_map;
        unsigned int (*of_map_mode)(unsigned int mode);
    }

.. _`rpmh_vreg_hw_data.members`:

Members
-------

regulator_type
    RPMh accelerator type used to manage this
    regulator

ops
    Pointer to regulator ops callback structure

voltage_range
    The single range of voltages supported by this
    PMIC regulator type

n_voltages
    The number of unique voltage set points defined
    by voltage_range

hpm_min_load_uA
    Minimum load current in microamps that requires
    high power mode (HPM) operation.  This is used
    for LDO hardware type regulators only.

pmic_mode_map
    Array indexed by regulator framework mode
    containing PMIC hardware modes.  Must be large
    enough to index all framework modes supported
    by this regulator hardware type.

of_map_mode
    Maps an RPMH_REGULATOR_MODE\_\* mode value defined
    in device tree to a regulator framework mode

.. _`rpmh_vreg`:

struct rpmh_vreg
================

.. c:type:: struct rpmh_vreg

    individual RPMh regulator data structure encapsulating a single regulator device

.. _`rpmh_vreg.definition`:

Definition
----------

.. code-block:: c

    struct rpmh_vreg {
        struct device *dev;
        u32 addr;
        struct regulator_desc rdesc;
        const struct rpmh_vreg_hw_data *hw_data;
        bool always_wait_for_ack;
        int enabled;
        bool bypassed;
        int voltage_selector;
        unsigned int mode;
    }

.. _`rpmh_vreg.members`:

Members
-------

dev
    Device pointer for the top-level PMIC RPMh
    regulator parent device.  This is used as a
    handle in RPMh write requests.

addr
    Base address of the regulator resource within
    an RPMh accelerator

rdesc
    Regulator descriptor

hw_data
    PMIC regulator configuration data for this RPMh
    regulator

always_wait_for_ack
    Boolean flag indicating if a request must always
    wait for an ACK from RPMh before continuing even
    if it corresponds to a strictly lower power
    state (e.g. enabled --> disabled).

enabled
    Flag indicating if the regulator is enabled or
    not

bypassed
    Boolean indicating if the regulator is in
    bypass (pass-through) mode or not.  This is
    only used by BOB rpmh-regulator resources.

voltage_selector
    Selector used for \ :c:func:`get_voltage_sel`\  and
    \ :c:func:`set_voltage_sel`\  callbacks

mode
    RPMh VRM regulator current framework mode

.. _`rpmh_vreg_init_data`:

struct rpmh_vreg_init_data
==========================

.. c:type:: struct rpmh_vreg_init_data

    initialization data for an RPMh regulator

.. _`rpmh_vreg_init_data.definition`:

Definition
----------

.. code-block:: c

    struct rpmh_vreg_init_data {
        const char *name;
        const char *resource_name;
        const char *supply_name;
        const struct rpmh_vreg_hw_data *hw_data;
    }

.. _`rpmh_vreg_init_data.members`:

Members
-------

name
    Name for the regulator which also corresponds
    to the device tree subnode name of the regulator

resource_name
    RPMh regulator resource name format string.
    This must include exactly one field: '%s' which
    is filled at run-time with the PMIC ID provided
    by device tree property qcom,pmic-id.  Example:
    "ldo%s1" for RPMh resource "ldoa1".

supply_name
    Parent supply regulator name

hw_data
    Configuration data for this PMIC regulator type

.. _`rpmh_regulator_send_request`:

rpmh_regulator_send_request
===========================

.. c:function:: int rpmh_regulator_send_request(struct rpmh_vreg *vreg, struct tcs_cmd *cmd, bool wait_for_ack)

    send the request to RPMh

    :param vreg:
        Pointer to the RPMh regulator
    :type vreg: struct rpmh_vreg \*

    :param cmd:
        Pointer to the RPMh command to send
    :type cmd: struct tcs_cmd \*

    :param wait_for_ack:
        Boolean indicating if execution must wait until the
        request has been acknowledged as complete
    :type wait_for_ack: bool

.. _`rpmh_regulator_send_request.return`:

Return
------

0 on success, errno on failure

.. _`rpmh_regulator_vrm_set_load`:

rpmh_regulator_vrm_set_load
===========================

.. c:function:: int rpmh_regulator_vrm_set_load(struct regulator_dev *rdev, int load_uA)

    set the regulator mode based upon the load current requested

    :param rdev:
        Regulator device pointer for the rpmh-regulator
    :type rdev: struct regulator_dev \*

    :param load_uA:
        Aggregated load current in microamps
    :type load_uA: int

.. _`rpmh_regulator_vrm_set_load.description`:

Description
-----------

This function is used in the regulator_ops for VRM type RPMh regulator
devices.

.. _`rpmh_regulator_vrm_set_load.return`:

Return
------

0 on success, errno on failure

.. _`rpmh_regulator_init_vreg`:

rpmh_regulator_init_vreg
========================

.. c:function:: int rpmh_regulator_init_vreg(struct rpmh_vreg *vreg, struct device *dev, struct device_node *node, const char *pmic_id, const struct rpmh_vreg_init_data *pmic_rpmh_data)

    initialize all attributes of an rpmh-regulator

    :param vreg:
        *undescribed*
    :type vreg: struct rpmh_vreg \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param node:
        *undescribed*
    :type node: struct device_node \*

    :param pmic_id:
        *undescribed*
    :type pmic_id: const char \*

    :param pmic_rpmh_data:
        *undescribed*
    :type pmic_rpmh_data: const struct rpmh_vreg_init_data \*

.. _`rpmh_regulator_init_vreg.vreg`:

vreg
----

Pointer to the individual rpmh-regulator resource

.. _`rpmh_regulator_init_vreg.dev`:

dev
---

Pointer to the top level rpmh-regulator PMIC device

.. _`rpmh_regulator_init_vreg.node`:

node
----

Pointer to the individual rpmh-regulator resource
device node

.. _`rpmh_regulator_init_vreg.pmic_id`:

pmic_id
-------

String used to identify the top level rpmh-regulator
PMIC device on the board

.. _`rpmh_regulator_init_vreg.pmic_rpmh_data`:

pmic_rpmh_data
--------------

Pointer to a null-terminated array of rpmh-regulator
resources defined for the top level PMIC device

.. _`rpmh_regulator_init_vreg.return`:

Return
------

0 on success, errno on failure

.. This file was automatic generated / don't edit.

