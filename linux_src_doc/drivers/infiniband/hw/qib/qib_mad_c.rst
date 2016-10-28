.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_mad.c

.. _`set_overrunthreshold`:

set_overrunthreshold
====================

.. c:function:: int set_overrunthreshold(struct qib_pportdata *ppd, unsigned n)

    set the overrun threshold

    :param struct qib_pportdata \*ppd:
        the physical port data

    :param unsigned n:
        the new threshold

.. _`set_overrunthreshold.description`:

Description
-----------

Note that this will only take effect when the link state changes.

.. _`set_phyerrthreshold`:

set_phyerrthreshold
===================

.. c:function:: int set_phyerrthreshold(struct qib_pportdata *ppd, unsigned n)

    set the physical error threshold

    :param struct qib_pportdata \*ppd:
        the physical port data

    :param unsigned n:
        the new threshold

.. _`set_phyerrthreshold.description`:

Description
-----------

Note that this will only take effect when the link state changes.

.. _`get_linkdowndefaultstate`:

get_linkdowndefaultstate
========================

.. c:function:: int get_linkdowndefaultstate(struct qib_pportdata *ppd)

    get the default linkdown state

    :param struct qib_pportdata \*ppd:
        the physical port data

.. _`get_linkdowndefaultstate.description`:

Description
-----------

Returns zero if the default is POLL, 1 if the default is SLEEP.

.. _`get_pkeys`:

get_pkeys
=========

.. c:function:: int get_pkeys(struct qib_devdata *dd, u8 port, u16 *pkeys)

    return the PKEY table

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param u8 port:
        the IB port number

    :param u16 \*pkeys:
        the pkey table is placed here

.. _`subn_set_portinfo`:

subn_set_portinfo
=================

.. c:function:: int subn_set_portinfo(struct ib_smp *smp, struct ib_device *ibdev, u8 port)

    set port information

    :param struct ib_smp \*smp:
        the incoming SM packet

    :param struct ib_device \*ibdev:
        the infiniband device

    :param u8 port:
        the port on the device

.. _`subn_set_portinfo.description`:

Description
-----------

Set Portinfo (see ch. 14.2.5.6).

.. _`rm_pkey`:

rm_pkey
=======

.. c:function:: int rm_pkey(struct qib_pportdata *ppd, u16 key)

    decrecment the reference count for the given PKEY

    :param struct qib_pportdata \*ppd:
        *undescribed*

    :param u16 key:
        the PKEY index

.. _`rm_pkey.description`:

Description
-----------

Return true if this was the last reference and the hardware table entry
needs to be changed.

.. _`add_pkey`:

add_pkey
========

.. c:function:: int add_pkey(struct qib_pportdata *ppd, u16 key)

    add the given PKEY to the hardware table

    :param struct qib_pportdata \*ppd:
        *undescribed*

    :param u16 key:
        the PKEY

.. _`add_pkey.description`:

Description
-----------

Return an error code if unable to add the entry, zero if no change,
or 1 if the hardware PKEY register needs to be updated.

.. _`set_pkeys`:

set_pkeys
=========

.. c:function:: int set_pkeys(struct qib_devdata *dd, u8 port, u16 *pkeys)

    set the PKEY table for ctxt 0

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param u8 port:
        the IB port number

    :param u16 \*pkeys:
        the PKEY table

.. _`qib_process_mad`:

qib_process_mad
===============

.. c:function:: int qib_process_mad(struct ib_device *ibdev, int mad_flags, u8 port, const struct ib_wc *in_wc, const struct ib_grh *in_grh, const struct ib_mad_hdr *in, size_t in_mad_size, struct ib_mad_hdr *out, size_t *out_mad_size, u16 *out_mad_pkey_index)

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

    :param const struct ib_mad_hdr \*in:
        *undescribed*

    :param size_t in_mad_size:
        *undescribed*

    :param struct ib_mad_hdr \*out:
        *undescribed*

    :param size_t \*out_mad_size:
        *undescribed*

    :param u16 \*out_mad_pkey_index:
        *undescribed*

.. _`qib_process_mad.description`:

Description
-----------

Returns IB_MAD_RESULT_SUCCESS if this is a MAD that we are not
interested in processing.

Note that the verbs framework has already done the MAD sanity checks,
and hop count/pointer updating for IB_MGMT_CLASS_SUBN_DIRECTED_ROUTE
MADs.

This is called by the ib_mad module.

.. This file was automatic generated / don't edit.

