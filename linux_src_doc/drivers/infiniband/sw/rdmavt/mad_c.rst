.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/mad.c

.. _`rvt_process_mad`:

rvt_process_mad
===============

.. c:function:: int rvt_process_mad(struct ib_device *ibdev, int mad_flags, u8 port_num, const struct ib_wc *in_wc, const struct ib_grh *in_grh, const struct ib_mad_hdr *in, size_t in_mad_size, struct ib_mad_hdr *out, size_t *out_mad_size, u16 *out_mad_pkey_index)

    process an incoming MAD packet

    :param ibdev:
        the infiniband device this packet came in on
    :type ibdev: struct ib_device \*

    :param mad_flags:
        MAD flags
    :type mad_flags: int

    :param port_num:
        the port number this packet came in on, 1 based from ib core
    :type port_num: u8

    :param in_wc:
        the work completion entry for this packet
    :type in_wc: const struct ib_wc \*

    :param in_grh:
        the global route header for this packet
    :type in_grh: const struct ib_grh \*

    :param in:
        *undescribed*
    :type in: const struct ib_mad_hdr \*

    :param in_mad_size:
        *undescribed*
    :type in_mad_size: size_t

    :param out:
        *undescribed*
    :type out: struct ib_mad_hdr \*

    :param out_mad_size:
        *undescribed*
    :type out_mad_size: size_t \*

    :param out_mad_pkey_index:
        *undescribed*
    :type out_mad_pkey_index: u16 \*

.. _`rvt_process_mad.description`:

Description
-----------

Note that the verbs framework has already done the MAD sanity checks,
and hop count/pointer updating for IB_MGMT_CLASS_SUBN_DIRECTED_ROUTE
MADs.

This is called by the ib_mad module.

.. _`rvt_process_mad.return`:

Return
------

IB_MAD_RESULT_SUCCESS or error

.. _`rvt_create_mad_agents`:

rvt_create_mad_agents
=====================

.. c:function:: int rvt_create_mad_agents(struct rvt_dev_info *rdi)

    create mad agents

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

.. _`rvt_create_mad_agents.description`:

Description
-----------

If driver needs to be notified of mad agent creation then call back

Return 0 on success

.. _`rvt_free_mad_agents`:

rvt_free_mad_agents
===================

.. c:function:: void rvt_free_mad_agents(struct rvt_dev_info *rdi)

    free up mad agents

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

.. _`rvt_free_mad_agents.description`:

Description
-----------

If driver needs notification of mad agent removal make the call back

.. This file was automatic generated / don't edit.

