.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlx4/fw_qos.h

.. _`mlx4_set_port_prio2tc`:

mlx4_SET_PORT_PRIO2TC
=====================

.. c:function:: int mlx4_SET_PORT_PRIO2TC(struct mlx4_dev *dev, u8 port, u8 *prio2tc)

    This routine maps user priorities to traffic classes of a given port and device.

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param port:
        Physical port number.
    :type port: u8

    :param prio2tc:
        Array of TC associated with each priorities.
    :type prio2tc: u8 \*

.. _`mlx4_set_port_prio2tc.description`:

Description
-----------

Returns 0 on success or a negative mlx4_core errno code.

.. _`mlx4_set_port_scheduler`:

mlx4_SET_PORT_SCHEDULER
=======================

.. c:function:: int mlx4_SET_PORT_SCHEDULER(struct mlx4_dev *dev, u8 port, u8 *tc_tx_bw, u8 *pg, u16 *ratelimit)

    This routine configures the arbitration between traffic classes (ETS) and configured rate limit for traffic classes. tc_tx_bw, pg and ratelimit are arrays where each index represents a TC. The description for those parameters below refers to a single TC.

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param port:
        Physical port number.
    :type port: u8

    :param tc_tx_bw:
        The percentage of the bandwidth allocated for traffic class
        within a TC group. The sum of the bw_percentage of all the traffic
        classes within a TC group must equal 100% for correct operation.
    :type tc_tx_bw: u8 \*

    :param pg:
        The TC group the traffic class is associated with.
    :type pg: u8 \*

    :param ratelimit:
        The maximal bandwidth allowed for the use by this traffic class.
    :type ratelimit: u16 \*

.. _`mlx4_set_port_scheduler.description`:

Description
-----------

Returns 0 on success or a negative mlx4_core errno code.

.. _`mlx4_allocate_vpp_get`:

mlx4_ALLOCATE_VPP_get
=====================

.. c:function:: int mlx4_ALLOCATE_VPP_get(struct mlx4_dev *dev, u8 port, u16 *available_vpp, u8 *vpp_p_up)

    Query port VPP available resources and allocation. Before distribution of VPPs to priorities, only available_vpp is returned. After initialization it returns the distribution of VPPs among priorities.

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param port:
        Physical port number.
    :type port: u8

    :param available_vpp:
        Pointer to variable where number of available VPPs is stored
    :type available_vpp: u16 \*

    :param vpp_p_up:
        Distribution of VPPs to priorities is stored in this array
    :type vpp_p_up: u8 \*

.. _`mlx4_allocate_vpp_get.description`:

Description
-----------

Returns 0 on success or a negative mlx4_core errno code.

.. _`mlx4_allocate_vpp_set`:

mlx4_ALLOCATE_VPP_set
=====================

.. c:function:: int mlx4_ALLOCATE_VPP_set(struct mlx4_dev *dev, u8 port, u8 *vpp_p_up)

    Distribution of VPPs among differnt priorities. The total number of VPPs assigned to all for a port must not exceed the value reported by available_vpp in mlx4_ALLOCATE_VPP_get. VPP allocation is allowed only after the port type has been set, and while no QPs are open for this port.

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param port:
        Physical port number.
    :type port: u8

    :param vpp_p_up:
        Allocation of VPPs to different priorities.
    :type vpp_p_up: u8 \*

.. _`mlx4_allocate_vpp_set.description`:

Description
-----------

Returns 0 on success or a negative mlx4_core errno code.

.. _`mlx4_set_vport_qos_get`:

mlx4_SET_VPORT_QOS_get
======================

.. c:function:: int mlx4_SET_VPORT_QOS_get(struct mlx4_dev *dev, u8 port, u8 vport, struct mlx4_vport_qos_param *out_param)

    Query QoS proporties of a Vport. Each priority allowed for the Vport is assigned with a share of the BW, and a BW limitation. This commands query the current QoS values.

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param port:
        Physical port number.
    :type port: u8

    :param vport:
        Vport id.
    :type vport: u8

    :param out_param:
        Array of mlx4_vport_qos_param that will contain the values.
    :type out_param: struct mlx4_vport_qos_param \*

.. _`mlx4_set_vport_qos_get.description`:

Description
-----------

Returns 0 on success or a negative mlx4_core errno code.

.. _`mlx4_set_vport_qos_set`:

mlx4_SET_VPORT_QOS_set
======================

.. c:function:: int mlx4_SET_VPORT_QOS_set(struct mlx4_dev *dev, u8 port, u8 vport, struct mlx4_vport_qos_param *in_param)

    Set QoS proporties of a Vport. QoS parameters can be modified at any time, but must be initialized before any QP is associated with the VPort.

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param port:
        Physical port number.
    :type port: u8

    :param vport:
        Vport id.
    :type vport: u8

    :param in_param:
        *undescribed*
    :type in_param: struct mlx4_vport_qos_param \*

.. _`mlx4_set_vport_qos_set.description`:

Description
-----------

Returns 0 on success or a negative mlx4_core errno code.

.. This file was automatic generated / don't edit.

