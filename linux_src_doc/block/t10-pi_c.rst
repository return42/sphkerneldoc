.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/t10-pi.c

.. _`t10_pi_prepare`:

t10_pi_prepare
==============

.. c:function:: void t10_pi_prepare(struct request *rq, u8 protection_type)

    prepare PI prior submitting request to device

    :param rq:
        request with PI that should be prepared
    :type rq: struct request \*

    :param protection_type:
        PI type (Type 1/Type 2/Type 3)
    :type protection_type: u8

.. _`t10_pi_prepare.description`:

Description
-----------

For Type 1/Type 2, the virtual start sector is the one that was
originally submitted by the block layer for the ref_tag usage. Due to
partitioning, MD/DM cloning, etc. the actual physical start sector is
likely to be different. Remap protection information to match the
physical LBA.

Type 3 does not have a reference tag so no remapping is required.

.. _`t10_pi_complete`:

t10_pi_complete
===============

.. c:function:: void t10_pi_complete(struct request *rq, u8 protection_type, unsigned int intervals)

    prepare PI prior returning request to the block layer

    :param rq:
        request with PI that should be prepared
    :type rq: struct request \*

    :param protection_type:
        PI type (Type 1/Type 2/Type 3)
    :type protection_type: u8

    :param intervals:
        total elements to prepare
    :type intervals: unsigned int

.. _`t10_pi_complete.description`:

Description
-----------

For Type 1/Type 2, the virtual start sector is the one that was
originally submitted by the block layer for the ref_tag usage. Due to
partitioning, MD/DM cloning, etc. the actual physical start sector is
likely to be different. Since the physical start sector was submitted
to the device, we should remap it back to virtual values expected by the
block layer.

Type 3 does not have a reference tag so no remapping is required.

.. This file was automatic generated / don't edit.

