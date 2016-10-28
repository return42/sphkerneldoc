.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/cfq-iosched.c

.. _`cfqg_scale_charge`:

cfqg_scale_charge
=================

.. c:function:: u64 cfqg_scale_charge(unsigned long charge, unsigned int vfraction)

    scale disk time charge according to cfqg weight

    :param unsigned long charge:
        disk time being charged

    :param unsigned int vfraction:
        vfraction of the cfqg, fixed point w/ CFQ_SERVICE_SHIFT

.. _`cfqg_scale_charge.description`:

Description
-----------

Scale \ ``charge``\  according to \ ``vfraction``\ , which is in range (0, 1].  The
scaling is inversely proportional.

scaled = charge / vfraction

The result is also in fixed point w/ CFQ_SERVICE_SHIFT.

.. _`cfq_init_cfqg_base`:

cfq_init_cfqg_base
==================

.. c:function:: void cfq_init_cfqg_base(struct cfq_group *cfqg)

    initialize base part of a cfq_group

    :param struct cfq_group \*cfqg:
        cfq_group to initialize

.. _`cfq_init_cfqg_base.description`:

Description
-----------

Initialize the base part which is used whether \ ``CONFIG_CFQ_GROUP_IOSCHED``\ 
is enabled or not.

.. This file was automatic generated / don't edit.

