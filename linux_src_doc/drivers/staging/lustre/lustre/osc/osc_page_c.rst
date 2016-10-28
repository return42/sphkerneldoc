.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/osc/osc_page.c

.. _`osc_page_transfer_add`:

osc_page_transfer_add
=====================

.. c:function:: void osc_page_transfer_add(const struct lu_env *env, struct osc_page *opg, enum cl_req_type crt)

    either opportunistic (\ :c:func:`osc_page_cache_add`\ ), or immediate (\ :c:func:`osc_page_submit`\ ).

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

.. _`osc_page_submit`:

osc_page_submit
===============

.. c:function:: void osc_page_submit(const struct lu_env *env, struct osc_page *opg, enum cl_req_type crt, int brw_flags)

    transfer (i.e., transferred synchronously).

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

    :param int brw_flags:
        *undescribed*

.. _`osc_lru_del`:

osc_lru_del
===========

.. c:function:: void osc_lru_del(struct client_obd *cli, struct osc_page *opg)

    has never finished(error occurred).

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

.. _`osc_lru_use`:

osc_lru_use
===========

.. c:function:: void osc_lru_use(struct client_obd *cli, struct osc_page *opg)

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

.. _`osc_lru_shrink`:

osc_lru_shrink
==============

.. c:function:: int osc_lru_shrink(const struct lu_env *env, struct client_obd *cli, int target, bool force)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct client_obd \*cli:
        *undescribed*

    :param int target:
        *undescribed*

    :param bool force:
        *undescribed*

.. This file was automatic generated / don't edit.

