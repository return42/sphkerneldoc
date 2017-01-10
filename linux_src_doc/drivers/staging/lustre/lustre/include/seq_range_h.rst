.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/seq_range.h

.. _`fld_range_type`:

fld_range_type
==============

.. c:function:: unsigned int fld_range_type(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`fld_range_is_ost`:

fld_range_is_ost
================

.. c:function:: bool fld_range_is_ost(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`fld_range_is_mdt`:

fld_range_is_mdt
================

.. c:function:: bool fld_range_is_mdt(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`fld_range_is_any`:

fld_range_is_any
================

.. c:function:: unsigned int fld_range_is_any(const struct lu_seq_range *range)

    but it does not know whether the seq is an MDT or OST, so it will send the request with ANY type, which means any seq type from the lookup can be expected. /a range

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`fld_range_set_type`:

fld_range_set_type
==================

.. c:function:: void fld_range_set_type(struct lu_seq_range *range, unsigned int flags)

    :param struct lu_seq_range \*range:
        *undescribed*

    :param unsigned int flags:
        *undescribed*

.. _`fld_range_set_mdt`:

fld_range_set_mdt
=================

.. c:function:: void fld_range_set_mdt(struct lu_seq_range *range)

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`fld_range_set_ost`:

fld_range_set_ost
=================

.. c:function:: void fld_range_set_ost(struct lu_seq_range *range)

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`fld_range_set_any`:

fld_range_set_any
=================

.. c:function:: void fld_range_set_any(struct lu_seq_range *range)

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`lu_seq_range_space`:

lu_seq_range_space
==================

.. c:function:: u64 lu_seq_range_space(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`lu_seq_range_init`:

lu_seq_range_init
=================

.. c:function:: void lu_seq_range_init(struct lu_seq_range *range)

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`lu_seq_range_within`:

lu_seq_range_within
===================

.. c:function:: bool lu_seq_range_within(const struct lu_seq_range *range, u64 seq)

    :param const struct lu_seq_range \*range:
        *undescribed*

    :param u64 seq:
        *undescribed*

.. _`lu_seq_range_is_sane`:

lu_seq_range_is_sane
====================

.. c:function:: bool lu_seq_range_is_sane(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`lu_seq_range_is_zero`:

lu_seq_range_is_zero
====================

.. c:function:: bool lu_seq_range_is_zero(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`lu_seq_range_is_exhausted`:

lu_seq_range_is_exhausted
=========================

.. c:function:: bool lu_seq_range_is_exhausted(const struct lu_seq_range *range)

    :param const struct lu_seq_range \*range:
        *undescribed*

.. _`lu_seq_range_compare_loc`:

lu_seq_range_compare_loc
========================

.. c:function:: int lu_seq_range_compare_loc(const struct lu_seq_range *r1, const struct lu_seq_range *r2)

    different \a r1 \a r2

    :param const struct lu_seq_range \*r1:
        *undescribed*

    :param const struct lu_seq_range \*r2:
        *undescribed*

.. _`lustre_swab_lu_seq_range`:

lustre_swab_lu_seq_range
========================

.. c:function:: void lustre_swab_lu_seq_range(struct lu_seq_range *range)

    :param struct lu_seq_range \*range:
        *undescribed*

.. _`drange`:

DRANGE
======

.. c:function::  DRANGE()

.. This file was automatic generated / don't edit.

