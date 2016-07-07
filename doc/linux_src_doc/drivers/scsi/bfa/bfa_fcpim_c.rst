.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bfa/bfa_fcpim.c

.. _`bfa_fcpim_get_throttle_cfg`:

bfa_fcpim_get_throttle_cfg
==========================

.. c:function:: u16 bfa_fcpim_get_throttle_cfg(struct bfa_s *bfa, u16 drv_cfg_param)

    If 0, then use driver parameter We need to use min(flash_val, drv_val) because memory allocation was done based on this cfg'd value

    :param struct bfa_s \*bfa:
        *undescribed*

    :param u16 drv_cfg_param:
        *undescribed*

.. This file was automatic generated / don't edit.

