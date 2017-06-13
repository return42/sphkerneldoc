.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ccree/ssi_request_mgr.c

.. _`init_cc_monitor_desc`:

INIT_CC_MONITOR_DESC
====================

.. c:function::  INIT_CC_MONITOR_DESC( desc_p)

    Used to measure CC performance.

    :param  desc_p:
        *undescribed*

.. _`cc_cycle_desc_head`:

CC_CYCLE_DESC_HEAD
==================

.. c:function::  CC_CYCLE_DESC_HEAD( cc_base_addr,  desc_p,  lock_p,  is_monitored_p)

    :param  cc_base_addr:
        *undescribed*

    :param  desc_p:
        *undescribed*

    :param  lock_p:
        *undescribed*

    :param  is_monitored_p:
        *undescribed*

.. _`cc_cycle_desc_tail`:

CC_CYCLE_DESC_TAIL
==================

.. c:function::  CC_CYCLE_DESC_TAIL( cc_base_addr,  desc_p,  is_monitored)

    1. Add memory barrier descriptor to ensure last AXI transaction. 2. Add monitor descriptor to sequence tail AFTER enqueuing sequence.

    :param  cc_base_addr:
        *undescribed*

    :param  desc_p:
        *undescribed*

    :param  is_monitored:
        *undescribed*

.. _`end_cc_monitor_count`:

END_CC_MONITOR_COUNT
====================

.. c:function::  END_CC_MONITOR_COUNT( cc_base_addr,  stat_op_type,  stat_phase,  monitor_null_cycles,  lock_p,  is_monitored)

    Can only succeed if the lock_p is taken by the owner of the given request.

    :param  cc_base_addr:
        *undescribed*

    :param  stat_op_type:
        *undescribed*

    :param  stat_phase:
        *undescribed*

    :param  monitor_null_cycles:
        *undescribed*

    :param  lock_p:
        *undescribed*

    :param  is_monitored:
        *undescribed*

.. This file was automatic generated / don't edit.

