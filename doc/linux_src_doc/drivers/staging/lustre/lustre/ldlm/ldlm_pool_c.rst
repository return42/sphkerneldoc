.. -*- coding: utf-8; mode: rst -*-

===========
ldlm_pool.c
===========


.. _`ldlm_pool_t2gsp`:

ldlm_pool_t2gsp
===============

.. c:function:: int ldlm_pool_t2gsp (unsigned int t)

    :param unsigned int t:

        *undescribed*



.. _`ldlm_pool_t2gsp.description`:

Description
-----------

\a period. This is later used in grant_plan calculations.



.. _`ldlm_pool_recalc_stats`:

ldlm_pool_recalc_stats
======================

.. c:function:: void ldlm_pool_recalc_stats (struct ldlm_pool *pl)

    :param struct ldlm_pool \*pl:

        *undescribed*



.. _`ldlm_pool_recalc_stats.description`:

Description
-----------


\pre ->pl_lock is locked.



.. _`ldlm_cli_pool_pop_slv`:

ldlm_cli_pool_pop_slv
=====================

.. c:function:: void ldlm_cli_pool_pop_slv (struct ldlm_pool *pl)

    :param struct ldlm_pool \*pl:

        *undescribed*



.. _`ldlm_cli_pool_pop_slv.description`:

Description
-----------

ns_pool)->ns_obd tp passed \a pl.



.. _`ldlm_cli_pool_recalc`:

ldlm_cli_pool_recalc
====================

.. c:function:: int ldlm_cli_pool_recalc (struct ldlm_pool *pl)

    :param struct ldlm_pool \*pl:

        *undescribed*



.. _`ldlm_cli_pool_shrink`:

ldlm_cli_pool_shrink
====================

.. c:function:: int ldlm_cli_pool_shrink (struct ldlm_pool *pl, int nr, gfp_t gfp_mask)

    :param struct ldlm_pool \*pl:

        *undescribed*

    :param int nr:

        *undescribed*

    :param gfp_t gfp_mask:

        *undescribed*



.. _`ldlm_cli_pool_shrink.description`:

Description
-----------

side.  Main goal of this function is to cancel some number of locks on
passed \a pl according to \a nr and \a gfp_mask.



.. _`ldlm_pool_recalc`:

ldlm_pool_recalc
================

.. c:function:: int ldlm_pool_recalc (struct ldlm_pool *pl)

    :param struct ldlm_pool \*pl:

        *undescribed*



.. _`ldlm_pool_recalc.description`:

Description
-----------

depending what pool \a pl is used.



.. _`ldlm_pool_add`:

ldlm_pool_add
=============

.. c:function:: void ldlm_pool_add (struct ldlm_pool *pl, struct ldlm_lock *lock)

    :param struct ldlm_pool \*pl:

        *undescribed*

    :param struct ldlm_lock \*lock:

        *undescribed*



.. _`ldlm_pool_del`:

ldlm_pool_del
=============

.. c:function:: void ldlm_pool_del (struct ldlm_pool *pl, struct ldlm_lock *lock)

    :param struct ldlm_pool \*pl:

        *undescribed*

    :param struct ldlm_lock \*lock:

        *undescribed*



.. _`ldlm_pool_get_slv`:

ldlm_pool_get_slv
=================

.. c:function:: __u64 ldlm_pool_get_slv (struct ldlm_pool *pl)

    :param struct ldlm_pool \*pl:

        *undescribed*



.. _`ldlm_pool_get_slv.description`:

Description
-----------


\pre ->pl_lock is not locked.



.. _`ldlm_pool_set_clv`:

ldlm_pool_set_clv
=================

.. c:function:: void ldlm_pool_set_clv (struct ldlm_pool *pl, __u64 clv)

    :param struct ldlm_pool \*pl:

        *undescribed*

    :param __u64 clv:

        *undescribed*



.. _`ldlm_pool_set_clv.description`:

Description
-----------


\pre ->pl_lock is not locked.



.. _`ldlm_pool_get_lvf`:

ldlm_pool_get_lvf
=================

.. c:function:: __u32 ldlm_pool_get_lvf (struct ldlm_pool *pl)

    :param struct ldlm_pool \*pl:

        *undescribed*

