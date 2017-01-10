.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre_mdc.h

.. _`mdc_update_max_ea_from_body`:

mdc_update_max_ea_from_body
===========================

.. c:function:: void mdc_update_max_ea_from_body(struct obd_export *exp, struct mdt_body *body)

    :param struct obd_export \*exp:
        *undescribed*

    :param struct mdt_body \*body:
        *undescribed*

.. _`mdc_update_max_ea_from_body.description`:

Description
-----------

This value is learned from ptlrpc replies sent by the MDT. The
default easize is initialized to the minimum value but allowed
to grow up to a single page in size if required to handle the
common case.

\see client_obd::cl_default_mds_easize

\param[in] exp       export for MDC device
\param[in] body      body of ptlrpc reply from MDT

.. This file was automatic generated / don't edit.

