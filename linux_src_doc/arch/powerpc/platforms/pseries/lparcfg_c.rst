.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/lparcfg.c

.. _`parse_mpp_data`:

parse_mpp_data
==============

.. c:function:: void parse_mpp_data(struct seq_file *m)

    Parse out data returned from h_get_mpp

    :param m:
        *undescribed*
    :type m: struct seq_file \*

.. _`parse_mpp_x_data`:

parse_mpp_x_data
================

.. c:function:: void parse_mpp_x_data(struct seq_file *m)

    Parse out data returned from h_get_mpp_x

    :param m:
        *undescribed*
    :type m: struct seq_file \*

.. _`update_mpp`:

update_mpp
==========

.. c:function:: ssize_t update_mpp(u64 *entitlement, u8 *weight)

    :param entitlement:
        *undescribed*
    :type entitlement: u64 \*

    :param weight:
        *undescribed*
    :type weight: u8 \*

.. _`update_mpp.description`:

Description
-----------

Update the memory entitlement and weight for the partition.  Caller must
specify either a new entitlement or weight, not both, to be updated
since the h_set_mpp call takes both entitlement and weight as parameters.

.. This file was automatic generated / don't edit.

