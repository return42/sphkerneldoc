.. -*- coding: utf-8; mode: rst -*-

=============
si476x-core.h
=============


.. _`si476x_power_state`:

enum si476x_power_state
=======================

.. c:type:: si476x_power_state

    possible power state of the si476x device.


.. _`si476x_power_state.definition`:

Definition
----------

.. code-block:: c

    enum si476x_power_state {
      SI476X_POWER_DOWN,
      SI476X_POWER_UP_FULL,
      SI476X_POWER_INCONSISTENT
    };


.. _`si476x_power_state.constants`:

Constants
---------

:``SI476X_POWER_DOWN``:
    In this state all regulators are turned off
    and the reset line is pulled low. The device is completely
    inactive.

:``SI476X_POWER_UP_FULL``:
    In this state all the power regualtors are
    turned on, reset line pulled high, IRQ line is enabled(polling is
    active for polling use scenario) and device is turned on with
    POWER_UP command. The device is ready to be used.

:``SI476X_POWER_INCONSISTENT``:
    This state indicates that previous
    power down was inconsistent, meaning some of the regulators were
    not turned down and thus use of the device, without power-cycling
    is impossible.


.. _`si476x_core`:

struct si476x_core
==================

.. c:type:: si476x_core

    internal data structure representing the underlying "core" device which all the MFD cell-devices use.


.. _`si476x_core.definition`:

Definition
----------

.. code-block:: c

  struct si476x_core {
    struct i2c_client * client;
    int chip_id;
    struct mfd_cell cells[SI476X_MFD_CELLS];
    struct mutex cmd_lock;
    atomic_t users;
    wait_queue_head_t rds_read_queue;
    struct kfifo rds_fifo;
    struct work_struct rds_fifo_drainer;
    bool rds_drainer_is_working;
    struct mutex rds_drainer_status_lock;
    wait_queue_head_t command;
    atomic_t cts;
    wait_queue_head_t tuning;
    atomic_t stc;
    struct si476x_power_up_args power_up_parameters;
    int gpio_reset;
    struct si476x_pinmux pinmux;
    enum si476x_phase_diversity_mode diversity_mode;
    struct delayed_work status_monitor;
    #define SI476X_WORK_TO_CORE(w) container_of(to_delayed_work(w),						    struct si476x_core,						    status_monitor)
    int revision;
  };


.. _`si476x_core.members`:

Members
-------

:``client``:
    Actual I2C client used to transfer commands to the chip.

:``chip_id``:
    Last digit of the chip model(E.g. "1" for SI4761)

:``cells[SI476X_MFD_CELLS]``:
    MFD cell devices created by this driver.

:``cmd_lock``:
    Mutex used to serialize all the requests to the core
    device. This filed should not be used directly. Instead
    :c:func:`si476x_core_lock`/:c:func:`si476x_core_unlock` should be used to get
    exclusive access to the "core" device.

:``users``:
    Active users counter(Used by the radio cell)

:``rds_read_queue``:
    Wait queue used to wait for RDS data.

:``rds_fifo``:
    FIFO in which all the RDS data received from the chip is
    placed.

:``rds_fifo_drainer``:
    Worker that drains on-chip RDS FIFO.

:``rds_drainer_is_working``:
    Flag used for launching only one instance
    of the ``rds_fifo_drainer``\ .

:``rds_drainer_status_lock``:
    Lock used to guard access to the
    ``rds_drainer_is_working`` variable.

:``command``:
    Wait queue for wainting on the command comapletion.

:``cts``:
    Clear To Send flag set upon receiving first status with CTS
    set.

:``tuning``:
    Wait queue used for wainting for tune/seek comand
    completion.

:``stc``:
    Similar to ``cts``\ , but for the STC bit of the status value.

:``power_up_parameters``:
    Parameters used as argument for POWER_UP
    command when the device is started.

:``gpio_reset``:
    GPIO pin connectet to the RSTB pin of the chip.

:``pinmux``:
    Chip's configurable pins configuration.

:``diversity_mode``:
    Chips role when functioning in diversity mode.

:``status_monitor``:
    Polling worker used in polling use case scenarion
    (when IRQ is not avalible).

:``revision``:
    Chip's running firmware revision number(Used for correct
    command set support).




.. _`si476x_core_lock`:

si476x_core_lock
================

.. c:function:: void si476x_core_lock (struct si476x_core *core)

    lock the core device to get an exclusive access to it.

    :param struct si476x_core \*core:

        *undescribed*



.. _`si476x_core_unlock`:

si476x_core_unlock
==================

