.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/sec_config.c

.. _`sptlrpc_rule_set_choose`:

sptlrpc_rule_set_choose
=======================

.. c:function:: int sptlrpc_rule_set_choose(struct sptlrpc_rule_set *rset, enum lustre_sec_part from, enum lustre_sec_part to, lnet_nid_t nid, struct sptlrpc_flavor *sf)

    return 1 if a match found, otherwise return 0.

    :param struct sptlrpc_rule_set \*rset:
        *undescribed*

    :param enum lustre_sec_part from:
        *undescribed*

    :param enum lustre_sec_part to:
        *undescribed*

    :param lnet_nid_t nid:
        *undescribed*

    :param struct sptlrpc_flavor \*sf:
        *undescribed*

.. _`sptlrpc_conf_merge_rule`:

sptlrpc_conf_merge_rule
=======================

.. c:function:: int sptlrpc_conf_merge_rule(struct sptlrpc_conf *conf, const char *target, struct sptlrpc_rule *rule)

    :param struct sptlrpc_conf \*conf:
        *undescribed*

    :param const char \*target:
        *undescribed*

    :param struct sptlrpc_rule \*rule:
        *undescribed*

.. _`__sptlrpc_process_config`:

__sptlrpc_process_config
========================

.. c:function:: int __sptlrpc_process_config(struct lustre_cfg *lcfg, struct sptlrpc_conf *conf)

    find one through the target name in the record inside conf_lock; otherwise means caller already hold conf_lock.

    :param struct lustre_cfg \*lcfg:
        *undescribed*

    :param struct sptlrpc_conf \*conf:
        *undescribed*

.. _`sptlrpc_conf_log_update_end`:

sptlrpc_conf_log_update_end
===========================

.. c:function:: void sptlrpc_conf_log_update_end(const char *logname)

    :param const char \*logname:
        *undescribed*

.. _`sptlrpc_conf_client_adapt`:

sptlrpc_conf_client_adapt
=========================

.. c:function:: void sptlrpc_conf_client_adapt(struct obd_device *obd)

    do import_sec_adapt later.

    :param struct obd_device \*obd:
        *undescribed*

.. This file was automatic generated / don't edit.

