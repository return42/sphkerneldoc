.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/lmv/lmv_obd.c

.. _`lmv_set_mdc_active`:

lmv_set_mdc_active
==================

.. c:function:: int lmv_set_mdc_active(struct lmv_obd *lmv, struct obd_uuid *uuid, int activate)

    :param struct lmv_obd \*lmv:
        *undescribed*

    :param struct obd_uuid \*uuid:
        *undescribed*

    :param int activate:
        *undescribed*

.. _`lmv_set_mdc_active.description`:

Description
-----------

-EINVAL  : UUID can't be found in the LMV's target list
-ENOTCONN: The UUID is found, but the target connection is bad (!)
-EBADF   : The UUID is found, but the OBD of the wrong type (!)

.. _`lmv_connect`:

lmv_connect
===========

.. c:function:: int lmv_connect(const struct lu_env *env, struct obd_export **exp, struct obd_device *obd, struct obd_uuid *cluuid, struct obd_connect_data *data, void *localdata)

    caller that everything is okay. Real connection will be performed later.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct obd_export \*\*exp:
        *undescribed*

    :param struct obd_device \*obd:
        *undescribed*

    :param struct obd_uuid \*cluuid:
        *undescribed*

    :param struct obd_connect_data \*data:
        *undescribed*

    :param void \*localdata:
        *undescribed*

.. _`lmv_placement_policy`:

lmv_placement_policy
====================

.. c:function:: int lmv_placement_policy(struct obd_device *obd, struct md_op_data *op_data, u32 *mds)

    :param struct obd_device \*obd:
        *undescribed*

    :param struct md_op_data \*op_data:
        *undescribed*

    :param u32 \*mds:
        *undescribed*

.. _`lmv_quotactl`:

lmv_quotactl
============

.. c:function:: int lmv_quotactl(struct obd_device *unused, struct obd_export *exp, struct obd_quotactl *oqctl)

    process with other slave MDTs. The only exception is Q_GETOQUOTA for which we directly fetch data from the slave MDTs.

    :param struct obd_device \*unused:
        *undescribed*

    :param struct obd_export \*exp:
        *undescribed*

    :param struct obd_quotactl \*oqctl:
        *undescribed*

.. This file was automatic generated / don't edit.

