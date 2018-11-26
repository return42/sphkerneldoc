.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_mad.c

.. _`set_overrunthreshold`:

set_overrunthreshold
====================

.. c:function:: int set_overrunthreshold(struct qib_pportdata *ppd, unsigned n)

    set the overrun threshold

    :param ppd:
        the physical port data
    :type ppd: struct qib_pportdata \*

    :param n:
        the new threshold
    :type n: unsigned

.. _`set_overrunthreshold.description`:

Description
-----------

Note that this will only take effect when the link state changes.

.. _`set_phyerrthreshold`:

set_phyerrthreshold
===================

.. c:function:: int set_phyerrthreshold(struct qib_pportdata *ppd, unsigned n)

    set the physical error threshold

    :param ppd:
        the physical port data
    :type ppd: struct qib_pportdata \*

    :param n:
        the new threshold
    :type n: unsigned

.. _`set_phyerrthreshold.description`:

Description
-----------

Note that this will only take effect when the link state changes.

.. _`get_linkdowndefaultstate`:

get_linkdowndefaultstate
========================

.. c:function:: int get_linkdowndefaultstate(struct qib_pportdata *ppd)

    get the default linkdown state

    :param ppd:
        the physical port data
    :type ppd: struct qib_pportdata \*

.. _`get_linkdowndefaultstate.description`:

Description
-----------

Returns zero if the default is POLL, 1 if the default is SLEEP.

.. _`get_pkeys`:

get_pkeys
=========

.. c:function:: int get_pkeys(struct qib_devdata *dd, u8 port, u16 *pkeys)

    return the PKEY table

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param port:
        the IB port number
    :type port: u8

    :param pkeys:
        the pkey table is placed here
    :type pkeys: u16 \*

.. _`subn_set_portinfo`:

subn_set_portinfo
=================

.. c:function:: int subn_set_portinfo(struct ib_smp *smp, struct ib_device *ibdev, u8 port)

    set port information

    :param smp:
        the incoming SM packet
    :type smp: struct ib_smp \*

    :param ibdev:
        the infiniband device
    :type ibdev: struct ib_device \*

    :param port:
        the port on the device
    :type port: u8

.. _`subn_set_portinfo.description`:

Description
-----------

Set Portinfo (see ch. 14.2.5.6).

.. _`rm_pkey`:

rm_pkey
=======

.. c:function:: int rm_pkey(struct qib_pportdata *ppd, u16 key)

    decrecment the reference count for the given PKEY

    :param ppd:
        *undescribed*
    :type ppd: struct qib_pportdata \*

    :param key:
        the PKEY index
    :type key: u16

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

    :param ppd:
        *undescribed*
    :type ppd: struct qib_pportdata \*

    :param key:
        the PKEY
    :type key: u16

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

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param port:
        the IB port number
    :type port: u8

    :param pkeys:
        the PKEY table
    :type pkeys: u16 \*

.. _`qib_process_mad`:

qib_process_mad
===============

.. c:function:: int qib_process_mad(struct ib_device *ibdev, int mad_flags, u8 port, const struct ib_wc *in_wc, const struct ib_grh *in_grh, const struct ib_mad_hdr *in, size_t in_mad_size, struct ib_mad_hdr *out, size_t *out_mad_size, u16 *out_mad_pkey_index)

    process an incoming MAD packet

    :param ibdev:
        the infiniband device this packet came in on
    :type ibdev: struct ib_device \*

    :param mad_flags:
        MAD flags
    :type mad_flags: int

    :param port:
        the port number this packet came in on
    :type port: u8

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

