.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/raid5.h

.. _`check_states`:

enum check_states
=================

.. c:type:: enum check_states

    handles syncing / repairing a stripe \ ``check_state_idle``\  - check operations are quiesced \ ``check_state_run``\  - check operation is running \ ``check_state_result``\  - set outside lock when check result is valid \ ``check_state_compute_run``\  - check failed and we are repairing \ ``check_state_compute_result``\  - set outside lock when compute result is valid

.. _`check_states.definition`:

Definition
----------

.. code-block:: c

    enum check_states {
        check_state_idle,
        check_state_run,
        check_state_run_q,
        check_state_run_pq,
        check_state_check_result,
        check_state_compute_run,
        check_state_compute_result
    };

.. _`check_states.constants`:

Constants
---------

check_state_idle
    *undescribed*

check_state_run
    *undescribed*

check_state_run_q
    *undescribed*

check_state_run_pq
    *undescribed*

check_state_check_result
    *undescribed*

check_state_compute_run
    *undescribed*

check_state_compute_result
    *undescribed*

.. _`reconstruct_states`:

enum reconstruct_states
=======================

.. c:type:: enum reconstruct_states

    handles writing or expanding a stripe

.. _`reconstruct_states.definition`:

Definition
----------

.. code-block:: c

    enum reconstruct_states {
        reconstruct_state_idle,
        reconstruct_state_prexor_drain_run,
        reconstruct_state_drain_run,
        reconstruct_state_run,
        reconstruct_state_prexor_drain_result,
        reconstruct_state_drain_result,
        reconstruct_state_result
    };

.. _`reconstruct_states.constants`:

Constants
---------

reconstruct_state_idle
    *undescribed*

reconstruct_state_prexor_drain_run
    *undescribed*

reconstruct_state_drain_run
    *undescribed*

reconstruct_state_run
    *undescribed*

reconstruct_state_prexor_drain_result
    *undescribed*

reconstruct_state_drain_result
    *undescribed*

reconstruct_state_result
    *undescribed*

.. This file was automatic generated / don't edit.

