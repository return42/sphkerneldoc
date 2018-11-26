.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/ss/mls.c

.. _`mls_export_netlbl_lvl`:

mls_export_netlbl_lvl
=====================

.. c:function:: void mls_export_netlbl_lvl(struct policydb *p, struct context *context, struct netlbl_lsm_secattr *secattr)

    Export the MLS sensitivity levels to NetLabel

    :param p:
        *undescribed*
    :type p: struct policydb \*

    :param context:
        the security context
    :type context: struct context \*

    :param secattr:
        the NetLabel security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`mls_export_netlbl_lvl.description`:

Description
-----------

Given the security context copy the low MLS sensitivity level into the
NetLabel MLS sensitivity level field.

.. _`mls_import_netlbl_lvl`:

mls_import_netlbl_lvl
=====================

.. c:function:: void mls_import_netlbl_lvl(struct policydb *p, struct context *context, struct netlbl_lsm_secattr *secattr)

    Import the NetLabel MLS sensitivity levels

    :param p:
        *undescribed*
    :type p: struct policydb \*

    :param context:
        the security context
    :type context: struct context \*

    :param secattr:
        the NetLabel security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`mls_import_netlbl_lvl.description`:

Description
-----------

Given the security context and the NetLabel security attributes, copy the
NetLabel MLS sensitivity level into the context.

.. _`mls_export_netlbl_cat`:

mls_export_netlbl_cat
=====================

.. c:function:: int mls_export_netlbl_cat(struct policydb *p, struct context *context, struct netlbl_lsm_secattr *secattr)

    Export the MLS categories to NetLabel

    :param p:
        *undescribed*
    :type p: struct policydb \*

    :param context:
        the security context
    :type context: struct context \*

    :param secattr:
        the NetLabel security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`mls_export_netlbl_cat.description`:

Description
-----------

Given the security context copy the low MLS categories into the NetLabel
MLS category field.  Returns zero on success, negative values on failure.

.. _`mls_import_netlbl_cat`:

mls_import_netlbl_cat
=====================

.. c:function:: int mls_import_netlbl_cat(struct policydb *p, struct context *context, struct netlbl_lsm_secattr *secattr)

    Import the MLS categories from NetLabel

    :param p:
        *undescribed*
    :type p: struct policydb \*

    :param context:
        the security context
    :type context: struct context \*

    :param secattr:
        the NetLabel security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`mls_import_netlbl_cat.description`:

Description
-----------

Copy the NetLabel security attributes into the SELinux context; since the
NetLabel security attribute only contains a single MLS category use it for
both the low and high categories of the context.  Returns zero on success,
negative values on failure.

.. This file was automatic generated / don't edit.

