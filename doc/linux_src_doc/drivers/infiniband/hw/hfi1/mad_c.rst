.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/mad.c

.. _`get_pkeys`:

get_pkeys
=========

.. c:function:: int get_pkeys(struct hfi1_devdata *dd, u8 port, u16 *pkeys)

    return the PKEY table

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u8 port:
        the IB port number

    :param u16 \*pkeys:
        the pkey table is placed here

.. _`__subn_set_opa_portinfo`:

__subn_set_opa_portinfo
=======================

.. c:function:: int __subn_set_opa_portinfo(struct opa_smp *smp, u32 am, u8 *data, struct ib_device *ibdev, u8 port, u32 *resp_len)

    set port information

    :param struct opa_smp \*smp:
        the incoming SM packet

    :param u32 am:
        *undescribed*

    :param u8 \*data:
        *undescribed*

    :param struct ib_device \*ibdev:
        the infiniband device

    :param u8 port:
        the port on the device

    :param u32 \*resp_len:
        *undescribed*

.. _`set_pkeys`:

set_pkeys
=========

.. c:function:: int set_pkeys(struct hfi1_devdata *dd, u8 port, u16 *pkeys)

    set the PKEY table for ctxt 0

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u8 port:
        the IB port number

    :param u16 \*pkeys:
        the PKEY table

.. _`hfi1_process_mad`:

hfi1_process_mad
================

.. c:function:: int hfi1_process_mad(struct ib_device *ibdev, int mad_flags, u8 port, const struct ib_wc *in_wc, const struct ib_grh *in_grh, const struct ib_mad_hdr *in_mad, size_t in_mad_size, struct ib_mad_hdr *out_mad, size_t *out_mad_size, u16 *out_mad_pkey_index)

    process an incoming MAD packet

    :param struct ib_device \*ibdev:
        the infiniband device this packet came in on

    :param int mad_flags:
        MAD flags

    :param u8 port:
        the port number this packet came in on

    :param const struct ib_wc \*in_wc:
        the work completion entry for this packet

    :param const struct ib_grh \*in_grh:
        the global route header for this packet

    :param const struct ib_mad_hdr \*in_mad:
        the incoming MAD

    :param size_t in_mad_size:
        *undescribed*

    :param struct ib_mad_hdr \*out_mad:
        any outgoing MAD reply

    :param size_t \*out_mad_size:
        *undescribed*

    :param u16 \*out_mad_pkey_index:
        *undescribed*

.. _`hfi1_process_mad.description`:

Description
-----------

Returns IB_MAD_RESULT_SUCCESS if this is a MAD that we are not
interested in processing.

Note that the verbs framework has already done the MAD sanity checks,
and hop count/pointer updating for IB_MGMT_CLASS_SUBN_DIRECTED_ROUTE
MADs.

This is called by the ib_mad module.

.. This file was automatic generated / don't edit.