.. c:function:: void si476x_core_unlock (struct si476x_core *core)

    unlock the core device to relinquish an exclusive access to it.

    :param struct si476x_core \*core:

        *undescribed*



.. _`si476x_func_info`:

struct si476x_func_info
=======================

.. c:type:: si476x_func_info

    structure containing result of the FUNC_INFO command.


.. _`si476x_func_info.definition`:

Definition
----------

.. code-block:: c

  struct si476x_func_info {
    enum si476x_func func;
  };


.. _`si476x_func_info.members`:

Members
-------

:``func``:
    Mode tuner is working in.




.. _`si476x_func_info.description`:

Description
-----------


``firmware``\ .major: Firmware major number.
``firmware``\ .minor[...]: Firmware minor numbers.



.. _`si476x_power_down_args`:

struct si476x_power_down_args
=============================

.. c:type:: si476x_power_down_args

    structure used to pass parameters to POWER_DOWN command


.. _`si476x_power_down_args.definition`:

Definition
----------

.. code-block:: c

  struct si476x_power_down_args {
    bool xosc;
  };


.. _`si476x_power_down_args.members`:

Members
-------

:``xosc``:
    true - Power down, but leav oscillator running.
    false - Full power down.




.. _`si476x_tunemode`:

enum si476x_tunemode
====================

.. c:type:: si476x_tunemode

    enum representing possible tune modes for the chip.


.. _`si476x_tunemode.definition`:

Definition
----------

.. code-block:: c

    enum si476x_tunemode {
      SI476X_TM_VALIDATED_NORMAL_TUNE,
      SI476X_TM_INVALIDATED_FAST_TUNE,
      SI476X_TM_VALIDATED_AF_TUNE,
      SI476X_TM_VALIDATED_AF_CHECK
    };


.. _`si476x_tunemode.constants`:

Constants
---------

:``SI476X_TM_VALIDATED_NORMAL_TUNE``:
    Unconditionally stay on the new
    channel after tune, tune status is valid.

:``SI476X_TM_INVALIDATED_FAST_TUNE``:
    Unconditionally stay in the new
    channel after tune, tune status invalid.

:``SI476X_TM_VALIDATED_AF_TUNE``:
    Jump back to previous channel if
    metric thresholds are not met.

:``SI476X_TM_VALIDATED_AF_CHECK``:
    Unconditionally jump back to the
    previous channel.


.. _`si476x_smoothmetrics`:

enum si476x_smoothmetrics
=========================

.. c:type:: si476x_smoothmetrics

    enum containing the possible setting fo audio transitioning of the chip


.. _`si476x_smoothmetrics.definition`:

Definition
----------

.. code-block:: c

    enum si476x_smoothmetrics {
      SI476X_SM_INITIALIZE_AUDIO,
      SI476X_SM_TRANSITION_AUDIO
    };


.. _`si476x_smoothmetrics.constants`:

Constants
---------

:``SI476X_SM_INITIALIZE_AUDIO``:
    Initialize audio state to match this
    new channel

:``SI476X_SM_TRANSITION_AUDIO``:
    Transition audio state from previous
    channel values to the new values


.. _`si476x_rds_status_report`:

struct si476x_rds_status_report
===============================

.. c:type:: si476x_rds_status_report

    the structure representing the response to 'FM_RD_STATUS' command


.. _`si476x_rds_status_report.definition`:

Definition
----------

.. code-block:: c

  struct si476x_rds_status_report {
    bool rdstpptyint;
    bool rdspiint;
    bool rdssyncint;
    bool rdsfifoint;
    bool tpptyvalid;
    bool pivalid;
    bool rdssync;
    bool rdsfifolost;
    bool tp;
    u8 pty;
    u16 pi;
    u8 rdsfifoused;
  };


.. _`si476x_rds_status_report.members`:

Members
-------

:``rdstpptyint``:
    Traffic program flag(TP) and/or program type(PTY)
    code has changed.

:``rdspiint``:
    Program identification(PI) code has changed.

:``rdssyncint``:
    RDS synchronization has changed.

:``rdsfifoint``:
    RDS was received and the RDS FIFO has at least
    'FM_RDS_INTERRUPT_FIFO_COUNT' elements in it.

:``tpptyvalid``:
    TP flag and PTY code are valid falg.

:``pivalid``:
    PI code is valid flag.

:``rdssync``:
    RDS is currently synchronized.

:``rdsfifolost``:
    On or more RDS groups have been lost/discarded flag.

:``tp``:
    Current channel's TP flag.

:``pty``:
    Current channel's PTY code.

:``pi``:
    Current channel's PI code.

:``rdsfifoused``:
    Number of blocks remaining in the RDS FIFO (0 if
    empty).


